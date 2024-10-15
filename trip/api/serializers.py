from rest_framework import serializers
from ..models import Trip


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = [
            "id",
            "destination",
            "description",
            "start_at",
            "end_at",
        ]
        read_only_fields = ["account"]
