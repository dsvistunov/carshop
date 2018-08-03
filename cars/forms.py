import itertools
from django import forms
from django.utils.text import slugify
from .models import Car

class AddCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['car_mark', 'car_model', 'car_year', 'car_description', 'car_image']

    def save(self, commit=True):
        instance = super(AddCarForm, self).save(commit=False)

        max_length = Car._meta.get_field('slug').max_length
        value = instance.car_mark + ' ' + instance.car_model
        instance.slug = orig = slugify(value)[:max_length]

        for x in itertools.count(1):
            if Car.objects.filter(slug=instance.slug).exists():
                # Truncate the original slug dynamically. Minus 1 for the hyphen.
                instance.slug = "%s-%d" % (orig[:max_length - len(str(x)) - 1], x)
            else:
                break
        instance.save()

        return instance


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


