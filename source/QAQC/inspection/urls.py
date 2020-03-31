from django.conf.urls import url, include
from .views import *
from . import views
from django.urls import path

urlpatterns = [
    # elements
    url(r'^elements/$', element_list, name='element_list'),
    url(r'^elements/create$', element_create, name='element_create'),
    url(r'^elements/(?P<id>\d+)/update$', element_update, name='element_update'),
    url(r'^elements/(?P<id>\d+)/delete$', element_delete, name='element_delete'),
    # groups
    url(r'^elements/(?P<id>\d+)/groups$', group_list, name='group_list'),
    url(r'^groups/create$', group_create, name='group_create'),
    #
    url(r'^forms/type', form_type, name='form_type'),
    url(r'^forms/create$', form_type_create, name='form_type_create'),
    url(r'^forms/(?P<id>\d+)/update$', form_type_update, name='form_type_update'),
    url(r'^forms/(?P<id>\d+)/delete$', form_type_delete, name='form_type_delete'),
    url(r'^forms/(?P<id>\d+)', forms, name='forms'),
    # number_series
    url(r'^number_series/$', number_series_list, name='number_series_list'),
    url(r'^number_series/create$', number_series_create, name='number_series_create'),
    url(r'^number_series/(?P<id>\d+)/update$', number_series_update, name='number_series_update'),
    url(r'^number_series/(?P<id>\d+)/delete$', number_series_delete, name='number_series_delete'),
]
