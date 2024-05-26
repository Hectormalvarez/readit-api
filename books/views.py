"""readit views"""
from rest_framework import generics, permissions

from .models import CustomUser
from .serializers import UserSerializer


class SignupView(generics.CreateAPIView):
    """Signup view"""
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
