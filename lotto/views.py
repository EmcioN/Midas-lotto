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

stripe.api_key = settings.STRIPE_SECRET_KEY

def draw_list(request):
    draws = Draw.objects.select_related('monthly_summary').all()
    return render(request, 'lotto/draw_list.html', {'draws': draws})


def draw_detail(request, draw_id):
    draw = get_object_or_404(Draw, id=draw_id)

    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, 'You need to log in to post a comment.')
            return redirect('login')

        form = DrawCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.draw = draw
            comment.user = request.user
            comment.save()
            messages.success(request, 'Your comment has been added.')
            return redirect('draw_detail', draw_id=draw.id)
    else:
        form = DrawCommentForm()

    context = {
        'draw': draw,
        'form': form,
    }
    return render(request, 'lotto/draw_detail.html', context)


@login_required
def join_subscription(request):
    latest_month = MonthlySummary.objects.first()

    if not latest_month:
        messages.error(request, 'No active lotto month is available right now.')
        return redirect('profile')

    existing_subscription = Subscription.objects.filter(
        user=request.user,
        monthly_summary=latest_month
    ).first()

    if existing_subscription and existing_subscription.payment_completed:
        messages.info(request, 'You already joined the current month.')
        return redirect('profile')

    remaining_draws = Subscription.calculate_remaining_draws(latest_month)

    if remaining_draws <= 0:
        messages.error(request, 'This month is already finished. No draws remain to join.')
        return redirect('profile')

    amount_to_pay = Subscription.calculate_price(
        latest_month.subscription_price,
        remaining_draws
    )

    if request.method == 'POST':
        form = SubscriptionJoinForm(request.POST)
        if form.is_valid():
            expiry_date = date(
                latest_month.year,
                latest_month.month,
                calendar.monthrange(latest_month.year, latest_month.month)[1]
            )

            subscription, created = Subscription.objects.get_or_create(
                user=request.user,
                monthly_summary=latest_month,
                defaults={
                    'draws_paid_for': remaining_draws,
                    'amount_paid': amount_to_pay,
                    'joined_at': date.today(),
                    'expiry_date': expiry_date,
                    'active': False,
                    'payment_completed': False,
                }
            )

            if not created:
                subscription.draws_paid_for = remaining_draws
                subscription.amount_paid = amount_to_pay
                subscription.expiry_date = expiry_date
                subscription.active = False
                subscription.payment_completed = False
                subscription.save()

            checkout_session = stripe.checkout.Session.create(
                mode='payment',
                success_url=request.build_absolute_uri(reverse('subscription_success')) + '?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=request.build_absolute_uri(reverse('subscription_cancel')),
                client_reference_id=str(subscription.id),
                customer_email=request.user.email or None,
                line_items=[
                    {
                        'price_data': {
                            'currency': 'eur',
                            'product_data': {
                                'name': f'Midas Lotto subscription for {latest_month}',
                            },
                            'unit_amount': int(amount_to_pay * 100),
                        },
                        'quantity': 1,
                    }
                ],
                metadata={
                    'subscription_id': str(subscription.id),
                    'user_id': str(request.user.id),
                    'monthly_summary_id': str(latest_month.id),
                    'remaining_draws': str(remaining_draws),
                },
            )

            subscription.stripe_checkout_session_id = checkout_session.id
            subscription.save()

            return redirect(checkout_session.url, code=303)
    else:
        form = SubscriptionJoinForm()

    context = {
        'form': form,
        'latest_month': latest_month,
        'remaining_draws': remaining_draws,
        'amount_to_pay': amount_to_pay,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
    }
    return render(request, 'lotto/join_subscription.html', context)
