from django.db import models
from django import forms

# Match class
class Match(models.Model):
    place = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True, auto_now=False)

    def loser(self):
        return self.participation_set.all().order_by("score")[0]

    def winner(self):
        return self.participation_set.all().order_by("score").reverse()[0]
    
    def __unicode__(self):
        return self.place
  
# Ajout d'un match
class MatchForm(forms.Form):
	place = forms.CharField(label="Lieu du match", max_length=200, widget=forms.TextInput)
	date = forms.DateField(label="Date", input_formats=['%m/%d/%Y','%d/%m/%Y'], widget=forms.DateInput(attrs={'size':'15','id':'datepicker'},format=["%m/%d/%Y","%d/%m/%Y"]))  
	# winner = Match.winner()
	# loser = Match.loser()


# Player class
class Player(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name


# Participation Class
class Participation(models.Model):
    score = models.IntegerField(default=0)
    player = models.ForeignKey(Player)
    match = models.ForeignKey(Match)

    def __unicode__(self):
        return self.match.place + " " + self.player.name


# Ajout d'une participation
class ParticipationForm(forms.Form):
    score = forms.IntegerField(label = "Score")
    player = forms.ModelMultipleChoiceField(queryset=Player.objects.all())
    match = forms.ModelMultipleChoiceField(queryset=Match.objects.all())

