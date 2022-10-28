from django.shortcuts import render
from rental_transport.models import *
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def show_transportlist(request):
    transport_item = TransportList.objects.all()
    context = {
    'list_item': transport_item 
    }
    return render(request, "transportlist.html", context)

def create_transport(request):
    if request.method == "POST":
        transport_name = request.POST.get("Name")
        transport_price = request.POST.get("price")
        description = request.POST.get("description")
        TransportList.objects.create(
            transport_name=transport_name,
            transport_price=transport_price,
            description=description,
        )
        return HttpResponseRedirect(reverse("todolist:show_todolist"))
    return render(request, "create_task.html")