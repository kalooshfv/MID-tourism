from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from tourguide.models import Task
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def show_schedule(request):
    data_schedule_item = Task.objects.all()
    context = {
        'list_item': data_schedule_item,
    }
    return render(request, "tourguide.html",context)

def show_json(request):
    task = Task.objects.all()
    return HttpResponse(
        serializers.serialize("json", task), content_type="application/json"
    )

@login_required(login_url="login/")
def update_booked(request, id):
    task = Task.objects.get(id=id)
    task.is_booked = not task.is_booked
    task.save(update_fields=["is_booked"])
    return HttpResponseRedirect(reverse("tourguide:show_schedule"))

@login_required(login_url="login/")
def add_schedule(request):
    if request.method == "POST":
        date = request.POST.get("date")
        month = date[0:2]
        day = date[3:5]
        year = date[6:]
        destination = request.POST.get("destination")
        company = request.POST.get("company")
        task = Task.objects.create(
            company=company,
            date = year + '-' + month + '-' + day,
            destination=destination,
        )
        task.save()
        return JsonResponse(
            {
                "pk": task.id,
                "fields": {
                    "company":task.company,
                    "date": task.date,
                    "destination": task.destination,
                },
            },
            status=200,
        )

@csrf_exempt
def add_schedule_flutter(request):
    if request.method == "POST":
        date = request.POST.get("date")
        destination = request.POST.get("destination")
        company = request.POST.get("company")
        task = Task.objects.create(
            company=company,
            date = date,
            destination=destination,
        )
        task.save()
        return HttpResponse(status=201)

@csrf_exempt
def update_booked_flutter(request, id):
    task = Task.objects.get(id=id)
    task.is_booked = not task.is_booked
    task.save(update_fields=["is_booked"])
    return HttpResponse(200)