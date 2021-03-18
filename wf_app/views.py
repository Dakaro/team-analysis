from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Player

def player_list(request):
    players = Player.objects.all()
    return render(request, "wf_app/wf_voting.html", {'players': players} )
