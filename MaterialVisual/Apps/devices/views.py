from django.shortcuts import render
from rest_framework import serializers, viewsets,permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import DeviceConfigSerializer, DeviceSerializer,DeviceAreaSerializer,DeviceBorrowSerializer,DeviceBorrowNestedSerializer
from .models import Device,DeviceArea,DeviceBorrow, DeviceConfig
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter

# Create your views here.

class DeviceViewSet(viewsets.ModelViewSet):

    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ['name','type','sn','number','hostname','is_cse','status']
    search_fields = ['name','hostname']
    ordering_fields = ['name']

    @action(detail=False,methods=['get'])
    def alldevices(self,request,*args,**kwargs):
        return Response(DeviceSerializer(self.get_queryset(),many=True).data)

    @action(detail=True,methods=['get'])
    def devicehistory(self,request,*args,**kwargs):
        queryset = self.get_object().history.all()
        serializer = DeviceSerializer(queryset,many=True)
        return Response(serializer.data)


class DeviceAreaViewSet(viewsets.ModelViewSet):

    queryset = DeviceArea.objects.all()
    serializer_class = DeviceAreaSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ['info']
    search_fields = ['info']
    ordering_fields = ['info']

class DeviceConfigViewSet(viewsets.ModelViewSet):
    queryset = DeviceConfig.objects.all()
    serializer_class = DeviceConfigSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_fields = ['model','vender','cpu','memory']
    search_fields = ['model','vender']


class DeviceBorrowViewSet(viewsets.ModelViewSet):
    queryset = DeviceBorrow.objects.all()
    serializer_class = DeviceBorrowSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ['user','device','is_return']
    search_fields = ['reason']
    ordering_fields = ['time_borrowed','time_end']

    @action(detail=False,methods=['get'])
    def devicestatus(self,request,*args,**kwargs):
        #queryset = Device.objects.all()
        queryset = self.filter_queryset(self.get_queryset())
        device_ids = []
        new_queryset = []#DeviceBorrow.objects.values('reason').distinct()
        for borrow in queryset:
            if borrow.device_id not in device_ids:
                new_queryset.append(borrow)
                device_ids.append(borrow.device_id)
        # for device in queryset:
        #     row_data = DeviceBorrow.objects.filter(device=device).first()
        #     if row_data:
        #     #if item.borrows.exists():
        #         #row_data = item.borrows.all().first()
        #         new_queryset.append(row_data)
        page = self.paginate_queryset(new_queryset)
        if page is not None:
            serializer = DeviceBorrowNestedSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        return Response(DeviceBorrowNestedSerializer(new_queryset,many=True).data)



    