from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CarViewSet, CustomerViewSet, RentalViewSet

router = DefaultRouter()
router.register(r'cars', CarViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'rentals', RentalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
