from django.db import models

# Create your models here.
from django.db import models

class User(models.Model): # Tabela "m" no diagrama
name = models.CharField(max_length=255)
email = models.EmailField(unique=True)
password = models.CharField(max_length=255)
platform = models.CharField(max_length=255)
availability = models.TextField() # "Horários de disponibilidade"

def __str__(self):
return self.name

class Team(models.Model): # Tabela "Time"
name = models.CharField(max_length=255)
captain = models.ForeignKey('Player', on_delete=models.SET_NULL, null=True, blank=True, related_name='captain_of')
player_count = models.PositiveIntegerField()
region = models.CharField(max_length=255)
information = models.TextField(blank=True, null=True)

def __str__(self):
return self.name

class Player(models.Model): # Tabela "Jogador"
name = models.CharField(max_length=255)
position = models.CharField(max_length=100)
description = models.TextField(blank=True, null=True)
team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='players')

def __str__(self):
return self.name

class Match(models.Model): # Tabela "Partida"
goals = models.PositiveIntegerField(default=0)
assists = models.PositiveIntegerField(default=0)
rating = models.DecimalField(max_digits=4, decimal_places=2)

def __str__(self):
return f"Match {self.id}"

class Championship(models.Model): # Tabela "Campeonato"
name = models.CharField(max_length=255)
organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organized_championships')
mode = models.CharField(max_length=100)
format = models.CharField(max_length=100)
max_players = models.PositiveIntegerField()
date = models.DateField()
time = models.TimeField()

def __str__(self):
return self.name

class ChampionshipRegistration(models.Model): # Relação "Inscreve"
championship = models.ForeignKey(Championship, on_delete=models.CASCADE, related_name='registrations')
user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registrations')

def __str__(self):
return f"{self.user.name} -> {self.championship.name}"