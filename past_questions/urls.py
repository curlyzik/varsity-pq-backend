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
]
