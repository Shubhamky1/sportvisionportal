from django.db import models
from users.models import User

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    contact = models.CharField(max_length=15)
    skills = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username
