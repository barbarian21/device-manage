from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from uuid import uuid4
from django.core.validators import MinValueValidator

from users.models import DeviceUser
from devices.models import DeviceBorrow


def customer_info():
    return {
        'name': '',
        'contact': '',
        'locate': '',
        'phone': '',
        'email': '',
        'company': '',
        'position': '',
        'industry': '',
        'use': ''
}


def login_info():
    return {
        'ssh': 'ssh root@58.247.94.54 -p 32222',
        'port': '32222,32333',
        'user': 'root',
        'pwd': 'passwd'
    }


class BaseModel(models.Model):

    id = models.UUIDField(verbose_name='编号', primary_key=True, default=uuid4)
    date_created = models.DateTimeField(verbose_name='添加时间', auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    remark = models.TextField(verbose_name='备注信息', blank=True, null=True)

    class Meta:
        abstract = True


class AccountInfo(BaseModel):

    url = models.CharField(verbose_name='地址信息', max_length=20, unique=True)
    account = models.CharField(verbose_name='账号信息', max_length=10, null=False)
    passwd = models.CharField(verbose_name='密码信息', max_length=20, null=False)
    is_https = models.BooleanField(verbose_name='https', default=False)

    class Meta:
        verbose_name = '账号信息'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.url


class LabRequests(BaseModel):

    title = models.CharField(verbose_name='需求主题', max_length=50, null=False)
    request = models.TextField(verbose_name='需求详情')
    user = models.ForeignKey(DeviceUser, verbose_name='提交者', on_delete=models.DO_NOTHING)
    result = models.BooleanField(verbose_name='处理结果', default=False)
    handler = models.CharField(verbose_name='处理人', max_length=20, default='cse')
    type = models.CharField(verbose_name='需求分类', max_length=20, null=True, blank=True)
    req_time = models.DateTimeField(verbose_name='需求时间', null=True, blank=True)
    borrowed = models.ForeignKey(DeviceBorrow, verbose_name='设备借用', null=True, blank=True, on_delete=models.DO_NOTHING)
    
    class Meta:
        verbose_name = '机房需求'
        verbose_name_plural = verbose_name
        ordering = ['-date_created']

    def __str__(self) -> str:
        return self.title + '_' + self.user.username


class Attachment(models.Model):
    report = models.ForeignKey(LabRequests, verbose_name='Lab需求', on_delete=models.CASCADE, related_name='attachments', null=True, blank=True)
    attach = models.FileField(upload_to='static/uploads/labrequests/%Y-%d-%d/', verbose_name='附件', null=True, blank=True)

    class Meta:
        verbose_name = '附件信息'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return f'{self.report_id}\'s attach'


class LabcloudModel(BaseModel):

    STATUS = (
        ('0', '使用中'),
        ('1', '已完成')
    )
    CARD_TYPE = (
        ('0', '训练'),
        ('1', '推理')
    )
    name = models.CharField(verbose_name='客户名称',max_length=50,default='Enflame',null=False)
    customer = models.JSONField(verbose_name='客户信息',default=customer_info,help_text='customer info')
    owner = models.ForeignKey(DeviceUser,on_delete=models.DO_NOTHING,verbose_name='CSE负责人',max_length=20)
    bussiness = models.CharField(verbose_name='商务负责人',max_length=20)
    status = models.CharField(verbose_name='状态',choices=STATUS,default='0',max_length=5,null=True,blank=True)
    card_type = models.CharField(verbose_name='卡类型',choices=CARD_TYPE,default='0',max_length=5)
    use_time = models.DateTimeField(verbose_name='申请时间')
    end_time = models.DateTimeField(verbose_name='结束时间',null=True,blank=True)
    use_days = models.IntegerField(verbose_name='使用天数',validators=[MinValueValidator(0)])
    software = models.CharField(verbose_name='软件版本',max_length=40,null=False)
    device = models.CharField(verbose_name='设备名称',max_length=50,null=False)
    login = models.JSONField(verbose_name='登录信息',encoder=DjangoJSONEncoder,default=login_info,help_text='login info ssh,port,user,pwd')


    class Meta:
        verbose_name = '远测使用'
        verbose_name_plural = verbose_name
    
    def __str__(self) -> str:
        return self.name + '_' + self.card_type + '_' + self.status


