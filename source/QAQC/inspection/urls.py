from django.conf.urls import url, include
from .views import *
from . import views
from django.urls import path


urlpatterns = [
    url(r'^elements/$', element_list, name='element_list'),
    url(r'^elements/create$', element_create, name='element_create'),
    url(r'^elements/(?P<id>\d+)/update$', element_update, name='element_update'),
    url(r'^elements/(?P<id>\d+)/delete$', element_delete, name='element_delete'),
    url(r'^groups/create$', group_create, name='group_create'),
    url(r'^groups/(?P<id>\d+)/update$', group_update, name='group_update'),
    url(r'^groups/(?P<id>\d+)/delete$', group_delete, name='group_delete'),


]
