from __future__ import absolute_import
import xadmin
from xadmin import views
from .models import DeviceUser
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side
from xadmin.plugins.inline import Inline
from xadmin.plugins.batch import BatchChangeAction


@xadmin.sites.register(DeviceUser)
class DeviceUserAdmin(object):
    list_display = ('username', 'user_type',)
    list_display_links = ("username",)
    # wizard_form_list = [
    #     ("First's Form", ("name", "description")),
    #     ("Second Form", ("contact", "telphone", "address")),
    #     ("Thread Form", ("customer_id",))
    # ]
    search_fields = ['username', 'user_type']
    list_filter = ['user_type']
    # list_quick_filter = [{"field": "name", "limit": 10}]
    #
    show_bookmards = False
    relfield_style = "fk-select"
    reversion_enable = True
    #
    # actions = [BatchChangeAction, ]
    # batch_fields = ("remark",)