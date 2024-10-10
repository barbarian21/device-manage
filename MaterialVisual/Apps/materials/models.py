from django.db import models
from django.core.validators import MinValueValidator
from uuid import uuid4
from django.core.serializers.json import DjangoJSONEncoder

# Create your models here.

class BaseModel(models.Model):

    id = models.UUIDField(verbose_name='编号',primary_key=True,default=uuid4)
    date_created = models.DateTimeField(verbose_name='添加时间',auto_now_add=True,null=True,blank=True)
    date_updated = models.DateTimeField(verbose_name='修改时间',auto_now=True)
    quarter = models.CharField(verbose_name='采购季度',max_length=50,null=False)
    price = models.FloatField(verbose_name='单价',null=False,validators=[MinValueValidator(0)])
    link = models.CharField(verbose_name='链接',max_length=100,null=True,blank=True)
    name = models.CharField(verbose_name='物品名称',max_length=50,null=False)
    detail = models.TextField(verbose_name='详细描述',blank=True,null=True)
    count = models.IntegerField(verbose_name='数量',null=False,validators=[MinValueValidator(0)]),
    remark = models.TextField(verbose_name='备注信息',blank=True,null=True)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.name

class MaterialsModel(BaseModel):

    users =models.JSONField(verbose_name='使用者',encoder=DjangoJSONEncoder,default=dict,null=True,blank=True)
    residue = models.IntegerField(verbose_name='剩余数量',null=True,blank=True)

    class Meta:
        verbose_name = '耗材使用'
        verbose_name_plural = verbose_name

    def __str__(self) -> str:
        return super().__str__()

class OtherMaterials(BaseModel):
    users =models.JSONField(verbose_name='使用者',encoder=DjangoJSONEncoder,default=dict,null=True,blank=True)
    residue = models.IntegerField(verbose_name='剩余数量',null=True,blank=True)

    class Meta:
        verbose_name = '其他耗材'
        verbose_name_plural = verbose_name


class PurchaseModel(BaseModel):

    user =models.CharField(verbose_name='申请者',max_length=20,null=False)
    reason = models.CharField(verbose_name='申请理由',max_length=100,null=False)

    class Meta:
        verbose_name = '采购申请'
        verbose_name_plural = verbose_name

    def __str__(self) -> str:
        return super().__str__()


class BudgetModel(models.Model):

    STATUS = (
        ('0','未发生'),
        ('1','已发生')
    )
    id = models.UUIDField(verbose_name='编号',primary_key=True,default=uuid4)
    dept = models.CharField(verbose_name='预算部门',max_length=10,default='CSE')
    year = models.CharField(verbose_name='年份',max_length=10,null=False,default=2021)
    source = models.CharField(verbose_name='数据源头',max_length=20)
    status = models.CharField(verbose_name='状态',choices=STATUS,default='0',max_length=5,null=True,blank=True)
    project = models.CharField(verbose_name='项目',null=False,max_length=20)
    budget_body = models.IntegerField(verbose_name='采购主体',default=1)
    budget_num = models.CharField(verbose_name='预算编号',max_length=20,null=False,unique=True,help_text='采购申请所需')
    type_one = models.CharField(verbose_name='类别-1',max_length=30)
    type_two = models.CharField(verbose_name='类别-2',max_length=100)
    description = models.CharField(verbose_name='内容描述',max_length=50)
    user_dept = models.CharField(verbose_name='使用部门',default='CSE',max_length=5)
    start_time = models.CharField(verbose_name='预计采购时间',max_length=10)
    end_time = models.CharField(verbose_name='预计到货时间',max_length=10)
    currency = models.CharField(verbose_name='预算币种',max_length=5,default='RMB')
    count = models.IntegerField(verbose_name='数量',null=False,validators=[MinValueValidator(0)])
    price = models.FloatField(verbose_name='不含税总价',null=False)
    tax = models.FloatField(verbose_name='税额',)
    total = models.FloatField(verbose_name='含税总价')

    class Meta:
        verbose_name = '预算汇总'
        verbose_name_plural = verbose_name

    def __str__(self) -> str:
        return self.budget_num


    