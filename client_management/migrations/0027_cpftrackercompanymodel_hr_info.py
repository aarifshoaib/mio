# Generated by Django 4.0.5 on 2024-07-18 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_management', '0026_cpftrackercompanymodel_addcompanymodel_cpf_tracker'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpftrackercompanymodel',
            name='hr_info',
            field=models.JSONField(null=True),
        ),
    ]
