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
	url(r'^account/', views.account, name='account'),
	url(r'^gameList/', views.gameList, name='gameList'),
	url(r'^index/', views.index, name='index'),
	url(r'^matchList/', views.matchList, name='matchList'),
	url(r'^myMatches/', views.myMatches, name='myMatches'),
	url(r'^myTeams/', views.myTeams, name='myTeams'),
	url(r'^teamList/', views.teamList, name='teamList'),
]

"""

Urls to do:

account
gameList
index
matchList
myMatches
myTeams
teamList

"""
