# Generated by Django 5.0.3 on 2024-03-26 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_jobapplication_resume'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapplication',
            name='resume',
        ),
    ]
