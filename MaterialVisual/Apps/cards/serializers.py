from django.db import models
from rest_framework import serializers

from .models import CardModel, CardBorrow


class CardModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardModel
        fields = '__all__'


class CardModelNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardModel
        fields = '__all__'
        depth = 1


class CardBorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardBorrow
        fields = '__all__'
