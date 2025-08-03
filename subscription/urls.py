from django.urls import path
from .views import subscriptions_list

urlpatterns = [
    path('subscriptions/', subscriptions_list, name='subscriptions_list'),
]
