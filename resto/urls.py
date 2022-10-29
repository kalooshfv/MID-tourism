from django.urls import path
from resto.views import *
app_name = 'resto'

urlpatterns = [
    path('', show_restaurant, name='show_restaurant'),
    # path('detail/<int:id>', show_restaurant_detail, name='show_restaurant_detail'),
    path('create_resto/', create_restaurant, name = 'create_resto'),
    path('show_restaurant_json/', show_restaurant_json, name = 'show_restaurant_json'),
    # path('create_food/<int:id>', create_food, name='create_food'),
    # path('delete_food/<int:food_id>/<int:resto_id>', delete_food, name='delete_food'),
    path('delete_restaurant/<int:id>', delete_restaurant, name='delete_restaurant'),
    # path('create_schedule/', create_schedule, name= 'create_schedule'),
    # path('hours_json/', show_hours_json, name='hours_json'),
]