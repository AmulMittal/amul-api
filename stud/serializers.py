from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Student
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        
        
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username','email','first_name','last_name']
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
        write_only_fields = ('password',)
        read_only_fields = ('id',)
        extra_kwargs = {'password': {'write_only': True}}

        email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
        username = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
        password = serializers.CharField(min_length=8)
        
        def create(self, validated_data):
            user = User.objects.create_user(
                username=validated_data['username'],
                email=validated_data['email'],
                
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name']
    
            )
            user.set_password(make_password(validated_data['password']))
            user.save(using=self._db)

            return user
        