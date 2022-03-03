from django.contrib.auth import get_user_model
from rest_framework import serializers
from dj_rest_auth.serializers import UserDetailsSerializer

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
        ]


class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta(UserDetailsSerializer.Meta):
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
        ]
