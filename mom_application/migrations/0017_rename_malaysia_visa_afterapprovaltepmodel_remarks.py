# Generated by Django 4.0.5 on 2023-04-26 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mom_application', '0016_workpassmodel_rejected_reason'),
    ]

    operations = [
        migrations.RenameField(
            model_name='afterapprovaltepmodel',
            old_name='malaysia_visa',
            new_name='remarks',
        ),
    ]
