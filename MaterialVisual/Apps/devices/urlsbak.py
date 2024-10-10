from django.urls import path,include
from rest_framework import routers
from . import views
app_name = 'devices'
router = routers.DefaultRouter()
router.register(r'devices',views.DeviceViewSet)
router.register(r'areas',views.DeviceAreaViewSet)
router.register(r'borrows',views.DeviceBorrowViewSet)
router.register(r'config',views.DeviceConfigViewSet)
urlpatterns = [
    path(r'',include(router.urls)),
]