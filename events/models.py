from django.db import models
from teams.models import Team

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name} - {self.date}"

class Match(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team1_matches')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team2_matches')
    match_date = models.DateTimeField()
    result = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return f"{self.team1.name} vs {self.team2.name} ({self.event.name})"