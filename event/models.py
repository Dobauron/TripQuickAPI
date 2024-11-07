from django.db import models
from trip.models import Trip
from django.utils.translation import gettext_lazy as _


class BaseEvent(models.Model):
    TRANSPORT = "transport"
    ACCOMMODATION = "accommodation"
    VEHICLE_RENTAL = "vehicle_rental"
    ACTIVITIES = "activities"
    OTHER = "other"

    EVENT_TYPE_CHOICES = [
        (TRANSPORT, _("Transport")),
        (ACCOMMODATION, _("Zakwaterowanie")),
        (VEHICLE_RENTAL, _("Wypożyczenie pojazdu")),
        (ACTIVITIES, _("Aktywności")),
        (OTHER, _("Inne")),
    ]

    event_type = models.CharField(max_length=50, choices=EVENT_TYPE_CHOICES)
    img_url = models.URLField(null=True, blank=True)
    event_sub_type = models.CharField(max_length=50)

    class Meta:
        abstract = True


class Event(BaseEvent):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name="events")
    name = models.CharField(max_length=255, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField(blank=True)
    img_url = None
    links = models.JSONField(
        default=list, blank=True, help_text="List of links associated with the event"
    )
    attachments = models.JSONField(
        default=list,
        blank=True,
        help_text="List of attachments associated with the event",
    )

    def __str__(self):
        return f"{self.name} ({self.event_type})"

    class Meta:
        ordering = ["trip", "start_date"]


class EventSubLabel(BaseEvent):

    def __str__(self):
        return self.event_sub_type


class EventLabel(BaseEvent):
    event_sub_type = None

    def __str__(self):
        return self.event_type
