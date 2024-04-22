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
        
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import car
from .serializers import CarSerializer
 
class CarUpdateView(APIView):
    def get_object(self, pk):
        try:
            return car.objects.get(pk=pk)
        except car.DoesNotExist:
            return None
 
    def put(self, request, pk):
        car_instance = self.get_object(pk)
        if car_instance is None:
            return Response({"message": "Car not found"}, status=status.HTTP_404_NOT_FOUND)
 
        serializer = CarSerializer(car_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def patch(self, request, pk):
        car_instance = self.get_object(pk)
        if car_instance is None:
            return Response({"message": "Car not found"}, status=status.HTTP_404_NOT_FOUND)
 
        serializer = CarSerializer(car_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import car
 
class CarDeleteView(APIView):
    def get_object(self, pk):
        try:
            return car.objects.get(pk=pk)
        except car.DoesNotExist:
            return None
 
    def delete(self, request, pk):
        car_instance = self.get_object(pk)
        if car_instance is None:
            return Response({"message": "Car not found"}, status=status.HTTP_404_NOT_FOUND)
 
        try:
            car_instance.delete()
            return Response({"message": "Car deleted successfully"})
        except Exception as e:
            return Response({"message": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import car
 
class BulkDeleteAPIView(APIView):
    def delete(self, request):
        data = request.data
        car_data = data.get("car", [])
 
        if not car_data:
            return Response({"message": "No car IDs provided"}, status=status.HTTP_400_BAD_REQUEST)
 
        try:
            car_objects_deleted = car.objects.filter(pk__in=car_data).delete()
            cars_deleted_count = car_objects_deleted[0]
            return Response({"message": f"{cars_deleted_count} cars deleted successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": "Bulk deletion failed", "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from .models import car
from .serializers import CarSerializer
        
class carlistView(ListAPIView):
    queryset = car.objects.all()
    serializer_class = CarSerializer
    pagination_class = LimitOffsetPagination
    def get_queryset(self):
        q= self.request.GET.get('q')
        queryset=car.objects.all()
        if q:
            queryset=car.objects.filter(carname__icontains=q)
       
        tag = self.request.GET.get('tag')
        if tag is not None:
            queryset = queryset.filter(tag=tag)
        return queryset
    
class carsListView(ListAPIView):
    queryset = car.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(carname__icontains=q)
        
        tag = self.request.GET.get('tag')
        if tag:
            queryset = queryset.filter(tag=tag)
        
        # Assuming 'ordering' parameter is passed as 'asc' or 'desc'
        ordering = self.request.GET.get('ordering')  
        if ordering:
            if ordering == 'asc':
                queryset = queryset.order_by('year')
            elif ordering == 'desc':
                queryset = queryset.order_by('-year')

        return queryset