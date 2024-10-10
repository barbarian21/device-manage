from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework import viewsets,permissions
from .models import DeviceUser,WorkNotes
from .serializers import DeviceUserSerializer,WorkNotesSerializer

from .permissions import IsOwnerPermission
# Create your views here.

class DeviceUserViewSet(viewsets.ReadOnlyModelViewSet):
    #permission_classes = [permissions.IsAuthenticated,]
    queryset = DeviceUser.objects.all()
    serializer_class = DeviceUserSerializer

    # @action(methods=['get'],detail=False)
    # def get_device(self,request):
    #     pass

    # @action(methods=['get'],detail=False)
    # def get_material(self,request):
    #     pass

    @action(methods=['get'],detail=False)
    def admin_info(self,request,*args,**kargs):

        admin_info = {
            'id': 1, 
            'password': '', 
            'last_login': '2021-11-16T13:37:40.955432Z', 
            'is_superuser': False, 
            'username': 'admin',
            'date_joined': '2021-11-11T13:59:47Z',
            'email': 'admin@test.com',
            'first_name': '',
            'groups': [],
            'header_icon': 'http://10.12.120.200:8085/static/images/headers/default.jpg',
            'is_active': True,
            'is_staff': True,
            'is_superuser': True,
            'last_name': '',
            'user_permissions': [],
            'user_type': '0'
        }
        serializer = DeviceUserSerializer(admin_info)
        return Response(serializer.data)
        
class WorkNotesViewSet(viewsets.ModelViewSet):

    permission_classes = [IsOwnerPermission,]
    queryset = WorkNotes.objects.all()
    serializer_class = WorkNotesSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ['user','is_done']
    search_fields = ['summery','content']
    ordering_fields = ['time_borrowed','time_end']