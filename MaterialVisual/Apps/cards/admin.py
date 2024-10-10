from django.contrib import admin

# Register your models here.
from .models import CardModel, CardBorrow
from simple_history.admin import SimpleHistoryAdmin

admin.site.register(CardModel, SimpleHistoryAdmin)
admin.site.register(CardBorrow)
