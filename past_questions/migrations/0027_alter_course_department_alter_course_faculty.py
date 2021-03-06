# Generated by Django 4.0 on 2021-12-21 01:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("past_questions", "0026_alter_semester_semester"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="department",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="past_questions.department",
            ),
        ),
        migrations.AlterField(
            model_name="course",
            name="faculty",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="past_questions.faculty",
            ),
        ),
    ]
