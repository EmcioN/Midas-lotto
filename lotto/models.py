from decimal import Decimal

from django.conf import settings
from django.db import models
from django.utils import timezone


class Draw(models.Model):
    monthly_summary = models.ForeignKey(
        MonthlySummary,
        on_delete=models.CASCADE,
        related_name='draws'
    )
    title = models.CharField(max_length=200)
    draw_date = models.DateField()
    draw_number = models.PositiveSmallIntegerField()
    result_text = models.TextField(blank=True)
    winnings_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_current = models.BooleanField(default=False)

    class Meta:
        ordering = ['-draw_date', '-draw_number']

    def __str__(self):
        return f"{self.title} ({self.draw_date})"

