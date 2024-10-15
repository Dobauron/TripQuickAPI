from rest_framework import viewsets
from ..models import Event, EventSubType, EventLabel
from .serializers import EventSerializer, EventSubTypeSerializer, EventLabelSerializer
from rest_framework.generics import ListAPIView


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventSubTypeAPIView(ListAPIView):
    queryset = EventSubType.objects.all()
    serializer_class = EventSubTypeSerializer

class EventLabelAPIView(ListAPIView):
    queryset = EventLabel.objects.all()
    serializer_class = EventLabelSerializer
