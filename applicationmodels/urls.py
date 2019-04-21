from . import views, urls
from django.urls import re_path, path, include
from django.conf.urls import url


urlpatterns = [
     url(r'^/$', views.startpage)
]