from django.contrib import admin

# Register your models here.
from .models import DeviceUser,WorkNotes

admin.site.register(DeviceUser)
admin.site.register(WorkNotes)