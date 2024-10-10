from django.urls import path,include
from rest_framework import routers
from users.views import DeviceUserViewSet
from cards.views import CardModelViewSet,CardBorrowViewSet
from devices.views import DeviceViewSet,DeviceAreaViewSet,DeviceBorrowViewSet,DeviceConfigViewSet
from materials.views import MaterialsViewSet, PurchasesViewSet, BudgetsViewSet, OthersViewSet
from labsmanage.views import LabRequestsViewSet,LabcloudsViewSet
from questions.views import QuestionModelViewSet,SupportModelViewSet
from modelzoo.views import ReportModelViewSet,ReleaseModelViewSet
from sampletest.views import SampleTestViewSet
router = routers.DefaultRouter()

# users
router.register(r'users', DeviceUserViewSet)

# cards
router.register(r'cards/card', CardModelViewSet)
router.register(r'cards/borrow', CardBorrowViewSet)

# devices
router.register(r'devices/device', DeviceViewSet)
router.register(r'devices/location', DeviceAreaViewSet)
router.register(r'devices/borrow', DeviceBorrowViewSet)
router.register(r'devices/config', DeviceConfigViewSet)

# material & purchase & budget (permission)
router.register(r'materials/use', MaterialsViewSet)
router.register(r'materials/purchase', PurchasesViewSet)
router.register(r'materials/budget', BudgetsViewSet)
router.register(r'materials/other', OthersViewSet)

# model zoo visual,daily report visual,release version Link
router.register(r'modelzoo/report', ReportModelViewSet)
router.register(r'modelzoo/release', ReleaseModelViewSet)

# lab requests,lab cloud use(permission)
router.register(r'labsmanage/request', LabRequestsViewSet)
router.register(r'labsmanage/labcloud', LabcloudsViewSet)


# questionnaire investigation （uxt,uat,support offline,bug and advice commit)
router.register(r'questions/question', QuestionModelViewSet)
router.register(r'questions/support', SupportModelViewSet)

# sample test
router.register(r'sampletest/sampletest', SampleTestViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
]