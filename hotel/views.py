from django.shortcuts import render, redirect, get_object_or_404
from hotel.models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core import serializers

# Create your views here.
def show_hotel(request):
    data_hotel_item = Hotel.objects.all()
    context = {
        'hotel_items' : data_hotel_item,
        'user' : request.user
    }
    return render(request, "hotel.html", context)

def show_json(request): 
    data = Hotel.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_room(request): 
    data = Rooms.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_hotel_rooms(request, id):
    hotel = Hotel.objects.get(pk=id)
    data_room_item = Rooms.objects.filter(room_hotel = hotel)
    context = {
        'hotel' : hotel,
        'room' : data_room_item,
        'id' : id,
        'user' : request.user
    }
    return render(request, "rooms.html", context)

def delete_room(request, room_id, hotel_id):
    object = Rooms.objects.get(room_hotel=hotel_id, pk=room_id)
    object.delete()
    return HttpResponseRedirect(reverse("hotel:show_hotel_rooms"))

def delete_hotel(request, id):
    object = get_object_or_404(Hotel, pk = id) 
    object.delete()
    return HttpResponseRedirect(reverse("hotel:show_hotel"))

def add_hotel(request):
    if request.method == "POST":
        hotel_name = request.POST.get("hotel_name")
        hotel_photo = request.POST.get('hotel_photo', None)
        hotel_address = request.POST.get("hotel_address")
        email = request.POST.get("email")
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
                    "hotel_photo" : hotel_photo,
                    "email": email,
                    "star": star,
                    "description": hotel.description,
                },
            },
            status=200,
        )

def add_room(request):
    if request.method == "POST":
        room_type = request.POST.get("room_type")
        room_description = request.POST.get("room_description")
        room_price = request.POST.get("room_price")
        room_photo = request.POST.get('room_photo', None)
        room_hotel = Hotel.objects.get(pk=request.POST.get("room_hotel"))
        room = Rooms.objects.create(
            room_type=room_type,
            room_description=room_description,
            room_price=room_price,
            room_hotel=room_hotel,
            room_photo=room_photo
        )
        return JsonResponse(
            {
                "pk": room.id,
                "fields": {
                    "room_type" : room_type,
                    "room_description": room_description,
                    "room_photo": room_photo,
                    "room_price": room_price,
                    "room_hotel": room_hotel.pk,
                },
            },
            status=200,
        )

def is_booked(request, id):
    item = Rooms.objects.get(pk=id)
    item.is_booked = not item.is_booked
    item.save()
    print(item.is_booked)
    return redirect('hotel:show_hotel')