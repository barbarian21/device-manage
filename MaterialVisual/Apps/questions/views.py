from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser,FormParser,FileUploadParser
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import QuestionModel,SupportModel
from .serializers import QuestionModelSerializer, QuestionModelNoFileSerializer,SupportModelSerializer
# Create your views here.

class SupportModelViewSet(viewsets.ModelViewSet):

    queryset = SupportModel.objects.all()
    serializer_class = SupportModelSerializer
    filter_backends = [DjangoFilterBackend,]
    filter_fields = ['customer','owner','project']

class QuestionModelViewSet(viewsets.ModelViewSet):

    queryset = QuestionModel.objects.all()
    serializer_class = QuestionModelSerializer
    parser_classes = (MultiPartParser, FormParser,FileUploadParser)

    @action(detail=False,methods=['post'])
    def nofiles(self,request,*args,**kargs):

        data = request.data
        serializer = QuestionModelNoFileSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

