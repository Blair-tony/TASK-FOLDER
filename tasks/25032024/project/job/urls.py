from django.urls import path
from . import views
from user.views import *

urlpatterns = [
    path('job/create/', views.create_job_listing, name='create_job_listing'),
    path('job/edit/<int:job_id>/', views.edit_job_listing, name='edit_job_listing'),
    path('job/detail/', views.job_listing_detail, name='job_listing_detail'),
    path('job/delete/<int:job_id>/', views.delete_job_listing, name='delete_job_listing'),
    path('job/dashboard/', views.employer_dashboard, name='employer_dashboard'),
    path('job/CompanyProfile/', views.CompanyProfile, name='CompanyProfile'),
    path('manage-job-applications/', views.manage_job_applications, name='manage_job_applications'),
   path('view_job_application/<int:job_application_id>/', views.view_job_application, name='view_job_application'),
    


]
