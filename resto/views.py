from django.shortcuts import render, get_object_or_404
from resto.models import *
from resto.forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.decorators import login_required 
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def show_restaurant(request):
    data_restaurant_items = Restaurant.objects.all()
    context = {
        'restaurants': data_restaurant_items,
        'user': request.user,
    }
    return render(request, 'resto.html', context)

def show_restaurant_json(request):
    data = Restaurant.objects.all()
    return HttpResponse(serializers.serialize("json", data), \
        content_type="application/json")

@login_required(login_url='/login')
def create_restaurant(request):
    if request.method == "POST":
        resto_name = request.POST.get("resto_name")
        resto_address = request.POST.get("resto_address")
        resto_email = request.POST.get("resto_email")
        resto_phone = request.POST.get("resto_phone")
        resto_description = request.POST.get("resto_description")
        resto_photo = request.FILES["resto_photo"]
        resto_delivery = request.POST.get("resto_delivery")
        resto = Restaurant.objects.create(
            resto_name = resto_name,
            resto_address = resto_address,
            resto_email = resto_email,
            resto_phone = resto_phone,
            resto_description = resto_description,
            resto_photo = resto_photo,
            resto_delivery = resto_delivery,
        )
        resto.save()
        return HttpResponse(b"CREATED", status=201)

@login_required(login_url='/login')
def delete_restaurant(request, id):
    object = get_object_or_404(Restaurant, pk = id) 
    object.delete()
    return HttpResponseRedirect(reverse("resto:show_restaurant"))

@csrf_exempt
def create_restaurant_flutter(request):
    if request.method == "POST":
        resto_name = request.POST.get("resto_name")
        resto_address = request.POST.get("resto_address")
        resto_email = request.POST.get("resto_email")
        resto_phone = int(request.POST.get("resto_phone"))
        resto_description = request.POST.get("resto_description")
        resto_photo = request.POST.get("resto_photo")
        resto_delivery = request.POST.get("resto_delivery")
        resto = Restaurant.objects.create(
            resto_name = resto_name,
            resto_address = resto_address,
            resto_email = resto_email,
            resto_phone = resto_phone,
            resto_description = resto_description,
            resto_photo = resto_photo,
            resto_delivery = resto_delivery,
        )
        resto.save()
        return HttpResponse(status=201)
        
        

