from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from project.models import *
from django.core import serializers
import HTMLParser
import json

# Index page
def index(request):
      Log.objects.all().delete()
      if request.method == 'GET':
        form = login()
      else:
        form = login(request.POST)
        if form.is_valid() :
          name = form.cleaned_data["name"] #formate data recues
          password = form.cleaned_data["password"]

          for l in Account.objects.all():
            if l.login==name:
              if l.password==password:
                 personne=Log(login=name)
                 personne.save()
                 return HttpResponseRedirect(reverse('indexlog'))

      return render(request, "index.html", {"form": form})

#    return render(request, "index.html")


def indexlog(request):
    personne=Log.objects.all()[0]
    return render(request, "indexlog.html",{"personne": personne} )

# List all players in a simple way
def players(request):
    res = [x.name+"<br>" for x in Player.objects.all()]
    return HttpResponse(res, {"personne": personne})

# List all players in a simple way
def playerslog(request):
    res = [x.name+"<br>" for x in Player.objects.all()]
    return HttpResponse(res)


# List all players using templates
def players2(request):
    if request.method == 'GET':
      form = login()
    else:
      form = login(request.POST)
      if form.is_valid() :
        name = form.cleaned_data["name"] #formate data recues
        password = form.cleaned_data["password"]

        for l in Account.objects.all():
          if l.login==name:
            if l.password==password:
              personne=Log(login=name)
              personne.save()
              return HttpResponseRedirect(reverse('indexlog'))
    res = [x for x in Player.objects.all()]
    return render(request, "players.html", {"form": form, "players": res})

def players2log(request):
  personne=Log.objects.all()[0]
  res = [x for x in Player.objects.all()]
  return render(request, "playerslog.html", {"personne": personne, "players": res})

# List of Teams
def team(request):
    #account=Account.objects.all()
    #account.delete()
    if request.method == 'GET':
      form = login()
    else:
      form = login(request.POST)
      if form.is_valid() :
        name = form.cleaned_data["name"] #formate data recues
        password = form.cleaned_data["password"]

        for l in Account.objects.all():
          if l.login==name:
            if l.password==password:
              personne=Log(login=name)
              personne.save()
              return HttpResponseRedirect(reverse('indexlog'))
    res = [x for x in Team.objects.all()]
    people= []
    for x in range(Team.objects.count()):
      people.append(Player.objects.filter(team=Team.objects.all()[x]))
    return render(request, "team.html", {"form":form, "team": res, "people": people})

def teamlog(request):
  personne=Log.objects.all()[0]
  res = [x for x in Team.objects.all()]
  people = [x for x in Player.objects.all()]
  return render(request, "teamlog.html", {"personne":personne, "team": res, "people": people})


# List all matchs using templates
def matchs(request):
    if request.method == 'GET':
      form = login()
    else:
      form = login(request.POST)
      if form.is_valid() :
        name = form.cleaned_data["name"] #formate data recues
        password = form.cleaned_data["password"]

        for l in Account.objects.all():
          if l.login==name:
            if l.password==password:
              personne=Log(login=name)
              personne.save()
              return HttpResponseRedirect(reverse('indexlog'))

    res = [x for x in Match.objects.all()]
    return render(request, "matchs.html", {"form":form, "matchs": res})


def matchslog(request):
  personne=Log.objects.all()[0]
  res = [x for x in Match.objects.all()]
  return render(request, "matchslog.html", {"personne":personne, "matchs": res})

# List Player details
def player_details(request, player):
    res = next(x for x in Player.objects.all() if x.name == player)
    return render(request, "player_details.html", {"player": res})

# List Player details
def player_detailslog(request, player):
    personne=Log.objects.all()[0]
    res = next(x for x in Player.objects.all() if x.name == player)
    return render(request, "player_detailslog.html", {"personne":personne, "player": res})


# List all players (JSON)
def players_json(request):
    res = []
    for p in Player.objects.all():
        c = len(Participation.objects.filter(player=p.id))
        res += [{ "name": p.name, "age": p.age, "matchesCount": c }]
    return HttpResponse(json.dumps(res), content_type="application/json")

def players_table(request):
    h = HTMLParser.HTMLParser()
    filter = h.unescape(request.GET.get('filter', ''))
    res = Player.objects.filter(name__icontains=filter)
    return render(request, "players_table.html", {"players": res})


# Create new account
def new_account(request):
    if request.method == 'GET':
        res = newaccount()
    else:
        res = newaccount(request.POST)
        if res.is_valid() :
            name = res.cleaned_data["name"] #formate data recues
            age = res.cleaned_data["age"]
            password = res.cleaned_data["password"]
            title = res.cleaned_data["title"]
            team = res.cleaned_data["team"]
            appartien=False
            for n in Account.objects.all():
              if n.login==name:
                return HttpResponseRedirect(reverse('new_account'))
            for t in Team.objects.all():
              if t.name==team:
                appartien=True
                nt=t
            if appartien==False and team!="none":
              nt= Team(name=team)
              nt.save()
            if team=="none":
              nt=None
            if title!='g':
              p = Player(name=name, age=age, team=nt)
              p.save()
            l = Account(login=name, password=password, title=title)
            l.save()
            return HttpResponseRedirect(reverse('index'))

    return render(request, "new_account.html", {"res": res})

# Modify an account
def profil(request):
    personne=Log.objects.all()[0]
    if request.method == 'GET':
        res = newaccount()
    else:
        res = newaccount(request.POST)
        if res.is_valid() :
            name = res.cleaned_data["name"] #formate data recues
            age = res.cleaned_data["age"]
            password = res.cleaned_data["password"]
            title = res.cleaned_data["title"]
            team = res.cleaned_data["team"]
            appartien=False
            for t in Team.objects.all():
              if t.name==team:
                appartien=True
                nt=t
            if appartien==False and team!="none":
              nt= Team(name=team)
              nt.save()
            if team=="none":
              nt=None
            if title!='g':
              playermodif=Player.objects.filter(name=personne.login)
              playermodif.update(name=name, age=age, team=nt)
            accountmodif=Account.objects.filter(login=personne.login)
            accountmodif.update(login=name, password=password, title=title)
            Log.objects.filter(login=personne.login).update(login=name)
            return HttpResponseRedirect(reverse('indexlog'))

    return render(request, "profil.html", {"res": res, "personne": personne})
