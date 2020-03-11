from django.urls import path
from . import views
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('createobject/', views.createObject, name='createObject'),
    path('createproject/', views.createProject, name='createProject'),
    path('createphase/', views.createPhase, name='createPhase'),
    path('test/', views.test, name='test'),
    path('projectlist/', views.projectList, name='projectList'),
   # path('ajax/loadproject/', views.load_project, name='ajax_load_project'),
]