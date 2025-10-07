from django.shortcuts import render
from django.shortcuts import render
from cars.models import Car

def cars_view(request):
    cars = Car.objects.all().order_by('brand')
    search = request.GET.get('search')

    if search:
        cars = Car.objects.filter(model__contains=search)
    
    return render(
        request,
        'cars.html',
        {'cars': cars}
    )
