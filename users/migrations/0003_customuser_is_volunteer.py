# Generated by Django 4.0 on 2022-02-16 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_department_customuser_faculty_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_volunteer',
            field=models.BooleanField(default=True),
        ),
    ]
