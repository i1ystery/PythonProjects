import datetime
import os
import sys
import time
import traceback
import xml.etree.cElementTree as ET
from sys import exc_info
from tkinter.filedialog import askopenfilename, askdirectory
from OrderDAO import *
from ProductDAO import *
from CustomerDAO import *


def make_choice(action: str, values: list):
    """
    Makes user choose one object from values argument
    :param action: Action that user should do
    :param values: List of values from which user must select one
    :return: Selected object from list
    """
    try:
        choices = dict(enumerate(values, 1))
        for key in choices.keys():
            print(f'\033[1;35;40mOption {key})\033[0m\n{choices[key]}\n')
        action = input(f'{action}(option number): ')
        if int(action) in choices.keys():
            return choices[int(action)]
        else:
            raise ValueError
    except ValueError:
        print('Invalid input')
        make_choice(action, values)


def cls():
    """
    Cleans console
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def back_to_menu(from_method):
    """
    Asks user if user want go back to main menu.
    :param from_method: Function to call if user don't want to go back to menu.
    """
    back = make_choice('Done.\nDo you want go back to menu?', ['Yes', 'No'])
    menu() if back == 'Yes' else from_method()


def create_product(product_id=None) -> Product:
    """
    Makes user create new product or existing product.
    If product_id argument is given, makes user to change existing product otherwise creates new product
    :return: Product object
    """
    try:
        cls()
        name = input('Product name: ')
        price = input('Product price (float): ')
        price = float(price)
        a = make_choice('Is your product edible?', ['Yes', 'No'])
        if a == 'Yes':
            is_edible = True
            exp_date = input('Expiration date YYYY-MM-DD: ')
        else:
            is_edible = False
            exp_date = None
        product_category = make_choice('Choose category: ', [e.name for e in ProductCategory])
        product = Product(name, price, is_edible, exp_date, ProductCategory[product_category], product_id)
        return product
    except ValueError:
        print('Incorrect value')
        time.sleep(3)
        crud_product()
    except AssertionError as a:
        print(a)
        time.sleep(3)
        crud_product()


def create_order(existing_order=None):
    """
    Makes user create new order or change existing order.
    :param existing_order: Order object. If given, makes user to change existing order otherwise creates new order.
    :return: Order Object
    """
    try:
        cls()
        customer_dao = CustomerDAO()
        customers = customer_dao.get_all_customers()
        customer = make_choice('Choose customer: ', customers)
        if existing_order is not None:
            date = input('Enter order date and time YYYY-MM-DD HH:MM:SS')
        else:
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        name = input('Order recipient full name: ')
        city = input('City: ')
        address = input('Address: ')
        zip_code = int(input('Zip code: '))
        tracking = input('Tracking code: ')
        order_id = existing_order.order_id if existing_order is not None else None
        order_details = existing_order.order_details if existing_order is not None else list
        order = Order(customer, date, name, city, address, zip_code, tracking, order_id, order_details)
        product_dao = ProductDAO()
        products = product_dao.get_all_products()
        if existing_order is None:
            add_products(products, order)
            a = make_choice('Do you want to remove products from this order?: ', ['Yes', 'No'])
            remove_products(order, order.order_details) if a == 'Yes' else None
        else:
            a = make_choice('Do you want to add products to this order?: ', ['Yes', 'No'])
            add_products(products, order) if a == 'Yes' else None
            a = make_choice('Do you want to remove products from this order?: ', ['Yes', 'No'])
            remove_products(order, order.order_details) if a == 'Yes' else None
        return order
    except AssertionError as a:
        print(a)
        time.sleep(3)
        crud_order()
    except ValueError:
        print('Invalid input value')
        time.sleep(3)
        crud_order()


def create_customer(customer_id=None):
    """
    Makes user create a new or change existing customer
    :param customer_id: If given, makes user to change existing customer otherwise creates new customer
    :return: Customer Object
    """
    try:
        cls()
        name = input('Name: ')
        lastname = input('Lastname: ')
        city = input('City: ')
        phone = int(input('Phone number: '))
        email = input('Email: ')
        money = float(input('Money: '))
        return Customer(name, lastname, city, phone, email, money, customer_id)
    except ValueError:
        print('Incorrect value')
        time.sleep(3)
        crud_product()
    except AssertionError as a:
        print(a)
        time.sleep(3)
        crud_customer()


def crud_product():
    """
    Create Read Update Delete UI for Products.
    """
    cls()
    product_dao = ProductDAO()
    products = product_dao.get_all_products()
    choice = make_choice('Choose action', ['Create product', 'Print all products', 'Update product', 'Delete product', 'Export products', 'Import products', 'Back'])
    if choice == 'Create product':
        product = create_product()
        print(product)
        save = make_choice('Do you want to insert this product to database?', ['Insert', 'Cancel'])
        if save == 'Insert':
            product_dao.save(product)
            back_to_menu(crud_product)
        else:
            crud_product()
    if choice == 'Print all products':
        for product in products:
            print(product)
        back_to_menu(crud_product)
    if choice == 'Update product':
        product = make_choice('Choose product: ', products)
        new_product = create_product(product.product_id)
        product_dao.save(new_product)
        back_to_menu(crud_product)
    if choice == 'Delete product':
        product = make_choice('Choose product: ', products)
        confirm = make_choice('Do you really want to delete product from database?\nAll rows that are connected with this product will be deleted.', ['Yes', 'No'])
        product_dao.delete_product(product) if confirm == 'Yes' else crud_product()
        back_to_menu(crud_product)
    if choice == 'Export products':
        print('Choose folder where do you want to export products')
        path = askdirectory()
        product_dao.export_products(path)
        back_to_menu(crud_product)
    if choice == 'Import products':
        print('Choose csv file with customers')
        path = askopenfilename()
        product_dao.import_products(path)
        back_to_menu(crud_product)
    if choice == 'Back':
        menu()


def crud_customer():
    """
    Create Read Update Delete UI for Customers.
    """
    cls()
    customer_dao = CustomerDAO()
    customers = customer_dao.get_all_customers()
    choice = make_choice('Choose action: ', ['Create customer', 'Print all customers', 'Update customer', 'Delete customer', 'Send money from customer to customer', 'Export customers', 'Import customers', 'Back'])
    if choice == 'Create customer':
        customer = create_customer()
        print(customer)
        save = make_choice('Do you want to insert this customer to database?', ['Insert', 'Cancel'])
        if save == 'Insert':
            customer_dao.save(customer)
            back_to_menu(crud_customer)
        else:
            crud_order()
    if choice == 'Print all customers':
        for customer in customers:
            print(customer)
        back_to_menu(crud_customer)
    if choice == 'Update customer':
        customer = make_choice('Choose customer: ', customers)
        new_customer = create_customer(customer.customer_id)
        customer_dao.save(new_customer)
        back_to_menu(crud_customer)
    if choice == 'Delete customer':
        customer = make_choice('Choose customer: ', customers)
        confirm = make_choice('Do you really want to delete customer from database?\nAll rows that are connected with this customer will be deleted.', ['Yes', 'No'])
        customer_dao.delete_customer(customer) if confirm == 'Yes' else crud_customer()
        back_to_menu(crud_customer)
    if choice == 'Send money from customer to customer':
        from_customer = make_choice('Choose from customer: ', customers)
        to_customer = make_choice('Choose to customer: ', customers)
        money = input('Enter amount of money(float): ')
        assert float(money), 'Amount of money should be float number'
        print(f'Chosen customers: \nFrom customer:{from_customer}\nTo customer{to_customer}\nAmount to transfer: {money}')
        customer_dao.send_money_to_customer(from_customer, to_customer, float(money))
        back_to_menu(crud_customer)
    if choice == 'Export customers':
        print('Choose folder where do you want to export customers')
        path = askdirectory()
        customer_dao.export_customers(path)
        back_to_menu(crud_customer)
    if choice == 'Import customers':
        print('Choose csv file with data')
        path = askopenfilename()
        customer_dao.import_customers(path)
        back_to_menu(crud_customer)
    if choice == 'Back':
        menu()


def crud_order():
    """
    Create Read Update Delete UI for Orders.
    """
    cls()
    order_dao = OrderDAO()
    customer_dao = CustomerDAO()
    product_dao = ProductDAO()
    customers = customer_dao.get_all_customers()
    products = product_dao.get_all_products()
    orders = order_dao.get_all_orders()
    if not customers or not products:
        print("You can't create order when there's no customers or products saved in database.")
        back_to_menu(crud_order)
    choice = make_choice('Choose action: ', ['Create order', 'Print all orders', 'Update order', 'Delete order', 'Export orders', 'Import orders', 'Back'])
    if choice == 'Create order':
        order = create_order()
        save = make_choice('Do you want to insert this order to database?', ['Insert', 'Cancel'])
        if save == 'Insert':
            order_dao.save(order)
            back_to_menu(crud_order)
        else:
            crud_order()
    if choice == 'Print all orders':
        for order in orders:
            print(order)
        back_to_menu(crud_order)
    if choice == 'Update order':
        order = make_choice('Choose order: ', orders)
        new_order = create_order(order)
        order_dao.save(new_order)
        back_to_menu(crud_order)
    if choice == 'Delete order':
        order = make_choice('Choose order: ', orders)
        confirm = make_choice(
            'Do you really want to delete order from database?\nAll rows that are connected with this order will be deleted.',
            ['Yes', 'No'])
        order_dao.delete_order(order) if confirm == 'Yes' else crud_order()
        back_to_menu(crud_order)
    if choice == 'Export orders':
        print('Choose folder where do you want to export orders')
        path = askdirectory()
        order_dao.export_orders(path)
        back_to_menu(crud_order)
    if choice == 'Import orders':
        print('Choose csv file with orders')
        order_path = askopenfilename()
        print('Choose csv file with order details')
        order_details_path = askopenfilename()
        order_dao.import_orders(order_path, order_details_path)
        back_to_menu(crud_order)
    if choice == 'Back':
        menu()


def add_products(products: list[Product], order: Order):
    """
    Adds product to an order specified in args
    :param products: Products to add into order
    :param order: An order to which products are added or removed from it
    """
    try:
        action = "Choose product to add to an order: "
        product = make_choice(action, products)
        quantity = input('Quantity: ')
        quantity = int(quantity)
        order.add_product(product, quantity)
        products.remove(product)
        more = make_choice('Do you want to add another product?', ['Yes', 'No'])
        add_products(products, order) if more == 'Yes' and products else None
    except ValueError:
        print('Invalid quantity value')
        add_products(products, order)


def remove_products(order: Order, order_details: list[OrderDetails]):
    """
    Removes product from an order
    :param order: An order from products are removed.
    :param order_details: Order OrderDetails list
    """
    product = make_choice('Choose product to delete from an order: ', order_details)
    order.remove_product(product)
    order_details.remove(product)
    more = make_choice('Do you want to remove another product?', ['Yes', 'No'])
    remove_products(order, order_details) if more == 'Yes' and order_details else None


def generate_report():
    """
    Prints Aggregate report from DB
    :return:
    """
    cls()
    dao = OrderDAO()
    print(dao.get_report())
    input('Press enter to go back to menu')
    menu()


def log_error(exc_type: type, exc_value, exc_tb: traceback):
    """
    Logs errors into XML file
    :param exc_type: Exception type from sys.exc_info()
    :param exc_value: Exception value from sys.exc_info()
    :param exc_tb: Traceback from sys.exc_info()
    """
    error_time = datetime.today().__str__()
    traceback_str = ''
    for trb in traceback.format_tb(exc_tb):
        traceback_str += trb
    log_path = os.path.abspath(os.path.join(os.getcwd(), '../logs/error.log'))
    if not os.path.exists(log_path):
        os.makedirs(os.path.dirname(log_path), exist_ok=True)
        root = ET.Element("Error_log")
        tree = ET.ElementTree(root)
    else:
        tree = ET.parse(log_path)
    exc = ET.SubElement(tree.getroot(), "Exception")
    ET.SubElement(exc, 'Type').text = exc_type.__name__
    ET.SubElement(exc, 'Value').text = exc_value.__str__()
    ET.SubElement(exc, 'Traceback').text = traceback_str
    ET.SubElement(exc, 'Time').text = error_time
    ET.indent(tree, space="\t", level=0)
    string = ET.tostring(tree.getroot())
    with open(log_path, 'wb') as f:
        f.write(string)
    print(f'\033[1;31;40mUnexpected error.\nError log saved to {log_path}\033[40m')


def menu():
    """
    Main Menu UI
    """
    try:
        cls()
        dao = OrderDAO()
        print('Shop Database Application')
        choice = make_choice('Menu', ['CRUD Product', 'CRUD Customer', 'CRUD Order', 'Generate database report', 'Exit'])
        if choice == 'CRUD Product':
            crud_product()
        if choice == 'CRUD Customer':
            crud_customer()
        if choice == 'CRUD Order':
            crud_order()
        if choice == 'Generate database report':
            generate_report()
        if choice == 'Exit':
            sys.exit()
    except Exception as e:
        exc_type, exc_name, ext_tb = exc_info()
        log_error(exc_type, exc_name, ext_tb)
        time.sleep(3)
        sys.exit()


if __name__ == '__main__':
    menu()
