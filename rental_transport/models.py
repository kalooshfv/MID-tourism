from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class TransportList(models.Model):
    company_name = models.CharField(max_length=50, null=True)
    transport_name = models.CharField(max_length=50)
    transport_price = models.TextField()
    description = models.TextField()
    availability = models.CharField(max_length=10, default='Available')
