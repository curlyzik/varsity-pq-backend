# Generated by Django 4.0 on 2021-12-21 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('past_questions', '0025_alter_department_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester',
            name='semester',
            field=models.CharField(choices=[('1', '1st Semester'), ('2', '2nd Semester')], default='1', max_length=50, unique=True),
        ),
    ]
