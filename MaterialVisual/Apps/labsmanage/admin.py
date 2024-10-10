from django.contrib import admin
from .models import LabRequests, LabcloudModel, Attachment, AccountInfo
# Register your models here.

admin.site.register(LabRequests)
admin.site.register(LabcloudModel)
admin.site.register(Attachment)
admin.site.register(AccountInfo)