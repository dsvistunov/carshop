from django.forms import ModelForm
from .models import Car

class AddCarForm(ModelForm):
    class Meta:
        model = Car
        fields = ['car_mark', 'car_model', 'car_year', 'car_description', 'car_image']

