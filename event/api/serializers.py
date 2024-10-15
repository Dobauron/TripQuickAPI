from rest_framework import serializers
from ..models import Event, EventSubType, EventLabel


class EventSubTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventSubType
        fields = ["event_type", "event_sub_type", "img_url"]

class EventLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventLabel
        fields = ["event_type", "event_label", "img_url"]

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "trip",
            "name",
            "start_date",
            "end_date",
            "attachment",
            "links",
            "price",
            "notes",
            "event_type",
            "event_sub_type",
        ]
