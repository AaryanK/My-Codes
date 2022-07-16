from api.serializers import RoomSerializer
from django.shortcuts import render,HttpResponse
from rest_framework import generics
from .models import *
from .serializers import *
# Create your views here.

class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer