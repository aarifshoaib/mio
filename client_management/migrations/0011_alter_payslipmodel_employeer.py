# Generated by Django 4.0.5 on 2023-06-21 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client_management', '0010_payslipmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payslipmodel',
            name='employeer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='client_management.addcompanymodel'),
        ),
    ]
