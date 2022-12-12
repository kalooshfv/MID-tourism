from django.urls import path
from hotel.views import *

app_name = 'hotel'

urlpatterns = [
    path('', show_hotel, name='show_hotel'),
    path('room/<int:id>', show_hotel_rooms, name='show_hotel_rooms'),
    path('json/', show_json, name="show_json"),
    path('json_room/', show_json_room, name="show_json_room"),
    path('delete_hotel/<int:id>', delete_hotel, name='delete_hotel'),
    path('delete_room/<int:id>', delete_room, name='delete_room'),
    path('add_hotel/', add_hotel, name='add_hotel'),
    path('add_room/<int:id>', add_room, name='add_room'),
    path('room/is_booked/<int:id>', is_booked, name='is_booked'),
    path('add_hotel_flutter/', add_hotel_flutter, name='add_hotel_flutter'),
    path('add_room_flutter/<int:id>', add_room_flutter, name='add_room_flutter'),
    path('show_json_room_flutter/<int:id>', show_json_room_flutter, name='show_json_room_flutter'),
]