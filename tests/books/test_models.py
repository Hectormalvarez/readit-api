import pytest
from books.models import CustomUser


@pytest.mark.django_db
class TestCustomUser:
    def test_create_user(self):
        user = CustomUser.objects.create_user(
            username="testuser", email="test@example.com", password="testpass"
        )
        assert user.username == "testuser"
        assert user.email == "test@example.com"

    def test_update_user(self):
        user = CustomUser.objects.create_user(
            username="testuser", email="test@example.com", password="testpass"
        )
        user.first_name = "John"
        user.last_name = "Doe"
        user.save()
        assert user.first_name == "John"
        assert user.last_name == "Doe"

    def test_delete_user(self):
        user = CustomUser.objects.create_user(
            username="testuser", email="test@example.com", password="testpass"
        )
        user.delete()
        assert not CustomUser.objects.filter(username="testuser").exists()
