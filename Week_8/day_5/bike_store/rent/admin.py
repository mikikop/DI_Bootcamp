from django.contrib import admin
from.models import *

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicle_type', 'created_date', 'size')
admin.site.register(Vehicle, VehicleAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email','phone_number','address','city','country')
admin.site.register(Customer, CustomerAdmin)

class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(VehicleType, VehicleTypeAdmin)

class VehicleSizeAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(VehicleSize, VehicleSizeAdmin)

class RentalAdmin(admin.ModelAdmin):
    list_display = ('rental_date', 'return_date', 'customer','vehicle')
admin.site.register(Rental, RentalAdmin)

class RentalRateAdmin(admin.ModelAdmin):
    list_display = ('daily_rate', 'vehicle_type', 'vehicle_size')
admin.site.register(RentalRate, RentalRateAdmin)
