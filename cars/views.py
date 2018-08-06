from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.template.context_processors import csrf
from django.contrib import auth
from django.core.mail import EmailMessage, send_mail, EmailMultiAlternatives
from django.template import Context
from django.template.loader import get_template
from django.views.generic import ListView, DetailView, CreateView, FormView
from .models import Car
from .forms import AddCarForm, ContactForm, SearchForm


class IndexView(ListView):
    context_object_name = 'cars'
    template_name = 'carlist.html'
    queryset = Car.objects.order_by('-car_public')[:3]


class CarDetail(DetailView):
    model = Car
    template_name = 'carditail.html'


class AddCarView(CreateView):
    template_name = 'addcarform.html'
    form_class = AddCarForm


class ContactView(FormView):
    template_name = 'contactform.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super(ContactView, self).form_valid(form)
