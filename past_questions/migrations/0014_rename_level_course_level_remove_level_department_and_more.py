# Generated by Django 4.0 on 2021-12-19 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("past_questions", "0013_remove_level_course_course_level"),
    ]

    operations = [
        migrations.RenameField(
            model_name="course",
            old_name="Level",
            new_name="level",
        ),
        migrations.RemoveField(
            model_name="level",
            name="department",
        ),
        migrations.RemoveField(
            model_name="level",
            name="semester",
        ),
        migrations.RemoveField(
            model_name="level",
            name="year",
        ),
        migrations.AddField(
            model_name="course",
            name="department",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="past_questions.department",
            ),
        ),
        migrations.AddField(
            model_name="course",
            name="semester",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="past_questions.semester",
            ),
        ),
        migrations.AddField(
            model_name="course",
            name="year",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="past_questions.year",
            ),
        ),
    ]
