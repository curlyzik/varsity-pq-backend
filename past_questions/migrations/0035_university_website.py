# Generated by Django 4.0 on 2022-02-04 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("past_questions", "0034_remove_university_website_alter_university_faculty"),
    ]

    operations = [
        migrations.AddField(
            model_name="university",
            name="website",
            field=models.URLField(blank=True, null=True),
        ),
    ]
