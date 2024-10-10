from django.contrib import admin
from .models import ReportModel,ReleaseModel,Attachment
# Register your models here.
admin.site.register(ReleaseModel)
admin.site.register(ReportModel)
admin.site.register(Attachment)