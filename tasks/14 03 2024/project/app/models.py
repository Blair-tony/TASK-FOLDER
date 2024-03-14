from django.db import models

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=120)
    author=models.CharField(max_length=20)
    genre=models.CharField(max_length=20)
    language=models.CharField(max_length=20)
    year=models.IntegerField()

class NewBook(models.Model):
    title=models.CharField(max_length=120)

class Library(models.Model):
    name=models.CharField(max_length=120)
    place=models.CharField(max_length=120)
    record_id=models.IntegerField()