from django.shortcuts import render
from django.http import HttpResponse
import json

with open ("animal.json") as f:
    data = json.load(f)
    
def family(request,fam_id):
    fam_list = data['families']
    context = {}
    for fam in fam_list:
        if fam_id == fam['id']:
            context['name'] = fam['name']
    
    context['animals'] = []
    for fam_animal in data['animals']:
        if fam_animal['family'] == fam_id:
            context['animals'].append(fam_animal)
    
    html_page = render(request , 'family.html', context)
    return html_page

def animal(request, anim_id):

    animal_list = data['animals']
    context = {}
    
    context['animals'] = []
    for my_animal in animal_list:
        if my_animal['id'] == anim_id:
            context['animals'].append(my_animal)

    html_page = render(request , 'animal.html', context)
    return html_page
    
