from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser,FormParser,FileUploadParser
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import ReportModel,ReleaseModel
from .serializers import ReportModelSerializer, ReportModelNoFileSerializer,ReleaseModelSerializer
# Create your views here.

class ReleaseModelViewSet(viewsets.ModelViewSet):

    queryset = ReleaseModel.objects.all()
    serializer_class = ReleaseModelSerializer
    filter_backends = [DjangoFilterBackend,]
    filter_fields = ['version','dept','type']


class ReportModelViewSet(viewsets.ModelViewSet):

    queryset = ReportModel.objects.all()
    serializer_class = ReportModelSerializer
    parser_classes = (MultiPartParser, FormParser,FileUploadParser)

    @action(detail=False,methods=['post'])
    def nofiles(self,request,*args,**kargs):

        data = request.data
        serializer = ReportModelNoFileSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

