# Generated by Django 5.0.3 on 2024-03-25 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_joblisting_companyprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joblisting',
            name='job_title',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
