# user/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
from .models import Profile, Resume, JobApplication
from .models import CompanyProfile, JobListing

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    user_type = forms.ChoiceField(choices=[('job_seeker', 'Job Seeker'), 
                                           ('company_user', 'Company User'),
                                             ('admin', 'Admin')])

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254)
    full_name = forms.CharField(max_length=100)
    user_type = forms.ChoiceField(choices=UserProfile.USER_TYPE_CHOICES)  # Add user_type field

    class Meta:
        model = User
        fields = ('username', 'full_name','email', 'password1', 'password2', 'user_type')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('full_name', 'username', 'email', 'user_type')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email']  # Add more fields as needed

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['file']  # Assuming 'file' is the field to upload resume

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['cover_letter']  # Assuming 'cover_letter' is the field for cover letter


class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        fields = ['company_name', 'industry', 'location', 'description', 'website']

class JobListingForm(forms.ModelForm):
    class Meta:
        model = JobListing
        fields = ['job_title', 'job_description', 'required_qualifications', 'desired_qualifications',
                  'responsibilities', 'application_deadline', 'salary_range', 'employment_type',
                  'company_benefits', 'how_to_apply']