from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('vendors', VendorView ,basename='vendors')
router.register('purchase_orders', PurchaseOrderView,basename='purchase_orders')
router.register('vendor_performance', VendorPerformanceView,basename='vendor_performance')

urlpatterns = [
    path('', include(router.urls)),
]