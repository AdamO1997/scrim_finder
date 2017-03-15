from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import datetime

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


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
        game_list = Games.objects
        context_dict = {'teams': team_list, 'matches': match_list, 'games': game_list}


    return render(request, 'scrim_finder/index.html', context_dict)


def account(request, username):

    user= User.objects.get(username = username)
    profile = userProfile.objects.get(user = user)

    context_dict = {'user':username, 'profile': profile}


    return render(request, 'scrim_finder/account.html', context_dict)


@login_required
def myGames(request):

    teams = request.user.teams
    matches = Match.objects.filter()

    context_dict = {'matches': matches}

    return render(request, 'scrim_finder/myGames.html', context_dict)




