# user/models.py
from django.db import models
from django.contrib.auth.models import User
from job.models import JobListing
class UserProfile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    USER_TYPE_CHOICES = [('job_seeker', 'Job Seeker'), ('company_user', 'Company User'),('admin', 'Admin')
    ]
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    # Add more fields as needed

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='resumes/')  # Assuming resumes will be uploaded to 'resumes/' directory
    uploaded_at = models.DateTimeField(auto_now_add=True)

class JobApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(JobListing, on_delete=models.CASCADE)  # Assuming JobListing model exists
    cover_letter = models.TextField()
    applied_at = models.DateTimeField(auto_now_add=True)

class CompanyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    website = models.URLField(blank=True)
    about = models.TextField(blank=True)

# class JobListing(models.Model):
#     company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     required_qualifications = models.TextField()
#     desired_qualifications = models.TextField()
#     responsibilities = models.TextField()
#     application_deadline = models.DateField()
#     salary_range = models.CharField(max_length=100)
#     location = models.CharField(max_length=255)
#     EMPLOYMENT_TYPE_CHOICES = [
#         ('full_time', 'Full-time'),
#         ('part_time', 'Part-time'),
#         ('contract', 'Contract'),
#         ('internship', 'Internship'),
#         ('remote', 'Remote'),
#         ('other', 'Other'),
#     ]
#     employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_TYPE_CHOICES)
#     benefits = models.TextField(blank=True)
#     how_to_apply = models.TextField()