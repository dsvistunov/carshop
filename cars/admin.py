from django.contrib import admin
from .models import Car
from .forms import AddCarForm

class CarAdmin(admin.ModelAdmin):
    # list_display = ('car_mark', 'car_model', 'car_year',)
    # prepopulated_fields = {'car_slug': ('car_mark', 'car_model', 'car_year')}
    form = AddCarForm

admin.site.register(Car, CarAdmin)

# Register your models here.
