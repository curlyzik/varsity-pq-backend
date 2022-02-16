from rest_framework import serializers

from django.contrib.auth import get_user_model

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
