from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import RatesViewSet

router_v1 = DefaultRouter()
router_v1.register('get-current-usd', RatesViewSet, basename='rates')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]