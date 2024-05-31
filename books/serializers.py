"""books serializers"""

from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    """User serializer"""

    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def create(self, validated_data):
        if validated_data["password1"] != validated_data["password2"]:
            raise serializers.ValidationError({"password": "Passwords must match."})

        data = {
            key: value
            for key, value in validated_data.items()
            if key not in ("password1", "password2")
        }
        data["password"] = validated_data["password1"]
        return self.Meta.model.objects.create_user(**data)

    class Meta:
        """Meta class"""

        model = CustomUser
        fields = (
            "id",
            "username",
            "password1",
            "password2",
            "email",
            "first_name",
            "last_name",
        )
        read_only_fields = ("id",)
        extra_kwargs = {
            "password1": {"write_only": True},
            "password2": {"write_only": True},
        }
