from django import forms
from .models import Player
from users.models import User

class PlayerForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        queryset=User.objects.filter(role__in=['player', '']).exclude(player__isnull=False),
        label="Select User (Player)"
    )

    class Meta:
        model = Player
        fields = ['user', 'age', 'contact', 'skills']