import random
import string

from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions

from users.serializers import UserSerializer

User = get_user_model()


class VolunteerRequest(APIView):
    def post(self, request):
        full_name = request.data.get("full_name")
        university = request.data.get("university")
        faculty = request.data.get("faculty")
        department = request.data.get("department")
        year = request.data.get("year")
        email = request.data.get("email")

        if User.objects.filter(email=email).exists():
            return Response(
                data={"detail": "User with this email already exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        volunteer = User.objects.create(
            full_name=full_name,
            university=university,
            faculty=faculty,
            department=department,
            year=year,
            email=email,
        )
        password = "".join(
            random.choice(
                string.ascii_uppercase + string.digits + string.ascii_lowercase
            )
            for _ in range(8)
        )
        volunteer.set_password(password)
        volunteer.save()

        serializer = UserSerializer(volunteer)
        return Response(
            status=status.HTTP_201_CREATED,
            data={"password": password, "data": serializer.data},
        )
