"""testing authentication api endpoints"""

import base64
import json

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse
import pytest

PASSWORD = "pAssw0rd!"


def create_user(username="user@example.com", password=PASSWORD):
    """Create and return a new user."""
    return get_user_model().objects.create_user(
        username=username, first_name="Test", last_name="User", password=password
    )


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
    url = reverse("sign_up")
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
    create_user(username=valid_user_data["username"])
    url = reverse("sign_up")
    response = client.post(url, valid_user_data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "username" in response.data


@pytest.mark.django_db
def test_customuser_full_name(valid_user_data):
    """Test the full_name property of CustomUser."""
    user = create_user(username=valid_user_data["username"])
    assert user.full_name == f"{user.first_name} {user.last_name}"


@pytest.mark.django_db
def test_user_can_log_in(client, valid_user_data):
    """Test that a user can log in."""
    user = create_user(username=valid_user_data["username"])
    url = reverse("log_in")
    response = client.post(
        url, data={"username": valid_user_data["username"], "password": PASSWORD}
    )
    assert response.status_code == status.HTTP_200_OK
    assert "refresh" in response.data
    assert "access" in response.data

    access_token = response.data["access"]
    header, payload, signature = access_token.split(".")
    decoded_payload = base64.b64decode(f"{payload}==").decode("utf-8")
    payload_data = json.loads(decoded_payload)

    assert payload_data["id"] == user.id
    assert payload_data["username"] == user.username
    assert payload_data['email'] == user.email
