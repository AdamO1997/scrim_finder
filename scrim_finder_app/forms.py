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
        exclude = ('full', 'users', 'slug')

class MatchForm(forms.ModelForm):
    date = forms.DateTimeField(initial="yyyy-mm-dd hh:mm")

    class Meta:
        model = Match
        exclude = ('full', 'teams')



