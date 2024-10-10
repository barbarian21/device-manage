from django.db import models
from rest_framework import serializers
from .models import SampleTestModel
class SampleTestSerializer(serializers.ModelSerializer):

    class Meta:
        model = SampleTestModel
        fields = '__all__'