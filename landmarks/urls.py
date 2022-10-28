from django.urls import path
from landmarks.views import *

app_name = 'landmarks'

urlpatterns = [
    path('', show_landmarks, name='show_landmarks'),
]