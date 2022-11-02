from django.urls import path
from about.views import show_about_section, post_suggestion

app_name = 'about'

urlpatterns = [
    path('', show_about_section, name='launch'),
    path('post-suggestion/', post_suggestion, name='post-suggestion')
]