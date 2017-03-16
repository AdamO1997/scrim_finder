from forms import *
from models import *
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from datetime import datetime

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def create_team(request):
    form = TeamForm()

    if request.method == 'POST':
        form = TeamForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return index(request)
        else:
            print(form.errors)

    return render(request, 'scrim_finder/createTeam.html', {'form':form})

@login_required
def create_match(request):
    form = MatchForm()

    if request.method == 'POST':
        form = MatchForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return index(request)
        else:
            print(form.errors)

    return render(request, 'scrim_finder/createMatch.html', {'form':form})

@login_required
def edit_match(request, matchID):

    instance = Match.objects.get(matchID = matchID)

    if request.method == 'POST':
        form = MatchForm(request.POST, instance = instance)

        if form.is_valid():
            form.save(commit=True)

            return match(request)
        else:
            print(form.errors)
    else:
        form = MatchForm(instance = instance)

    return render(request, 'scrim_finder/editMatch.html', {'form':form})


@login_required
def edit_team(request, teamName):
    #get team from teamName
    #get list of users from TeamMembers
    #is user in the list?
    if request.user.is_authenticated() :
        instance = Team.objects.get(title=teamName)

        if request.method == 'POST':
            form = TeamForm(request.POST, instance=instance)

            if form.is_valid():
                form.save(commit=True)

                return team(request, teamName)
            else:
                print(form.errors)
        else:
            form = TeamForm(instance=instance)

        return render(request, 'scrim_finder/editTeam.html', {'form': form})


@login_required
def edit_account(request):
    instance = Team.objects.get(title=teamName)

    if request.method == 'POST':
        form = TeamForm(request.POST, instance=instance)

        if form.is_valid():
            form.save(commit=True)

            return team(request, teamName)
        else:
            print(form.errors)
    else:
        form = TeamForm(instance=instance)

    return render(request, 'scrim_finder/editAccount.html', {'form': form})

def team(request, teamName):
    team = Team.objects.get(title = teamName)

    return render(request, 'scrim_finder/team.html', {'team': team})

def match(request, matchID):
    match = Match.objects.get(matchID = matchID)

    return render(request, 'scrim_finder/match.html', {'match': match})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your Scrim Finder account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'scrim_finder/login.html', {})


def register(request):

    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)


        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()

            user.set_password(user.password)
            user.save()


            profile = profile_form.save(commit=False)
            profile.user = user


            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']


            profile.save()


            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:

        user_form = UserForm()
        profile_form = UserProfileForm()


    return render(request,
                  'scrim_finder/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})

def index(request):

    today = datetime.today()
    if request.user.is_authenticated():

    else:
        team_list = Team.objects.order_by('?')[:10]
        match_list = Match.objects.filter(date=today)
        game_list = Games.objects.order
        context_dict = {'teams': team_list, 'matches': match_list, 'games': game_list}


    return render(request, 'scrim_finder/index.html', context_dict)


def account(request, username):

    user= User.objects.get(username = username)
    profile = userProfile.objects.get(user = user)

    context_dict = {'user':username, 'profile': profile}


    return render(request, 'scrim_finder/account.html', context_dict)


@login_required
def myMatches(request):

    teams = request.user.teams
    matches = Match.objects.filter(teamsPlaying__in = teams)

    context_dict = {'matches': matches}

    return render(request, 'scrim_finder/myMatches.html', context_dict)


@login_required
def myTeams(request):

    teams = request.user.teams

    context_dict = {'teams': teams}

    return render(request, 'scrim_finder/myTeams.html', context_dict)


def matchList(request, gameName):
    game = Games.objects.get(game = gameName)
    matches = Match.objects.filter(game = game).order_by('date')
    context_dict = {'matches': matches}

    return render(request, 'scrim_finder/matchList.html', context_dict)


def teamList(request):
    teams = Team.objects.order_by('?')
    context_dict = {'teams': teams}

    return render(request, 'scrim_finder/teamList.html', context_dict)


def gameList(request):
    games = Games.objects.all()
    context_dict = {'games': games}

    return render(request, 'scrim_finder/gameList.html', context_dict)


