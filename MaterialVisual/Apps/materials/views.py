from django.db import models
from django.db.models import query
from django.shortcuts import render
from rest_framework import viewsets
from .models import MaterialsModel, PurchaseModel, BudgetModel
from .serializers import MaterialsSerializer,PurchaseModelSerializer,BudgetModelSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class MaterialsViewSet(viewsets.ModelViewSet):
    queryset = MaterialsModel.objects.all()
    serializer_class = MaterialsSerializer
    filter_backends = [DjangoFilterBackend,]
    filter_fields = ['name',]

class PurchasesViewSet(viewsets.ModelViewSet):
    queryset = PurchaseModel.objects.all()
    serializer_class = PurchaseModelSerializer
    filter_backends = [DjangoFilterBackend,]
    filter_fields = ['name','user']

class BudgetsViewSet(viewsets.ModelViewSet):

    queryset = BudgetModel.objects.all()
    serializer_class = BudgetModelSerializer
    filter_backends = [DjangoFilterBackend,]
    filter_fields = ['status','budget_num']

class OthersViewSet(viewsets.ModelViewSet):
    queryset = MaterialsModel.objects.all()
    serializer_class = MaterialsSerializer
    filter_backends = [DjangoFilterBackend,]
    filter_fields = ['name',]