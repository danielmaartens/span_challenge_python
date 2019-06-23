from challenge.team_value import TeamValue


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
