from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response 
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import StudentSerializer , UserSerializer
from .models import Student
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# CustomAuthToken
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# ListUsers
from rest_framework.views import APIView

from rest_framework import authentication, permissions
from django.contrib.auth.models import User


@api_view(['GET','POST'])
def student(request):
    if request.method == 'GET':
        students = Student.objects.all()
        print("------",students)
        serializer = StudentSerializer(students, many = True)
        
        print(serializer.data)
        
        return Response(serializer.data)
    else:
        s = Student(name=request.data['name'], marks=request.data['marks'])
        s.save()
        return Response({"message : Successfull added"})
    


       
class CustomAuthToken(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
       
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })



    
    
          
    
    



