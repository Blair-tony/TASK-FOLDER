from django import forms
from .models import JobListing,CompanyProfile

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

