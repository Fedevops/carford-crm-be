from django.contrib import admin
from .models import (
    Car, 
    Customer, 
)

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'email',
        'phone', 
    )
    search_fields = ('name', 'email')
    list_filter = ('email',)


class CarAdmin(admin.ModelAdmin):
    list_display = (
        'model',
        'year', 
        'price',
        'type',
        'owner',
    )
    search_fields = (
        'model', 
        'year',
    )
    list_filter = ('model',)


admin.site.register(Car, CarAdmin)
admin.site.register(Customer, CustomerAdmin)
