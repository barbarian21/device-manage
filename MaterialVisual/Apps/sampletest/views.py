from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SampleTestSerializer
from .models import SampleTestModel
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class SampleTestViewSet(viewsets.ModelViewSet):

    queryset = SampleTestModel.objects.all()
    serializer_class = SampleTestSerializer
    filter_backends = [DjangoFilterBackend,]
    filter_fields = ['customer','user',]