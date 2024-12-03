from django.contrib import admin
from .models import Event, EventSubLabel, EventLabel


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "event_type", "trip", "start_date", "end_date", "price")
    list_filter = ("event_type", "trip", "start_date", "end_date")
    search_fields = ("name", "notes", "trip__name")
    ordering = ("trip", "start_date")
    fieldsets = (
        (None, {
            "fields": (
                "trip",
                "name",
                "event_type",
                "event_sub_type",
                "start_date",
                "end_date",
                "price",
                "notes",
                "links",
                "attachments"
            )
        }),
    )


@admin.register(EventSubLabel)
class EventSubLabelAdmin(admin.ModelAdmin):
    list_display = ("event_sub_type", "event_type")
    list_filter = ("event_type",)
    search_fields = ("event_sub_type",)


@admin.register(EventLabel)
class EventLabelAdmin(admin.ModelAdmin):
    list_display = ("event_type",)
    search_fields = ("event_type",)
