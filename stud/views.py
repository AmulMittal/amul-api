from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from .serializers import StudentSerializer
from .models import Student

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
        