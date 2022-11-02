from django.urls import path
from tourguide.views import *


app_name = 'tourguide'

urlpatterns = [
    path('', show_schedule, name='show_schedule'),
    path("json/", show_json, name="show_json"),
    path("add/", add_schedule, name="add_schedule"),
    path("update-booked/<int:id>", update_booked, name="update_booked"),
]