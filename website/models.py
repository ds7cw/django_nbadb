from django.db import models

# Create your models here.

class Player(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    games_played = models.IntegerField(default=0)
    ppg = models.FloatField(default=0.0)
    rpg = models.FloatField(default=0.0)
    apg = models.FloatField(default=0.0)
    fg_pct = models.FloatField(default=0.0)
    fg3_pct = models.FloatField(default=0.0)
    ft_pct = models.FloatField(default=0.0)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} [{self.ppg} Points Per Game]"
