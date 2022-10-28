from django import forms
from hotel.models import *

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = [
            'hotel_name',
            'hotel_address',
            'hotel_photo',
            'email',
            'description'
        ]

class RoomForm(forms.ModelForm):
    class Meta:
        model = Rooms
        fields = [
            'room_type',
            'room_description',
            'room_photo',
            'room_price'
        ]