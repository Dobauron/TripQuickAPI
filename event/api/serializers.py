from rest_framework import serializers
from ..models import Event, ServiceType


class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = ["id", "service_type", "service_picture"]


class EventSerializer(serializers.ModelSerializer):
    servicetype = ServiceTypeSerializer()  # Zmieniamy na 'servicetype'

    class Meta:
        model = Event
        fields = [
            "id",
            "trip",
            "name",
            "start_date",
            "end_date",
            "attachment",
            "links",
            "price",
            "notes",
            "event_type",
            "servicetype",
        ]

    def create(self, validated_data):
        service_type_data = validated_data.pop(
            "servicetype", None
        )

        # Tworzymy event
        event = Event.objects.create(**validated_data)

        # Tworzymy związany service_type
        if service_type_data:
            ServiceType.objects.create(event=event, **service_type_data)

        return event

    def update(self, instance, validated_data):
        service_type_data = validated_data.pop(
            "servicetype", None
        )  # Zmieniamy na 'servicetype'

        # Zaktualizuj dane eventu
        instance.name = validated_data.get("name", instance.name)
        instance.start_date = validated_data.get("start_date", instance.start_date)
        instance.end_date = validated_data.get("end_date", instance.end_date)
        instance.attachment = validated_data.get("attachment", instance.attachment)
        instance.links = validated_data.get("links", instance.links)
        instance.price = validated_data.get("price", instance.price)
        instance.notes = validated_data.get("notes", instance.notes)
        instance.event_type = validated_data.get("event_type", instance.event_type)
        instance.save()

        # Zaktualizuj service_type
        if service_type_data:
            service_type_id = service_type_data.get("id")
            if service_type_id:
                service_type = ServiceType.objects.get(id=service_type_id)
                service_type.service_type = service_type_data.get(
                    "service_type", service_type.service_type
                )
                service_type.service_picture = service_type_data.get(
                    "service_picture", service_type.service_picture
                )
                service_type.save()
            else:
                ServiceType.objects.create(event=instance, **service_type_data)

        return instance
