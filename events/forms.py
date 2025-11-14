# events/forms.py
from django import forms

from teams.models import Team
from .models import Event, Match



class EventForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d']
    )

    class Meta:
        model = Event
        fields = ['name', 'date', 'location']


class MatchForm(forms.ModelForm):
    match_date = forms.DateTimeField(
        label="Match Date & Time",
        widget=forms.DateTimeInput(
            attrs={'type': 'datetime-local', 'class': 'rounded-xl p-4 w-full'}
        ),
        input_formats=['%Y-%m-%dT%H:%M']  # ✅ this matches browser format
    )

    event = forms.ModelChoiceField(
        queryset=Event.objects.all(),
        label="Select Event",
        empty_label="-- Choose an Event --"
    )

    team1 = forms.ModelChoiceField(queryset=Team.objects.all(), label="Team 1")
    team2 = forms.ModelChoiceField(queryset=Team.objects.all(), label="Team 2")

    class Meta:
        model = Match
        fields = ['event', 'team1', 'team2', 'match_date', 'result']