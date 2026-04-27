from django.db.models import Sum
from django.shortcuts import render

from lotto.models import MonthlySummary, Draw


def home(request):
    latest_month = MonthlySummary.objects.first()
    current_draw = Draw.objects.filter(is_current=True).first()
    overall_winnings = (
        MonthlySummary.objects.aggregate(total=Sum("total_winnings"))["total"] or 0
    )

    context = {
        "latest_month": latest_month,
        "current_draw": current_draw,
        "overall_winnings": overall_winnings,
    }
    return render(request, "core/home.html", context)
