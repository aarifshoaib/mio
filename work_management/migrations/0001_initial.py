# Generated by Django 4.0.5 on 2023-01-23 10:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agent_candidate', '0008_alter_agentformmodel_candidate_dob_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateTaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('subject', models.TextField()),
                ('employer_name', models.CharField(max_length=300)),
                ('company_name', models.CharField(max_length=300)),
                ('priority', models.CharField(max_length=300, null=True)),
                ('description', models.TextField()),
                ('completed_date', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(max_length=300, null=True)),
                ('asigned_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='asigned_by', to=settings.AUTH_USER_MODEL)),
                ('asigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agent_candidate.createusermodel')),
            ],
        ),
        migrations.CreateModel(
            name='AttachmentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachments', models.FileField(upload_to='CreateTask/')),
                ('task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='work_management.createtaskmodel')),
            ],
        ),
    ]
