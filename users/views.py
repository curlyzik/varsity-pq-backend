import random
import string
from django.conf import settings

from django.contrib.auth import get_user_model
from django.http import Http404
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


class VolunteersApiView(APIView):
    permission_classes = [permissions.AllowAny or permissions.IsAuthenticated]

    # get all volunteers
    def get(self, request):
        print(request.user)
        users = User.objects.filter(is_volunteer=True).exclude(email=request.user)
        serializer = UserSerializer(users, many=True)
        return Response(data=serializer.data)


# This class is to update user permissions
class UsersUpdateApiView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    # get single user
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    # set and remove volunteer as admin, active
    def put(self, request, pk):
        user = self.get_object(pk)
        action = request.data.get("action")

        # set user to admin
        if action == "set_admin":
            user.is_staff = True
            user.save()
            return Response(
                data={"message": f"{user.full_name} updated to admin"},
                status=status.HTTP_200_OK,
            )

        # remove as admin
        if action == "remove_admin":
            user.is_staff = False
            user.save()
            return Response(
                data={"message": f"{user.full_name} removed as admin"},
                status=status.HTTP_200_OK,
            )

        # deactivate user account
        if action == "deactivate_user":
            user.is_active = False
            user.save()
            return Response(
                data={"message": f"{user.full_name} account deactivate"},
                status=status.HTTP_200_OK,
            )

        # activate user account
        if action == "activate_user":
            user.is_active = True
            user.save()
            return Response(
                data={"message": f"{user.full_name} account activated"},
                status=status.HTTP_200_OK,
            )

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(
            data={"message": f"{user.full_name} account deleted"},
            status=status.HTTP_200_OK,
        )