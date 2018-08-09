from django.conf.urls import url
from . import views
from .views import IndexView, CarDetail, AddCarView, ContactView, AllCarsView


urlpatterns = [
	url(r'^all/$', AllCarsView.as_view(), name='all_cars'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^car/add/$', AddCarView.as_view(), name='addcar'),
    url(r'^car/(?P<slug>[\w-]+)/$', CarDetail.as_view(), name='carditail'),
    url(r'^$', IndexView.as_view(), name='carlist'),
]