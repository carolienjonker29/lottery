from django.conf.urls import url, patterns
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^registration/$', views.registration, name='registration'),
     url(r'^sample/$', views.sample, name='sample'),
     url(r'^confirmation/$', views.confirmation, name='confirmation'),
]
