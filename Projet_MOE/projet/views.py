from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from projet.models import *
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

# Formulaire de participation
def participationForm(request):
	if request.method == 'GET':
		res = ParticipationForm()
	else:
		res = ParticipationForm(request.POST)
        if res.is_valid():
			score = res.cleaned_data["score"]
			player = res.cleaned_data["player"]
			match = res.cleaned_data["match"]
			p = Participation(score=score, player=player, match=match)
			return HttpResponseRedirect("matchs")
        
	return render(request, "matchsForms.html",{"res":res})

#Ajout d'un match
def matchForm(request):
	if request.method == 'GET':
		res = MatchForm()
	else:
		res = MatchForm(request.POST)
        if res.is_valid():
			lieu = res.cleaned_data["lieu"]
			date = res.cleaned_data["date"]
			m = Match(lieu=lieu, date=date)
			m.save()
			return HttpResponseRedirect("mForm")
        
	return render(request, "matchsForms2.html",{"res":res})
