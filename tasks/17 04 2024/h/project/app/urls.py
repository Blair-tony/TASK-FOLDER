# urls.py

from django.urls import path
from .views import UserRegistrationAPIView, RoleListAPIView,UserListView,RoleCreateView,UserLoginAPIView,UserDetailView

urlpatterns = [
    path('userregister/', UserRegistrationAPIView.as_view(), name='user-register'),
    path('userlist/', UserListView.as_view(), name='user-list'),
    path('roles/', RoleCreateView.as_view(), name='role-create'),
    path('roleslist/', RoleListAPIView.as_view(), name='role-list'),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
    path('users/<int:user_id>/', UserDetailView.as_view(), name='user-detail'),
 
]