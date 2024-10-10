from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from .models import CardModel, CardBorrow
from .serializers import CardModelSerializer, CardModelNestedSerializer, CardBorrowSerializer
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class CardModelViewSet(viewsets.ModelViewSet):
    queryset = CardModel.objects.all()
    serializer_class = CardModelSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['sn', 'card_type', 'card_project', 'name', 'owner', 'device']
    search_fields = ['sn', 'name', 'card_project']
    ordering_fields = '__all__'

    @action(detail=True, methods=['get'])
    def cardhistory(self, request, *args, **kwargs):
        queryset = self.get_object().history.all()
        serializer = CardModelSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def allcards(self, request, *args, **kwargs):
        return Response(CardModelSerializer(self.get_queryset(), many=True).data)

    @action(detail=False, methods=['get'])
    def nested(self, reqeust, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = CardModelNestedSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = CardModelNestedSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class CardBorrowViewSet(viewsets.ModelViewSet):
    queryset = CardBorrow.objects.all()
    serializer_class = CardBorrowSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['user', 'card', 'is_return']
    search_fields = ['reason']
    ordering_fields = ['time_borrowed', 'time_end']
