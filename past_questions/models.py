from django.db import models

class University(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    website = models.URLField(max_length=200)
    type = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Faculty(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey("Department", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    

class Department(models.Model):
    name = models.CharField(max_length=50)
    courses = models.ForeignKey("Course", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name