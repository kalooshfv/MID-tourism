from django.shortcuts import render, redirect, get_object_or_404
from resto.models import *
from resto.forms import *
from django.contrib import messages
from django.views.generic import DetailView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

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
        
    # form = RestaurantForm()
    # if request.method == "POST":
    #     form = RestaurantForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         new_resto = form.save()
    #         response = HttpResponseRedirect(reverse("resto:show_restaurant_detail", kwargs = {'id': new_resto.pk}))
    #         return response
    # context = {'form': form}
    # return render(request, 'resto_form.html', context)

def delete_restaurant(request, id):
    object = get_object_or_404(Restaurant, pk = id) 
    object.delete()
    return HttpResponseRedirect(reverse("resto:show_restaurant"))

# def show_restaurant_detail(request, id):
#     restaurant = Restaurant.objects.get(pk = id)
#     data_menu_items = Food.objects.filter(food_resto = restaurant)
#     # data_hours_items = OpeningHours.objects.filter(hours_restaurant = restaurant)
#     # data_hours_cleaned = [str(hour) for hour in data_hours_items]
#     context = {
#         'restaurant' : restaurant,
#         'foods': data_menu_items,
#         # 'hours': data_hours_cleaned,
#         'id': id,
#     }
#     return render(request, "resto_detail.html", context)

# def create_food(request, id):
#     form = FoodForm()
#     if request.method == "POST":
#         form = FoodForm(request.POST ,request.FILES)
#         if form.is_valid():
#             # Use passed argument from create_restaurant to set restaurant instance of
#             # Food object
#             resto = Restaurant.objects.get(pk=id)
#             food_form = form.save(commit=False)
#             food_form.food_resto = resto
#             food_form.save()
#             response = HttpResponseRedirect(reverse('resto:show_restaurant_detail', kwargs={'id':id}))
#             return response
#     else:
#         form = FoodForm()
#     return render(request, 'resto_menu.html', {'form':form})

# def delete_food(request, food_id, resto_id):
#     object = get_object_or_404(Food, pk = food_id)
#     object.delete()
#     return HttpResponseRedirect(reverse("resto:show_restaurant_detail", kwargs={'id':resto_id}))

# def show_hours_json(request):
#     resto_id = call_resto_id()
#     data = OpeningHours.objects.filter(hours_restaurant = Restaurant.objects.get(pk=resto_id))
#     return HttpResponse(serializers.serialize("json", data), \
#         content_type="application/json")

# @csrf_exempt
# def create_schedule(request):
#     form = OpeningHoursForm()
#     resto_id = call_resto_id()
#     if request.method == "POST":
#         form = OpeningHoursForm(request.POST)
#         if form.is_valid():
#             # Use passed argument from create_restaurant to set restaurant instance of
#             # OpeningHours object
#             resto = Restaurant.objects.get(pk=resto_id)
#             hours_form = form.save(commit=False)
#             hours_form.hours_restaurant = resto
#             hours_form.save()
#             data = OpeningHours.objects.filter(hours_restaurant = resto)
#             response = HttpResponse(serializers.serialize("json", data), \
#                 content_type="application/json")
#             response.set_cookie('resto_id', resto_id)
#             return response
#     return render(request, 'resto_schedule.html', {'form':form, 'id': resto_id})

