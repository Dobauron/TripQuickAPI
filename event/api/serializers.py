from rest_framework import serializers
from ..models import Event, EventSubLabel, EventLabel


class EventSubLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventSubLabel
        fields = ["event_type", "event_sub_type", "img_url"]


class EventLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventLabel
        fields = ["event_type", "img_url"]


class EventSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(
        max_digits=10, decimal_places=2, coerce_to_string=False
    )

    class Meta:
        model = Event
        fields = [
            "trip",
            "name",
            "start_date",
            "end_date",
            "attachments",
            "links",
            "price",
            "notes",
            "event_type",
            "event_sub_type",
        ]
