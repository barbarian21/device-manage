from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from uuid import uuid4

class BaseModel(models.Model):
    id = models.UUIDField(verbose_name='编号',primary_key=True,default=uuid4)
    date_created = models.DateTimeField(verbose_name='添加时间',auto_now_add=True,null=True,blank=True)
    date_updated = models.DateTimeField(verbose_name='修改时间',auto_now=True)
    remark = models.TextField(verbose_name='备注信息',blank=True,null=True)

    class Meta:
        abstract = True

class DeviceUser(User):
    USER_TYPE = (
        ('0','设备管理员'),
        ('1','使用者')
    )
    header_icon = models.ImageField(verbose_name='用户头像',
                                    upload_to='static/images/headers/',
                                    default='static/images/headers/default.jpg')
    user_type = models.CharField(verbose_name='用户类型',max_length=10,choices=USER_TYPE)
    class Meta:
        verbose_name = '平台用户'
        verbose_name_plural = verbose_name


class WorkNotes(BaseModel):

    summery = models.CharField(verbose_name='简述',max_length=50)
    content = models.TextField(verbose_name='内容',null=True,blank=True)
    user = models.ForeignKey(verbose_name='用户',to=DeviceUser,on_delete=models.CASCADE)
    is_done = models.BooleanField(verbose_name='是否完成',default=False,null=False)

    class Meta:
        verbose_name = '工作记录'
        verbose_name_plural = verbose_name

    def __str__(self) -> str:
        return self.summery+'_'+self.user.username+'_' + str(self.is_done)
