from django.urls import path

from . import views

urlpatterns = [
    path("new-volunteer/", views.VolunteerRequest.as_view()),
]
