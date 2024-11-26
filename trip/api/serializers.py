from rest_framework import serializers
from ..models import Trip


class TripSerializer(serializers.ModelSerializer):
    event_ids = serializers.SerializerMethodField()

    class Meta:
        model = Trip
        fields = ["id", "destination", "description", "start_at", "end_at", "event_ids"]
        read_only_fields = ["account"]

    def get_event_ids(self, obj):
        # Zwraca listę ID powiązanych Eventów
        return list(obj.events.values_list("id", flat=True))
