# Generated by Django 4.0 on 2022-03-06 19:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        (
            "past_questions",
            "0038_course_author_pastquestion_author_alter_level_level_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="course",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="pastquestion",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="pastquestion",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="level",
            name="level",
            field=models.PositiveIntegerField(
                choices=[
                    (100, "100"),
                    (200, "200"),
                    (300, "300"),
                    (400, "400"),
                    (500, "500"),
                    (600, "600"),
                ],
                unique=True,
            ),
        ),
    ]
