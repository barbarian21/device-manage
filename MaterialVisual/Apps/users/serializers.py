from django.db import models
from rest_framework import serializers
from .models import DeviceUser,WorkNotes

class DeviceUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceUser
        fields = '__all__'

class WorkNotesSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkNotes
        field = '__all__'