from django.urls import path
from rental_transport.views import *

app_name = 'rental_transport'

urlpatterns = [
    path('', show_transportlist, name='show_wishlist'),
]