from django.db import models
from django.utils import timezone

class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=40)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=20)

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f" {self.first_name} {self.last_name}"


class Vehicle(models.Model):
    vehicle_type = models.ForeignKey('VehicleType', on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    size = models.ForeignKey('VehicleSize', on_delete=models.SET_NULL, null=True)

    def __repr__(self):
        return f"{self.vehicle_type}"

    def __str__(self):
        return f"{self.vehicle_type} - {self.size}"
    
    def daily_rate(self):
        rental_rate = RentalRate.objects.filter(vehicle_type=self.vehicle_type, vehicle_size=self.size).first() 
        if rental_rate:
            return rental_rate.daily_rate 
        else:
            return 'N/A'

class VehicleType(models.Model):
    name = models.CharField(max_length=20)
    
    def __repr__(self):
        return f"{self.name}"

    def __str__(self):
        return f"{self.name}"

class VehicleSize(models.Model):
    name = models.CharField(max_length=20)
    
    def __repr__(self):
        return f"{self.name}"

    def __str__(self):
        return f"{self.name}"

class Rental(models.Model):
    rental_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True)

    def __repr__(self):
        return f"{self.rental_date} {self.customer}"

    def __str__(self):
        return f"Rental: ID: {self.id}: {self.rental_date} {self.customer}"
    
    def is_active(self):
        if self.return_date > timezone.now():
            return True
        else:
            return False
    
    def period(self):
        return (self.return_date - self.rental_date).days
    
    def bill(self):
        days = self.return_date - self.rental_date
        rental_rate = RentalRate.objects.filter(vehicle_type=self.vehicle.vehicle_type, vehicle_size=self.vehicle.size).first()
        cost = days.days * rental_rate.daily_rate
        return round(cost,2)

class RentalRate(models.Model):
    daily_rate = models.FloatField(default=0)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.SET_NULL, null=True)
    vehicle_size = models.ForeignKey(VehicleSize, on_delete=models.SET_NULL, null=True)
    

    def __repr__(self):
        return f"{self.daily_rate}"

    def __str__(self):
        return f"{self.vehicle_type.name} - {self.vehicle_size.name}: {self.daily_rate}"
