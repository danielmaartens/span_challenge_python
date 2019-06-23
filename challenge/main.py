import sys

from challenge.utils import *


def run():
    running = True

    delay = 1.5

    print('\nWelcome to the Match Point Calculator !\n')

    delayed_print('This program will calculate the ranking table for a soccer league.\n', delay)

    delayed_print('The data for the results of the games should be stored in a text file.', delay)

    while running:

        delayed_print('\nPlease provide the full path of the file where your results are stored:\n', delay)

        file_path = input('Full File Path: ')

        ranked_teams = get_ordered_match_points_from_file(file_path)

        print('\nRESULTS\n')

        for team in ranked_teams:
            print(str(team.getrank()) + '. ' + team.getname() + ', ' + str(team.getvalue()) + (
                ' pt' if team.getvalue() == 1 else ' pts'))

        user_carry_on = input('\nWould you like to check match point results of another league ? [Y/N]: ')

        running = boolean_from_string(user_carry_on)

    print('\nThank you for using the Match Point Calculator !')
    sys.exit()
