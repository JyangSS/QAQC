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

    path('unitlist/', views.unit_list, name='unit_list'),
    path('projectlist/', views.project_list, name='project_list'),
    path('phaselist/', views.phase_list, name='phase_list'),
    path('unitlist/<int:id>', views.edit_unit, name='edit_unit'),
    path('projectlist/<int:id>', views.edit_project, name='edit_project'),
    path('phaselist/<int:id>', views.edit_phase, name='edit_phase'),
]
