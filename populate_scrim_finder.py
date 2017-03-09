import os
os.environ.setdefault('SCRIM_FINDER_SETTINGS_MODULE','scrim_finder_app.settings')

import django
django.setup()
from scrim_finder_app.models import Team,Games,Match

def populate():
    usersProfiles = [
        {'User.username':'Ali', 'User.password': 'ali1234', 'email':'alimunn@gmail.com'
         , 'playedGames' : ['Fifa','Madden','Dishonoured 2']}
        {'User.username':'Jason', 'User.password': 'jason1234', 'email':'jegan@gmail.com'
         , 'playedGames' : ['Fifa','Battlefield','Dishonoured 2']}



def add_user(userProfile,User.username,User.password,email,playedGames):
        u = userProfile.get_or_create(User.username)[0]
        u.email = email
        u.playedGames = playedGames
        u.User.password = User.password
        u.User.username = User.username
        u.save()
        return u
