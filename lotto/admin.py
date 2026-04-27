from django.contrib import admin
from .models import MonthlySummary, Draw, DrawImage, DrawComment, Subscription


class DrawImageInline(admin.TabularInline):
    model = DrawImage
    extra = 1


class DrawCommentInline(admin.TabularInline):
    model = DrawComment
    extra = 0
    readonly_fields = ("user", "body", "created_at")


@admin.register(MonthlySummary)
class MonthlySummaryAdmin(admin.ModelAdmin):
    list_display = ("month", "year", "subscription_price", "total_winnings")
    ordering = ("-year", "-month")


@admin.register(Draw)
class DrawAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "draw_date",
        "draw_number",
        "winnings_amount",
        "is_current",
    )
    list_filter = ("is_current", "draw_date")
    inlines = [DrawImageInline, DrawCommentInline]


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "monthly_summary",
        "draws_paid_for",
        "amount_paid",
        "payment_completed",
        "active",
        "expiry_date",
    )
    list_filter = ("active", "payment_completed", "monthly_summary")
    search_fields = ("user__username", "user__email")


admin.site.register(DrawImage)
admin.site.register(DrawComment)
