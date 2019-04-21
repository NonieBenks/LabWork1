from . import views, urls
from django.urls import re_path, path, include
from django.conf.urls import url

new_patterns = [
    url(r'^comments/(?P<number>[\d]+)/', views.number_comment ),
    url(r'^comments/$', views.first_comment)

]

urlpatterns = {
    url(r'^new_patterns/', include(new_patterns)),
    re_path(r'^review/page(?P<number>[\d]+)/(?P<ACTION>[\w]+)/$', views.page_action),
    re_path(r'^review/page(?P<number>[\d]+)/$', views.page_number),
    re_path(r'^$', views.show),

}
