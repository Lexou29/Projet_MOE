from django.db import models

# Create your models here.
from django.db import models

# Match class
class Match(models.Model):
    place = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    sport = models.ForeignKey(Sport)

    def __unicode__(self):
	return self.sport

    def loser(self):
        return self.participation_set.all().order_by("score")[0]

    def winner(self):
        return self.participation_set.all().order_by("score").reverse()[0]
    
    def __unicode__(self):
        return self.place

#Class permettant d'ajouter un match
class MatchForm(forms.Form):
    date = forms.DateField() 
    lieu = forms.CharField(label="Lieu", max_length=200, widget=forms.TextInput)
       


# Player class
class Player(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

# Sport class
class Sport(models.Model):
    sport = models.CharField(max_length=200)

    def __unicode__(self):
        return self.sport


# Participation Class
class Participation(models.Model):
    score = models.IntegerField(default=0)
    player = models.ForeignKey(Player)
    match = models.ForeignKey(Match)

    def __unicode__(self):
        return self.match.place + " " + self.player.name
