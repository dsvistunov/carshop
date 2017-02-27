from django.conf.urls import url
from . import views

app_name = 'carshop'
urlpatterns = [
    url(r'^car/add/$', views.addcar, name='addcar'),
    url(r'^car/(?P<car_id>[0-9]+)/$', views.carditail, name='carditail'),
    url(r'^$', views.carlist, name='carlist'),
]