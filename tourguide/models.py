import datetime
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null = True,
    )
    date = models.DateField(default=datetime.date.today)
    destination = models.CharField(max_length=255)