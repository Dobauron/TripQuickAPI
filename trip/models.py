from django.db import models
from user_func.models import Account
from django.core.exceptions import ValidationError


class Trip(models.Model):
    place = models.CharField(max_length=255, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.place

    def clean(self):
        if self.end_at < self.start_at:
            raise ValidationError("End date cannot be earlier than start date.")
