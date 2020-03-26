from django.conf.urls import url, include
from . import views
from django.urls import path


urlpatterns = [

    path('projectmainlist/', views.project_main_list_empty, name='project_main_list_empty'),
    path('projectmainlist/unitlist/<int:id>/', views.unit_main_list, name='unit_main_list'),
    path('projectmainlist/<int:id>/', views.project_main_list, name='project_main_list'),
   # path('projectmainlist/project/delete/<int:id>', views.project_delete, name='project_delete'),
   # path('phaselist/delete/<int:id>', views.phase_delete, name='phase_delete'),
    path('projectmainlist/phaselist/edit/<int:id>', views.phase_edit, name='phase_edit'),
]
