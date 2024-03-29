import sys
import os.path

from utils import *


def run():
    running = True

    delay = 1.5

    print('\nWelcome to the League Rank Calculator!\n')

    delayed_print('This program will calculate the ranking table for a soccer league.\n', delay)

    delayed_print('The data for the results of the games should be stored in a text file.', delay)

    while running:

        delayed_print('\nPlease provide the full path of the file where your results are stored:\n', delay)

        # read in user input and store it in the file_path variable
        file_path = input('Full File Path: ')

        # does file exist ?
        if os.path.exists(file_path):

            # it does so let's start processing
            # process the file contents and get the league results
            ranked_teams = get_league_results(file_path)

            print('\nRESULTS\n')

            # print out the ranks in a format specified in the challenge.
            for team in ranked_teams:
                print(str(team.getrank()) + '. ' + team.getname() + ', ' + str(team.getvalue()) + (
                    ' pt' if team.getvalue() == 1 else ' pts'))

            user_answer = input('\nWould you like to check match point results of another league ? [y/n]: ')

            user_carry_on = boolean_from_string(user_answer)

            while user_carry_on is None:
                print('\nI do not understand your command, please try again... ')
                user_answer = input('\nWould you like to check match point results of another league ? [y/n]: ')

                user_carry_on = boolean_from_string(user_answer)

            running = user_carry_on

        else:

            user_answer = input('\nSorry, your file does not exist ! Please double-check your file path and try again... Press [c] to continue, or any other key (besides ENTER) to exit...\n')
            running = boolean_from_string(user_answer)
            delay = 0

    print('\nThank you for using the League Rank Calculator !')
    sys.exit()


run()
