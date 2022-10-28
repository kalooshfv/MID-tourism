from django.db import models

# Create your models here.
class TransportList(models.Model):
    transport_name = models.CharField(max_length=40)
    transport_price = models.TextField()
    description = models.TextField()
