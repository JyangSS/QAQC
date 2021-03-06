from django.conf.urls import url, include
from . import views
from django.urls import path

urlpatterns = [
    # data manage
    path('companylist/', views.company_list, name='company_list'),
    path('companylist/create', views.company_create, name='company_create'),
    path('companylist/edit/<int:id>/', views.company_edit, name='company_edit'),
    path('companylist/delete/<int:id>/', views.company_delete, name='company_delete'),

    path('projectlist/<int:id>/', views.project_list, name='project_list'),
    path('projectlist/create/<int:id>/', views.project_create, name='project_create'),
    path('projectlist/edit/<int:id>/', views.project_edit, name='project_edit'),
    path('projectlist/delete/<int:id>/', views.project_delete, name='project_delete'),

    path('phaselist/<int:id>/', views.phase_list, name='phase_list'),
    path('phaselist/create/<int:id>/', views.phase_create, name='phase_create'),
    path('phaselist/edit/<int:id>/', views.phase_edit, name='phase_edit'),
    path('phaselist/delete/<int:id>/', views.phase_delete, name='phase_delete'),

    path('unitlist/<int:id>/', views.unit_list, name='unit_list'),
    path('unitlist/edit/<int:id>/', views.unit_edit, name='unit_edit'),
    path('unitlist/delete/<int:id>/', views.unit_delete, name='unit_delete'),

    # user register unit
    path('registernewblock/', views.register_new_block, name='register_new_block'),
    path('registerunitlist/all', views.register_unit_list_all, name='register_unit_list_all'),

]
