# Generated by Django 4.0.5 on 2023-04-08 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_management', '0006_createordermodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='createordermodel',
            name='application_id',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='createordermodel',
            name='result',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
