from django.contrib import admin

from past_questions.models import (Course, Department, Faculty, Level,
                                   Past_Question, Semester, University, Year)

admin.site.register(University)
admin.site.register(Faculty)
admin.site.register(Year)
admin.site.register(Department)
admin.site.register(Level)
admin.site.register(Semester)
admin.site.register(Course)
admin.site.register(Past_Question)
