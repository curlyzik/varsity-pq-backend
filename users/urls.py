from django.urls import path
from dj_rest_auth.views import PasswordResetConfirmView

from . import views

urlpatterns = [
    path("new-volunteer/", views.VolunteerRequest.as_view()),
    path(
        "password/reset/confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path("update/<int:pk>/", views.UsersUpdateApiView.as_view()),
]
