from django.db import models


def pq_file_upload_path(instance, filename):
    return f"{instance.course.university}/{instance.course.department}/{instance.course.year}/{instance.course.level}/{instance.course.semester}/{instance.course.course_code}{filename}"


class University(models.Model):
    TYPE_CHOICE = (
        ("federal", "Federal University"),
        ("state", "State University"),
        ("private", "Private University"),
    )
    name = models.CharField(max_length=50)
    address = models.TextField()
    website = models.URLField(max_length=200, null=True, blank=True)
    type = models.CharField(default="federal", choices=TYPE_CHOICE, max_length=250)

    def __str__(self) -> str:
        return self.name


class Faculty(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self) -> str:
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=50, unique=True)
    faculty = models.ForeignKey(
        Faculty, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self) -> str:
        return f"{self.name} in {self.faculty}"


class Year(models.Model):
    year = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.year


class Level(models.Model):
    LEVEL_CHOICES = (
        (100, "100"),
        (200, "200"),
        (300, "300"),
        (400, "400"),
        (500, "500"),
    )
    level = models.PositiveIntegerField(choices=LEVEL_CHOICES, unique=True)

    def __str__(self) -> str:
        return f"{self.level}"


class Semester(models.Model):
    SEMESTER_CHOICES = (("1", "1st Semester"), ("2", "2nd Semester"))
    semester = models.CharField(
        max_length=50, choices=SEMESTER_CHOICES, default="1", unique=True
    )

    def __str__(self) -> str:
        if self.semester == "1":
            return f"{self.semester}st Semester"
        return f"{self.semester}nd Semester"


class Course(models.Model):
    name = models.CharField(max_length=250)
    course_code = models.CharField(max_length=50, blank=True, null=True)
    university = models.ForeignKey(
        "University", on_delete=models.CASCADE, blank=True, null=True
    )
    faculty = models.ForeignKey(
        "Faculty", on_delete=models.CASCADE, blank=True, null=True
    )
    department = models.ForeignKey(
        "Department", on_delete=models.CASCADE, blank=True, null=True
    )
    year = models.ForeignKey("Year", on_delete=models.CASCADE, blank=True, null=True)
    level = models.ForeignKey("Level", on_delete=models.CASCADE, blank=True, null=True)
    semester = models.ForeignKey(
        "Semester", on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self) -> str:
        return f"{self.course_code}/{self.name} - {self.university} - {self.level} level - {self.department} - {self.semester} - {self.year} session"


class PastQuestion(models.Model):
    file = models.FileField(upload_to=pq_file_upload_path, max_length=1000)
    course = models.OneToOneField(
        "Course", on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self) -> str:
        return f"{self.course.name}/{self.course.course_code} - {self.course.university} - {self.course.faculty} - {self.course.department} - {self.course.year} session - {self.course.level} level - {self.course.semester} semester"
