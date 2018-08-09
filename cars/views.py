from django.views.generic import ListView, DetailView, CreateView, FormView
from .models import Car
from .forms import AddCarForm, ContactForm


class IndexView(ListView):
    context_object_name = 'cars'
    template_name = 'index.html'
    queryset = Car.objects.order_by('-car_public')[:3]


class AllCarsView(ListView):
    context_object_name = 'cars'
    template_name = 'allcars.html'
    paginate_by = 5
    queryset = Car.objects.all()        


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
