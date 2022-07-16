from django.db.models.base import Model
from .models import *
from rest_framework import serializers


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields=("id",
                "code",
                "host",
                "guest_can_pause",
                "votes_to_skip",
                "created_at",
                )