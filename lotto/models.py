from decimal import Decimal
from django.conf import settings
from django.db import models
from django.utils import timezone


class MonthlySummary(models.Model):
    month = models.PositiveSmallIntegerField()
    year = models.PositiveSmallIntegerField()
    total_winnings = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    notes = models.TextField(blank=True)

    class Meta:
        unique_together = ('month', 'year')
        ordering = ['-year', '-month']

    def __str__(self):
        return f"{self.month:02d}/{self.year}"

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

class DrawImage(models.Model):
    draw = models.ForeignKey(Draw, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='draw_images/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.draw.title}"

class DrawComment(models.Model):
    draw = models.ForeignKey(Draw, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Comment by {self.user.username} on {self.draw.title}"    