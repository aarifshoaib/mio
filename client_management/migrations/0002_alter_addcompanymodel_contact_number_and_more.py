# Generated by Django 4.0.5 on 2023-02-27 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcompanymodel',
            name='contact_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='addcompanymodel',
            name='contact_person',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='addcompanymodel',
            name='email',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='addcompanymodel',
            name='roc',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
