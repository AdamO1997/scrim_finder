import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','scrim_finder.settings')

import django
django.setup()
from scrim_finder_app.models import userProfile,Team,Games,Match

def populate():
    
    teams = [{'title': 'TeamGO','users':'','full':False,'image':''},
             {'title': 'Assassins','users': '','full':False,'image':''},
             {'title': 'NoMercy','users':'','full':False,'image':''}
        ]

    games = [{'title': 'Uncharted 4','genre': 'Adventure'},
             {'title': 'Overwatch', 'genre': 'FPS'},
             {'title': 'League of Legends', 'genre':'Multiplayer Online Battle Arena'},
             {'title': 'Dota 2', 'genre': 'Multiplayer Online Battle Area'}
        ]

    matches = [{'matchID': 'DTA198372', 'date':'2017-12-12', 'game':'Dota 2',
               'teamsPlaying':''}

        ]   

    for team in teams:
        team = add_team(team['title'],team['users'],team['full'],team['image'])

    for game in games:
        game = add_game(game['title'],game['genre'])

    
    for match in matches:
        match = add_match(match['matchID'], match['date'], match['game'],
                          match['teamsPlaying'])
        
   

def add_team(title,users,full,image):
    t = Team.objects.get_or_create(title = title)[0]
    t.users = users
    t.full = full
    t.image = image
    t.title = title
    t.save()
    return t

def add_game(title, genre):
    g = Games.objects.get_or_create(game = title)[0]
    g.game = title
    g.genre = genre
    g.save()
    return g


def add_match(ID, date, game, teamsPlaying):
    m = Match.objects.get_or_create(matchID = ID)[0]
    print ID
    print date
    print game
    print teamsPlaying
    

if __name__ == "__main__":
    print("Starting population script")
    populate()

