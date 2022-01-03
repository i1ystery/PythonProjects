# from CustomerDAO import *
# from ProductDAO import *
# from OrderDAO import *
import os
# import datetime


def make_choice(values: list):
    while True:
        choices = dict(enumerate(values))
        for key in choices.keys():
            print(f'{key}) {choices[key]}')
        action = input('Choose action: ')
        if int(action) in choices.keys():
            return choices[key]
        else:
            print('Incorrect choice.')


def start():
    cls()
    print('Shop Database Application')
    print(make_choice(['Insert Product', 'Insert Customer', 'Insert Order']))


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    start()
