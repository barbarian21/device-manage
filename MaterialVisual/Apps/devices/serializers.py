from django.db import models
from django.db.models.fields.related import ManyToManyField
from rest_framework import serializers
from .models import Device, DeviceArea, DeviceConfig, DeviceBorrow
from users.serializers import DeviceUserSerializer


class DeviceAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceArea
        fields = '__all__'


class DeviceConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceConfig
        fields = '__all__'


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


class DeviceBorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceBorrow
        fields = '__all__'


class DeviceBorrowNestedSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    device = DeviceSerializer(read_only=True)

    class Meta:
        model = DeviceBorrow
        fields = '__all__'
