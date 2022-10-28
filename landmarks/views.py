from django.shortcuts import render

from landmarks.models import Landmark

def show_landmarks(request):
    landmarks = Landmark.objects.all()
    context = {
        'landmarks': landmarks
    }
    return render(request, "landmarks.html", context)