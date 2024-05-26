"""testing authentication api endpoints"""

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse

PASSWORD = "pAssw0rd!"


def test_user_can_sign_up(client):
    """Test that a user can sign up."""
    url = reverse("sign_up")
    data = {
        "username": "user@example.com",
        "first_name": "Test",
        "last_name": "User",
        "password1": PASSWORD,
        "password2": PASSWORD,
    }
    response = client.post(url, data)
    assert status.HTTP_201_CREATED == response.status_code

    user = get_user_model().objects.get(username="user@example.com")
    assert response.data["id"] == user.id
    assert response.data["username"] == user.username
    assert response.data["first_name"] == user.first_name
    assert response.data["last_name"] == user.last_name


def test_user_cannot_sign_up_with_existing_username(client):
    """Test that a user cannot sign up with an existing username."""
    client.post(
        reverse("sign_up"),
        data={
            "username": "user@example.com",
            "first_name": "Test",
            "last_name": "User",
            "password1": PASSWORD,
            "password2": PASSWORD,
        },
    )
    response = client.post(
        reverse("sign_up"),
        data={
            "username": "user@example.com",
            "first_name": "Test",
            "last_name": "User",
            "password1": PASSWORD,
            "password2": PASSWORD,
        },
    )
    assert status.HTTP_400_BAD_REQUEST == response.status_code
    assert "username" in response.data


def test_user_cannot_sign_up_with_mismatched_passwords(client):
    """Test that a user cannot sign up with mismatched passwords."""
    response = client.post(
        reverse("sign_up"),
        data={
            "username": "user@example.com",
            "first_name": "Test",
            "last_name": "User",
            "password1": PASSWORD,
            "password2": "wrong_password",
        },
    )
    assert status.HTTP_400_BAD_REQUEST == response.status_code
    assert "password2" in response.data


def test_user_cannot_sign_up_with_blank_username(client):
    """Test that a user cannot sign up with a blank username."""
    response = client.post(
        reverse("sign_up"),
        data={
            "username": "",
            "first_name": "Test",
            "last_name": "User",
            "password1": PASSWORD,
            "password2": PASSWORD,
        },
    )
    assert status.HTTP_400_BAD_REQUEST == response.status_code
    assert "username" in response.data

