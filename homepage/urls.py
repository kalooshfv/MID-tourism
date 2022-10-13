from django.urls import path
from midtourism.homepage.views import homepage

app_name = 'homepage'

urlpatterns = [
    path('', homepage, name='homepage'),
]