from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator, MinLengthValidator, EmailValidator
from api.models import Blog, Product

from django.contrib.auth.models import User

# class UserSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=100)
#     last_name = serializers.CharField(max_length=100)
#     email = serializers.EmailField(write_only=True)
#     password = serializers.CharField(write_only=True, min_length=8)

#     id = serializers.PrimaryKeyRelatedField(read_only=True)
#     email = serializers.SlugRelatedField(read_only=True, slug_field='email')
#     email = serializers.StringRelatedField()

#     def create(self, validated_data):
#         return {"first_name": validated_data['first_name'],
#                 "last_name": validated_data['last_name'],
#                 "email": validated_data['email']}
    
#     def update(self, instance, validated_data):
#         instance['first_name'] = validated_data.get('first_name', instance['first_name'])
#         instance['last_name'] = validated_data.get('last_name', instance['last_name'])
#         instance['email'] = validated_data.get('email', instance['email'])
#         return instance
    
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

    
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'    

    
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
        )
        password = validated_data['password']
        user.set_password(password)
        user.save()
        
        return user