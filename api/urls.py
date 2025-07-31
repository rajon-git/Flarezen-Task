from django.urls import path
from .views import RegisterView
from subscription import views as subscription_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name='register'),
    path("login/", TokenObtainPairView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('subscribe/', subscription_views.CreateSubscriptionView.as_view()),
]