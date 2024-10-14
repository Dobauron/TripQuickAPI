from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import EventViewSet, EventSubTypeAPIView

router = DefaultRouter()
router.register(r"", EventViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("sub-types/", EventSubTypeAPIView.as_view(), name="event-subtypes"),
]
