from django.conf.urls import url, include
from . import views
from django.urls import path


urlpatterns = [

    path('unitlist/', views.unit_list, name='unit_list'),
    path('projectlist/', views.project_list, name='project_list'),
    path('phaselist/', views.phase_list, name='phase_list'),
    path('unitlist/<int:id>', views.unit_edit, name='unit_edit'),
    path('projectlist/<int:id>', views.project_edit, name='project_edit'),
    path('phaselist/<int:id>', views.phase_edit, name='phase_edit'),
    path('projectmainlist/<int:id>', views.project_main_list, name='project_main_list'),

]
