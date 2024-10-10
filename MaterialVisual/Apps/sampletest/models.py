from django.db import models
from uuid import uuid4
from django.core.validators import MinValueValidator
from django.core.serializers.json import DjangoJSONEncoder

# Create your models here.
def default_info():
    dic = {
        'version':'',
        'docs':'',
        'files':'',
    }

    return dic

class BaseModel(models.Model):
    id = models.UUIDField(verbose_name='编号',primary_key=True,default=uuid4)
    date_created = models.DateTimeField(verbose_name='添加时间',auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name='修改时间',auto_now=True)
    remark = models.TextField(verbose_name='备注信息',blank=True,null=True)
    class Meta:
        abstract = True

class SampleTestModel(BaseModel):

    customer = models.CharField(verbose_name='客户名称',max_length=100,null=False)
    info = models.JSONField(verbose_name='送测信息',encoder=DjangoJSONEncoder,default=default_info,help_text='info for sample test')
    user = models.CharField(verbose_name='处理人',max_length=20,null=False)

    class Meta:
        verbose_name = '送样测试'
        verbose_name_plural = verbose_name

    def __str__(self) -> str:
        return self.customer