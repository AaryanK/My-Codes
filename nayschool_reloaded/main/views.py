from .serializers import CourseSerializer
from rest_framework import generics
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
# Create your views here.
def home(request):
    # vars['courses'] = Subject.objects.all()
    # vars['num_courses']=len(Subject.objects.all())
    # vars['courses'] = Subject.objects.all()
    # vars['Subject'] = Subject
    # vars['show'] = ''
    return render(request,"home.html")

@api_view(('GET',))
def courses_info(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses,many=True)
    return Response(serializer.data)
