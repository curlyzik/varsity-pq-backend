from django.shortcuts import render

from rest_framework import viewsets

from past_questions.models import Course, Department, Faculty, Level, PastQuestion, Semester, University, Year
from past_questions.serializers import CourseSerializer, FacultySerializer, LevelSerializer, PastQuestionSerializer, SemesterSerializer, UniversitySerializer, DepartmentSerializer, YearSerializer

# Create your views here.

class UniversityViewSets(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class  = UniversitySerializer

class FacultyViewSets(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class  = FacultySerializer

class DepartmentViewSets(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class YearViewSets(viewsets.ModelViewSet):
    queryset = Year.objects.all()
    serializer_class = YearSerializer

class LevelViewSets(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class SemesterViewSets(viewsets.ModelViewSet):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer

class CourseViewSets(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class PastQuestionViewSets(viewsets.ModelViewSet):
    queryset = PastQuestion.objects.all()
    serializer_class = PastQuestionSerializer