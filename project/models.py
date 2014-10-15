from django.db import models

# Match class
class Match(models.Model):
    place = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)

    def loser(self):
        return self.participation_set.all().order_by("score")[0]

    def winer(self):
        return self.participation_set.all().order_by("score").reverse()[0]

    def comment(self)
    return self.comment_set.all()        


    def __unicode__(self):
        return self.place


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

#Commentaire
class Comment(models.Model):
    comm = models.CharField(max_length=1000)
    auteur = models.ForeignKey(Player)
    match = models.ForeignKey(Match)

    def __unicode__(self):
      return self.auteur.name
