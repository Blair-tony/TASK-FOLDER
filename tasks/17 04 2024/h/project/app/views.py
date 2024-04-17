from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Role
from .serializers import UserSerializer, RoleSerializer, UserLoginSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserLoginSerializer
 
class UserRegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
 
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(username__icontains=search_query) | \
                       queryset.filter(email__icontains=search_query) | \
                       queryset.filter(first_name__icontains=search_query) | \
                       queryset.filter(last_name__icontains=search_query)
        return queryset
 
class RoleCreateView(generics.CreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
 
class RoleListAPIView(generics.ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
   
 
 
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializer
 
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg = 'user_id'  # Define the URL keyword argument for user ID
 
    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 
 
 
 
 
class UserLoginAPIView(TokenObtainPairView):
    serializer_class = UserLoginSerializer
 