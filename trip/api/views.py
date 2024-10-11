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
        # Filtruj podróże, aby zwrócić tylko te przypisane do zalogowanego użytkownika
        user = self.request.user
        queryset = Trip.objects.filter(
            account=user
        )  # Filtrowanie po koncie użytkownika

        # # Dodatkowe filtrowanie, jeśli użytkownik chce zobaczyć tylko nadchodzące podróże
        # if self.request.query_params.get('upcoming', None):
        #     queryset = queryset.filter(travel_start_at__gte=timezone.now()).order_by('travel_start_at')

        return queryset

    def perform_create(self, serializer):
        serializer.save(account=self.request.user)

    def perform_destroy(self, instance):
        user = self.request.user
        if instance.account != user:
            raise PermissionDenied("Nie masz uprawnień do usunięcia tej podróży.")
        instance.delete()

    def perform_update(self, serializer):
        user = self.request.user
        trip = self.get_object()
        if trip.account != user:
            raise PermissionDenied("Nie masz uprawnień do aktualizacji tej podróży.")
        serializer.save()
