from django.db import models

# Create your models here.
class Hotel(models.Model):
    hotel_name = models.CharField(max_length=50)
    hotel_address = models.CharField(max_length=100)
    hotel_photo = models.ImageField(upload_to = 'hotel/', null=True, blank=True)
    email = models.EmailField()
    star = models.IntegerField()
    description = models.TextField()

class Rooms(models.Model):
    room_type = models.CharField(max_length=50)
    room_description = models.TextField()
    room_photo = models.ImageField(upload_to = 'room/', null=True, blank=True)
    room_price = models.BigIntegerField()
    room_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)