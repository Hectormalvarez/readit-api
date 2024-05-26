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

        user = CustomUser.objects.create(
            username=validated_data["username"]
        )
        user.set_password(validated_data["password1"])
        user.save()
        return user

    class Meta:
        """Meta class"""

        model = CustomUser
        fields = ("id", "username", "password1", "password2", "email")
        read_only_fields = ("id",)
