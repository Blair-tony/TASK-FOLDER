from django.urls import path
from .views import *
 
urlpatterns = [
    path('userregister/', UserRegistrationAPIView.as_view(), name='user-register'),
    path('userlist/', UserListView.as_view(), name='user-list'),
    path('roles/', RoleCreateView.as_view(), name='role-create'),
    path('roleslist/', RoleListAPIView.as_view(), name='role-list'),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
    path('users/<int:user_id>/',UserDetailView.as_view(),name='user-detail'),
    path('create/', CreateSnippetView.as_view(), name='create-snippet'),
    path('app/<int:pk>/', SnippetDetailView.as_view(), name='snippet-detail'),
    path('cars/', CreateCarView.as_view(), name='create-car'),
    path('carss/<int:pk>/', CarDetailView.as_view(), name='car-detail'),
    path('carsss/<int:pk>/', CarDetailViews.as_view(), name='car-detail'),]