import re
import operator
from time import sleep
from team_value import TeamValue

TEAM_RESULT_GROUPING_PATTERN = '^([a-zA-Z\\s]+)([0-9]+$)'


def dictionary_to_list(team_value_dictionary):
    """
    converts a dictionary to a list for easier processing of data later.

    :param team_value_dictionary:
    :return:
    """
    team_value_list = []

    for team, value in team_value_dictionary.items():
        team_value_list.append([team, value])

    return team_value_list


def list_to_dictionary(team_value_list):
    """
    converts a list to a dictionary for use in tests for easier access of team values with the team names we know.

    :param team_value_list:
    :return:
    """

    dictionary = {}

    for team_value in team_value_list:
        dictionary[team_value.getname()] = team_value.getvalue()

    return dictionary


def boolean_from_string(s):
    """
    converts expected user input for yes/no/continue questions into a boolean value.

    :param s:
    :return:
    """

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
    """
    helper function to print delayed text in the console.
    - it's so that the output isn't printed all at once.
    - the user has time to read each line.

    :param text:
    :param seconds:
    :return:
    """

    sleep(seconds)
    print(text)


def get_team_result_from_string(result, regex_pattern):
    """
    expects a string containing the name of the team followed by a space and then the team's score for that match.
    - e.g. team "GoGetters" with score 10 should have a string as follows: "GoGetters 10".

    - it will then convert this string into a TeamValue object that has a name and value variable.
    - it should also convert the string score into a number.

    :param result:
    :param regex_pattern:
    :return:
    """

    team_value = None

    # use regex pattern to match team names that include spaces
    r = re.search(regex_pattern, result)
    if r:
        # remove the space at the end of the team name
        name = r.group(1)[:-1]
        # convert string value into int type.
        result = int(r.group(2))
        team_value = TeamValue(name, result)

    # return a TeamValue class object
    return team_value


def set_team_ranks(sorted_team_match_points):
    """
    sets the rank value for all teams.
    note: the list must be sorted.

    :param sorted_team_match_points:
    :return:
    """
    ranked_teams = []

    index = 1
    rank = 0
    previous_team_points = None

    for team_match_point in sorted_team_match_points:
        name = team_match_point[0]
        points = team_match_point[1]

        #  only change rank to running index if current points and previous points are different
        #  this is to make sure that teams who have the same points have the same rank.
        if points != previous_team_points:
            rank = index

        team = TeamValue(name, points)
        team.setrank(rank)
        ranked_teams.append(team)

        # set previous points to current points for next iteration check.
        previous_team_points = points
        index += 1

    return ranked_teams


def calculate_match_points(match_results):
    """
    processes a list of the two team scores in a single match
    and returns a new TeamValue object for each team where the value parameter
    represents the points the team received from either Losing/Winning/Drawing the match.

    :param match_results:
    :return:
    """
    match_points = []

    team_a = match_results[0]
    team_b = match_results[1]

    # initialise new TeamValue objects for each team
    # setting initial points to 0
    team_a_name = team_a.getname()
    team_a_goals = team_a.getvalue()
    team_a_points = TeamValue(team_a_name, 0)

    team_b_name = team_b.getname()
    team_b_goals = team_b.getvalue()
    team_b_points = TeamValue(team_b_name, 0)

    # match is a DRAW
    if team_a_goals == team_b_goals:
        team_a_points.setvalue(1)
        team_b_points.setvalue(1)

    # team A WON
    elif team_a_goals > team_b_goals:
        team_a_points.setvalue(3)

    # team B WON
    else:
        team_b_points.setvalue(3)

    # add the new objects to an empty list
    match_points.append(team_a_points)
    match_points.append(team_b_points)

    return match_points


def reduce_team_match_points(all_teams_match_points):
    """
    when this function is called we have a list
    containing each team's match points for all games played.

    we want to reduced that list to one that only has
    one entry for each team, with each new object having it's
    value represent the sum of all match points gained in the league.

    :param all_teams_match_points:
    :return:
    """

    # using of a dictionary here makes it easier to reduce into a single entry per team.
    final_team_points = {}

    for team in all_teams_match_points:
        name = team.getname()
        points = team.getvalue()

        # if the name does not exist in the map, it will be initialised with the value of points.
        # otherwise it will just add this match's points to the previous points value.
        if name in final_team_points:
            next_points_total = final_team_points[name] + points
            final_team_points[name] = next_points_total
        else:
            final_team_points[name] = points

    # convert the dictionary back into a list for better processing later.
    return dictionary_to_list(final_team_points)


def get_league_results(file_path):
    """
    this is the most important function.
    it serves as the parent for most of the other functions within this module.
    it is responsible for reading through the file contents line by line and
    processing the final ranks of teams in the league based on all the matches played.

    :param file_path:
    :return:
    """

    team_match_points = []

    # read file contents
    with open(file_path) as f:
        content = f.readlines()

    # go through each line of the file
    content = [line.strip() for line in content]
    for line in content:
        scores = []

        # each line represents the outcome of a match.
        # each team's own outcome of the match is separated by a ", "
        # which is why we first split the line by ", " to get a match_results list
        # of two strings representing the outcome of each team for the match.
        match_results = line.split(', ')

        # now we loop through the match_results
        for result in match_results:

            # we parse the string into a TeamValue object for easy processing later.
            team_value = get_team_result_from_string(result, TEAM_RESULT_GROUPING_PATTERN)

            # we add this result to a list representing the scores for each team of this match.
            if team_value is not None:
                scores.append(team_value)

        # now that we have an array of TeamValue objects for the match representing each team
        # we can calculate the match points.
        match_points = calculate_match_points(scores)

        # here we concatenate the new match_points array with all previous added match_points.
        # the purpose of this is to have an array of TeamValue objects each representing
        # the points the team gained in a match.
        team_match_points.extend(match_points)

    # now we reduce this array of all our teams' match_points
    # into an array containing a single entry for each team
    # with the value representing the sum of all their match points gained.
    final_team_match_points = reduce_team_match_points(team_match_points)

    # sort final_team_match_points by points DESC, and then by name ASC.
    final_team_match_points.sort(key=operator.itemgetter(0))
    final_team_match_points.sort(key=operator.itemgetter(1), reverse=True)

    # set the team ranks and return the final league results.
    return set_team_ranks(final_team_match_points)
