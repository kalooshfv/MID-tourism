from django.shortcuts import render
from django.http.response import JsonResponse
from about.models import UserSuggestion
from django.http import HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def show_about_section(request):
    return render(
        request, 
        'about.html',
        {}
    )

@csrf_exempt
def post_suggestion(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(full_name)
        if full_name is not None and phone_number is not None and email is not None:
            UserSuggestion.objects.create(
                full_name=full_name,
                phone_number=phone_number,
                email=email,
                message=message
            )

            return JsonResponse({
                'name': full_name,
                'status': 'success',
                'error': False
            })

    return HttpResponseBadRequest('Bad Request')