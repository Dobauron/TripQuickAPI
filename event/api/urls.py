from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, EventSubTypeAPIView

router = DefaultRouter()
router.register(r"", EventViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("sub_type", EventSubTypeAPIView.as_view()),
]
