# Generated by Django 4.0 on 2021-12-21 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('past_questions', '0020_course_faculty_course_university'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='type',
            field=models.CharField(choices=[('federal', 'Federal University'), ('state', 'State University'), ('private', 'Private University')], default='federal', max_length=250),
        ),
    ]
