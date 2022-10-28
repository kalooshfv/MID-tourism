from django.shortcuts import render, redirect, get_object_or_404
from hotel.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from hotel.forms import *
from django.urls import reverse
from django.core import serializers

# Create your views here.
def show_hotel(request):
    data_hotel_item = Hotel.objects.all()
    context = {
        'hotel_items' : data_hotel_item,
    }
    return render(request, "hotel.html", context)

def show_json(request): 
    data = Hotel.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def create_hotel(request):
    form = HotelForm()
    if request.method == "POST":
        form = HotelForm(request.POST, request.FILES)
        if form.is_valid():
            new_hotel = form.save()
            global call_resto_id
            def call_resto_id():
                return new_hotel.pk
            response = HttpResponseRedirect(reverse("resto:create_schedule"))
            return response
    context = {'form': form}
    return render(request, 'hotel_form.html', context)

def show_hotel_rooms(request, id):
    hotel = Hotel.objects.get(pk=id)
    data_room_item = Rooms.objects.filter(room_hotel = hotel)
    context = {
        'hotel' : hotel,
        'room' : data_room_item,
        'id' : id
    }
    return render(request, "rooms.html", context)

def create_room(request, id):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST ,request.FILES)
        if form.is_valid():
            hotel = Hotel.objects.get(pk=id)
            room_form = form.save(commit=False)
            room_form.room_hotel = hotel
            room_form.save()
            response = HttpResponseRedirect(reverse('hotel:show_hotel_rooms', kwargs={'id':id}))
            return response
    else:
        form = RoomForm()
    return render(request, 'room_form.html', {'form':form})

def delete_room(request, room_id, hotel_id):
    object = get_object_or_404(Rooms, pk = room_id)
    object.delete()
    return HttpResponseRedirect(reverse("hotel:show_hotel_rooms", kwargs={'id':hotel_id}))

def delete_hotel(request, id):
    object = get_object_or_404(Hotel, pk = id) 
    object.delete()
    return HttpResponseRedirect(reverse("hotel:show_hotel"))

def add(request):
    if request.method == "POST":
        hotel_name = request.POST.get("hotel_name")
        hotel_address = request.POST.get("hotel_address")
        email = request.POST.get("hotel_email")
        star = request.POST.get("star")
        description = request.POST.get("description")
        hotel = Hotel.objects.create(
            hotel_name=hotel_name,
            hotel_address=hotel_address,
            email=email,
            star=star,
            description=description,
        )
        return JsonResponse(
            {
                "pk": hotel.id,
                "fields": {
                    "hotel_name" : hotel_name,
                    "hotel_address": hotel_address,
                    "email": email,
                    "star": star,
                    "description": hotel.description,
                },
            },
            
            status=200,
        )