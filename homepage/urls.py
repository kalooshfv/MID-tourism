from django.urls import path
from homepage.views import *

app_name = 'homepage'

urlpatterns = [
    path('', homepage, name='homepage'),
]