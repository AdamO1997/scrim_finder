import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','scrim_finder.settings')

import django
django.setup()
from scrim_finder_app.models import userProfile,Team,Games,Match

def populate():
    userProfiles = {'Ali': {'password': 'ali1234', 'email':'alimunn@gmail.com'
         , 'playedGames' : ['Fifa','Madden','Dishonoured 2']},
    'Jason' :{'password': 'jason1234', 'email':'jegan@gmail.com'
         , 'playedGames' : ['Fifa','Battlefield','Dishonoured 2']}}


    for user,userInfo in userProfiles.items():
        user = add_user(user,userInfo['password'],userInfo['email'],userInfo['playedGames'])


def add_user(user,password,email,playedGames):
        u = userProfile.objects.get_or_create(userName = user)[0]
        u.email = email
        u.playedGames = playedGames
        u.password = password
        u.userName = user
        u.save()
        return u



if __name__ == "__main__":
    print("Starting population script")
    populate()

