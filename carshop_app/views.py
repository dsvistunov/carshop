from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.template.context_processors import csrf
from django.contrib import auth
from .models import Car
from .forms import AddCarForm

# Create your views here.

def carlist(request):
    return render_to_response('carlist.html', {'cars': Car.objects.order_by('-car_public'), 'username': auth.get_user(request).username})

def carditail(request, car_id):
    args = {}
    args['car'] = get_object_or_404(Car, pk=car_id)
    args['username'] = auth.get_user(request).username
    return render_to_response('carditail.html', args)

def addcar(request):
    if request.POST:
        car = AddCarForm(request.POST)
        if car.is_valid():
            car.save()
        response = redirect('/')
    else:
        args = {}
        args.update(csrf(request))
        args['form'] = AddCarForm
        response = render_to_response('addcarform.html', args)
    return response

