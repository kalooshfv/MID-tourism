from django.urls import path
from about.views import launch

app_name = 'about'

urlpatterns = [
    path('', launch, name='launch'),
]