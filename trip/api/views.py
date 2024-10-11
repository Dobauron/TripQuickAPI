from rest_framework import viewsets
from ..models import Trip
from .serializers import TripSerializer
from rest_framework.permissions import IsAuthenticated
from datetime import timezone
from rest_framework.exceptions import PermissionDenied


class TripViewSet(viewsets.ModelViewSet):
    serializer_class = TripSerializer
    permission_classes = [IsAuthenticated]
    queryset = Trip.objects.all()

    def get_queryset(self):
        user = self.request.user
        queryset = Trip.objects.filter(
            account=user
        )
        return queryset

    def perform_create(self, serializer):
        serializer.save(account=self.request.user)
