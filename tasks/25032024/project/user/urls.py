# user/urls.py
from django.urls import path
from . import views
from job.views import *


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.registration_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('update-profile/', views.profile_update, name='update_profile'),
    path('profile/', views.profile_view, name='profile_view'),
    path('upload-resume/', views.upload_manage_resume, name='upload_resume'),
    path('resume_view/', views.resume_view, name='resume_view'),
    path('job-listings/', views.search_view_job_listings, name='job_listings'),
    path('apply-to-job//<int:job_id>/', views.apply_to_job, name='apply_to_job'),
    path('job-application-status/', views.job_application_status, name='job_application_status'),
    path('jobseekerhome/', views.jobseekerhome, name='job_seeker'),
    path('companyhome/', views.company_user, name='company_user'),
    path('job_openings_view/', views.job_openings_view, name='job_openings_view'),
    path('resumecover/<int:job_id>/', views.resumecover, name='resumecover'),
]