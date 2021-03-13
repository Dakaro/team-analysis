from django.db import models

# Create your models here.

class Player(models.Model):
    player_name = models.CharField(max_length = 30 )
    player_count = models.IntegerField(default = 0)
    player_percent = models.FloatField(default = 0)
    player_position = models.CharField(max_length = 30)

class Team(models.Model):
    team_name = models.CharField(max_length = 30)
    players_list = models.TextField(max_length = 200)
    team_power = models.IntegerField(default= 0)
