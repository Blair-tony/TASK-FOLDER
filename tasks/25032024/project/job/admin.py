from django.contrib import admin

# Register your models here.
from .models import JobApplication,JobListing,CompanyProfile

admin.site.register(JobApplication)
admin.site.register(JobListing)
admin.site.register(CompanyProfile)
