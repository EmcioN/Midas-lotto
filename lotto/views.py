from datetime import date
import calendar
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from accounts.models import Profile
from .forms import DrawCommentForm, SubscriptionJoinForm
from .models import Draw, MonthlySummary, Subscription


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

    if existing_subscription:
        messages.info(request, 'You already joined the current month.')
        return redirect('profile')

    remaining_draws = Subscription.calculate_remaining_draws(latest_month)

    if request.method == 'POST':
        form = SubscriptionJoinForm(request.POST)
        if form.is_valid():
            full_month_price = form.cleaned_data['full_month_price']
            amount_to_pay = Subscription.calculate_price(full_month_price, remaining_draws)

            subscription = Subscription.objects.create(
                user=request.user,
                monthly_summary=latest_month,
                draws_paid_for=remaining_draws,
                amount_paid=amount_to_pay,
                joined_at=date.today(),
                expiry_date=date(
                    latest_month.year,
                    latest_month.month,
                    calendar.monthrange(latest_month.year, latest_month.month)[1]
                    ),
                active=True
            )

            profile = Profile.objects.get(user=request.user)
            profile.subscription_expiry = subscription.expiry_date
            profile.save()

            messages.success(
                request,
                f'Subscription joined successfully. You were charged for {remaining_draws} remaining draw(s).'
            )
            return redirect('profile')
    else:
        form = SubscriptionJoinForm()

    amount_preview = None
    if remaining_draws >= 0:
        amount_preview = remaining_draws

    context = {
        'form': form,
        'latest_month': latest_month,
        'remaining_draws': remaining_draws,
        'amount_preview': amount_preview,
    }
    return render(request, 'lotto/join_subscription.html', context)
