from django.conf.urls import url, include
from .views import *
from . import views
from django.urls import path

path('unitlist/', views.unit_list, name='unit_list'),
path('projectlist/', views.project_list, name='project_list'),
path('phaselist/', views.phase_list, name='phase_list'),
path('unitlist/<int:id>', views.edit_unit, name='edit_unit'),
path('projectlist/<int:id>', views.edit_project, name='edit_project'),
path('phaselist/<int:id>', views.edit_phase, name='edit_phase'),