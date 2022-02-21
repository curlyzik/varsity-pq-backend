from django.contrib.auth import get_user_model
from rest_framework import serializers

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
