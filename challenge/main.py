import re
import operator
from challenge.team_value import TeamValue
from challenge.utils.convert import dictionary_to_team_value_list, dictionary_to_list

file = "/Users/danielmaartens/personal/span/span_challenge_python/challenge/resources/input.csv"

list = []

dictionary = {}

team_result_grouping_pattern = "^([a-zA-Z\\s]+)([0-9]+$)"

with open(file) as f:
    content = f.readlines()

content = [line.strip() for line in content]


def calculate_match_points(match_results):
    match_points = []

    team_a = match_results[0]
    team_b = match_results[1]

    team_a_name = team_a.getname()
    team_a_goals = team_a.getvalue()
    team_a_points = TeamValue(team_a_name, 0)

    team_b_name = team_b.getname()
    team_b_goals = team_b.getvalue()
    team_b_points = TeamValue(team_b_name, 0)

    if team_a_goals == team_b_goals:
        team_a_points.setvalue(1)
        team_b_points.setvalue(1)
    elif team_a_goals > team_b_goals:
        team_a_points.setvalue(3)
    else:
        team_b_points.setvalue(3)

    match_points.append(team_a_points)
    match_points.append(team_b_points)

    return match_points


def reduce_team_match_points(all_teams_match_points):
    final_team_points = {}

    for team in all_teams_match_points:
        name = team.getname()
        points = team.getvalue()

        if name in final_team_points:
            next_points_total = final_team_points[name] + points
            final_team_points[name] = next_points_total
        else:
            final_team_points[name] = points

    return dictionary_to_list(final_team_points)


def set_team_rank(sorted_team_match_points):
    ranked_teams = []

    index = 1
    rank = 0
    previous_team_points = None

    for team_match_point in sorted_team_match_points:
        name = team_match_point[0]
        points = team_match_point[1]

        if points != previous_team_points:
            rank += 1

        this_team_rank = rank

        if points == previous_team_points:
            rank = index

        team = TeamValue(name, points)
        team.setrank(this_team_rank)
        ranked_teams.append(team)

        previous_team_points = points
        index += 1

    return ranked_teams


def run():
    team_match_points = []

    for x in content:
        y = x.split(', ')
        match_outcome = []
        for xy in y:
            r = re.search(team_result_grouping_pattern, xy)
            if r:
                # remove space from name
                name = r.group(1)[:-1]
                result = int(r.group(2))
                team_value = TeamValue(name, result)
                match_outcome.append(team_value)

        match_points = calculate_match_points(match_outcome)
        team_match_points.extend(match_points)

    final_team_match_points = reduce_team_match_points(team_match_points)

    final_team_match_points.sort(key=operator.itemgetter(0))
    final_team_match_points.sort(key=operator.itemgetter(1), reverse=True)

    ranked_teams = set_team_rank(final_team_match_points)

    for team in ranked_teams:
        print(str(team.getrank()) + '. ' + team.getname() + ', ' + str(team.getvalue()) + (' pt' if team.getvalue() == 1 else ' pts'))
