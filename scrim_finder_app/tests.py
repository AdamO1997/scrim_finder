from django.test import TestCase
from scrim_finder_app.models import Team
from scrim_finder_app.models import User, userProfile
from scrim_finder_app.models import Games
from scrim_finder_app.models import Match
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
        user_profile = userProfile.objects.get_or_create(user=user,)[0]
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
