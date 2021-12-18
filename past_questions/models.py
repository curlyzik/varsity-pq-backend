from django.db import models

class University(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    website = models.URLField(max_length=200)
    type = models.CharField(max_length=50)
    faculty = models.ForeignKey("Faculty", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class Faculty(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey("Department", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
class Year(models.Model):
    year = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.year

class Department(models.Model):
    name = models.CharField(max_length=50)
    level = models.ForeignKey("Level", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class Level(models.Model):
    LEVEL_CHOICES = (
        (100, '100'),
        (200, '200'),
        (300, '300'),
        (400, '400'),
        (500, '500')
    )
    level = models.PositiveIntegerField(choices=LEVEL_CHOICES)
    semester = models.ForeignKey("Semester", on_delete=models.CASCADE)



class Semester(models.Model):
    SEMESTER_CHOICES = (
            ("1", "1st Semester"), 
            ("2", "2nd Semester")
        )
    semester = models.CharField(max_length=50, choices=SEMESTER_CHOICES, default="1")
    courses = models.ForeignKey("Course", on_delete=models.CASCADE)

class Course(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self) -> str:
        return self.name