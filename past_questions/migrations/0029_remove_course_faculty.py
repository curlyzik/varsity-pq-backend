# Generated by Django 4.0 on 2021-12-21 01:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("past_questions", "0028_alter_course_level_alter_course_semester_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="course",
            name="faculty",
        ),
    ]
