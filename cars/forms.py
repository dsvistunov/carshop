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


class SearchForm(forms.Form):
    MARC_CHOICES = (
        ('VW', 'VW'),
        ('C', 'Golf'),
        ('E', 'Tiguan'),
        ('B', 'Transporter2'),
        ('M', 'Transporter3'),
    )
    MODEL_CHOICES = (
        ('Transporter', 'Transporter'),
    )
    YEAR_CHOICES = (
        ('2010', '2010'),
        ('2016', '2016'),
    )
    marc = forms.ChoiceField(choices=MARC_CHOICES)
    model = forms.ChoiceField(choices=MODEL_CHOICES)
    year = forms.ChoiceField(choices=YEAR_CHOICES)


