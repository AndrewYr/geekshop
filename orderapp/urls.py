from django.conf.urls import url
import orderapp.views as views

# app_name = 'authapp'

urlpatterns = [
    # url(r'^order/$', views.order, name='login'),
    url(r'^$', views.order, name='order'),
    url(r'^add/$', views.order_add, name='add'),
    # url(r'^add/(?P<pk>\d+)/$', views.order_add, name='add'),
    ]