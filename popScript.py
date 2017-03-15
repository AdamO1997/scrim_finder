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

    for team in teams:
        team = add_team(team['title'],team['users'],team['full'],team['image'])

    i=1

def add_team(title,users,full,image):
        t = Team.objects.get_or_create(title = title)[0]
        t.users = users
        t.full = full
        t.image = image
        t.title = title
        t.save()
        return t




if __name__ == "__main__":
    print("Starting population script")
    populate()

