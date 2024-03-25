from django.shortcuts import render
from .models import JobListing
# Create your views here.
from django.contrib.auth.models import User

class CompanyProfile(models.Model):
    user = models.OneToOneField(User, related_name='company_profile', on_delete=models.CASCADE)
    # Other fields
