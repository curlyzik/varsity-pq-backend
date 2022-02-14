import random
import string

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserSerializer

User = get_user_model()


class VolunteerRequest(APIView):
    def post(self, request):
        print(request)
        full_name = request.data.get("full_name")
        university = request.data.get("university")
        faculty = request.data.get("faculty")
        department = request.data.get("department")
        year = request.data.get("year")
        email = request.data.get("email")

        volunteer = User.objects.create(
            full_name=full_name,
            university=university,
            faculty=faculty,
            department=department,
            year=year,
            email=email,
        )
        password = "".join(
            random.choice(string.ascii_uppercase + string.digits) for _ in range(15)
        )
        volunteer.set_password(password)
        volunteer.is_staff = True
        volunteer.save()

        serializer = UserSerializer(volunteer)
        return Response(
            status=status.HTTP_201_CREATED,
            data={"password": password, "data": serializer.data},
        )


# class GetUsers(APIView):
#     permission_classes = [permissions.AllowAny]
#     def get(self, request):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)
