# Generated by Django 4.0.5 on 2023-05-30 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mom_application', '0025_applicationqueuefiles_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailAttachmentsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachments', models.FileField(null=True, upload_to='EmailAttachments/')),
            ],
        ),
        migrations.AddField(
            model_name='emailtrackermodel',
            name='attachments',
            field=models.ManyToManyField(to='mom_application.emailattachmentsmodel'),
        ),
    ]
