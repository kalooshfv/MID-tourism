from django.urls import path
from rental_transport.views import *

app_name = 'rental_transport'

urlpatterns = [
    path('', show_transportlist, name='show_transportlist'),
    path('json/', show_json, name="show_json"),
    path('create_transport/', create_transport, name="create_transport"),
]