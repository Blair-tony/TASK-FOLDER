from django.contrib import admin

# Register your models here.
from .models import UserProfile,Profile

admin.site.register(UserProfile)
admin.site.register(Profile)
