# Generated by Django 4.0.5 on 2024-01-05 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent_candidate', '0020_candidateassigncompanymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='DashboardModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datas', models.JSONField()),
            ],
        ),
    ]
