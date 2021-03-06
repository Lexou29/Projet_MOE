from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from projet.models import *
import json
from django.core.urlresolvers import reverse

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
			score1 = res.cleaned_data["score1"]
			player1 = res.cleaned_data["player1"]
			match = res.cleaned_data["match"]
			player1 = Player.objects.filter(name = player1.first())
			match_id = match.values_list('id', flat=True)
			match = Match.objects.filter(id = match_id.first())
			p1 = Participation(score=score1, player=player1[0], match=match[0])
			p1.save()
			
			score2 = res.cleaned_data["score2"]
			player2 = res.cleaned_data["player2"]
			match = res.cleaned_data["match"]
			player2 = Player.objects.filter(name = player2.first())
			match_id = match.values_list('id', flat=True)
			match = Match.objects.filter(id = match_id.first())
			p2 = Participation(score=score2, player=player2[0], match=match[0])
			p2.save()
			return HttpResponseRedirect(reverse("matchs"))
        
	return render(request, "matchsForms.html",{"res":res})

#Ajout d'un match
def matchForm(request):
	if request.method == 'GET':
		res = MatchForm()
	else:
		res = MatchForm(request.POST)
        if res.is_valid():
			place = res.cleaned_data["place"]
			date = res.cleaned_data["date"]
			m = Match(place=place, date=date)
			m.save()
			return HttpResponseRedirect(reverse("mForm"))
        
	return render(request, "matchsForms2.html",{"res":res})
