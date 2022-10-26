from django.db import models
import uuid

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

WEEKDAYS = [
  (1, ("Monday")),
  (2, ("Tuesday")),
  (3, ("Wednesday")),
  (4, ("Thursday")),
  (5, ("Friday")),
  (6, ("Saturday")),
  (7, ("Sunday")),
]

weekday_dict = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}


class Restaurant(models.Model):
    resto_id = models.UUIDField(max_length = 64, unique = True, default=uuid.uuid4, editable=False)
    resto_name = models.CharField(max_length = 64)
    resto_address = models.CharField(max_length = 128)
    resto_email = models.EmailField()
    resto_phone = models.BigIntegerField()
    resto_description = models.TextField()
    resto_photo = models.ImageField(upload_to = 'resto/', null=True, blank=True)
    resto_delivery = models.URLField(null=True, blank=True)
    
class Food(models.Model):
    food_name = models.CharField(max_length = 64)
    food_price = models.IntegerField()
    food_stock = models.BooleanField()
    food_description = models.TextField()
    food_resto = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    food_photo = models.ImageField(upload_to = 'food/', null=True, blank=True)

# Source: https://www.youtube.com/watch?v=0dQQwN9iBbI
class OpeningHours(models.Model):
    hours_restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    hours_weekday = models.IntegerField(choices=WEEKDAYS)
    hours_from_hour = models.TimeField()
    hours_to_hour = models.TimeField()

    class Meta:
        ordering = ('hours_weekday', 'hours_from_hour')
        unique_together = ('hours_weekday', 'hours_from_hour', 'hours_to_hour', 'hours_restaurant')

    def __str__(self):
        return u'%s: %s - %s' % (weekday_dict[self.hours_weekday],
                                 self.hours_from_hour, self.hours_to_hour)

