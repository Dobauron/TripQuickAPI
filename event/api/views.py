from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from ..models import Event
from .serializers import EventSerializer


class EventWithServiceTypeViewSet(viewsets.ModelViewSet):
    """
    ViewSet obsługujący zarówno Event, jak i zagnieżdżone ServiceType.
    """

    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        """Tworzenie nowego Event z zagnieżdżonymi ServiceType."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def update(self, request, *args, **kwargs):
        """Aktualizacja Eventu z zagnieżdżonymi ServiceType."""
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
