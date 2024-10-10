from django.shortcuts import render
from rest_framework import serializers, viewsets
from .serializers import LabRequestsSerializer, LabcloudModelSerializer, LabRequestsNoFileSerializer, AccountInfoSerializer
from .models import LabRequests,LabcloudModel, AccountInfo
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.
class LabRequestsViewSet(viewsets.ModelViewSet):

    queryset = LabRequests.objects.all()
    serializer_class = LabRequestsSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ['title', 'user', 'result', 'handler']
    search_fields = ['title', 'request']
    ordering_fields = ['date_created', 'date_updated', 'result']
    parser_classes = (MultiPartParser, FormParser, FileUploadParser)

    @action(detail=False, methods=['post'])
    def nofiles(self, request, *args, **kargs):
        data = request.data
        serializer = LabRequestsNoFileSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

class LabcloudsViewSet(viewsets.ModelViewSet):

    queryset = LabcloudModel.objects.all()
    serializer_class = LabcloudModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['owner', 'status', 'card_type']

class AccountInfoViewSet(viewsets.ModelViewSet):

    queryset = AccountInfo.objects.all()
    serializer_class = AccountInfoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_https']
