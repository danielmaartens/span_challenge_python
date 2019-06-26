import unittest
import os
from utils import *
from team_value import TeamValue

team_value = TeamValue('GoGetters', 10)
test_file_path = os.path.abspath('./challenge/resources/input.csv')


class TestTeamValues(unittest.TestCase):

    def test_team_value_getname(self):
        print('\ngetname() should return GoGetters')
        self.assertEqual(team_value.getname(), 'GoGetters')

    def test_team_value_getvalue(self):
        print('\ngetvalue() should return 10 of type int')
        self.assertEqual(team_value.getvalue(), 10)

    def test_team_result_from_string_regex_name(self):
        print('\nRegex should take into account spaces within a team name')
        team_result = get_team_result_from_string('FC Awesome 1', TEAM_RESULT_GROUPING_PATTERN)
        self.assertEqual(team_result.getname(), 'FC Awesome')

    def test_team_result_from_string_regex_value(self):
        print('\nThis function should extract the team\'s score and convert it into a number')
        team_result = get_team_result_from_string('FC Awesome 1', TEAM_RESULT_GROUPING_PATTERN)
        self.assertEqual(team_result.getvalue(), 1)


class TestWinLose(unittest.TestCase):

    def setUp(self):
        team_a_result = TeamValue('A', 1)
        team_b_result = TeamValue('B', 0)
        match_results = [team_a_result, team_b_result]
        match_points = calculate_match_points(match_results)
        match_points_dictionary = list_to_dictionary(match_points)
        self.match_points_dictionary = match_points_dictionary

    def test_match_points_team_a(self):
        print('\nTeam A WON, so they should have 3 points')
        self.assertEqual(self.match_points_dictionary.get('A'), 3)

    def test_match_points_team_b(self):
        print('\nTeam B LOST, so they should have 0 points')
        self.assertEqual(self.match_points_dictionary.get('B'), 0)


class TestDraw(unittest.TestCase):

    def setUp(self):
        team_a_result = TeamValue('A', 1)
        team_b_result = TeamValue('B', 1)
        match_results = [team_a_result, team_b_result]
        match_points = calculate_match_points(match_results)
        match_points_dictionary = list_to_dictionary(match_points)
        self.match_points_dictionary = match_points_dictionary

    def test_match_points(self):
        print('\nIt was a DRAW, so Team A and Team B should have 1 point')
        self.assertEqual(self.match_points_dictionary.get('A'), 1)
        self.assertEqual(self.match_points_dictionary.get('B'), 1)


class TestFinalResult(unittest.TestCase):

    def setUp(self):
        self.final_results = get_league_results(test_file_path)

    def test_first_team_rank(self):
        print('\nThis team should have a rank of 1')
        team = self.final_results[0]
        self.assertEqual(team.getrank(), 1)

    def test_first_team_name(self):
        print('\n1st team should be Tarantulas')
        team = self.final_results[0]
        self.assertEqual(team.getname(), 'Tarantulas')

    def test_first_team_value(self):
        print('\nTarantulas should have 6 pts')
        team = self.final_results[0]
        self.assertEqual(team.getvalue(), 6)

    def test_second_team_rank(self):
        print('\nThis team should have a rank of 2')
        team = self.final_results[1]
        self.assertEqual(team.getrank(), 2)

    def test_second_team_name(self):
        print('\n2nd team should be Lions')
        team = self.final_results[1]
        self.assertEqual(team.getname(), 'Lions')

    def test_second_team_value(self):
        print('\nLions should have 5 pts')
        team = self.final_results[1]
        self.assertEqual(team.getvalue(), 5)

    def test_third_team_rank(self):
        print('\nThis team should have a rank of 3')
        team = self.final_results[2]
        self.assertEqual(team.getrank(), 3)

    def test_third_team_name(self):
        print('\n3rd team should be FC Awesome')
        team = self.final_results[2]
        self.assertEqual(team.getname(), 'FC Awesome')

    def test_third_team_value(self):
        print('\nFC Awesome should have 1 pt')
        team = self.final_results[2]
        self.assertEqual(team.getvalue(), 1)

    def test_fourth_team_rank(self):
        print('\nThis team should have a rank of 3')
        team = self.final_results[3]
        self.assertEqual(team.getrank(), 3)

    def test_fourth_team_name(self):
        print('\n4th team should be Snakes (after FC Awesome)')
        team = self.final_results[3]
        self.assertEqual(team.getname(), 'Snakes')

    def test_fourth_team_value(self):
        print('\nSnakes should have 1 pt')
        team = self.final_results[3]
        self.assertEqual(team.getvalue(), 1)

    def test_fifth_team_rank(self):
        print('\nThis team should have a rank of 5')
        team = self.final_results[4]
        self.assertEqual(team.getrank(), 5)

    def test_fifth_team_name(self):
        print('\n5th team should be Grouches')
        team = self.final_results[4]
        self.assertEqual(team.getname(), 'Grouches')

    def test_fifth_team_value(self):
        print('Grouches should have 0 pts')
        team = self.final_results[4]
        self.assertEqual(team.getvalue(), 0)


unittest.main()
