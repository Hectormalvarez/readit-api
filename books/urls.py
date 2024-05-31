"""urls for books"""
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import LogInView, SignupView


urlpatterns = [
    path("sign_up/", SignupView.as_view(), name="sign_up"),
    path("log_in/", LogInView.as_view(), name="log_in"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
