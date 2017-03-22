import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','scrim_finder.settings')

import django
django.setup()
from scrim_finder_app.models import userProfile,Team,Games,Match

def populate():

    teams = [{'title': 'TeamGO','users':'','full':False,'image':'team_images/Koala.jpg'},
             {'title': 'Assassins','users': '','full':False,'image':'team_images/assassins.jpg'},
             {'title': 'NoMercy','users':'','full':False,'image':'team_images/nomercy.png'},
             {'title': 'TeampSTOP', 'users':'','full':False,'image':'team_images/stop.png'},
             {'title': 'Dragons', 'users':'','full':False,'image':'team_images/dragons.jpg'},
             {'title': 'Glaswegians', 'users':'','full':False,'image':'team_images/glaswegians.jpg'}
        ]

    games = [{'title': 'Uncharted 4','genre': 'Adventure', 'icon':'game_logos/uncharted4.png'},
             {'title': 'Overwatch', 'genre': 'FPS', 'icon':'game_logos/overwatch.png'},
             {'title': 'League of Legends', 'genre':'Multiplayer Online Battle Arena', 'icon':'game_logos/lol.png'},
             {'title': 'Dota 2', 'genre': 'Multiplayer Online Battle Area','icon':'game_logos/dota2.png'},
             {'title': 'CIV 5', 'genre': 'Multiplayer Online Battle Area','icon':'game_logos/civ5.png'},
             {'title': 'Titanfall', 'genre': 'FPS', 'icon':'game_logos/titanfall.png'}
        ]



    for team in teams:
        team = add_team(team['title'],team['users'],team['full'],team['image'])

    for game in games:
        game = add_game(game['title'],game['genre'],game['icon'])



    matches = [{'matchID': 'DTA198372', 'date':'2017-12-12', 'game':Games.objects.get(game="Dota 2"),
               'teams':Team.objects.get(pk=1)},
               {'matchID': 'UNC298372', 'date':'2017-12-11', 'game':Games.objects.get(game="Uncharted 4"),
               'teams':Team.objects.get(pk=2)},
               {'matchID': 'LOL325634', 'date':'2017-12-10', 'game':Games.objects.get(game="League of Legends"),
               'teams':Team.objects.get(pk=3)},
               {'matchID': 'CIV998372', 'date':'2017-11-11', 'game':Games.objects.get(game="CIV 5"),
               'teams':Team.objects.get(pk=4)},
               {'matchID': 'TFL294572', 'date':'2017-06-11', 'game':Games.objects.get(game="Titanfall"),
               'teams':Team.objects.get(pk=1)},





        ]


    for match in matches:
        match = add_match(match['matchID'], match['date'], match['game'],
                          match['teams'])



def add_team(title,users,full,image):
    t = Team.objects.get_or_create(title = title)[0]
    t.users = users
    t.full = full
    t.image = image
    t.title = title
    t.save()
    return t

def add_game(title, genre, icon):
    g = Games.objects.get_or_create(game = title)[0]
    g.icon = icon
    g.game = title
    g.genre = genre
    g.save()
    return g


def add_match(ID, date, game, teams):
    m = Match.objects.get_or_create(matchID = ID, game = game, date = date)[0]
    m.date = date
    m.game = game
    m.save()
    return m


if __name__ == "__main__":
    print("Starting population script")
    populate()

