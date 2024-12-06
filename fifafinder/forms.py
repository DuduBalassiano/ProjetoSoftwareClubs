from django import forms
from .models import Player, Team

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'position', 'description', 'team']