from django.contrib import admin
from .models import Event, EventLabel, EventSubLabel


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "event_type", "trip", "start_date", "end_date", "price")
    list_filter = ("event_type", "trip", "start_date", "end_date")
    search_fields = ("name", "notes", "event_type")
    ordering = ("trip", "start_date")
    fieldsets = (
        (None, {
            "fields": ("name", "trip", "event_type", "event_sub_type")
        }),
        ("Details", {
            "fields": ("start_date", "end_date", "price", "notes", "links", "attachments"),
        }),
    )


@admin.register(EventLabel)
class EventLabelAdmin(admin.ModelAdmin):
    list_display = ("event_type",)
    search_fields = ("event_type",)


@admin.register(EventSubLabel)
class EventSubLabelAdmin(admin.ModelAdmin):
    list_display = ("event_sub_type", "event_label")
    list_filter = ("event_label",)
    search_fields = ("event_sub_type",)
