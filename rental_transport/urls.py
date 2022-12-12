from django.urls import path
from rental_transport.views import *

app_name = 'rental_transport'

urlpatterns = [
    path('', show_transportlist, name='show_transportlist'),
    path('json/', show_json, name="show_json"),
    path('create_transport/', create_transport, name="create_transport"),
    path('remove_transport/<int:id>', remove_transport, name="remove_transport"),
    path('change_availability/<int:id>', change_availability, name="change_availability"),
    path('create_transport_flutter/', create_transport_flutter, name="create_transport_flutter"),
    path('remove_transport_flutter/<int:id>', remove_transport_flutter, name="remove_transport_flutter"),
    path('change_availability_flutter/<int:id>', change_availability_flutter, name="change_availability_flutter"),
]