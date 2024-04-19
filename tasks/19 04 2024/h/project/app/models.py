from django.db import models
from django.contrib.auth.models import User
 
class Role(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
 
    def __str__(self):
        return self.name
   
class Snippet(models.Model):
    car = models.CharField(max_length=100)
    code = models.TextField()
    colour = models.CharField(max_length=100)
    year = models.DateTimeField(auto_now_add=True)
 
 
   
class Tag(models.Model):
    name = models.CharField(max_length=100)
 
    def __str__(self):
        return self.name
 
class car(models.Model):
    carname = models.CharField(max_length=100)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    year = models.DateField()
 
