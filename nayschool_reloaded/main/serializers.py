from django.db.models.base import Model
from .models import *
from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields=("name",)
