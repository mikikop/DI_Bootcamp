from django.shortcuts import render
from .models import Animal, Family


def all_animals(request):
    data = Animal.objects.all()
    
    context = {
        'animals': data,
    }
    return render (request, 'animals.html', context)

def all_families(request):
    data = Family.objects.all()
    
    context = {
        'families': data,
    }
    return render (request, 'families.html', context)

def animal(request, id):

    data = Animal.objects.get(id=id)
    
    context = {
        'animal': data,
    }
    return render (request, 'animal.html', context)


def family(request, id):
    data = Animal.objects.filter(family__id=id)
    data_name = Family.objects.get(id=id)

    context = {
        'animals': data,
        'family_name': data_name,
    }
    return render (request, 'family.html', context)