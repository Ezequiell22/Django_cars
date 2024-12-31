from django.shortcuts import render
from cars.models import Car
from cars.forms import Carform

def cars_view(request):
    search = request.GET.get('search')
    
    if not search:
      search = ''

    cars = Car.objects.filter(model__icontains=search).order_by('model')
      
    return render(
        request,
        'cars.html',
        {"cars" : cars }   
    )

def new_car_view(request):
   new_car_form = Carform()
   return render(request, 'new_car.html', {'new_car_form' :  new_car_form })