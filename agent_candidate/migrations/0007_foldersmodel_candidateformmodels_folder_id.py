# Generated by Django 4.0.6 on 2023-01-12 16:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agent_candidate', '0006_agentformmodel_current_location_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoldersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folder_name', models.CharField(max_length=250, unique=True)),
                ('createdby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='candidateformmodels',
            name='folder_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='agent_candidate.foldersmodel'),
        ),
    ]
