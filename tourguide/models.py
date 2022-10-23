import datetime
from unicodedata import name
from django.db import models
from django.conf import settings

class Task(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
    )
    date = models.DateField('',default=datetime.date.today)
    destination = models.CharField(max_length=255)