from __future__ import absolute_import
import xadmin
from xadmin import views
from .models import Device, DeviceBorrow, DeviceConfig, DeviceArea
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side
from xadmin.plugins.inline import Inline
from xadmin.plugins.batch import BatchChangeAction


@xadmin.sites.register(Device)
class DeviceAdmin(object):
    list_display = ('name', 'number', 'type', 'ip', 'remark', 'config','vender_type','locate')
    list_display_links = ("name",)
    # wizard_form_list = [
    #     ("First's Form", ("name", "description")),
    #     ("Second Form", ("contact", "telphone", "address")),
    #     ("Thread Form", ("customer_id",))
    # ]
    search_fields = ['number', 'name', 'ip', 'sn', 'vender_type', 'remark']
    list_filter = ['type', 'status', 'is_cse','vender_type']
    # list_quick_filter = [{"field": "name", "limit": 10}]
    #
    show_bookmards = False
    relfield_style = "fk-ajax"
    reversion_enable = True
    list_exclude = ('account', 'bmc', 'bmc_account')
    #
    # actions = [BatchChangeAction, ]
    # batch_fields = ("remark",)
    def get_model_form(self, **kwargs):
        if not self.request.user.is_superuser:
            self.fields = ['name', 'number', 'type', 'ip', 'remark', 'vender_type', 'config', 'locate']
        return super().get_model_form(**kwargs)


@xadmin.sites.register(DeviceBorrow)
class DeviceBorrowAdmin(object):
    list_display = ('device', 'user', 'reason', 'time_borrowed', 'time_end', 'is_return')
    list_display_links = ("device",)

    search_fields = ['device__number', 'device__name', 'device__ip', 'user__username', 'reason']
    list_filter = ['is_return', 'user']

    show_bookmards = False
    relfield_style = "fk-ajax"
    reversion_enable = True


@xadmin.sites.register(DeviceConfig)
class DeviceConfigAdmin(object):
    list_display = ('model', 'vender', 'cpu', 'memory', 'harddisk', 'network')
    list_display_links = ("model",)

    search_fields = ['model', 'vender', 'cpu', 'harddisk', 'memory', 'network']
    list_filter = ['model', 'vender']

    show_bookmards = False
    relfield_style = "fk-select"
    reversion_enable = True


@xadmin.sites.register(DeviceArea)
class DeviceAreaAdmin(object):
    list_display = ('info', 'location')
    list_display_links = ("info",)

    search_fields = ['info', 'location']
    list_filter = ['info']

    show_bookmards = False
    relfield_style = "fk-select"
    reversion_enable = True