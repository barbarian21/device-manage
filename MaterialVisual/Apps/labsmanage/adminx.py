from __future__ import absolute_import
import xadmin
from xadmin import views
from .models import LabRequests, LabcloudModel, Attachment, AccountInfo
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side
from xadmin.plugins.inline import Inline
from xadmin.plugins.batch import BatchChangeAction


# @xadmin.sites.register(LabRequests)
# class LabRequestsAdmin(object):
#     list_display = ('title', 'request', 'user', 'handler', 'result', 'type')
#     list_display_links = ('title',)
#     search_fields = ['title', 'request', 'type', 'remark']
#     list_filter = ['type', 'result', 'req_time']
#     show_bookmards = False
#     relfield_style = "fk-ajax"
#     reversion_enable = True


# @xadmin.sites.register(Attachment)
# class AttachmentAdmin(object):
#     list_display = ('id', 'report', 'attach')
#     list_display_links = ('id',)
#     search_fields = ['report__title', 'report__request', 'report__type']
#     list_filter = ['report__type']
#     show_bookmards = False
#     relfield_style = "fk-ajax"
#     reversion_enable = True


@xadmin.sites.register(LabcloudModel)
class LabcloudModelAdmin(object):
    list_display = ('name', 'customer', 'status', 'card_type', 'software', 'owner', 'use_days')
    list_display_links = ('name')


@xadmin.sites.register(AccountInfo)
class AccountInfoAdmin(object):
    list_display = ('url', 'account', 'passwd', 'remark')
    list_display_links = ('url')
    search_fields = ['url', 'account', 'passwd', 'remark']
    list_filter = ['is_https']

