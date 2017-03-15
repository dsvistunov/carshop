from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.template.context_processors import csrf
from django.contrib import auth
from django.core.mail import EmailMessage, send_mail, EmailMultiAlternatives
from django.template import Context
from django.template.loader import get_template
from .models import Car
from .forms import AddCarForm, ContactForm

# Create your views here.

def carlist(request):
    return render_to_response('carlist.html', {'cars': Car.objects.order_by('-car_public'), 'username': auth.get_user(request).username})

def carditail(request, car_id):
    args = {}
    args['car'] = get_object_or_404(Car, pk=car_id)
    args['username'] = auth.get_user(request).username
    return render_to_response('carditail.html', args)

def addcar(request):
    if request.POST:
        car = AddCarForm(request.POST, request.FILES)
        if car.is_valid():
            car.save()
        response = redirect('/')
    else:
        args = {}
        args.update(csrf(request))
        args['form'] = AddCarForm
        args['username'] = auth.get_user(request).username
        response = render_to_response('addcarform.html', args)
    return response

def contact(request):
    if request.POST:
        form = ContactForm(data=request.POST)

        if form.is_valid():

            contact_name = request.POST.get('contact_name', '')
            contact_email =request.POST.get('contact_email', '')
            subject = request.POST.get('contact_subject', '')
            form_content = request.POST.get('content', '')

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
            response = redirect('/')
        else:
            response = redirect('/contact')
    else:
        args = {}
        args.update(csrf(request))
        args['form'] = ContactForm
        response = render_to_response('contactform.html', args)

    return response
