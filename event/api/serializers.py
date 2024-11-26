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

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Cena nie może być ujemna.")
        return value

    def validate(self, data):
        # Walidacja: data rozpoczęcia musi być przed datą zakończenia
        start_date = data.get("start_date")
        end_date = data.get("end_date")

        if start_date and end_date and start_date > end_date:
            raise serializers.ValidationError(
                {
                    "end_date": "Data zakończenia nie może być wcześniejsza od daty rozpoczęcia."
                }
            )

        # Walidacja: "event_sub_type" nie może być podany bez "event_type"
        event_type = data.get("event_type")
        event_sub_type = data.get("event_sub_type")

        if event_sub_type and not event_type:
            raise serializers.ValidationError(
                {
                    "event_type": "Pole 'event_type' jest wymagane, gdy podano 'event_sub_type'."
                }
            )

        return data

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
