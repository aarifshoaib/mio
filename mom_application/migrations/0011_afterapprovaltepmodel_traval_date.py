# Generated by Django 4.0.5 on 2023-04-17 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mom_application', '0010_afterapprovaltepmodel_upload_ipa'),
    ]

    operations = [
        migrations.AddField(
            model_name='afterapprovaltepmodel',
            name='traval_date',
            field=models.DateField(null=True),
        ),
    ]
