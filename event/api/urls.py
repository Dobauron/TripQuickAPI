from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventWithServiceTypeViewSet

router = DefaultRouter()
router.register(r"", EventWithServiceTypeViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
