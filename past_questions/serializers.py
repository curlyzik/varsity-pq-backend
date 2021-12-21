from rest_framework import serializers

from .models import (Course, Department, Faculty, Level, PastQuestion,
                     Semester, University, Year)


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
    faculty = FacultySerializer()

    class Meta:
        model = Department
        fields = '__all__'

class YearSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Year
        fields = ['year']

class LevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Level
        fields = ['level']

class SemesterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Semester
        fields = ['semester']

class CourseSerializer(serializers.ModelSerializer):
    university = UniversitySerializer()
    department = DepartmentSerializer()
    year = YearSerializer()
    level = LevelSerializer()
    semester = Semester()

    class Meta:
        model = Course
        fields = '__all__'
    
class PastQuestionSerializer(serializers.ModelSerializer):
    course = serializers.SerializerMethodField()
    class Meta:
        model = PastQuestion
        fields = ['id', 'file', 'course']
    
    def get_course(self, obj):
        return obj.course.name
