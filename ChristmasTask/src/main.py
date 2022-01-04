# from CustomerDAO import *
from ProductDAO import *
# from OrderDAO import *
import os
# import datetime


def make_choice(question: str, values: list):
    while True:
        print(question)
        choices = dict(enumerate(values, 1))
        for key in choices.keys():
            print(f'Option {key})\n{choices[key]}')
        action = input('Choose option number: ')
        if int(action) in choices.keys():
            return choices[key]
        else:
            print('Incorrect choice.')


def crud_product():
    choice = make_choice('Choose action', ['Create product', 'Get product by name', 'Update product', 'Delete product'])
    if choice == 'Create product':
        name = input('Product name: ')
        price = input('Product price (float)')
        a = make_choice('Is your product edible?', ['Yes', 'No'])
        is_edible = True if a == 'Yes' else False
        exp_date = input('Expiration date YYYY-MM-DD')
        product_category = make_choice([e.value for e in ProductCategory])
        product = Product(name, product_category, is_edible, exp_date, product_category)
        print(product)
        print('Do you want to insert this product to database?', ['Insert', 'Cancel'])


def start():
    cls()
    print('Shop Database Application')
    print('Choose action:')
    choice = make_choice(['CRUD Product', 'CRUD Customer', 'CRUD Order'])
    if choice == 'CRUD Product':
        pass


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    start()
