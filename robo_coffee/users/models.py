from django.db import models

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    google_calendar_token = models.TextField(blank=True, null=True)
    weather_api_key = models.CharField(max_length=255, blank=True, null=True)
    sms_api_key = models.CharField(max_length=255, blank=True, null=True)
    preferences = models.JSONField(default=dict, blank=True, null=True)

    def __str__(self):
        return self.user.username
