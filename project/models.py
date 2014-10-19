from django.db import models
from django import forms

# Match class
class Match(models.Model):
    place = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)

    def loser(self):
        return self.participation_set.all().order_by("score")[0]

    def winer(self):
        return self.participation_set.all().order_by("score").reverse()[0]

    def __unicode__(self):
        return self.place

#Account class
class Account(models.Model):
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    CHOICES=(('a','Admin'), ('a','Player'), ('g','Guest'))
    title = models.CharField(max_length=1, choices=CHOICES)

class Log(models.Model):
    login = models.CharField(max_length=200)

# Team class
class Team(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


# Player class
class Player(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    team = models.ForeignKey(Team, blank=True, on_delete=models.SET_NULL, null=True, default=None)

    def __unicode__(self):
        return self.name



# Participation Class
class Participation(models.Model):
    score = models.IntegerField(default=0)
    player = models.ForeignKey(Player)
    match = models.ForeignKey(Match)

    def __unicode__(self):
        return self.match.place + " " + self.player.name

#new account class (Forms)
class newaccount(forms.Form):
    name = forms.CharField(label="login", max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Login'}))
    password = forms.CharField(label="password", max_length=200, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    age = forms.IntegerField(label="age")
    CHOICES=(('a','Admin'), ('a','Player'), ('g','Guest'))
    title = forms.ChoiceField(label="title", widget=forms.RadioSelect(), choices=CHOICES)
    team = forms.CharField(label="team", max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Team (default none)'}))

class login(forms.Form):
    name = forms.CharField(label="login", max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Login'}))
    password = forms.CharField(label="password", max_length=200, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
