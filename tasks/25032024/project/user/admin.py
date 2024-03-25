from django.contrib import admin

# Register your models here.
from .models import UserProfile,Profile,CompanyProfile,JobApplication,Resume
admin.site.register(UserProfile)
# admin.site.register(CompanyProfile)
admin.site.register(JobApplication)
admin.site.register(Resume)
