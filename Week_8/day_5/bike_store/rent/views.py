from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.http import Http404

def rental(request, id=None):
    if id == None:
        return render(request, 'rentals.html', {'Rentals': Rental.objects.all()})
    else:
        return render(request, 'rental.html', {'Rental': Rental.objects.get(pk=id)})

def rental_add(request):
    myform = RentalForm(request.POST)

    if myform.is_valid():
        return_date = myform.cleaned_data['return_date']
        customer=myform.cleaned_data['customer']
        vehicle = myform.cleaned_data['vehicle']
        
        r = Rental(return_date=return_date, customer=customer, vehicle=vehicle)
        r.save()

        return redirect('rental_add')

    else:
        return render(request, 'rental_add.html', {'myform':myform})

def customer(request, id=None):
    if id == None:
        return render(request, 'customer.html', {'Customers': Customer.objects.all()})
    else:
        return render(request, 'customer.html', {'Customer': Customer.objects.get(pk=id)})

def customer_add(request):
    myform = CustomerForm(request.POST)

    if myform.is_valid():
        first_name=myform.cleaned_data['first_name']
        last_name=myform.cleaned_data['last_name']
        email = myform.cleaned_data['email']
        phone_number = myform.cleaned_data['phone_number']
        city = myform.cleaned_data['city']
        country = myform.cleaned_data['country']
        
        c = Customer(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, city=city, country=country)
        c.save()

        return redirect('customer_add')

    else:
        return render(request, 'customer_add.html', {'myform':myform})


def vehicle(request, id=None):
    if id == None:
        return render(request, 'vehicle.html', {'Vehicles': Vehicle.objects.all()})
    else:
        return render(request, 'vehicle.html', {'Vehicle': Vehicle.objects.get(pk=id)})

def vehicle_add(request):
    myform = VehiculeForm(request.POST)

    if myform.is_valid():
        vehicle_type=myform.cleaned_data['first_name']
        created_date=myform.cleaned_data['last_name']
        size = myform.cleaned_data['email']
        
        v = Vehicle(vehicle_type=vehicle_type, created_date=created_date, size=size)
        v.save()

        return redirect('vehicle_add')

    else:
        return render(request, 'vehicle_add.html', {'myform':myform})
    