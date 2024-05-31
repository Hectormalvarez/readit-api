"""testing authentication api endpoints"""

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse
import pytest

PASSWORD = "pAssw0rd!"


@pytest.fixture
def valid_user_data():
    """Returns a dictionary with valid user data."""
    return {
        "username": "user@example.com",
        "email": "user@example.com",
        "first_name": "Test",
        "last_name": "User",
        "password1": PASSWORD,
        "password2": PASSWORD,
    }


@pytest.mark.django_db
def test_user_can_sign_up(client, valid_user_data):
    """Test that a user can sign up."""
    url = reverse("sign_up")  # Make sure your URL name for signup is correct
    response = client.post(url, valid_user_data)
    assert response.status_code == status.HTTP_201_CREATED

    user = get_user_model().objects.get(username=valid_user_data["username"])
    assert response.data["id"] == user.id
    assert response.data["username"] == user.username
    assert response.data["first_name"] == user.first_name
    assert response.data["last_name"] == user.last_name


@pytest.mark.django_db
def test_user_cannot_sign_up_with_existing_username(client, valid_user_data):
    """Test that a user cannot sign up with an existing username."""
    url = reverse("sign_up")  # Make sure your URL name for signup is correct
    client.post(url, valid_user_data)  # Create the user first
    response = client.post(url, valid_user_data)  # Try to create with same data
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "username" in response.data


@pytest.mark.django_db
def test_customuser_full_name(valid_user_data):
    """Test the full_name property of CustomUser."""
    user = get_user_model().objects.create_user(
        username=valid_user_data["username"],
        email=valid_user_data["email"],
        first_name=valid_user_data["first_name"],
        last_name=valid_user_data["last_name"],
        password=valid_user_data["password1"],
    )
    assert user.full_name == f"{user.first_name} {user.last_name}"
