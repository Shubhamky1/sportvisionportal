from django.db import models
from players.models import Player
from users.models import User

class Team(models.Model):
    name = models.CharField(max_length=100)
    coach = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, limit_choices_to={'role': 'coach'})
    players = models.ManyToManyField(Player, blank=True)

    def __str__(self):
        return self.name
