from view.view import View
from termcolor import colored, cprint
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

menu_options = {
    1: 'Add horse',
    2: 'View One Horse',
    3: 'View All Horses',
    4: 'Update Horse',
    5: 'Delete Horse',
    6: 'Let\'s Race !',
    7: 'View last results',
    8: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key])

def option1():
    cprint('ADD NEW HORSE', 'green', attrs=['bold'])
    view_add_horse = View.add_horse_view()
    for horse in view_add_horse:
        cprint(f'[+] ID: {horse["id"]}||NAME: {horse["name"]}||AGE: {horse["age"]}||WINS: {horse["wins"]} as been add to Database', 'green', attrs=['bold'])

def option2():
    cprint('VIEW ONE HORSE', 'green', attrs=['bold'])
    view_one_horse = View.read_horse_view()
    for horse in view_one_horse:
        cprint(f'[>>>] ID: {horse["id"]}||NAME: {horse["name"]}||AGE: {horse["age"]}||WINS: {horse["wins"]}', 'green', attrs=['bold'])

def option3():
    cprint('VIEW ALL HORSES', 'green', attrs=['bold'])
    view_all_horses = View.read_horses_view()
    for horse in view_all_horses:
        cprint(f'[>>>] ID: {horse["id"]}||NAME: {horse["name"]}||AGE: {horse["age"]}||WINS: {horse["wins"]}', 'green', attrs=['bold'])

def option4():
    cprint('UPDATE HORSE', 'green', attrs=['bold'])
    horse = View.updade_horse_view()
    cprint(f'[+/-] NAME: {horse}|| have been updated', 'green', attrs=['bold'])

def option5():
    cprint('DELETE HORSE', 'green', attrs=['bold'])
    horse = View.delete_horse_view()
    cprint(f'[-] ID: {horse}|| have been deleted', 'red', attrs=['bold'])

def option6():
    cprint('LET\'S RACE !', 'green', attrs=['bold'])
    race = View.start_race_view()
    for r in race: 
        cprint(f'[>>>>>>] HORSE: {r["name"]} have won !', 'green', attrs=['bold'])

def option7():
    cprint('VIEW LAST RESULTS', 'green', attrs=['bold'])
    races = View.last_results_race_view()
    for race in races:
        cprint(f'[>>>] DATE: {race["date"]}|| Name: {race["name"]}|| WINNER HORSE ID: {race["horse_id"]}|| WINNER HORSE NAME: {race["horse_name"]}', 'green', attrs=['bold'])


if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')

        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            option4()
        elif option == 5:
            option5()
        elif option == 6:
            option6()
        elif option == 7:
            option7()
        elif option == 8:
            cprint('Have a nice day !', 'green', attrs=['bold'])
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 6.')