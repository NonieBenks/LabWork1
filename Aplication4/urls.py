from . import views, urls
from django.urls import re_path, path, include
from django.conf.urls import url

urlpatterns = [
    url(r'^render-html/$', views.html),
    url(r'^redirect/redirected/$', views.redirected),
    url(r'^redirect/$', views.Redirect),
    url(r'^$', views.show),
    url(r'^render-template/$', views.render_html),
    url(r'^render-template/form-handler/$', views.postmethod)
]