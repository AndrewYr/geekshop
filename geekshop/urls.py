"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from mainApp import views as mainApp
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', mainApp.index, name='mainApp'),
    # url(r'^products/$', mainApp.products, name='products'),
    url(r'^products/', include(('mainApp.urls', 'mainApp'), namespace='products')),
    url(r'^fishnet_chair/$', mainApp.fishnet_chair, name='fishnet_chair'),
    url(r'^history/$', mainApp.history, name='history'),
    url(r'^showroom/$', mainApp.showroom, name='showroom'),
    url(r'^contact/$', mainApp.contacts, name='contact'),
    url(r'^auth/', include(('authapp.urls', 'authapp'), namespace='auth')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)