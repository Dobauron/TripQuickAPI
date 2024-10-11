from rest_framework import serializers
from ..models import Trip


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = [
            "id",
            "travel_place",
            "description",
            "travel_start_at",
            "travel_end_at",
        ]
        read_only_fields = ["account"]
