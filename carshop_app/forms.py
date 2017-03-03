from django import forms
from .models import Car

class AddCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['car_mark', 'car_model', 'car_year', 'car_description', 'car_image']

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, label='Name')
    contact_email = forms.EmailField(required=True, label='Email')
    contact_subject = forms.CharField(required=True, label='Subject')
    content = forms.CharField(required=True, widget=forms.Textarea, label='Text')

