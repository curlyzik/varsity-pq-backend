from django.urls import path, include
from rest_framework import routers

from past_questions import views

router = routers.DefaultRouter()
router.register(r"universities", views.UniversityViewSets)
router.register(r"faculty", views.FacultyViewSets)
router.register(r"department", views.DepartmentViewSets)
router.register(r"year", views.YearViewSets)
router.register(r"level", views.LevelViewSets)
router.register(r"semester", views.SemesterViewSets)
router.register(r"course", views.CourseViewSets)
router.register(r"past_question", views.PastQuestionViewSets)


urlpatterns = [
    path("", include(router.urls)),
    path("department-create/", views.DepartmentCreateApiView.as_view()),
    path("department-update/<int:pk>/", views.DepartmentUpdateApiView.as_view()),
    path("courses/", views.CourseApiView.as_view()),
    path("courses/<int:pk>/", views.CourseDetailApiView.as_view()),
    path("past-questions/", views.PastQuestionApiView.as_view()),
    path("past-questions/<int:pk>/", views.PastQuestionDetailApiView.as_view()),
]
