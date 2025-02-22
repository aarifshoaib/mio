# Generated by Django 4.0.6 on 2023-03-24 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client_management', '0003_newclientmodel_client_id'),
        ('work_management', '0005_alter_createtaskmodel_company_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createtaskmodel',
            name='company_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='client_management.addcompanymodel'),
        ),
        migrations.AlterField(
            model_name='createtaskmodel',
            name='employer_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='client_management.newclientmodel'),
        ),
    ]
