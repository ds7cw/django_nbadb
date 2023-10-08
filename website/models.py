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


class MainPlayer(models.Model):
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    suffix = models.CharField(max_length=5)
    pos = models.CharField(max_length=2)
    team = models.CharField(max_length=3)
    gp = models.IntegerField(default=0)
    mpg = models.FloatField(default=0.0)
    fg_pct = models.FloatField(default=0.0)
    ft_pct = models.FloatField(default=0.0)
    threes_made = models.FloatField(default=0.0)
    rpg = models.FloatField(default=0.0)
    apg = models.FloatField(default=0.0)
    stpg = models.FloatField(default=0.0)
    blkpg = models.FloatField(default=0.0)
    topg = models.FloatField(default=0.0)
    ppg = models.FloatField(default=0.0)
    salary = models.IntegerField(default=0.0)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} {self.suffix} | APG: {self.apg} | RPG: {self.rpg} | PPG:{self.ppg}'
