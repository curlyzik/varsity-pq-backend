from rest_framework import serializers

from .models import (
    Course,
    Department,
    Faculty,
    Level,
    PastQuestion,
    Semester,
    University,
    Year,
)


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ["id", "name"]


class UniversitySerializer(serializers.ModelSerializer):
    faculty = FacultySerializer(many=True, read_only=True)

    class Meta:
        model = University
        fields = ["id", "name", "address", "type", "faculty", "website"]

    def get_faculty(self, obj):
        return obj.faculty.name


class DepartmentSerializer(serializers.ModelSerializer):
    faculty = FacultySerializer()

    class Meta:
        model = Department
        fields = "__all__"


class YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year
        fields = ["id", "year"]


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ["id", "level"]


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = ["id", "semester"]


class CourseSerializer(serializers.ModelSerializer):
    course_details = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ["id", "name", "course_code", "course_details"]

    def get_course_details(self, obj):
        return [
            {
                "university": obj.university.name,
                "faculty": obj.faculty.name,
                "department": obj.department.name,
                "year": obj.year.year,
                "level": obj.level.level,
                "semester": obj.semester.semester,
            }
        ]


class PastQuestionSerializer(serializers.ModelSerializer):
    pq_details = serializers.SerializerMethodField()

    class Meta:
        model = PastQuestion
        fields = ["id", "file", "pq_details"]

    def get_pq_details(self, obj):
        return [
            {
                "course_id": obj.course.id,
                "course": obj.course.name,
                "course_code": obj.course.course_code,
                "university": obj.course.university.name,
                "faculty": obj.course.department.faculty.name,
                "department": obj.course.department.name,
                "year": obj.course.year.year,
                "level": obj.course.level.level,
                "semester": obj.course.semester.semester,
            }
        ]
