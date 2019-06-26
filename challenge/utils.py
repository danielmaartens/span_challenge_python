import re
import operator
from time import sleep
from team_value import TeamValue

TEAM_RESULT_GROUPING_PATTERN = '^([a-zA-Z\\s]+)([0-9]+$)'


def dictionary_to_team_value_list(team_value_dictionary):
    list = []

    for team, value in team_value_dictionary.items():
        list.append(TeamValue(team, value))

    return list


def dictionary_to_list(team_value_dictionary):
    list = []

    for team, value in team_value_dictionary.items():
        list.append([team, value])

    return list


def list_to_dictionary(team_value_list):
    dictionary = {}

    for team_value in team_value_list:
        dictionary[team_value.getname()] = team_value.getvalue()

    return dictionary


def boolean_from_string(s):
    lower_case = s.split('\n')[0].lower()

    switcher = {
        'y': True,
        'yes': True,
        'c': True,
        'n': False,
        'no': False
    }

    return switcher.get(lower_case, None)


def delayed_print(text, seconds):
    sleep(seconds)
    print(text)


def get_team_result_from_string(result, regex_pattern):
    team_value = None

    r = re.search(regex_pattern, result)
    if r:
        # remove space from end of name
        name = r.group(1)[:-1]
        result = int(r.group(2))
        team_value = TeamValue(name, result)

    return team_value


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


def get_ordered_match_points_from_file(file_path):
    team_match_points = []

    with open(file_path) as f:
        content = f.readlines()

    content = [line.strip() for line in content]

    for line in content:
        match_results = line.split(', ')
        match_outcome = []

        for result in match_results:
            team_value = get_team_result_from_string(result, TEAM_RESULT_GROUPING_PATTERN)

            if team_value is not None:
                match_outcome.append(team_value)

        match_points = calculate_match_points(match_outcome)
        team_match_points.extend(match_points)

    final_team_match_points = reduce_team_match_points(team_match_points)
    final_team_match_points.sort(key=operator.itemgetter(0))
    final_team_match_points.sort(key=operator.itemgetter(1), reverse=True)

    return set_team_rank(final_team_match_points)
