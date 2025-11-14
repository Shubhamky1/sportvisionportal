# teams/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.team_list, name='team_list'),
    path('create/', views.team_create, name='team_create'),
    path('update/<int:pk>/', views.team_update, name='team_update'),
    path('delete/<int:pk>/', views.team_delete, name='team_delete'),
]
