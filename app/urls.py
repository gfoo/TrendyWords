

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/<int:project_id>/',
         views.project_detail, name='project_detail'),
]
