import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from tourguide.models import Task
from tourguide.forms import TaskForms
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


@login_required(login_url="/tourguide/login/")
def show_schedule(request):
    data_schedule_item = Task.objects.all()
    current_user = request.user.username
    context = {
        'list_item': data_schedule_item,
        'user':current_user,
    }
    return render(request, "tourguide.html",context)

def my_form(request):
  form = TaskForms()
  if request.method == "POST":
    form = TaskForms(request.POST)
    if form.is_valid():
      last_user = form.save()
      last_user.user = request.user
      last_user.save()
      return redirect('tourguide:show_schedule')
  return render(request, 'cv-form.html', {'form': form})

def show_json(request):
    task = Task.objects.all()
    return HttpResponse(
        serializers.serialize("json", task), content_type="application/json"
    )

def add_schedule(request):
    if request.method == "POST":
        date = request.POST.get("date")
        destination = request.POST.get("destination")
        task = Task.objects.create(
            user=request.user,
            date=date,
            destination=destination,
        )
        task.save()
        return JsonResponse(
            {
                "pk": task.id,
                "fields": {
                    "user":task.user,
                    "date": task.date,
                    "destination": task.destination,
                },
            },
            status=200,
        )