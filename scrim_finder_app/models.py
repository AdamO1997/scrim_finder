from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models



class Team(models.Model):

    title = models.CharField(max_length = 30,unique = True)
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
    matches = models.ManyToManyField('Match')

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username



class Games(models.Model):
    game = models.CharField(max_length = 30, unique = True)
    usersPlayed = models.ManyToManyField(userProfile)
    teamsPlayed = models.ManyToManyField(Team)
    genre = models.CharField(max_length = 15)

    def __str__(self):
        return self.game

    def __unicode__(self):
        return self.game

    class Meta:

        ordering = ('game',)


class Match(models.Model):
    matchID = models.CharField(max_length = 15,unique = True)
    customName = models.CharField(max_length = 20)
    date = models.DateTimeField()
    numPlayers = models.IntegerField()
    game = models.ForeignKey(Games,on_delete = models.CASCADE)
    teamsPlaying = models.ManyToManyField(Team)

    def __str__(self):
        return self.customName

    def __unicode__(self):
        return self.customName

    class Meta:
        ordering = ('matchID',)
