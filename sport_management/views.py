from django.shortcuts import render
from events.models import Event, Match
from django.utils import timezone

def home(request):

    upcoming_events = Event.objects.filter(
        date__gte=timezone.now().date()
    ).order_by('date')[:5]

    upcoming_matches = Match.objects.filter(
        match_date__gte=timezone.now()
    ).order_by('match_date')[:5]

    recent_results = Match.objects.filter(
        result__isnull=False
    ).order_by('-match_date')[:5]

    return render(request, 'home.html', {
        'upcoming_events': upcoming_events,
        'upcoming_matches': upcoming_matches,
        'recent_results': recent_results,
    })
