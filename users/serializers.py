from django.contrib.auth import get_user_model
from rest_framework import serializers
from dj_rest_auth.serializers import (
    UserDetailsSerializer,
    PasswordResetConfirmSerializer,
)

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "full_name",
            "university",
            "faculty",
            "department",
            "year",
            "email",
            "is_volunteer",
            "is_staff",
            "is_active",
        ]


class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta(UserDetailsSerializer.Meta):
        model = User
        fields = [
            "id",
            "full_name",
            "university",
            "faculty",
            "department",
            "year",
            "email",
            "is_volunteer",
            "is_staff",
            "is_active",
        ]


class CustomPasswordResetConfirmSerializer(PasswordResetConfirmSerializer):
    class Meta:
        ref_name = "dj_rest_auth_reset_password_confirm"
