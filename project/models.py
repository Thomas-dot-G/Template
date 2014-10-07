from django.db import models

# Match class
class Match(models.Model):
    place = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    winer = models.ForeignKey('Player', related_name="win", default=None)
    loser = models.ForeignKey('Player', related_name="lose", default=None)

    def __unicode__(self):
        return self.winer.name + " VS " + self.loser.name

# Player class
class Player(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    matchs = models.ManyToManyField(Match , blank=True)
    
    def __unicode__(self):
        return self.name

