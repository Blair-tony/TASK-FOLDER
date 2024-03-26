from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import LoginForm, RegistrationForm, UserProfileForm ,ProfileForm, ResumeForm, JobApplicationForm
from .models import UserProfile,Profile,JobApplication,Resume,JobListing,CompanyProfile
from django.http import HttpResponse
from job.models import JobListing,CompanyProfile
from django.contrib import messages
from job.views import *
from django.shortcuts import get_object_or_404
from job.forms import CompanyProfile
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user_type = form.cleaned_data['user_type']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user_type == 'admin':
                    return redirect('admin_panel')
                if user_type == 'job_seeker':
                    return redirect('job_seeker')
                if user_type == 'company_user':
                    return redirect('company_user')
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'login.html',{'form':form})

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Create a new user object
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1']

            )
            # Save the user object
            user.save()
            # Create a new user profile object and link it to the user
            user_profile = UserProfile.objects.create(
                user=user,
                full_name=form.cleaned_data['full_name'],
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                user_type=form.cleaned_data['user_type']
            )
            # Save the user profile object
            user_profile.save()
            return HttpResponse('registration successfull')  # Redirect to admin panel after registration
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})

@login_required
def profile_view(request):
    if request.user.is_staff:
        users = UserProfile.objects.all()
        return render(request, 'admin_panel.html', {'users': users})
    else:
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        if request.method == 'POST':
            form = UserProfileForm(request.POST, instance=user_profile)
            if form.is_valid():
                form.save()
                return redirect('profile')  # Redirect to profile page after updating
        else:
            form = UserProfileForm(instance=user_profile)
        return render(request, 'profile.html', {'profile':Profile})
    
def profile_update(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = None
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile_view')
        else:
            messages.error(request, 'Profile update failed. Please correct the errors below.')
    else:
        form = UserProfileForm(instance=profile)
    
    return render(request, 'profile_update.html', {'form': form, 'profile': profile})

def upload_manage_resume(request):
    try:
        company_profile = CompanyProfile.objects.get(user=request.user)
    except CompanyProfile.DoesNotExist:
        # If CompanyProfile does not exist, create a new one
        company_profile = CompanyProfile.objects.create(user=request.user)
    
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()
            return redirect('resume_view')  # Redirect to resume view page
    else:
        form = ResumeForm()
    resumes = Resume.objects.filter(user=request.user)
    return render(request, 'upload_manage_resume.html', {'form': form, 'resumes': resumes, 'company_profile': company_profile})

def resume_view(request):
    # Retrieve resumes associated with the current user
    resumes = Resume.objects.filter(user=request.user)
    return render(request, 'resume_view.html', {'resumes': resumes})

def jobseekerhome(request):
    return render(request, 'jobseekerhome.html')


def search_view_job_listings(request):
    job_listings = JobListing.objects.all()  # Assuming JobListing model exists
    return render(request, 'job_listings.html', {'job_listings': job_listings})

def job_openings_view(request):
    job_list = JobListing.objects.filter(company=request.user.companyprofile)
    return render(request, 'applyjob.html', {'job_listings': job_list})

def apply_to_job(request, job_id):
    job_listing = get_object_or_404(JobListing, id=job_id)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            job_application = form.save(commit=False)
            job_application.user = request.user
            job_application.job = job_listing
            job_application.save()
            return redirect('job_application_status')  # Redirect to job application status page
    else:
        form = JobApplicationForm()
    return render(request, 'apply_to_job.html', {'form': form, 'job_listings': job_listing})

def job_application_status(request):
    job_applications = JobApplication.objects.filter(user=request.user)
    return render(request, 'job_application_status.html', {'job_applications': job_applications})

def company_user(request):
    return render(request, 'companyhome.html')

def resumecover(request, job_id):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            job_application = form.save(commit=False)
            job_application.user = request.user
            job_application.job = get_object_or_404(JobListing, pk=job_id)
            job_application.save()
            return HttpResponse('<script>alert("Job applied successfully."); window.location.replace("/apply_jobs");</script>')
    else:
        # Retrieve resumes uploaded by the current user
        resumes = Resume.objects.filter(user=request.user)
        form = JobApplicationForm()
    return render(request, 'resumecover.html', {'form': form, 'resumes': resumes})
