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
    # Wspólne pola dla wszystkich wydarzeń
    name = models.CharField(max_length=255, help_text="Nazwa wydarzenia")
    start_date = models.DateTimeField(help_text="Data rozpoczęcia wydarzenia")
    end_date = models.DateTimeField(help_text="Data zakończenia wydarzenia")
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

    def __str__(self):
        return f"{self.name} ({self.event_type})"

    class Meta:
        ordering = ["trip", "start_date"]


class ServiceType(models.Model):
    TRANSPORT_CHOICES = [
        ("bus", "Bus"),
        ("airplane", "Airplane"),
        ("train", "Train"),
        ("car", "Car"),
        ("boat", "Boat"),
        ("other", "Other"),
    ]
    ACCOMODATION_CHOICES = [
        ("hotel", "Hotel"),
        ("camping", "Camping"),
        ("apartment", "Apartment"),
        ("other", "Other"),
    ]
    VEHICALES_CHOICES = [
        ("hotel", "Hotel"),
        ("camping", "Camping"),
        ("apartment", "Apartment"),
        ("other", "Other"),
    ]

    service_type = models.CharField(max_length=50)
    event = models.OneToOneField(Event, on_delete=models.CASCADE)
    service_picture = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.service_type
