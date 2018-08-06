from django.conf.urls import url
from . import views
from .views import IndexView, CarDetail, AddCarView, ContactView


urlpatterns = [
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^car/add/$', AddCarView.as_view(), name='addcar'),
    url(r'^car/(?P<slug>[\w-]+)/$', CarDetail.as_view(), name='carditail'),
    url(r'^$', IndexView.as_view(), name='carlist'),
]