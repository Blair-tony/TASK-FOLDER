from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import JobListing
from .forms import JobListingForm,CompanyProfileForm
from user.views import * 
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from user.models import UserProfile,JobApplication
from user.forms import JobApplicationForm  

@login_required
def create_job_listing(request):
    if request.method == 'POST':
        form = JobListingForm(request.POST)
        if form.is_valid():
            job_listing = form.save(commit=False)
            job_listing.company = request.user.companyprofile
            job_listing.save()
            form.save()
            return HttpResponse('successfull')
    else:
        form = JobListingForm()
    return render(request, 'create_job_listing.html', {'form': form})

@login_required

def edit_job_listing(request, job_id):
    # Retrieve the job listing object
    job_listing = get_object_or_404(JobListing, id=job_id)
    
    # Check if the logged-in user is the owner of the job listing
    if request.user != job_listing.company.user:
        # If not, redirect back to the job listing detail page
        return redirect('job_listing_detail', job_id=job_id)
    
    if request.method == 'POST':
        # Populate the form with the submitted data and instance of the job listing
        form = JobListingForm(request.POST, instance=job_listing)
        if form.is_valid():
            # Save the changes to the job listing
            form.save()
            # Redirect to the updated job listing detail page
            return redirect('job_listing_detail')
    else:
        # If it's a GET request, render the form with the current job listing data
        form = JobListingForm(instance=job_listing)
    
    return render(request, 'edit_job_listing.html', {'form': form, 'job_listing': job_listing})

@login_required
def job_listing_detail(request):
    job_list = JobListing.objects.filter(company=request.user.companyprofile)
    return render(request, 'job_listing_detail.html', {'job_list': job_list})

@login_required
def delete_job_listing(request, job_id):
    job_listing = get_object_or_404(JobListing, id=job_id)
    if request.user.companyprofile == job_listing.company:
        job_listing.delete()
    return redirect('employer_dashboard')

@login_required
def employer_dashboard(request):
    job_listings = JobListing.objects.filter(company=request.user.companyprofile)
    return render(request, 'companyhome.html', {'job_listings': job_listings})

def company_user(request):
     return render(request, 'companyhome.html')

def CompanyProfile(request):
    try:
        profile = request.user.companyprofile
        editing = True
    except CompanyProfile.DoesNotExist:
        profile = None
        editing = False
        
    if request.method == 'POST':
        
        form = CompanyProfileForm(request.POST, instance=profile)
        if form.is_valid():
            
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            
            return redirect('company_user')
    else:
        
        form = CompanyProfileForm(instance=profile)
 
  
    return render(request, 'company_profile.html', {'form': form, 'editing': editing})

def manage_job_applications(request):
    # Retrieve job applications associated with the company's job listings
    job_applications = JobApplication.objects.filter(job__company=request.user.companyprofile)
    return render(request, 'manage_job_applications.html', {'job_applications': job_applications})

def view_job_application(request, job_application_id):
    job_application = JobApplication.objects.get(id=job_application_id)
    user_profile = UserProfile.objects.get(user=job_application.user)  # Retrieve user profile
    return render(request, 'view_job_application.html', {
        'job_application': job_application,
        'user_profile': user_profile,
    })