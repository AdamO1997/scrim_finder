"""scrim_finder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from scrim_finder_app import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^profile/(?P<username>[\w\-]+)/', views.account, name='account'),
	url(r'^gameList/', views.gameList, name='gameList'),
	url(r'^gameList/(?P<gameName>[\w\-]+)/', views.game, name='game'),
	url(r'^gameList/(?P<gameName>[\w\-]+)/matchList/', views.matchList, name='matchList'),
	url(r'^myMatches/', views.myMatches, name='myMatches'),
	url(r'^myTeams/', views.myTeams, name='myTeams'),
	url(r'^teamList/', views.teamList, name='teamList'),
	url(r'^register/', views.register, name='register'),
	url(r'^logout/', views.user_logout, name = 'logout'),
	url(r'^createTeam/', views.create_team, name= 'createTeam'),
	url(r'^createMatch/', views.create_match, name = 'createMatch'),
	url(r'^match/(?P<matchID>[\w\-]+)/', views.match, name = 'match'),
    url(r'^team/(?P<teamName>[\w\-]+)/', views.team, name = 'team'),
    url(r'^match/(?P<matchID>[\w\-]+)/edit', views.edit_match, name = 'editMatch'),
    url(r'^team/(?P<teamName>[\w\-]+)/edit', views.edit_team, name = 'editTeam'),
    url(r'^edit-account/', views.edit_account, name = 'editAccount'),
    url(r'^login/', views.user_login, name='login'),
    url(r'^profile/(?P<username>[\w\-]+)/', views.account, name='profile'),
    url(r'^match/(?P<matchID>[\w\-]+)/join', views.joinMatch, name='joinMatch'),
    url(r'^team/(?P<teamName>[\w\-]+)/join', views.team, name='joinTeam')
]


