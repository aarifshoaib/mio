# Generated by Django 4.0.5 on 2023-05-27 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mom_application', '0024_remove_cpfinvoicemodel_filename_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationQueueFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachments', models.FileField(null=True, upload_to='ApplicationQueueFiles/')),
            ],
        ),
        migrations.RemoveField(
            model_name='createapplicationqueuemodel',
            name='upload_docs',
        ),
        migrations.AddField(
            model_name='createapplicationqueuemodel',
            name='upload_docs',
            field=models.ManyToManyField(to='mom_application.applicationqueuefiles'),
        ),
    ]
