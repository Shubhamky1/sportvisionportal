from django.urls import path
from . import views

urlpatterns = [
    path('', views.player_list, name='player_list'),
    path('create/', views.player_create, name='player_create'),
    path('<int:pk>/edit/', views.player_update, name='player_update'),
    path('<int:pk>/delete/', views.player_delete, name='player_delete'),
]
