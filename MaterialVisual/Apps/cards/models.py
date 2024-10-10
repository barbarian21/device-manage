import datetime
from django.db import models
from uuid import uuid4
from simple_history.models import HistoricalRecords
from django.db.models.signals import post_init, post_save
from django.utils import timezone
from users.models import DeviceUser


class BaseModel(models.Model):
    id = models.UUIDField(verbose_name='板卡编号', primary_key=True, default=uuid4)
    date_created = models.DateTimeField(verbose_name='添加时间', auto_now_add=True, null=True, blank=True)
    date_updated = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    remark = models.TextField(verbose_name='备注信息', blank=True, null=True)

    class Meta:
        abstract = True


# Create your models here.
class CardModel(BaseModel):
    STATUS = (
        ('1', '可借'),
        ('2', '借出')
    )
    sn = models.CharField(verbose_name='序列号', unique=True, max_length=50, null=False)
    pn = models.CharField(verbose_name='产品号', max_length=20, null=True, blank=True)
    version = models.CharField(verbose_name='存放位置', max_length=20, null=True, blank=True)
    card_type = models.CharField(verbose_name='类型', max_length=20, null=True, blank=True)
    card_project = models.CharField(verbose_name='项目名', max_length=20, null=True, blank=True)
    name = models.CharField(verbose_name='名称', max_length=20, null=False)
    memory = models.CharField(verbose_name='显存', max_length=100, null=False)
    power = models.CharField(verbose_name='功耗', max_length=50, null=False)
    device = models.ForeignKey('devices.Device', on_delete=models.SET_NULL, null=True, blank=True)
    owner = models.CharField(verbose_name='用途分类', max_length=20, null=True, blank=True)
    status = models.CharField(verbose_name='设备状态', choices=STATUS, default='1', max_length=5)
    current_user = models.ForeignKey(verbose_name='当前使用者', to=DeviceUser, on_delete=models.DO_NOTHING, default=2)
    history = HistoricalRecords()

    class Meta:
        verbose_name = '板卡信息'
        verbose_name_plural = verbose_name

    def __str__(self) -> str:
        if self.device:
            return self.sn + '_' + self.name + '_' + self.device.number

        return self.sn + '_' + self.name + '_None'


class CardBorrow(BaseModel):
    card = models.ForeignKey(verbose_name='板卡借用', related_name='cardborrow', to=CardModel, on_delete=models.CASCADE)
    user = models.ForeignKey(verbose_name='使用者', to=DeviceUser, on_delete=models.DO_NOTHING)
    reason = models.TextField(verbose_name='借用理由', null=False)
    time_borrowed = models.DateTimeField(verbose_name='借用时间', null=True)
    time_end = models.DateTimeField(verbose_name='归还时间', null=True, blank=True)
    is_return = models.BooleanField(verbose_name='是否归还', default=False)

    class Meta:
        verbose_name = '板卡借用'
        verbose_name_plural = verbose_name

    def __str__(self) -> str:
        return self.card.sn + '_' + self.time_borrowed.strftime("%Y%m%d%H%M%S") + '_' + self.user.username


def borrow_record_op(instance):
    if instance and instance.__original_remark != instance.remark and instance.remark:
        # select latest borrow record and set end time to now,set is_return to true
        queryset = CardBorrow.objects.filter(card__sn=instance.sn)
        if queryset:
            dev_brr = queryset[0]
            dev_brr.is_return = True
            dev_brr.time_end = datetime.datetime.now(tz=timezone.utc)
            dev_brr.save()
        # new device borrow create
        user = instance.current_user
        tb = datetime.datetime.now(tz=timezone.utc)
        db = CardBorrow(card=instance, user=user, reason=instance.remark, time_borrowed=tb)
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


post_init.connect(post_init_hook, sender=CardModel)
post_save.connect(post_save_hook, sender=CardModel)