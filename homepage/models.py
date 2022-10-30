from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Player(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null = True,
    )
# Create your models here.
