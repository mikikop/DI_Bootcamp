from django.urls import path
from . import views

urlpatterns = [
    path('animals', views.all_animals),
    path('families', views.all_families),
    path('animal/<int:id>', views.animal),
    path('family/<int:id>', views.family),
]