from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from project.models import *
import json

# Index page
def index(request):
    return render(request, "index.html")


# List all players in a simple way
def players(request):
    res = [x.name+"<br>" for x in Player.objects.all()]
    return HttpResponse(res)


# List all players using templates
def players2(request):
    res = [x for x in Player.objects.all()]
    return render(request, "players.html", {"players": res})


# List all matchs using templates
def matchs(request):
    res = [x for x in Match.objects.all()]
    return render(request, "matchs.html", {"matchs": res})


# List Player details
def player_details(request, player):
    res = next(x for x in Player.objects.all() if x.name == player)
    return render(request, "player_details.html", {"player": res})


# List all players (JSON)
def players_json(request):
    res = [ {"name":x.name, "age":x.age} for x in Player.objects.all()]
    return HttpResponse(json.dumps(res), content_type="application/json")
