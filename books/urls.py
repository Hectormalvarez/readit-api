"""urls for books"""
from django.urls import path


from .views import SignupView


urlpatterns = [
    path("sign_up/", SignupView.as_view(), name="sign_up"),
]
