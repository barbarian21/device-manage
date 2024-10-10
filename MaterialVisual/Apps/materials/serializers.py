from rest_framework import serializers

from .models import MaterialsModel,PurchaseModel,BudgetModel,OtherMaterials


class MaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialsModel
        fields = '__all__'


class PurchaseModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = PurchaseModel
        fields = '__all__'

class BudgetModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = BudgetModel
        fields = '__all__'

class OtherMaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherMaterials
        fields = '__all__'