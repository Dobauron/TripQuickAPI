from django.db import models
from trip.models import Trip


class Event(models.Model):
    TRANSPORT = "transport"
    ACCOMMODATION = "accommodation"
    VEHICLE_RENTAL = "vehicle_rental"
    ACTIVITIES = "activities"
    OTHER = "other"

    EVENT_TYPE_CHOICES = [
        (TRANSPORT, "Transport"),
        (ACCOMMODATION, "Zakwaterowanie"),
        (VEHICLE_RENTAL, "Wypożyczenie pojazdu"),
        (ACTIVITIES, "Aktywności"),
        (OTHER, "Inne"),
    ]

    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name="events")
    name = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    attachment = models.FileField(
        upload_to="event_attachments/",
        blank=True,
        null=True,
        help_text="Załącznik wydarzenia",
    )
    links = models.URLField(blank=True, null=True, help_text="Powiązane linki URL")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, help_text="Cena wydarzenia"
    )
    notes = models.TextField(
        blank=True, null=True, help_text="Notatki dotyczące wydarzenia"
    )

    # Typ wydarzenia
    event_type = models.CharField(max_length=50, choices=EVENT_TYPE_CHOICES)
    event_sub_type = models.CharField(max_length=50, default="default")

    def __str__(self):
        return f"{self.name} ({self.event_type})"

    class Meta:
        ordering = ["trip", "start_date"]


class EventSubType(models.Model):
    EVENT_TYPE_CHOICES = [
        ("TRANSPORT", "Transport"),
        ("ACCOMMODATION", "Zakwaterowanie"),
        ("VEHICLE_RENTAL", "Wypożyczenie pojazdu"),
        ("ACTIVITIES", "Aktywności"),
        ("OTHER", "Inne"),
    ]
    event_type = models.CharField(max_length=50, choices=EVENT_TYPE_CHOICES)
    event_sub_type = models.CharField(max_length=50)
    img_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.event_type
