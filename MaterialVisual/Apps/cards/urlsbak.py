from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'cards'
router = routers.DefaultRouter()
router.register(r'', views.CardModelViewSet)
urlpatterns = [
    path(r'', include(router.urls)),
]
