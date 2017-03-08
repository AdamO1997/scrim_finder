from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

class userProfile(models.Model):

    user = models.OneToOneField(User,on_delete = models.CASCADE)
    email = models.EmailField(max_length = 254, **options)
    picture = models.ImageField(upload_to='profile_images',blank = True)


    def __str__(self):
        return self.user.username


    class Meta:

        ordering = ('user',)


class Team(models.Model):

    title = models.CharField(max_length = 30,unique = True)
    users = models.ManyToManyField(userProfile)
    full = models.BooleanField(default = False)
    image = models.ImageField(upload_to='team_images',blank = True)


    def _str__(self):
        return Team.title

    class Meta:

        ordering = ('title',)



class Games(models.Model):
    game = models.CharField(max_length = 30, unique = True)
    usersPlayed = models.ManyToManyField(userProfile)
    genre = models.CharField(max_length = 15)

    def __str__(self):
        return Games.game

    Class Meta:

        ordering = ('game',)


class Match(models.Model):
    matchID = models.charField(max_length = 15,unique = True)
    customName = models.charField(max_length = 20)
    date = models.DateTimeField()
    numPlayers = models.IntegerField()
    game = models.ForeignKey(Games,on_delete = models.CASCADE)

    def __str__(self):
        return Match.customName

    class Meta:
        ordering = ('matchID',)
