from django import forms
from django.contrib.auth.models import User
from scrim_finder_app.models import userProfile, Team, Match

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = userProfile
        fields = ('picture',)

class TeamForm(forms.ModelForm):

    class Meta:
        model = Team
        exclude = ('full',)

class MatchForm(forms.ModelForm):

    class Meta:
        model = Match
        exclude = ('teamsPlaying',)


    
