from django.contrib import admin

# Register your models here.
from .models import MaterialsModel,PurchaseModel,BudgetModel,OtherMaterials

admin.site.register(MaterialsModel)
admin.site.register(PurchaseModel)
admin.site.register(BudgetModel)
admin.site.register(OtherMaterials)