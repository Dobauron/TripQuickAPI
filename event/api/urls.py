from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import EventViewSet, EventSubLabelAPIView, EventLabelAPIView

router = DefaultRouter()
router.register(r"", EventViewSet)

urlpatterns = [
    path("/", include(router.urls)),
    path("sub-types/", EventSubLabelAPIView.as_view(), name="event-subtypes"),
    path("types/", EventLabelAPIView.as_view(), name="event-label"),
]
