# Generated by Django 4.0.5 on 2023-09-20 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agent_candidate', '0020_candidateassigncompanymodel'),
        ('mom_application', '0031_alter_createapplicationqueuemodel_employee_ref'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createapplicationqueuemodel',
            name='employee_ref',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='agent_candidate.agentmanagementcandidataformmodel'),
        ),
    ]
