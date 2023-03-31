from django.urls import path, include
from rest_framework import routers
from .views import CarViewSet, CustomerViewSet

router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'cars', CarViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
