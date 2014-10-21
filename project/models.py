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


# Participation Class
class ParticipationT(models.Model):
    score = models.IntegerField(default=0)
    team = models.ForeignKey(Team)
    match = models.ForeignKey(Match)

    def __unicode__(self):
        return self.match.place + " " + self.team.name

#Commentaire
class Comment(models.Model):
    comment = models.CharField(max_length=1000)
    match = models.ForeignKey(Match)

# new match class (Forms)
class newmatch(forms.Form):
    place = forms.CharField(label="Name", max_length=200, widget=forms.TextInput)
    date = forms.DateField(required = False)

    #liste = [ ,x.name for x in Player.objects.all()]
    #liste = (('a','a'))
    #choix = forms.MultipleChoiceField(label="Choices", widget=forms.CheckboxSelectMultiple, choices = Player.objects.all())
    player1 = forms.CharField(label="player1", max_length = 200, widget=forms.TextInput, required= True)
    player2 = forms.CharField(label="player2", max_length=200, widget=forms.TextInput, required = True)
    score1 = forms.IntegerField(label="score1")
    score2 = forms.IntegerField(label="score2")

class one_player(forms.Form):
    player = forms.ChoiceField(widget=forms.CheckboxInput, choices=('p',' '))


#new account class (Forms)
class newaccount(forms.Form):
    name = forms.CharField(label="login", max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Login'}))
    password = forms.CharField(label="password", max_length=200, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    age = forms.IntegerField(label="age")
    CHOICES=(('a','Admin'), ('a','Player'), ('g','Guest'))
    title = forms.ChoiceField(label="title", widget=forms.RadioSelect(), choices=CHOICES)
    team = forms.CharField(label="team", max_length=200, widget=forms.TextInput(attrs={'value': 'none'}))

class login(forms.Form):
    name = forms.CharField(label="login", max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Login'}))
    password = forms.CharField(label="password", max_length=200, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class newcomment(forms.Form):
    name = forms.CharField(label="Name", max_length=200, widget = forms.TextInput)
    comment = forms.CharField(label="Comments", max_length=1000, widget = forms.TextInput)
    liste = []
    match = forms.ChoiceField(label = "Match", widget = forms.TextInput)
