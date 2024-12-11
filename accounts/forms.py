from django import forms
from .models import Player, Team, Championship

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'position', 'description', 'team']
        
class ChampionshipForm(forms.ModelForm):
    class Meta:
        model = Championship
        fields = ['name', 'organizer', 'mode', 'format', 'max_players', 'date', 'time']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do campeonato'}),
            'organizer': forms.Select(attrs={'class': 'form-control'}),
            'mode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Modo de jogo'}),
            'format': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Formato do campeonato'}),
            'max_players': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número máximo de jogadores'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }