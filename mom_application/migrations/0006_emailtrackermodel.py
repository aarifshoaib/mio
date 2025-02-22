# Generated by Django 4.0.5 on 2023-04-01 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mom_application', '0005_workpassmodel_source'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailTrackerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_user', models.CharField(max_length=1000, null=True)),
                ('subject', models.CharField(max_length=1000, null=True)),
                ('receive_date', models.CharField(max_length=300, null=True)),
                ('body', models.TextField(null=True)),
            ],
        ),
    ]
