from django.contrib import admin
from .models import Player

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'contact', 'skills')
    search_fields = ('user__username', 'contact')