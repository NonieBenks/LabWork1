from django.urls import path, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
   url('menu/wrapper.html', views.wrapper),
   url('menu/main.html',views.main),
   url('menu/condition.html', views.condition),
   url('menu/content.html', views.content),
   url('menu/', views.menu),
   url('condition/', views.condition),
   path('user/', views.index),
   url(r'^$', views.show)
]