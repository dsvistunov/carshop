from django.utils import timezone
from django.db import models

# Create your models here.

class Car(models.Model):

    class Meta:
        db_table = 'cars'

    car_mark = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    car_year = models.CharField(max_length=4)
    car_description = models.TextField(max_length=10000)
    car_public = models.DateTimeField(auto_now_add=True)
    car_image = models.ImageField(null=True, blank=True, upload_to='images/', verbose_name='Image',)
