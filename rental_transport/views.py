from http.client import HTTPResponse
from django.shortcuts import render
from rental_transport.models import *
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core import serializers
from django.http import HttpResponse, JsonResponse

# Create your views here.
def show_transportlist(request):
    transport_item = TransportList.objects.all()
    context = {
    'user': request.user,
    'list_item': transport_item 
    }
    return render(request, "transportlist.html", context)


def create_transport(request):
    if request.method == "POST":
        company_name = request.POST.get("company_name")
        transport_name = request.POST.get("transport_name")
        transport_price = request.POST.get("transport_price")
        description = request.POST.get("description")
        transportss = TransportList.objects.create(
            company_name=company_name,
            transport_name=transport_name,
            transport_price=transport_price,
            description=description,
        )
        transportss.save()
        print(transportss)
        return JsonResponse(
            {
                "pk": transportss.id,
                "fields": {
                    "company_name":transportss.company_name,
                    "transport_name":transportss.transport_name,
                    "transport_price": transportss.transport_price,
                    "description": transportss.description,
                },
            },
            status=200,
        )

def show_json(request):
    data = TransportList.objects.all()
    return HttpResponse(serializers.serialize("json",data), content_type="application/json")

def remove_transport(request, id):
    itemtodelete = TransportList.objects.get(pk=id)
    itemtodelete.delete()
    return redirect('rental_transport:show_transportlist')
