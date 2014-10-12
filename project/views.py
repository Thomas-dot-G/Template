from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from project.models import *
from django.core import serializers
import HTMLParser
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
            login = res.cleaned_data["login"] #formate data recues
            age = res.cleaned_data["age"]
            password = res.cleaned_data["password"]
            title = res.cleaned_data["title"]
            team = res.cleaned_data["team"]
            p = Player(name=name, age=age, team=team)
            p.save()
            l = Account(login=login, password=password, title=title)
            l.save()
            return HttpResponseRedirect("index")

    return render(request, "new_account.html", {"res": res})
