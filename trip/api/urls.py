from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TripViewSet

router = DefaultRouter()
router.register(r"", TripViewSet)  # Rejestruje ViewSet pod ścieżką 'trips'

urlpatterns = [
    path("", include(router.urls)),  # Włącza wszystkie URL z routera
]
