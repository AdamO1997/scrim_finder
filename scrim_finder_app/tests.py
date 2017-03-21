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
        user = test_utils.create_user()
        testUser = userProfile.objects.get_or_create(user = user)[0]
        testUser.save()
        self.assertEquals(testUser.user, userProfile.objects.get(user = user).user)
        
        # Check there is only the saved user and its profile in the database
        #all_users = User.objects.all()
        #self.assertEquals(len(all_users),1)
        #all_profiles = userProfile.objects.all()
        #self.assertEquals(len(all_profiles),1)
        # Check profile fields were saved correctly
        #all_profiles[0].user = user

# Tests of the Games class in models.py
class GameMethodTests(TestCase):
    def test_create_games_for_matches(self):

        ###### Fixed

        #create new game
        fifa_game = Games.objects.get_or_create(game = "Fifa 17", genre="Sports")[0]

        #create new match with the game as the new game
        newMatch = Match(matchID="TestMatch", game=fifa_game)

        #save the new match
        newMatch.save()
        
        # Check to see if it was saved properly
        correct_game = Games.objects.get(game = "Fifa 17")
        self.assertEquals(correct_game,fifa_game)
        self.assertEquals(correct_game.game, "Fifa 17")
        self.assertEquals(correct_game.genre,"Sports")

# Tests of the Match class in models.py
class MatchMethodTests(TestCase):
    def test_create_new_match(self):


        ######## Fixed

        
        # create sample match
        fifa_game = Games.objects.get_or_create(game = "Fifa 17", genre="Sports")[0]
        match = Match(matchID="TestMatch", game = Games.objects.get(game = "Fifa 17"))
        match.save()
        # Check match is in database
        self.assertEquals(match, Match.objects.get(matchID = "TestMatch"))



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
        team = Team.objects.get_or_create(title="TeamGO")[0]
        response = self.client.get(reverse('team', args =(team,)))
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
        response = self.client.get(reverse('account',args=()))
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
        response = self.client.get(reverse('joinMatch', args=(matchID,)))
        self.assertTemplateUsed(response, 'scrim_finder/joinMatch.html')


class UrlLinkTests():
    def test_url_reference_index_page_when_logged(self):
        # Create user and log in
        test_utils.create_user()
        self.client.login(username='testuser', password='test1234')
        # Access index page
        response = self.client.get(reverse('index'))
        # Check links that appear for logged in person
        self.assertIn(reverse('index'), response.content)
        self.assertIn(reverse('logout'), response.content)
        self.assertIn(reverse('account'), response.content)
        self.assertIn(reverse('myGames'), response.content)
        self.assertIn(reverse('myTeams'), response.content)
        self.assertIn(reverse('editMatches'), response.content)
        self.assertIn(reverse('editTeams'), response.content)
        self.assertIn(reverse('gameList'), response.content)
        self.assertIn(reverse('teamList'), response.content)
        self.assertIn(reverse('editAccount'), response.content)

    def test_url_reference_index_page_not_logged(self):
        # Access index page
        response = self.client.get(reverse('index'))
        # Check links that appear for not logged in person
        self.assertIn(reverse('index'), response.content)
        self.assertIn(reverse('login'), response.content)
        self.assertIn(reverse('register'), response.content)
        self.assertIn(reverse('gameList'), response.content)
        self.assertIn(reverse('teamList'), response.content)
