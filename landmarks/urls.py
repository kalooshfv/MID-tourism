from django.urls import path
from landmarks.views import *

app_name = 'landmarks'

urlpatterns = [
    path('', show_landmarks, name='show_landmarks'),
    path('json', return_json, name='json'),
    path('add-landmark', add_landmark, name='add_landmark'),
    path('delete-landmark/<int:id>', delete_landmark, name='delete_landmark'),
]