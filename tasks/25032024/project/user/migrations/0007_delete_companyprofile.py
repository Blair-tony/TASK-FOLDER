# Generated by Django 5.0.3 on 2024-03-25 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_delete_joblisting'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CompanyProfile',
        ),
    ]
