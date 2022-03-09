

from django.shortcuts import redirect
from django.urls import path

from . import views

urlpatterns = [
    path('', lambda r: redirect('projects'), name='home'),
    path('projects', views.projects, name='projects'),
    path('projects/<int:project_id>/',
         views.project_detail, name='project_detail'),
]
