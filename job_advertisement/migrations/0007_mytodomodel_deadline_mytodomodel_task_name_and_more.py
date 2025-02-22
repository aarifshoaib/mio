# Generated by Django 4.0.5 on 2023-10-13 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_advertisement', '0006_mytodomodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='mytodomodel',
            name='deadline',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='mytodomodel',
            name='task_name',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='mytodomodel',
            name='task',
            field=models.TextField(null=True),
        ),
    ]
