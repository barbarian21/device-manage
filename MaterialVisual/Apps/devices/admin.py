from django.contrib import admin

# Register your models here.

from .models import Device, DeviceArea, DeviceBorrow, DeviceConfig
from simple_history.admin import SimpleHistoryAdmin

admin.site.register(Device, SimpleHistoryAdmin)
admin.site.register(DeviceArea)
admin.site.register(DeviceConfig)
admin.site.register(DeviceBorrow)
