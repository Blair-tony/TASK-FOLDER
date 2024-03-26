# Generated by Django 5.0.3 on 2024-03-23 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobListing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('required_qualifications', models.TextField()),
                ('desired_qualifications', models.TextField()),
                ('responsibilities', models.TextField()),
                ('application_deadline', models.DateField()),
                ('salary_range', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=255)),
                ('employment_type', models.CharField(max_length=100)),
                ('company_benefits', models.TextField()),
                ('how_to_apply', models.TextField()),
                ('other_information', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
