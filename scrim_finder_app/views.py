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
            profile = userProfile.objects.get(user = request.user)
            form.save(commit=True)
            data = form.cleaned_data
            title = data['title']
            team = Team.objects.get(title = title)
            team.users.add(profile)
            profile.teams.add(team)
            return index(request)
        else:
            print(form.errors)

    return render(request, 'scrim_finder/createTeam.html', {'form':form})

@login_required
def create_match(request):
    form = MatchForm()
    profile = userProfile.objects.get(user = request.user)
    teams = profile.teams.all()
    if request.method == 'POST':
        form = MatchForm(request.POST)
        joiningTeamName = request.POST.get('joiningTeam')
        joiningTeam = Team.objects.get(slug=joiningTeamName)
        if form.is_valid():
            form.save(commit=True)
            data = form.cleaned_data
            matchID = data['matchID']
            match = Match.objects.get(matchID = matchID)
            match.teams.add(joiningTeam)
            return index(request)
        else:
            print(form.errors)

    return render(request, 'scrim_finder/createMatch.html', {'form':form, 'teams':teams})

@login_required
def edit_match(request, matchID):

    if request.user.is_authenticated():
        profile = userProfile.objects.get(user = request.user)
        teams = profile.teams.all()
        matchToEdit = Match.objects.get(matchID = matchID)
        teamsPlaying = matchToEdit.teams.all()
        inMatch = False;

        for team1 in teams:
            for team2 in teamsPlaying:
                if team1 == team2:
                    inMatch = True;
                    break;

        if inMatch:
            if request.method == 'POST':
                form = MatchForm(request.POST, instance = matchToEdit)

                if form.is_valid():
                    form.save(commit=True)

                    return match(request, matchID)
                else:
                    print(form.errors)
            else:
                form = MatchForm(instance = matchToEdit)

            return render(request, 'scrim_finder/editMatch.html', {'form':form, 'match':matchID})

        else:
            return HttpResponse('You are not playing in this match')
    else:
        return HttpResponse('You must be logged in to view this page')

@login_required
def edit_team(request, teamSlug):

    if request.user.is_authenticated():
        inTeam = False
        user = request.user
        profile = userProfile.objects.get(user = user)
        teams = profile.teams.all()
        instance = Team.objects.get(slug=teamSlug)
        for currentTeam in teams:
            if instance == currentTeam:
                inTeam = True

        if inTeam:
            if request.method == 'POST':
                form = TeamForm(request.POST, instance=instance)

                if form.is_valid():
                    form.save(commit=True)

                    return team(request, teamSlug)
                else:
                    print(form.errors)
            else:
                form = TeamForm(instance=instance)

            return render(request, 'scrim_finder/editTeam.html', {'form': form, 'team':teamSlug})

        else:
            return HttpResponse('You are not on this team')
    else:
        return HttpResponse('You must be logged in to view this page')

@login_required
def edit_account(request):
    if request.user.is_authenticated():
        user = request.user
        userProfileInstance = userProfile.objects.get(user = user)

        if request.method == 'POST':
            userForm = UserForm(request.POST, instance=user)
            userProfileForm = UserProfileForm(request.POST, instance = userProfileInstance)

            if userForm.is_valid() and userProfileForm.is_valid():
                userForm.save(commit=True)
                userProfileForm.save(commit=True)

                return account(request, request.user.username)
            else:
                print(userForm.errors)
                print(userProfileForm.errors)
        else:
            userForm = UserForm(instance=user)
            userProfileForm = UserProfileForm(instance=userProfileInstance)

        return render(request, 'scrim_finder/editAccount.html', {'userForm': userForm, 'userProfileForm': userProfileForm})

    else:
        return HttpResponse('You must be logged in to view this page')

def team(request, teamSlug):
    team = Team.objects.get(slug = teamSlug)
    players = team.users.all()
    notInTeam = True
    if request.user.is_authenticated():
        profile = userProfile.objects.get(user = request.user)
        for player in players:
            if player == profile:
                notInTeam = False
                break;

    return render(request, 'scrim_finder/team.html', {'team': team, 'players': players, 'notInTeam':notInTeam})

def match(request, matchID):
    match = Match.objects.get(matchID = matchID)
    teams = match.teams.all()
    notInMatch = True
    if request.user.is_authenticated() and match.full:
        profile = userProfile.objects.get(user=request.user)
        userTeams = profile.teams.all()
        for team in teams:
            for userTeam in userTeams:
                if  team == userTeam:
                    notInMatch = False
                    break;

    return render(request, 'scrim_finder/match.html', {'match': match, 'teams': teams, 'notInMatch': notInMatch})


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


    team_list = Team.objects.order_by('?')[:10]
    match_list = Match.objects.filter(date=today).order_by('?')[:10]
    game_list = Games.objects.order_by('?')
    context_dict = {'teams': team_list, 'matches': match_list, 'games': game_list}


    return render(request, 'scrim_finder/index.html', context_dict)


def account(request, username):


    userExists= User.objects.filter(username = username).exists()

    if userExists:
        userToView = User.objects.filter(username= username)
        profile = userProfile.objects.get(user = userToView)
        teams = profile.teams.all()

        context_dict = {'username':username, 'profile': profile, 'teams': teams}
        return render(request, 'scrim_finder/account.html', context_dict)
    else:
        return HttpResponse('User does not exist')

@login_required
def myMatches(request):

    account = userProfile.objects.get(user = request.user)
    teams = account.teams.all()

    matches = Match.objects.filter(teams__in = teams)

    context_dict = {'matches': matches}

    return render(request, 'scrim_finder/myMatches.html', context_dict)


@login_required
def myTeams(request):

    user = request.user
    account = userProfile.objects.get(user=user)
    userTeams = account.teams.all()


    context_dict = {'teams': userTeams}

    return render(request, 'scrim_finder/myTeams.html', context_dict)


def matchList(request, gameSlug):
    game = Games.objects.get(slug = gameSlug)
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


@login_required
def joinTeam(request, teamSlug):
    teamToJoin = Team.objects.get(slug=teamSlug)
    locked = teamToJoin.passRequired
    joiningPlayer = userProfile.objects.get(user = request.user)


    if locked:
        if request.method == 'POST':
            password = request.POST.get('password')

            if teamToJoin.password == password:
                teamToJoin.users.add(joiningPlayer)
                joiningPlayer.teams.add(teamToJoin)

                return team(request, teamSlug)
            else:
                return HttpResponse("Invalid password")
        else:
            return render(request, 'scrim_finder/joinTeam.html', {'team': teamToJoin})

    else:
        teamToJoin.users.add(joiningPlayer)
        joiningPlayer.teams.add(teamToJoin)

        return team(request, teamSlug)


@login_required
def joinMatch(request, matchID):

    matchToJoin = Match.objects.get(matchID=matchID)
    full = matchToJoin.full
    currentUser = userProfile.objects.get(user=request.user)

    if not full:
        locked = matchToJoin.passRequired

        if request.method == 'POST':

            joiningTeamName = request.POST.get('joiningTeam')
            joiningTeam = Team.objects.get(slug=joiningTeamName)
            if locked:
                password = request.POST.get('password')
                if matchToJoin.password == password:
                    matchToJoin.teams.add(joiningTeam)
                    matchToJoin.full = True
                    matchToJoin.save()
                    return match(request, matchID)
                else:
                    return HttpResponse("Invalid password")
            else:
                matchToJoin.teams.add(joiningTeam)
                matchToJoin.full = True
                matchToJoin.save()
                return match(request, matchID)
        else:
            return render(request, 'scrim_finder/joinMatch.html', {'teams': currentUser.teams.all(), 'locked': locked, 'match':matchToJoin})

    else:
        return HttpResponse("Match is already full")


def game(request, gameSlug):
    game = Games.objects.get(slug = gameSlug)

    return render(request, 'scrim_finder/game.html', {'game': game})