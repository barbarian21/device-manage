from django.contrib import admin
from .models import QuestionModel,Attachment,SupportModel
# Register your models here.
admin.site.register(QuestionModel)
admin.site.register(Attachment)
admin.site.register(SupportModel)