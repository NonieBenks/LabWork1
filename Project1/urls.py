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
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url


urlpatterns = [
    path("admin/", admin.site.urls),
    path('applicationmodels/', include('applicationmodels.urls')),
    path('aplication3_1/', include('aplication3_1.urls')),
    path('Aplication4/', include('Aplication4.urls')),
    path('Aplication3/', include('Aplication3.urls')),
    path('Aplication2/', include('Aplication2.urls')),
    path('Aplication1/', include('Aplication1.urls'))


]
