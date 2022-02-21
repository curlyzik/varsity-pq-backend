from rest_framework import permissions, viewsets

# from url_filter.integrations.drf import DjangoFilterBackend

from django_url_filter.url_filter.integrations.drf import DjangoFilterBackend

from past_questions.models import (
    Course,
    Department,
    Faculty,
    Level,
    PastQuestion,
    Semester,
    University,
    Year,
)
from past_questions.serializers import (
    CourseSerializer,
    DepartmentSerializer,
    FacultySerializer,
    LevelSerializer,
    PastQuestionSerializer,
    SemesterSerializer,
    UniversitySerializer,
    YearSerializer,
)


class BaseViewSets(viewsets.ModelViewSet):
    # Solution from - https://stackoverflow.com/questions/35970970/django-rest-framework-permission-classes-of-viewset-method
    permission_classes_by_action = {
        "create": [permissions.AllowAny],  # Change later to permissions.IsAdminUser
        "list": [permissions.AllowAny],  # Change later to permissions.IsAdminUser
        "delete": [permissions.AllowAny],
        "update": [permissions.AllowAny],
        "destroy": [permissions.AllowAny],
    }

    def get_permissions(self):
        try:
            # return permission_classes depending on `action` dev
            return [
                permission()
                for permission in self.permission_classes_by_action[self.action]
            ]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]


class UniversityViewSets(BaseViewSets):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer


class FacultyViewSets(BaseViewSets):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    filter_backends = [DjangoFilterBackend]


class DepartmentViewSets(BaseViewSets):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ["faculty"]


class YearViewSets(BaseViewSets):
    queryset = Year.objects.all()
    serializer_class = YearSerializer


class LevelViewSets(BaseViewSets):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class SemesterViewSets(BaseViewSets):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer


class CourseViewSets(BaseViewSets):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ["university", "faculty", "department", "level", "year", "semester"]


class PastQuestionViewSets(BaseViewSets):
    queryset = PastQuestion.objects.all()
    serializer_class = PastQuestionSerializer
