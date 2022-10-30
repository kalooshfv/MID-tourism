from django.db import models

class Landmark(models.Model):
    name = models.CharField(max_length=32)
    location = models.CharField(max_length=64)
    description = models.TextField()
    image = models.ImageField(upload_to = 'landmarks/', null=True, blank=True)