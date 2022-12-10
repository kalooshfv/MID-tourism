from django.urls import path
from homepage.views import *

app_name = 'homepage'

urlpatterns = [
    path('', homepage, name='homepage'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('login_flutter/', login_flutter, name='login_flutter'),
]
