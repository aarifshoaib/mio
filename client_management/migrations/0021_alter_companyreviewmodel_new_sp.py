# Generated by Django 4.0.5 on 2024-03-29 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_management', '0020_companyreviewmodel_local_col'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyreviewmodel',
            name='new_sp',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
