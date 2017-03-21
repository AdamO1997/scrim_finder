from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from django.db import models



class Team(models.Model):

    title = models.CharField(max_length = 30,unique = True)
    password = models.CharField(max_length = 15, default = "")
    passRequired = models.BooleanField(default = False)
    full = models.BooleanField(default = False)
    image = models.ImageField(upload_to='team_images',blank = True)
    users = models.ManyToManyField('userProfile')
    slug = models.SlugField(unique = True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Team, self).save(*args, **kwargs)

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
    icon = models.ImageField(upload_to = "game_images", blank = True)
    slug = models.SlugField(unique = True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.game)
        super(Games, self).save(*args,**kwargs)

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
    teams = models.ManyToManyField(Team)
    full = models.BooleanField(default = False)

    def __str__(self):
        return self.matchID

    def __unicode__(self):
        return self.matchID

    class Meta:
        ordering = ('matchID',)
