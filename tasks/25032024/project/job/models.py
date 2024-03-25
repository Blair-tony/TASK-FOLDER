

from django.db import models
from django.contrib.auth.models import User

class JobListing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    required_qualifications = models.TextField()
    desired_qualifications = models.TextField()
    responsibilities = models.TextField()
    application_deadline = models.DateField()
    salary_range = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    employment_type = models.CharField(max_length=100)
    company_benefits = models.TextField()
    how_to_apply = models.TextField()
    other_information = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class CompanyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
