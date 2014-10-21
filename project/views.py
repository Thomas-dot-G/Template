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
    res = next(x for x in Player.objects.all() if x.name == player)
    return render(request, "player_details.html", {"player": res, "form":form})

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


# Liste des commentaires
def comments(request):
    personne=Log.objects.all()[0]
    res = [x for x in Comment.objects.all()]
    return render(request, "comments.html", {"personne":personne,"comments": res})


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

#Create a new match
def new_match(request):
    personne=Log.objects.all()[0]
    if request.method =='GET':
       res = newmatch()
    else:
        res = newmatch(request.POST)

        if res.is_valid():
            place = res.cleaned_data["place"]
            #date = res.cleaned_data["date"]
            player1 = res.cleaned_data['player1']
            player2 = res.cleaned_data['player2']
            score1 = res.cleaned_data['score1']
            score2 = res.cleaned_data['score2']
            m=Match(place = place)
            m.save()

            #loser=request.POST['loser']
            #winner = request.POST['winner']

            for p in Player.objects.all():
              if p.name==player1:
                Participation(player = p, match =m, score=score1).save()

            for p2 in Player.objects.all():
              if p2.name == player2:
                Participation(player = p2, match = m, score=score2).save()

            return HttpResponseRedirect(reverse('index'))
    return render(request, "new_match.html", {"res": res, "players": players,  "personne": personne})


# Modifier un match
def alter_match(request, name):
    personne=Log.objects.all()[0]
    if request.method =='GET':
       res = newmatch()
    else:
        res = newmatch(request.POST)

        if res.is_valid():
            place = res.cleaned_data["place"]
            #date = res.cleaned_data["date"]
            player1 = res.cleaned_data['player1']
            player2 = res.cleaned_data['player2']

            thematch = next(x for x in Match.objects.all() if x.place == name)

            match2 = Match.objects.filter(place = name)

            matchmodif = Match.objects.filter(place = name)
            matchmodif.update(place = place)

            for p in Player.objects.all():
              if p.name==player1:
                partcip1 = Participation.objects.filter(player=p1, match=match2)
                particip1.update(player=p, match=matchmodif)

            for p2 in Player.objects.all():
              if p2.name == player2:
                partcip2 = Participation.objects.filter(player=p2, match=match2)
                particip2.update(player=p2, match=matchmodif)


            return HttpResponseRedirect(reverse('index'))
    return render(request, "alter_match.html", {"res": res, "matchs": match, "personne": personne})
