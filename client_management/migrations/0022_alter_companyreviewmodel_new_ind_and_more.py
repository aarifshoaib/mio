# Generated by Django 4.0.5 on 2024-03-29 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_management', '0021_alter_companyreviewmodel_new_sp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyreviewmodel',
            name='new_ind',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='companyreviewmodel',
            name='new_prc',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='companyreviewmodel',
            name='new_wp',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
