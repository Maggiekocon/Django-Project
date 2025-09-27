from django.shortcuts import render
from .models import Car

def car_list(request):
    car=Car.objects.all()
    return render(request, 'car_list.html', {'car': car})
