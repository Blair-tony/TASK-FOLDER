from django.db import models
from django.contrib.auth.models import User

class CompanyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, default='')
    description = models.TextField(default='')
    # Add more fields as needed

class JobListing(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, related_name='job_listings',default='')
    job_title = models.CharField(max_length=100, default='')
    job_description = models.TextField(default='')
    required_qualifications = models.TextField(default='')
    desired_qualifications = models.TextField(default='')
    responsibilities = models.TextField(default='')
    application_deadline = models.DateField()
    salary_range = models.CharField(max_length=100, default='')
    location = models.CharField(max_length=100, default='')
    employment_type = models.CharField(max_length=100, default='')
    company_benefits = models.TextField(default='')
    how_to_apply = models.TextField(default='')

    how_to_apply = models.TextField()
    # Add more fields as needed

# class JobApplication(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_applications')
#     job_listing = models.ForeignKey(JobListing, on_delete=models.CASCADE, related_name='job_applications')
#     cover_letter = models.TextField()
#     applied_at = models.DateTimeField(auto_now_add=True)
    # Add more fields as needed
