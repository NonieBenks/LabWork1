"""Project1 URL Configuration

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
from django.urls import path
from . import views
from django.urls import re_path

urlpatterns = [

    re_path(r'^folder/$', views.folder),
    re_path(r'^folder/product/$', views.show),
    re_path(r'^folder/product(?P<number>[\d]+)/$', views.productNum),
    re_path(r'^folder/product/(?P<year>[\d]{3,4})/(?P<month>[\d]{2})/(?P<day>[\d]{2})/$', views.day),
    re_path(r'^folder/product/(?P<year>[\d]{3,4})/(?P<month>[\d]{2})/$', views.month),
    re_path(r'^folder/product/([\d]{3,4})/$', views.number),
    re_path(r'^(?P<argument>[\w]*)/$', views.argument),
    re_path(r'^$', views.show),

]
