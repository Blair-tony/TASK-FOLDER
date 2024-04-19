from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Role,Snippet,Tag,car
 
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
 
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
 
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
 
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'
 
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
 
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id','car', 'code', 'colour', 'year']
 
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']
 
class carCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = car
        fields = "__all__"
 
class carDetailsSerializer(serializers.ModelSerializer):
    tag = TagSerializer()
    class Meta:
        model = car
        fields = ['id', 'carname', 'tag', 'year']

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = car
        fields = ['id', 'carname', 'tag', 'year']