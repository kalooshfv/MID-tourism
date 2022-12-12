from django.urls import path
from tourguide.views import *


app_name = 'tourguide'

urlpatterns = [
    path('', show_schedule, name='show_schedule'),
    path("json/", show_json, name="show_json"),
    path("add/", add_schedule, name="add_schedule"),
    path("update-booked/<int:id>", update_booked, name="update_booked"),
    path("add_schedule_flutter/", add_schedule_flutter, name="add_schedule_flutter"),
    path("update_booked_flutter/<int:id>", update_booked_flutter, name="update_booked_flutter"),
]