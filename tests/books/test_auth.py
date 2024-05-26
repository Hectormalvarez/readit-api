"""testing authentication api endpoints"""

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


PASSWORD = "pAssw0rd!"


class AuthenticationTest(APITestCase):
    """Test case for the authentication API endpoints."""

    def test_user_can_sign_up(self):
        """Test that a user can sign up."""
        response = self.client.post(
            reverse("sign_up"),
            data={
                "username": "user@example.com",
                "first_name": "Test",
                "last_name": "User",
                "password1": PASSWORD,
                "password2": PASSWORD,
            },
        )
        user = get_user_model().objects.last()
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(response.data["id"], user.id)
        self.assertEqual(response.data["username"], user.username)

