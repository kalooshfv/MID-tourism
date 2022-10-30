from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core import serializers

from landmarks.models import Landmark

def return_json(request):
    data = Landmark.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_landmarks(request):
    landmarks = Landmark.objects.all()
    context = {
        'landmarks': landmarks,
        'user': request.user,
    }
    return render(request, "landmarks.html", context)

def add_landmark(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        location = request.POST.get('location')
        description = request.POST.get('description')
        image = request.FILES['image']

        new = Landmark(name=name, location=location, description=description, image=image)
        new.save()

        return HttpResponse(b"CREATED", status=201)

def delete_landmark(request, id):
    item = get_object_or_404(Landmark, pk = id)
    item.delete()
    return HttpResponse()