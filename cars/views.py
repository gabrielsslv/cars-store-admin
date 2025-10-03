from django.shortcuts import render
from django.shortcuts import render

def cars_view(request):
    return render(request, 'cars.html')
