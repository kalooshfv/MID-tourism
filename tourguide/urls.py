from django.urls import path
from tourguide.views import *
from tourguide.views import show_schedule
from tourguide.views import my_form
from tourguide.views import register
from tourguide.views import login_user
from tourguide.views import logout_user
from tourguide.views import show_json
from tourguide.views import add_schedule
from tourguide.views import update_booked


app_name = 'tourguide'

urlpatterns = [
    path('', show_schedule, name='show_schedule'),
    path('create-task/', my_form, name='create-forms'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path("json/", show_json, name="show_json"),
    path("add/", add_schedule, name="add_schedule"),
    path("update-booked/<int:id>", update_booked, name="update_booked"),
]