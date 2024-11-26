from rest_framework import viewsets
from ..models import Event, EventSubLabel, EventLabel
from .serializers import EventSerializer, EventSubLabelSerializer, EventLabelSerializer
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]


class EventSubLabelAPIView(ListAPIView):
    queryset = EventSubLabel.objects.all()
    serializer_class = EventSubLabelSerializer


class EventLabelAPIView(ListAPIView):
    queryset = EventLabel.objects.all()
    serializer_class = EventLabelSerializer
