from django.db import models
from uuid import uuid4
from django.core.validators import MinValueValidator

# Create your models here.

class BaseModel(models.Model):
    id = models.UUIDField(verbose_name='编号',primary_key=True,default=uuid4)
    date_created = models.DateTimeField(verbose_name='添加时间',auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name='修改时间',auto_now=True)
    remark = models.TextField(verbose_name='备注信息',blank=True,null=True)
    class Meta:
        abstract = True


class SupportModel(BaseModel):

    date_support = models.DateTimeField(verbose_name='日期',null=False)
    customer = models.CharField(verbose_name='客户名称',max_length=50,null=False)
    location = models.CharField(verbose_name='地点',max_length=20,null=False)
    project = models.CharField(verbose_name='项目',max_length=10,null=False)
    subject = models.CharField(verbose_name='主题',max_length=100,null=False)
    owner = models.CharField(verbose_name='支持代表',max_length=20,null=False)
    day_counts = models.IntegerField(verbose_name='天数',validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = '线下支持'
        verbose_name_plural = verbose_name

class QuestionModel(BaseModel):
    TYPE = (
        ('0','UAT'),
        ('1','UXT'),
        ('2','BUG'),
        ('3','OTHER')
    )
    type = models.CharField(verbose_name='类别',choices=TYPE,default='0',max_length=5,null=True,blank=True)
    title = models.CharField(verbose_name='标题',max_length=100,null=True,blank=True)
    detail = models.TextField(verbose_name='详细描述',null=True,blank=True)
    user = models.CharField(verbose_name='创建者',max_length=20,null=True,blank=True)
    version = models.CharField(verbose_name='版本',max_length=50,null=True,blank=True)

    class Meta:
        verbose_name = '问题信息'
        verbose_name_plural = verbose_name

    def __str__(self) -> str:
        return self.title

class Attachment(models.Model):
    question = models.ForeignKey(QuestionModel,on_delete=models.CASCADE,related_name='attachments',null=True,blank=True)
    attach = models.FileField(upload_to='static/images/questions/%Y-%d-%d/',verbose_name='附件',null=True,blank=True)

    class Meta:
        verbose_name = '附件信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.question_id}\'s attach'
