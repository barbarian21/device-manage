import datetime
import json
from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.signals import post_init, post_save
from django.utils import timezone
from users.models import DeviceUser
# Create your models here.
from simple_history.models import HistoricalRecords


def os_config():
    return {'os_name': '', 'kernel': ''}


def area_temp():
    ret_dict = {
        'lab_loc': 'CSE-JQ',
        'rack_num': 'Rack01',
        'u_num': '2u-4u'
    }
    return ret_dict


def get_admin():
    return User.objects.get(id=1)


class BaseModel(models.Model):
    id = models.UUIDField(verbose_name='编号', primary_key=True, default=uuid4)
    date_created = models.DateTimeField(verbose_name='添加时间', auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    remark = models.TextField(verbose_name='备注信息', blank=True, null=True)

    class Meta:
        abstract = True


class DeviceArea(BaseModel):
    info = models.CharField(verbose_name='提示信息', max_length=20, null=True, blank=True)
    location = models.JSONField(encoder=DjangoJSONEncoder, verbose_name='设备位置', default=area_temp)

    class Meta:
        verbose_name = '位置信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.info


class DeviceConfig(BaseModel):
    model = models.CharField(verbose_name='型号', null=True, blank=True, max_length=100)
    vender = models.CharField(verbose_name='厂商', max_length=20, null=True, blank=True)
    cpu = models.CharField(verbose_name='CPU配置', max_length=20)
    memory = models.CharField(verbose_name='内存配置', max_length=50)
    pcie = models.CharField(verbose_name='pcie信息', max_length=20, default='Gen3')
    mainboard = models.CharField(verbose_name='主板配置', null=True, blank=True, max_length=100)
    harddisk = models.TextField(verbose_name='硬盘配置', null=False)
    power = models.CharField(verbose_name='电源配置', max_length=50, null=True, blank=True)
    network = models.CharField(verbose_name='网卡配置', max_length=50, null=True, blank=True)
    osconfig = models.JSONField(verbose_name='系统配置', encoder=DjangoJSONEncoder, default=os_config)

    class Meta:
        verbose_name = '配置信息'
        verbose_name_plural = verbose_name

    def __str__(self) -> str:
        return self.model + ' ' + self.cpu + ' ' + self.memory + ' ' + self.pcie


class Device(BaseModel):
    STATUS = (
        ('1', '可借'),
        ('2', '借出')
    )
    name = models.CharField(verbose_name='设备名称', unique=True, max_length=200)
    type = models.CharField(verbose_name='设备类型', choices=(('0', '服务器'), ('1', '工作站')), max_length=20)
    locate = models.ForeignKey(verbose_name='存放位置', to=DeviceArea, on_delete=models.SET_NULL, null=True, blank=True)
    sn = models.CharField(verbose_name='序列号', null=False, max_length=100)
    number = models.CharField(verbose_name='财编号', null=False, max_length=50)
    hostname = models.CharField(verbose_name='主机名', null=False, max_length=60)
    ip = models.CharField(verbose_name='IP地址', null=False, max_length=20)
    account = models.CharField(verbose_name='账户', null=False, max_length=100)
    bmc = models.CharField(verbose_name='BMC地址', null=True, blank=True, max_length=20)
    bmc_account = models.CharField(verbose_name='BMC账户', null=True, blank=True, max_length=50)
    config = models.ForeignKey(verbose_name='设备配置', to=DeviceConfig, on_delete=models.SET_NULL, null=True, blank=True)
    is_cse = models.BooleanField(verbose_name='是否CSE', default=True, null=False)
    status = models.CharField(verbose_name='设备状态', choices=STATUS, default='1', max_length=5, null=True, blank=True)
    vender_type = models.CharField(verbose_name='用途分类', max_length=50, null=True, blank=True)
    current_user = models.ForeignKey(verbose_name='当前使用者', to=DeviceUser, on_delete=models.DO_NOTHING, default=2)
    history = HistoricalRecords()

    class Meta:
        verbose_name = '设备信息'
        verbose_name_plural = verbose_name

    def __str__(self) -> str:
        return self.name + '-' + self.ip + '_' + self.number


class DeviceBorrow(BaseModel):
    device = models.ForeignKey(verbose_name='借用的设备', related_name='borrows', to=Device, on_delete=models.CASCADE)
    user = models.ForeignKey(verbose_name='使用者', to=DeviceUser, on_delete=models.DO_NOTHING)
    reason = models.TextField(verbose_name='借用理由', null=False)
    time_borrowed = models.DateTimeField(verbose_name='借用时间', null=True)
    time_end = models.DateTimeField(verbose_name='归还时间', null=True, blank=True)
    is_return = models.BooleanField(verbose_name='是否归还', default=False)

    class Meta:
        verbose_name = '设备借用'
        verbose_name_plural = verbose_name
        ordering = ['-time_borrowed']
        indexes = [
            models.Index(fields=['time_borrowed']),
            models.Index(fields=['date_created']),
            models.Index(fields=['date_updated']),
            models.Index(fields=['is_return'])
        ]

    def __str__(self) -> str:
        return self.device.name + '_' + self.time_borrowed.strftime(
            "%Y%m%d%H%M%S") + '_' + self.user.username + '_' + self.device.number


def borrow_record_op(instance):
    if instance and instance.__original_remark != instance.remark and instance.remark:
        # select latest borrow record and set end time to now,set is_return to true
        queryset = DeviceBorrow.objects.filter(device__number=instance.number)
        if queryset:
            dev_brr = queryset[0]
            dev_brr.is_return = True
            dev_brr.time_end = datetime.datetime.now(tz=timezone.utc)
            dev_brr.save()
        # new device borrow create
        user = instance.current_user
        rm = instance.ip + ' ' + instance.account
        if instance.config:
            rm = instance.ip + ' ' + instance.account + ' ' + json.dumps(instance.config.osconfig)
        tb = datetime.datetime.now(tz=timezone.utc)
        db = DeviceBorrow(device=instance, user=user, reason=instance.remark, time_borrowed=tb, remark=rm)
        db.save()


def post_init_hook(sender, **kwargs):
    instance = kwargs.get('instance', None)
    if instance:
        instance.__original_remark = instance.remark


def post_save_hook(sender, **kwargs):
    created = kwargs.get('created', None)
    if not created:
        instance = kwargs.get('instance', None)
        borrow_record_op(instance)


post_init.connect(post_init_hook, sender=Device)
post_save.connect(post_save_hook, sender=Device)
