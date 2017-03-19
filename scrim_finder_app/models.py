from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models



class Team(models.Model):

    title = models.CharField(max_length = 30,unique = True)
    password = models.CharField(max_length = 15, default = "")
    full = models.BooleanField(default = False)
    image = models.ImageField(upload_to='team_images',blank = True)
    users = models.ManyToManyField('userProfile')

    def _str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    class Meta:

        ordering = ('title',)



class userProfile(models.Model):

    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images',blank = True)
    teams = models.ManyToManyField(Team)

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username



class Games(models.Model):
    game = models.CharField(max_length = 30, unique = True)
    genre = models.CharField(max_length = 15)

    def __str__(self):
        return self.game

    def __unicode__(self):  
        return self.game

    class Meta:

        ordering = ('game',)


class Match(models.Model):
    matchID = models.CharField(max_length = 10,unique = True)
    password = models.CharField(max_length = 15, blank = True)
    passRequired = models.BooleanField(default = False)
    date = models.DateTimeField(auto_now_add=True)
    game = models.ForeignKey(Games,on_delete = models.CASCADE)
    teamsPlaying = models.ManyToManyField(Team)

    def __str__(self):
        return self.matchID

    def __unicode__(self):
        return self.matchID

    class Meta:
        ordering = ('matchID',)
