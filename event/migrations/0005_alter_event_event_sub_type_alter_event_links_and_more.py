# Generated by Django 5.1.1 on 2024-10-14 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("event", "0004_eventsubtype_event_event_sub_type_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="event_sub_type",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="event",
            name="links",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="event",
            name="notes",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="event",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
