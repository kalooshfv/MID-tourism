from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.core import serializers


# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully created!')
            return redirect('homepage:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # login first
            return HttpResponseRedirect(reverse("homepage:homepage")) # create response
        else:
            messages.info(request, 'Wrong Username or Password!')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('homepage:homepage'))
    return response

def show_user_json(request):
    data = User.objects.all()
    return HttpResponse(serializers.serialize("json", data), \
        content_type="application/json")

# Flutter login
@csrf_exempt
def login_flutter(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                return JsonResponse({
                "status": True,
                "message": "Successfully Logged In!"
                # Insert any extra data if you want to pass data to Flutter
                }, status=200)
            else:
                return JsonResponse({
                "status": False,
                "message": "Failed to Login, Account Disabled."
                }, status=401)

        else:
            return JsonResponse({
            "status": False,
            "message": "Failed to Login, check your email/password."
            }, status=401)
    else:
        return render(request, 'login.html')

@csrf_exempt
def register_flutter(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(201)

@csrf_exempt
def logout_flutter(request):
    logout(request)
    return HttpResponse(status=200)

