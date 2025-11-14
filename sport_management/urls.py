from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

from django.urls import path, include
from django.shortcuts import render
from .views import home
# def home(request):
#     return render(request, 'home.html')

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('user/', include('users.urls')),
    path('players/', include('players.urls')),
    path('events/', include('events.urls')),
    path('teams/', include('teams.urls')),
]
