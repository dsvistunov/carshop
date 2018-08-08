import itertools
from django import forms
from django.forms import Form, ModelForm, TextInput, Textarea
from django.core.mail import send_mail
from django.utils.text import slugify
from django.template import Context
from django.template.loader import get_template
from .models import Car

class AddCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['car_mark', 'car_model', 'car_year', 'car_description', 'car_image']
        widgets = {
            'car_mark': TextInput(attrs={
                    'class': 'form-control'
                }),
            'car_model': TextInput(attrs={
                    'class': 'form-control'
                }),
            'car_year': TextInput(attrs={
                    'class': 'form-control'
                }),
            'car_description': Textarea(attrs={
                    'class': 'form-control',
                    'rows': '5',
                })
        }

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

    def send_email(self):
        contact_name = self.cleaned_data['contact_name']
        contact_email = self.cleaned_data['contact_email']
        subject = self.cleaned_data['contact_subject']
        form_content = self.cleaned_data['content']

        template = get_template('contact_template.html')

        context = Context({
            'contact_name': contact_name,
            'contact_email': contact_email,
            'subject': subject,
            'form_content': form_content
        })

        content = template.render(context)

        send_mail(
            context['subject'],
            content,
            contact_email,
            ['d.svistunov1991@gmail.com'],
            fail_silently=False,
            html_message=content
        )

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


