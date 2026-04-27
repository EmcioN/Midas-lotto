from datetime import date
import calendar
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from accounts.models import Profile
from .forms import DrawCommentForm, SubscriptionJoinForm
from .models import Draw, MonthlySummary, Subscription
import stripe
from django.conf import settings
from django.http import HttpResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import logging

stripe.api_key = settings.STRIPE_SECRET_KEY

logger = logging.getLogger(__name__)


def draw_list(request):
    draws = Draw.objects.select_related("monthly_summary").all()
    return render(request, "lotto/draw_list.html", {"draws": draws})


def draw_detail(request, draw_id):
    draw = get_object_or_404(Draw, id=draw_id)

    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.error(request, "You need to log in to post a comment.")
            return redirect("login")

        form = DrawCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.draw = draw
            comment.user = request.user
            comment.save()
            messages.success(request, "Your comment has been added.")
            return redirect("draw_detail", draw_id=draw.id)
    else:
        form = DrawCommentForm()

    context = {
        "draw": draw,
        "form": form,
    }
    return render(request, "lotto/draw_detail.html", context)


@login_required
def join_subscription(request):
    latest_month = MonthlySummary.objects.first()

    if not latest_month:
        messages.error(request, "No active lotto month is available right now.")
        return redirect("profile")

    existing_subscription = Subscription.objects.filter(
        user=request.user, monthly_summary=latest_month
    ).first()

    if existing_subscription:
        if existing_subscription.payment_completed:
            messages.info(
                request, "You already have a paid subscription for the current month."
            )
        else:
            messages.info(
                request,
                "You already started checkout for the current month. Please complete that payment or contact support.",
            )
        return redirect("profile")

    remaining_draws = Subscription.calculate_remaining_draws(latest_month)

    if remaining_draws <= 0:
        messages.error(
            request, "This month is already finished. No draws remain to join."
        )
        return redirect("profile")

    amount_to_pay = Subscription.calculate_price(
        latest_month.subscription_price, remaining_draws
    )

    if request.method == "POST":
        form = SubscriptionJoinForm(request.POST)
        if form.is_valid():
            expiry_date = date(
                latest_month.year,
                latest_month.month,
                calendar.monthrange(latest_month.year, latest_month.month)[1],
            )

            subscription, created = Subscription.objects.get_or_create(
                user=request.user,
                monthly_summary=latest_month,
                defaults={
                    "draws_paid_for": remaining_draws,
                    "amount_paid": amount_to_pay,
                    "joined_at": date.today(),
                    "expiry_date": expiry_date,
                    "active": False,
                    "payment_completed": False,
                },
            )

            if not created:
                subscription.draws_paid_for = remaining_draws
                subscription.amount_paid = amount_to_pay
                subscription.expiry_date = expiry_date
                subscription.active = False
                subscription.payment_completed = False
                subscription.save()

            try:
                checkout_session = stripe.checkout.Session.create(
                    mode="payment",
                    success_url=request.build_absolute_uri(
                        reverse("subscription_success")
                    )
                    + "?session_id={CHECKOUT_SESSION_ID}",
                    cancel_url=request.build_absolute_uri(
                        reverse("subscription_cancel")
                    ),
                    client_reference_id=str(subscription.id),
                    customer_email=request.user.email or None,
                    line_items=[
                        {
                            "price_data": {
                                "currency": "eur",
                                "product_data": {
                                    "name": f"Midas Lotto subscription for {latest_month}",
                                },
                                "unit_amount": int(amount_to_pay * 100),
                            },
                            "quantity": 1,
                        }
                    ],
                    metadata={
                        "subscription_id": str(subscription.id),
                        "user_id": str(request.user.id),
                        "monthly_summary_id": str(latest_month.id),
                        "remaining_draws": str(remaining_draws),
                    },
                )

                subscription.stripe_checkout_session_id = checkout_session.id
                subscription.save()

                return redirect(checkout_session.url, code=303)

            except stripe.error.StripeError:
                messages.error(
                    request,
                    "There was a problem starting the Stripe checkout. Please try again.",
                )
                return redirect("join_subscription")
    else:
        form = SubscriptionJoinForm()

    context = {
        "form": form,
        "latest_month": latest_month,
        "remaining_draws": remaining_draws,
        "amount_to_pay": amount_to_pay,
        "stripe_public_key": settings.STRIPE_PUBLIC_KEY,
    }
    return render(request, "lotto/join_subscription.html", context)


@login_required
def subscription_success(request):
    session_id = request.GET.get("session_id")
    payment_status = None

    if session_id:
        try:
            session = stripe.checkout.Session.retrieve(session_id)
            payment_status = session.payment_status

            if payment_status == "paid":
                subscription = Subscription.objects.filter(
                    stripe_checkout_session_id=session_id, user=request.user
                ).first()

                if subscription and not subscription.payment_completed:
                    subscription.payment_completed = True
                    subscription.active = True
                    subscription.save()

                    profile = Profile.objects.get(user=subscription.user)
                    profile.subscription_expiry = subscription.expiry_date
                    profile.save()

        except stripe.error.StripeError:
            payment_status = None

    context = {
        "session_id": session_id,
        "payment_status": payment_status,
    }
    return render(request, "lotto/subscription_success.html", context)


@login_required
def subscription_cancel(request):
    return render(request, "lotto/subscription_cancel.html")


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE")

    logger.info("Stripe webhook received")

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError:
        logger.exception("Invalid Stripe webhook payload")
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        logger.exception("Stripe webhook signature verification failed")
        return HttpResponse(status=400)

    logger.info("Stripe webhook type: %s", event["type"])

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        session_id = session.get("id")

        logger.info("Checkout session completed: %s", session_id)

        subscription = Subscription.objects.filter(
            stripe_checkout_session_id=session_id
        ).first()

        if not subscription:
            logger.warning("No subscription found for session %s", session_id)
            return HttpResponse(status=200)

        if not subscription.payment_completed:
            subscription.payment_completed = True
            subscription.active = True
            subscription.save()

            profile = Profile.objects.get(user=subscription.user)
            profile.subscription_expiry = subscription.expiry_date
            profile.save()

            logger.info("Subscription activated for user %s", subscription.user_id)

    return HttpResponse(status=200)
