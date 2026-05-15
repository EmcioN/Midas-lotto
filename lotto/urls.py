from django.urls import path

from .views import (
    delete_comment,
    draw_detail,
    draw_list,
    join_subscription,
    stripe_webhook,
    subscription_cancel,
    subscription_success,
)


urlpatterns = [
    path("draws/", draw_list, name="draw_list"),
    path("draws/<int:draw_id>/", draw_detail, name="draw_detail"),
    path(
        "subscriptions/join/",
        join_subscription,
        name="join_subscription",
    ),
    path(
        "subscriptions/success/",
        subscription_success,
        name="subscription_success",
    ),
    path(
        "subscriptions/cancel/",
        subscription_cancel,
        name="subscription_cancel",
    ),
    path("stripe/webhook/", stripe_webhook, name="stripe_webhook"),
    path(
        "comments/<int:comment_id>/delete/",
        delete_comment,
        name="delete_comment",
    ),
]
