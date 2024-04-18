from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Role,Snippet,Tag,car
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserLoginSerializer,UserSerializer, UserSerializer, RoleSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView,RetrieveAPIView
from .serializers import *
from rest_framework.views import APIView
 
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
 
class UserLoginAPIView(TokenObtainPairView):
    serializer_class = UserLoginSerializer
 
class UserDetailsView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'
 
class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'
 
class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'
 
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg = 'user_id'  # Define the URL keyword argument for user ID
 
    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
   
 
 
class CreateSnippetView(CreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
 
class SnippetDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        instance = Snippet.objects.filter(pk=pk)
        if instance.exists():
            serializer = SnippetSerializer(instance.first())
            return Response(serializer.data)
        return Response({"message": "Snippet not found"}, status=status.HTTP_404_NOT_FOUND)
   
class CreateCarView(CreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = carCreateSerializer  
 
class CarDetailView(RetrieveAPIView):
    queryset = car.objects.all()
    serializer_class = carDetailsSerializer
 
class CarDetailViews(APIView):
    def get(self, request, pk):
        try:
            instance = car.objects.get(pk=pk)
            serializer = carDetailsSerializer(instance)
            return Response(serializer.data)
        except car.DoesNotExist:
            return Response({"message": "car not found"}, status=status.HTTP_404_NOT_FOUND)