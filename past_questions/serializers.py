from django.db.models import fields
from rest_framework import serializers

from .models import (Course, Department, Faculty, Level, Past_Question, Semester, University,
                     Year)

class FacultySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Faculty
        fields = ['name']

class UniversitySerializer(serializers.ModelSerializer):
    faculty = FacultySerializer(many=True)

    class Meta:
        model = University
        fields = ['name', 'address', 'website', 'type', 'faculty']
    
    def get_faculty(self, obj):
        return obj.faculty.name

class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = '__all__'

class YearSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Year
        fields = '__all__'

class LevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Level
        fields = '__all__'

class SemesterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Semester
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'

class PastQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Past_Question
        fields = '__all__'