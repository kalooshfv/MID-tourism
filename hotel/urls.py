from django.urls import path
from hotel.views import *

app_name = 'hotel'

urlpatterns = [
    path('', show_hotel, name='show_hotel'),
    path('room/<int:id>', show_hotel_rooms, name='show_hotel_rooms'),
    path('json/', show_json, name="show_json"),
    path('create_hotel/', create_hotel, name='create_hotel'),
    path('create_room/<int:id>', create_room, name='create_room'),
    path('delete_hotel/<int:id>', delete_hotel, name='delete_hotel'),
    path('delete_room/<int:room_id>/<int:hotel_id>', delete_room, name='delete_room'),
    path('add_hotel/', add_hotel, name='add_hotel'),
]