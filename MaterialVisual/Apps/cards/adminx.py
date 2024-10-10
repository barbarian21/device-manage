from __future__ import absolute_import
import xadmin
from xadmin import views
from .models import CardModel, CardBorrow
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side
from xadmin.plugins.inline import Inline
from xadmin.plugins.batch import BatchChangeAction


@xadmin.sites.register(views.BaseAdminView)
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


@xadmin.sites.register(views.CommAdminView)
class GlobalSettings(object):
    site_title = "CSE资产管理系统"
    site_footer = "cse@enflame-tech.com"
    #menu_style = "accordion"


@xadmin.sites.register(CardModel)
class CardModelAdmin(object):
    list_display = ('sn', 'name', 'card_type', 'card_project', 'remark', 'status', 'owner','version')
    list_display_links = ("sn",)
    # wizard_form_list = [
    #     ("First's Form", ("name", "description")),
    #     ("Second Form", ("contact", "telphone", "address")),
    #     ("Thread Form", ("customer_id",))
    # ]
    search_fields = ['sn', 'name', 'card_type', 'remark', 'owner']
    list_filter = ['sn', 'name', 'card_type','owner']
    # list_quick_filter = [{"field": "name", "limit": 10}]
    #
    show_bookmards = True
    relfield_style = "fk-select"
    reversion_enable = True
    #
    # actions = [BatchChangeAction, ]
    # batch_fields = ("remark",)


@xadmin.sites.register(CardBorrow)
class CardBorrowAdmin(object):
    list_display = ('card', 'user', 'reason', 'time_borrowed', 'time_end', 'is_return')
    list_display_links = ('card',)
    search_fields = ['card', 'reason']
    list_filter = ['card', 'user', 'is_return']

    show_bookmards = False
    relfield_style = "fk-select"
    reversion_enable = True

