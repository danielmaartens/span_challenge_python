import unittest
import os
from utils import *
from team_value import TeamValue

team_value = TeamValue('GoGetters', 10)
test_file_path = os.path.abspath('./resources/input.csv')


class TestTeamValues(unittest.TestCase):

    def test_team_value(self):
        self.assertEqual(team_value.getname(), 'GoGetters')
        self.assertEqual(team_value.getvalue(), 10)

    def test_team_result_from_string(self):
        team_result = get_team_result_from_string('FC Awesome 1', team_result_grouping_pattern)
        self.assertEqual(team_result.getname(), 'FC Awesome')
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
        self.assertEqual(self.match_points_dictionary.get('A'), 3)

    def test_match_points_team_b(self):
        self.assertEqual(self.match_points_dictionary.get('B'), 0)


class TestDraw(unittest.TestCase):

    def setUp(self):
        team_a_result = TeamValue('A', 1)
        team_b_result = TeamValue('B', 1)
        match_results = [team_a_result, team_b_result]
        match_points = calculate_match_points(match_results)
        match_points_dictionary = list_to_dictionary(match_points)
        self.match_points_dictionary = match_points_dictionary

    def test_match_points_team_a(self):
        self.assertEqual(self.match_points_dictionary.get('A'), 1)

    def test_match_points_team_b(self):
        self.assertEqual(self.match_points_dictionary.get('B'), 1)


class TestFinalResult(unittest.TestCase):

    def setUp(self):
        self.final_results = get_ordered_match_points_from_file(test_file_path)

    def test_first_team(self):
        team = self.final_results[0]
        self.assertEqual(team.getname(), 'Tarantulas')
        self.assertEqual(team.getrank(), 1)
        self.assertEqual(team.getvalue(), 6)

    def test_second_team(self):
        team = self.final_results[1]
        self.assertEqual(team.getname(), 'Lions')
        self.assertEqual(team.getrank(), 2)
        self.assertEqual(team.getvalue(), 5)

    def test_third_team(self):
        team = self.final_results[2]
        self.assertEqual(team.getname(), 'FC Awesome')
        self.assertEqual(team.getrank(), 3)
        self.assertEqual(team.getvalue(), 1)

    def test_fourth_team(self):
        team = self.final_results[3]
        self.assertEqual(team.getname(), 'Snakes')
        self.assertEqual(team.getrank(), 3)
        self.assertEqual(team.getvalue(), 1)

    def test_fifth_team(self):
        team = self.final_results[4]
        self.assertEqual(team.getname(), 'Grouches')
        self.assertEqual(team.getrank(), 5)
        self.assertEqual(team.getvalue(), 0)


unittest.main()
