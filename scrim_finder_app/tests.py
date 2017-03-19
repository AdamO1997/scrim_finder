from django.test import TestCase
from scrim_finder_app.models import Team
from scrim_finder_app.models import User, userProfile
from scrim_finder_app.models import Games
from scrim_finder_app.models import Match

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
        user, user_profile = test_utils.create_user()
        # Check there is only the saved user and its profile in the database
        all_users = User.objects.all()
        self.assertEquals(len(all_users),1)
        all_profiles = userProfile.objects.all()
        self.assertEquals(len(all_profiles),1)
        # Check profile fields were saved correctly
        all_profiles[0].user = user
        all_profiles[0].webstie = user_profile.website

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
