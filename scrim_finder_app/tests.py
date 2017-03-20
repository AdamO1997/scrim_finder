from django.test import TestCase
from scrim_finder_app.models import Team
from scrim_finder_app.models import User, userProfile
from scrim_finder_app.models import Games
from scrim_finder_app.models import Match
from django.core.urlresolvers import reverse
import test_utils

# Tests of the team class in models.py
class TeamMethodTests(TestCase):
    def test_create_new_team(self):
        team = Team(title="TestTeam")
        team.save()
        # Check team is in database
        team_in_database = Team.objects.all()
        self.assertEquals(len(team_in_database),1)
        only_team_in_database = team_in_database[0]
        self.assertEquals(only_team_in_database, team)

# Tests of the userProfile class in models.py
class userProfileMethodTests(TestCase):
    def test_user_profile_model(self):
        # Create a user
        test_utils.create_user()
        user_profile = userProfile.objects.get_or_create(user=User,)[0]
        user_profile.save()
        # Check there is only the saved user and its profile in the database
        all_users = User.objects.all()
        self.assertEquals(len(all_users),1)
        all_profiles = userProfile.objects.all()
        self.assertEquals(len(all_profiles),1)
        # Check profile fields were saved correctly
        all_profiles[0].user = user

# Tests of the Games class in models.py
class GameMethodTests(TestCase):
    def test_create_games_for_matches(self):
        newMatch = Match(matchID="TestMatch")
        newMatch.save()
        # Create game for match
        fifa_game = Game()
        fifa_game.match = newMatch
        fifa_game.game = "Fifa 17"
        fifa_game.genre = "Sports"
        # Check to see if it was saved
        games = newMatch.game_set.all()
        self.assertEquals(games.count(),1)
        # Check to see if it was saved properly
        correct_game = games[0]
        self.assertEquals(correct_game,fifa_game)
        self.assertEquals(correct_game.game, "Fifa 17")
        self.assertEquals(correct_game.genre,"Sports")

# Tests of the Match class in models.py
class MatchMethodTests(TestCase):
    def test_create_new_match(self):
        match = Match(matchID="TestMatch")
        match.save()
        # Check match is in database
        match_in_database = Match.objects.all()
        self.assertEquals(len(match_in_database),1)
        only_match_in_database = match_in_database[0]
        self.assertEquals(only_match_in_database, match)



# Tests of the login view
class LoginViewTests(TestCase):
    def test_login_redirects_to_index(self):
        # Create User
        test_utils.create_user()
        # Access login page via POST with user data
        try:
            response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'test1234'})
        except:
                return False
        # Check it redirects to index
        self.assertRedirects(response, reverse('index'))

    def test_incorrect_login_provides_error_message(self):
        # Access login page with incorrect user data
        try:
            response = self.client.post(reverse('login'), {'username': 'wronguser', 'password': 'wrongpass'})
        except:
            return False
        print response.content
        try:
            self.assertIn('wronguser', response.content)
        except:
            self.assertIn('Invalid login details supplied.', response.content)

    #def test_login_form_is_displayed_correctly(self):



# Tests of the logout view
#class LogoutViewTests(TestCase):
    #def test_logout_redirects_to_index(self):

#Test ideas
#player has no matches message
#player has no team message
#player tries to create a match in the past
#test to see if all views use a template, and template exists

class ViewsUsingTemplateTests(TestCase):
    def test_index_using_template(self):
        response = self.client.get(reverse('index'))
        # Check the template used to render index page
        self.assertTemplateUsed(response, 'scrim_finder/index.html')

    def test_create_team_using_template(self):
        response = self.client.get(reverse('createTeam'))
        self.assertTemplateUsed(response, 'scrim_finder/createTeam.html')

    def test_create_match_using_template(self):
        response = self.client.get(reverse('createMatch'))
        self.assertTemplateUsed(response, 'scrim_finder/createMatch.html')

    def test_edit_match_using_template(self):
        response = self.client.get(reverse('editMatch'))
        self.assertTemplateUsed(response, 'scrim_finder/editMatch.html')

    def test_edit_team_using_template(self):
        response = self.client.get(reverse('editTeam'))
        self.assertTemplateUsed(response, 'scrim_finder/editTeam.html')

    def test_edit_account_using_template(self):
        response = self.client.get(reverse('editAccount'))
        self.assertTemplateUsed(response, 'scrim_finder/editAccount.html')

    def test_team_using_template(self):
        response = self.client.get(reverse('team'))
        self.assertTemplateUsed(response, 'scrim_finder/team.html')

    def test_match_using_template(self):
        response = self.client.get(reverse('match'))
        self.assertTemplateUsed(response, 'scrim_finder/match.html')

    def test_user_login_using_template(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'scrim_finder/login.html')

    def test_register_using_template(self):
        response = self.client.get(reverse('register'))
        self.assertTemplateUsed(response, 'scrim_finder/register.html')

    def test_account_using_template(self):
        user = test_utils.create_user()
        self.client.login(username='testuser', password='test1234')
        response = self.client.get(reverse('account',args=['testuser']))
        self.assertTemplateUsed(response, 'scrim_finder/account.html')

    def test_myMatches_using_template(self):
        response = self.client.get(reverse('myMatches'))
        self.assertTemplateUsed(response, 'scrim_finder/myMatches.html')

    def test_myTeams_using_template(self):
        response = self.client.get(reverse('myTeams'))
        self.assertTemplateUsed(response, 'scrim_finder/myTeams.html')

    def test_matchList_using_template(self):
        response = self.client.get(reverse('matchList'))
        self.assertTemplateUsed(response, 'scrim_finder/matchList.html')

    def test_teamList_using_template(self):
        response = self.client.get(reverse('teamList'))
        self.assertTemplateUsed(response, 'scrim_finder/teamList.html')

    def test_gameList_using_template(self):
        response = self.client.get(reverse('gameList'))
        self.assertTemplateUsed(response, 'scrim_finder/gameList.html')

    def test_joinTeam_using_template(self):
        response = self.client.get(reverse('joinTeam'))
        self.assertTemplateUsed(response, 'scrim_finder/joinTeam.html')

    def test_joinMatch_using_template(self):
        matchID = "DTA198372"
        response = self.client.get(reverse('joinMatch', args=[matchID]))
        self.assertTemplateUsed(response, 'scrim_finder/joinMatch.html')

