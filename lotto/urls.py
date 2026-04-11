from django.urls import path
from .views import draw_list, draw_detail, join_subscription

urlpatterns = [
    path('draws/', draw_list, name='draw_list'),
    path('draws/<int:draw_id>/', draw_detail, name='draw_detail'),
    path('subscriptions/join/', join_subscription, name='join_subscription'),
]
