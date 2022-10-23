import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from todolist.models import Task
from todolist.forms import TaskForms
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


@login_required(login_url="/touguide/login/")
def show_schedule(request):
    data_schedule_item = Task.objects.all()
    current_user = request.user.username
    context = {
        'list_item': data_schedule_item,
        'user':current_user,
    }
    return render(request, "tourguide.html",context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully created!')
            return redirect('tourguide:login')

    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # login first
            response = HttpResponseRedirect(reverse("tourguide:show_todolist")) # create response
            response.set_cookie('last_login', str(datetime.datetime.now())) # create last_login cookie and add it to response
            return response
        else:
            messages.info(request, 'Wrong Username or Password!')
    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('tourguide:login'))
    response.delete_cookie('last_login')
    return redirect('tourguide:login')


def add_task(request):
    if request.method == "POST":
        date = request.POST.get("date")
        destination = request.POST.get("destination")
        task = Task.objects.create(
            user=request.user,
            date=date,
            destination=destination,
        )
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