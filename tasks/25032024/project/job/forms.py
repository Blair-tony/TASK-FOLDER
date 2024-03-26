from django import forms
from .models import JobListing,CompanyProfile
from user.models import UserProfile,JobApplication


class JobListingForm(forms.ModelForm):
    class Meta:
        model = JobListing
        fields = '__all__'

# class JobApplicationForm(forms.ModelForm):
#     class Meta:
#         model = JobApplication
#         fields = ['cover_letter']

class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        fields = '__all__'


