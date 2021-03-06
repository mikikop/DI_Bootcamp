from django.urls import path
from . import views

urlpatterns = [
    path('rentals/', views.rental, name='rentals'),
    path('rental/<int:id>', views.rental, name='rental'),
    path('rental/add', views.rental_add, name='rental_add'),
    path('customer/', views.customer, name='customers'),
    path('customer/<int:id>', views.customer, name='customer'),
    path('customer/add', views.customer_add, name='customer_add'),
    path('vehicle/', views.vehicle, name='vehicles'),
    path('vehicle/<int:id>', views.vehicle, name='vehicle'),
    path('vehicle/add', views.vehicle_add, name='vehicle_add'),
]