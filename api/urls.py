from django.urls import path
from .views import RegisterView
from subscription import views as subscription_views
from exchangerate import views as exchnagerate_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name='register'),
    path("login/", TokenObtainPairView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('subscribe/', subscription_views.CreateSubscriptionView.as_view()),
    path('subscriptions/', subscription_views.UserSubscriptionsListView.as_view()),
    path('cancel/<int:subscription_id>/', subscription_views.CancelSubscriptionView.as_view()),
    path('exchange-rate/', exchnagerate_views.ExchangeRateView.as_view()),
]