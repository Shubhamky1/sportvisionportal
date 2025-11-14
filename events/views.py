# events/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Match
from .forms import EventForm, MatchForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def event_list(request):
    events = Event.objects.all().order_by('-date')
    matches = Match.objects.select_related('event', 'team1', 'team2').order_by('-match_date')
    return render(request, 'events/event_list.html', {
        'events': events,
        'matches': matches,
    })

@login_required
def event_create(request):
    if request.user.role != "admin":
        messages.error(request, "Only admin can add events.")
        return redirect('event_list')

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Event added successfully!")
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form})

@login_required
def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.user.role != "admin":
        messages.error(request, "Only admin can edit events.")
        return redirect('event_list')

    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        messages.success(request, "Event updated successfully!")
        return redirect('event_list')
    return render(request, 'events/event_form.html', {'form': form})

@login_required
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.user.role != "admin":
        messages.error(request, "Only admin can delete events.")
        return redirect('event_list')

    if request.method == 'POST':
        event.delete()
        messages.success(request, "Event deleted successfully!")
        return redirect('event_list')
    return render(request, 'events/event_confirm_delete.html', {'event': event})

@login_required
def match_create(request):
    if request.user.role != "admin":
        messages.error(request, "Only admin can add matches.")
        return redirect('event_list')
    
    if request.method == 'POST':
        form = MatchForm(request.POST)
        if form.is_valid():
            print("Form is valid", form.cleaned_data)
            form.save()
            messages.success(request, "Match added successfully!")
            return redirect('event_list')
    else:
        form = MatchForm()
    return render(request, 'events/match_form.html', {'form': form})


def event_details(request, pk):
    event = get_object_or_404(Event, pk=pk)

    matches = Match.objects.filter(event=event)

    return render(request, 'events/event_details.html', {
        'event': event,
        'matches': matches
    })


def match_details(request, pk):
    match = get_object_or_404(Match, pk=pk)

    team1_players = match.team1.players.all()
    team1_coach = match.team1.coach

    team2_players = match.team2.players.all()
    team2_coach = match.team2.coach

    return render(request, 'events/match_details.html', {
        'match': match,
        'team1_players': team1_players,
        'team1_coach': team1_coach,
        'team2_players': team2_players,
        'team2_coach': team2_coach,
    })
