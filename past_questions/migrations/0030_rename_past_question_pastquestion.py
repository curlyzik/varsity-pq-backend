# Generated by Django 4.0 on 2021-12-21 02:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("past_questions", "0029_remove_course_faculty"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Past_Question",
            new_name="PastQuestion",
        ),
    ]
