# Generated by Django 4.0 on 2022-01-24 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("past_questions", "0033_course_faculty"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="university",
            name="website",
        ),
        migrations.AlterField(
            model_name="university",
            name="faculty",
            field=models.ManyToManyField(
                blank=True, related_name="university", to="past_questions.Faculty"
            ),
        ),
    ]
