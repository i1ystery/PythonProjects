from CustomerDAO import *
from ProductDAO import *
from OrderDAO import *
import os
import datetime


def choice(*args):
    for arg in args:
        print(arg)


def start():
    cls()
    print('Shop Database Application')
    print('Choose action: ')
    choice('Insert Product', 'Insert Customer', 'Insert Order', '')


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    pass
