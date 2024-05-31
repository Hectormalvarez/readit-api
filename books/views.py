"""readit views"""
from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import CustomUser
from .serializers import LogInSerializer, UserSerializer


class SignupView(generics.CreateAPIView):
    """Signup view"""
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class LogInView(TokenObtainPairView):
    """Login view"""

    serializer_class = LogInSerializer
