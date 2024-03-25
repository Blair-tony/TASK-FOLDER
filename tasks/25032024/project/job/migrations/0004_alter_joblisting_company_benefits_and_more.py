# Generated by Django 5.0.3 on 2024-03-25 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_remove_joblisting_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joblisting',
            name='company_benefits',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='joblisting',
            name='desired_qualifications',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='joblisting',
            name='employment_type',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='joblisting',
            name='job_description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='joblisting',
            name='job_title',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='joblisting',
            name='location',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='joblisting',
            name='required_qualifications',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='joblisting',
            name='responsibilities',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='joblisting',
            name='salary_range',
            field=models.CharField(default='', max_length=100),
        ),
    ]
