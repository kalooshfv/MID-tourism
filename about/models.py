from django.db import models

# Create your models here.
from django.db import models

class UserSuggestion(models.Model):
    full_name = models.CharField(max_length=50, null=True, blank=True),
    phone_number = models.CharField(max_length=15, null=True, blank=True),
    email = models.CharField(max_length=50, null=True, blank=True)
    message = models.TextField()
    date = models.DateField(auto_now=True)
