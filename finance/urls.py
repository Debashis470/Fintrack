from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FinanceDataViewSet

router = DefaultRouter()
router.register(r'finance', FinanceDataViewSet, basename='finance')

urlpatterns = [
    path('', include(router.urls)),
]
