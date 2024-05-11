"""models for books api"""

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Custom user model with additional fields."""

    profile_picture_url = models.URLField(blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)

    @property
    def full_name(self):
        """Returns the full name of the user."""
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def create_user(cls, username, email, password):
        """Creates a new user with the given username, email, and password."""
        user = cls(username=username, email=email)
        user.set_password(password)
        user.save()
        return user
