from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

class userProfile(models.Model):

    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images',blank = True)


    def __str__(self):
        return self.user.username
