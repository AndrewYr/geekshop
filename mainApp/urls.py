from django.conf.urls import url
from .views import products

urlpatterns = [
    url(r'^$', products, name='index'),
    url(r'^(?P<pk>\d+)/$', products, name='products'),
]
