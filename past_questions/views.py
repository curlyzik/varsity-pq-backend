from django.http import Http404
from rest_framework import permissions, viewsets, views, status
from rest_framework.response import Response

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
        "create": [permissions.AllowAny],
        "list": [permissions.AllowAny],
        "delete": [permissions.IsAdminUser],
        "update": [permissions.IsAdminUser],
        "destroy": [permissions.IsAdminUser],
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


# This is the department view to create and save
# new department with its selected faculty
class DepartmentCreateApiView(views.APIView):
    def post(self, request):
        try:
            faculty = Faculty.objects.get(name=request.data.get("faculty"))
        except Faculty.DoesNotExist:
            raise Http404

        department = Department.objects.create(
            name=request.data.get("department_name"), faculty=faculty
        )
        serializer = DepartmentSerializer(department)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# This is the department view to update and save
# department with its initial or new faculty
class DepartmentUpdateApiView(views.APIView):
    def get_object(self, pk):
        try:
            return Department.objects.get(pk=pk)
        except Department.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        department = self.get_object(pk)
        department.name = request.data.get("name")
        try:
            department.faculty = Faculty.objects.get(name=request.data.get("faculty"))
        except Faculty.DoesNotExist:
            raise Http404

        serializer = DepartmentSerializer(department)
        return Response(serializer.data)


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
