from django import forms
from .models import Player



class MyVote(forms.Form):
    DISPLAY_CHOICE=()
    for player in Player.objects.all():
        DISPLAY_CHOICE += (player.player_count, player.player_name),
    display_type = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=DISPLAY_CHOICE )
