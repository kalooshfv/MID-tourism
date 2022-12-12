from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User


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
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            create = User.objects.create_user(username = username, password = password)
            create.save()
            return HttpResponse(201)

@csrf_exempt
def logout_flutter(request):
    logout(request)
    return HttpResponse(status=200)

