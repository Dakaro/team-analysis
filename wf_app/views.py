from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Player
from .forms import MyVote

"""""
def player_list(request):
    players = Player.objects.all()
    return render(request, "wf_app/wf_voting.html", {'players': players} ) """


def playerList(request):
    form = MyVote(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            display_type = request.POST["display_type"]
    return render(request, 'wf_app/wf_voting.html', {'form': form})
