# Generated by Django 4.0.5 on 2023-10-14 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_advertisement', '0007_mytodomodel_deadline_mytodomodel_task_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mytodomodel',
            name='task_name',
        ),
        migrations.AddField(
            model_name='mytodomodel',
            name='created_date',
            field=models.DateField(auto_now=True),
        ),
    ]
