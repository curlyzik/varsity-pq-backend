from django.http import Http404
from rest_framework import permissions, viewsets, views, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

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


class GetModelObjects:
    def get_model(self, request):
        try:
            university = University.objects.get(name=request.data.get("university"))
        except University.DoesNotExist:
            raise Http404

        try:
            faculty = Faculty.objects.get(name=request.data.get("faculty"))
        except Faculty.DoesNotExist:
            raise Http404

        try:
            department = Department.objects.get(name=request.data.get("department"))
        except Department.DoesNotExist:
            raise Http404

        try:
            level = Level.objects.get(level=request.data.get("level"))
        except Level.DoesNotExist:
            raise Http404

        try:
            year = Year.objects.get(year=request.data.get("year"))
        except Year.DoesNotExist:
            year = Year.objects.get_or_create(year=request.data.get("year"))[0]

        try:
            semester = Semester.objects.get(semester=request.data.get("semester"))
        except Semester.DoesNotExist:
            raise Http404

        return {
            "university": university,
            "faculty": faculty,
            "department": department,
            "level": level,
            "year": year,
            "semester": semester,
        }


class BaseViewSets(viewsets.ModelViewSet):
    # Solution from - https://stackoverflow.com/questions/35970970/django-rest-framework-permission-classes-of-viewset-method
    permission_classes_by_action = {
        "create": [permissions.IsAdminUser],
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

    permission_classes_by_action = {
        "create": [permissions.IsAdminUser],
        "list": [permissions.IsAdminUser],
        "delete": [permissions.IsAdminUser],
        "update": [permissions.IsAdminUser],
        "destroy": [permissions.IsAdminUser],
    }


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


# LIST ALL COURSES
class CourseViewSets(BaseViewSets):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ["university", "faculty", "department", "level", "year", "semester"]


class CourseApiView(views.APIView, GetModelObjects):
    """
    List all Courses, or create a new course.
    """

    permission_classes = [permissions.IsAuthenticated]

    # get all courses created by the authenticated user
    def get(self, request):
        courses = Course.objects.filter(author=request.user).order_by("-updated_at")
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):

        check_if_course_already_exists = Course.objects.filter(
            name=request.data.get("name"),
            course_code=request.data.get("course_code"),
            university=self.get_model(request)["university"],
            faculty=self.get_model(request)["faculty"],
            department=self.get_model(request)["department"],
            level=self.get_model(request)["level"],
            year=self.get_model(request)["year"],
            semester=self.get_model(request)["semester"],
            author=request.user,
        ).exists()

        if check_if_course_already_exists:
            return Response(
                {"message": "Course already exists"}, status=status.HTTP_400_BAD_REQUEST
            )

        course = Course.objects.create(
            name=request.data.get("name"),
            course_code=request.data.get("course_code"),
            university=self.get_model(request)["university"],
            faculty=self.get_model(request)["faculty"],
            department=self.get_model(request)["department"],
            level=self.get_model(request)["level"],
            year=self.get_model(request)["year"],
            semester=self.get_model(request)["semester"],
            author=request.user,
        )
        serializer = CourseSerializer(course)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CourseDetailApiView(views.APIView, GetModelObjects):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        course = self.get_object(pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def put(self, request, pk):
        course = self.get_object(pk)
        course.name = request.data.get("name")
        course.course_code = request.data.get("course_code")

        university = self.get_model(request)["university"]
        course.university = university

        faculty = self.get_model(request)["faculty"]
        course.faculty = faculty

        course.department = self.get_model(request)["department"]
        course.level = self.get_model(request)["level"]
        course.year = self.get_model(request)["year"]
        course.semester = self.get_model(request)["semester"]

        # save the course if the logged in user created the course
        if request.user == course.author:
            course.save()
            serializer = CourseSerializer(course)
            return Response(serializer.data)
        return Response(
            data={"message": "unauthorized to edit course"},
            status=status.HTTP_401_UNAUTHORIZED,
        )


class PastQuestionViewSets(BaseViewSets):
    queryset = PastQuestion.objects.order_by("-updated_at")
    serializer_class = PastQuestionSerializer


class PastQuestionApiView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    # get all past questions created by the authenticated user
    def get(self, request):
        pq = PastQuestion.objects.filter(author=request.user).order_by("-updated_at")
        serializer = PastQuestionSerializer(pq, many=True)
        return Response(serializer.data)

    def post(self, request):
        # get the course you want to create past question for
        course = int(request.data.get("course"))
        try:
            course = Course.objects.get(pk=course, author=request.user)
        except Course.DoesNotExist:
            raise Http404

        # check if logged in user created the course
        if request.user != course.author:
            return Response(
                data={
                    "message": "You are not authorised to create past question for the course"
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )

        file = request.data.get("file")
        author = request.user
        past_question = PastQuestion(file=file, course=course, author=author)

        # check if past question already exists with that course
        if PastQuestion.objects.filter(course=course).exists():
            return Response(
                data={
                    "message": "Cannot create past question that already exists with this course"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        course.has_pastquestion = True
        course.save()
        past_question.save()
        serializer = PastQuestionSerializer(past_question)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PastQuestionDetailApiView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get_object(self, pk):
        try:
            return PastQuestion.objects.get(pk=pk)
        except PastQuestion.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        pq = self.get_object(pk)
        serializer = PastQuestionSerializer(pq)
        return Response(serializer.data)

    def put(self, request, pk):
        pq = self.get_object(pk)
        pq.file = request.data.get("file")

        if request.user == pq.author:
            pq.save()
            serializer = PastQuestionSerializer(pq)
            return Response(serializer.data)
        return Response(
            data={"message": "unauthorized to edit past question"},
            status=status.HTTP_401_UNAUTHORIZED,
        )
