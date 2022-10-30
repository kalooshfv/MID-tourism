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



def show_schedule(request):
    data_schedule_item = Task.objects.all()
    current_user = request.user
    context = {
        'list_item': data_schedule_item,
        'user':current_user,
    }
    return render(request, "tourguide.html",context)

def show_json(request):
    task = Task.objects.all()
    return HttpResponse(
        serializers.serialize("json", task), content_type="application/json"
    )

# def my_form(request):
#   form = TaskForms()
#   if request.method == "POST":
#     form = TaskForms(request.POST)
#     if form.is_valid():
#       last_user = form.save()
#       last_user.user = request.user
#       last_user.save()
#       return redirect('tourguide:show_schedule')
#   return render(request, 'cv-form.html', {'form': form})

# # @login_required(login_url="/tourguide/login/")
# def register(request):
#     form = UserCreationForm()

#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Account successfully created!')
#             return redirect('tourguide:login')

#     context = {'form':form}
#     return render(request, 'register.html', context)

# def login_user(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user) # login first
#             response = HttpResponseRedirect(reverse("tourguide:show_schedule")) # create response
#             response.set_cookie('last_login', str(datetime.datetime.now())) # create last_login cookie and add it to response
#             return response
#         else:
#             messages.info(request, 'Wrong Username or Password!')
#     context = {}
#     return render(request, 'login.html', context)


# def logout_user(request):
#     logout(request)
#     response = HttpResponseRedirect(reverse('tourguide:login'))
#     response.delete_cookie('last_login')
#     return redirect('tourguide:login')

@login_required(login_url="/login/")
def update_booked(request, id):
    task = Task.objects.get(user=request.user, id=id)
    task.is_booked = not task.is_booked
    task.save(update_fields=["is_booked"])
    return HttpResponseRedirect(reverse("tourguide:show_schedule"))

def add_schedule(request):
    if request.method == "POST":
        date = request.POST.get("date")
        month = date[0:2]
        day = date[3:5]
        year = date[6:]
        destination = request.POST.get("destination")
        company = request.POST.get("company")
        task = Task.objects.create(
            user=request.user,
            company=company,
            date = year + '-' + month + '-' + day,
            destination=destination,
        )
        task.save()
        print(task.user)
        return JsonResponse(
            {
                "pk": task.id,
                "fields": {
                    "user":task.user.username,
                    "company":task.company,
                    "date": task.date,
                    "destination": task.destination,
                },
            },
            status=200,
        )