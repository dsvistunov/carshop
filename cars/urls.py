from django.conf.urls import url
from . import views
from .views import IndexView, CarDetail

app_name = 'carshop'
urlpatterns = [
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^car/add/$', views.addcar, name='addcar'),
    url(r'^car/(?P<slug>[\w-]+)/$', CarDetail.as_view(), name='carditail'),
    url(r'^$', IndexView.as_view(), name='carlist'),
]