from django.db import models
from uuid import uuid4
from django.core.serializers.json import DjangoJSONEncoder

# Create your models here.
class BaseModel(models.Model):
    id = models.UUIDField(verbose_name='编号',primary_key=True,default=uuid4)
    date_created = models.DateTimeField(verbose_name='添加时间',auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name='修改时间',auto_now=True)
    remark = models.TextField(verbose_name='备注信息',blank=True,null=True)
    class Meta:
        abstract = True


class ReportModel(BaseModel):
    TYPE = (
        ('0','Modelzoo-Infer'),
        ('1','Modelzoo-Train'),
        ('2','Daily-Infer'),
        ('3','Daily-Train')
    )
    type = models.CharField(verbose_name='类别',choices=TYPE,default='0',max_length=5,null=True,blank=True)
    title = models.CharField(verbose_name='标题',max_length=100,null=True,blank=True)
    detail = models.TextField(verbose_name='详细描述',null=True,blank=True)
    user = models.CharField(verbose_name='创建者',max_length=20,null=True,blank=True)
    version = models.CharField(verbose_name='版本',max_length=50,null=True,blank=True)
    other = models.JSONField(verbose_name='其他信息',encoder=DjangoJSONEncoder,default=dict)

    class Meta:
        verbose_name = '报告信息'
        verbose_name_plural = verbose_name

    def __str__(self) -> str:
        return self.title

class Attachment(models.Model):
    report = models.ForeignKey(ReportModel,on_delete=models.CASCADE,related_name='attachments',null=True,blank=True)
    attach = models.FileField(upload_to='static/uploads/modelzoo/%Y-%d-%d/',verbose_name='附件',null=True,blank=True)

    class Meta:
        verbose_name = '附件信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.report_id}\'s attach'

class ReleaseModel(BaseModel):

    DEPT = (
        ('0','CSE'),
        ('1','QA')
    )
    TYPE = (
        ('0','Infer'),
        ('1','Train')
    )
    version = models.CharField(verbose_name='版本',null=True,unique=True,blank=True,max_length=50)
    url = models.URLField(verbose_name='链接',null=True,blank=True)
    dept = models.CharField(verbose_name='部门',choices=DEPT,default='0',max_length=5,null=True,blank=True)
    type = models.CharField(verbose_name='类别',choices=TYPE,default='0',max_length=5,null=True,blank=True)
    note = models.TextField(verbose_name='发布信息',null=True,blank=True)
    other = models.JSONField(verbose_name='其他信息',encoder=DjangoJSONEncoder,default=dict)

    class Meta:
        verbose_name = '版本发布'
        verbose_name_plural = verbose_name

    def __str__(self) -> str:
        return self.version