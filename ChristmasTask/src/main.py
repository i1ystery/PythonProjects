import datetime
import os
import sys
import time
import traceback
import xml.etree.cElementTree as ET
from sys import exc_info
from tkinter.filedialog import askopenfilename, askdirectory

from pyodbc import ProgrammingError

from OrderDAO import *
from ProductDAO import *
from CustomerDAO import *
from Command import *


def back_to_menu():
    """
    Returns user back to the main menu
    """
    input('\033[1;35;40mPress ENTER to go back to menu\033[0m')
    menu()


back = Command('Back to main menu', back_to_menu)   # Back command


def make_choice(action: str, values: list):
    """
    Makes user choose one value from given values list
    :param action: Action that user should do
    :param values: List of values from which user must select one
    :return: Selected object from list
    """
    try:
        choices = dict(enumerate(values, 1))
        for key in choices.keys():
            print(f'\033[1;35;40mOption {key}) \033[0m{choices[key]}')
        action = input(f'{action} (option number): ')
        if int(action) in choices.keys():
            return choices[int(action)]
        else:
            raise ValueError
    except ValueError as e:
        print(e)
        print('Invalid input')
        make_choice(action, values)


def cls():
    """
    Clears console
    """
    os.system('cls' if os.name == 'nt' else 'clear')


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


def create_product():
    product = make_product()
    print(product)
    save = make_choice('Do you want to insert this product to database?', ['Insert', 'Cancel'])
    if save == 'Insert':
        product_dao = ProductDAO()
        product_dao.save(product)
    back_to_menu()


def make_product(product_id=None) -> Product:
    """
    Makes user create new product or existing product.
    If product_id argument is given, makes user to change existing product otherwise creates new product
    """
    try:
        cls()
        name = input('Product name: ')
        price = input('Product price (float): ')
        a = make_choice('Is your product edible?', ['Yes', 'No'])
        if a == 'Yes':
            is_edible = True
            exp_date = input('Expiration date YYYY-MM-DD: ')
        else:
            is_edible = False
            exp_date = None
        product_category = make_choice('Choose category: ', [e.name for e in ProductCategory])
        return Product(name, price, is_edible, exp_date, ProductCategory[product_category], product_id)
    except AssertionError as a:
        print(a)
        time.sleep(3)
        choose_create()


def create_order():
    order = make_order()
    print(order)
    save = make_choice('Do you want to insert this order to database?', ['Insert', 'Cancel'])
    if save == 'Insert':
        order_dao = OrderDAO()
        order_dao.save(order)
    back_to_menu()


def make_order(existing_order=None) -> Order:
    """
    Makes user create new order or change existing order.
    :param existing_order: Order object. If given, makes user to change existing order otherwise creates new order.
    """
    try:
        cls()
        customer_dao = CustomerDAO()
        customers = customer_dao.get_all()
        customer = make_choice('Choose customer: ', customers)
        if existing_order is not None:
            date = input('Enter order date and time YYYY-MM-DD HH:MM:SS')
        else:
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        name = input('Order recipient full name: ')
        city = input('City: ')
        address = input('Address: ')
        zip_code = input('Zip code: ')
        tracking = input('Tracking code: ')
        order_id = existing_order.order_id if existing_order is not None else None
        order_details = existing_order.order_details if existing_order is not None else None
        order = Order(customer, date, name, city, address, zip_code, tracking, order_id, order_details)
        product_dao = ProductDAO()
        products = product_dao.get_all()
        if not existing_order:
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
        print(a.__context__)
        time.sleep(3)
        choose_create()


def create_customer():
    customer = make_customer()
    print(customer)
    save = make_choice('Do you want to insert this customer to database?', ['Insert', 'Cancel'])
    if save == 'Insert':
        customer_dao = CustomerDAO()
        customer_dao.save(customer)
    back_to_menu()


def make_customer(customer_id=None) -> Customer:
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
        phone = input('Phone number: ')
        email = input('Email: ')
        money = input('Money: ')
        return Customer(name, lastname, city, phone, email, money, customer_id)
    except AssertionError as a:
        print(a.__context__)
        time.sleep(3)
        choose_create()


def print_products():
    product_dao = ProductDAO()
    products = product_dao.get_all()
    for product in products:
        print(product)
    back_to_menu()


def print_customers():
    customer_dao = CustomerDAO()
    customers = customer_dao.get_all()
    for customer in customers:
        print(customer)
    back_to_menu()


def print_orders():
    order_dao = OrderDAO()
    orders = order_dao.get_all()
    for order in orders:
        print(order)
    back_to_menu()


def update_product():
    product_dao = ProductDAO()
    products = product_dao.get_all()
    product = make_choice('Choose product: ', products)
    new_product = make_product(product.product_id)
    product_dao.save(new_product)
    back_to_menu()


def update_customer():
    customer_dao = CustomerDAO()
    customers = customer_dao.get_all()
    customer = make_choice('Choose customer: ', customers)
    new_customer = make_customer(customer.customer_id)
    customer_dao.save(new_customer)
    back_to_menu()


def update_order():
    order_dao = OrderDAO()
    orders = order_dao.get_all()
    order = make_choice('Choose order: ', orders)
    new_order = make_order(order)
    order_dao.save(new_order)
    back_to_menu()


def delete_product():
    product_dao = ProductDAO()
    products = product_dao.get_all()
    product = make_choice('Choose product: ', products)
    confirm = make_choice(
        'Do you really want to delete product from database?\nAll rows that are connected with this product will be deleted.',
        ['Yes', 'No'])
    product_dao.delete(product) if confirm == 'Yes' else choose_delete()
    back_to_menu()


def delete_customer():
    customer_dao = CustomerDAO()
    customers = customer_dao.get_all()
    customer = make_choice('Choose customer: ', customers)
    confirm = make_choice(
        'Do you really want to delete customer from database?\nAll rows that are connected with this customer will be deleted.',
        ['Yes', 'No'])
    customer_dao.delete(customer) if confirm == 'Yes' else choose_delete()
    back_to_menu()


def delete_order():
    order_dao = OrderDAO()
    orders = order_dao.get_all()
    order = make_choice('Choose order: ', orders)
    confirm = make_choice(
        'Do you really want to delete order from database?\nAll rows that are connected with this order will be deleted.',
        ['Yes', 'No'])
    order_dao.delete(order) if confirm == 'Yes' else choose_delete()
    back_to_menu()


def export_products():
    product_dao = ProductDAO()
    print('Choose folder where do you want to export products')
    path = askdirectory()
    product_dao.export_data(path)
    back_to_menu()


def export_customers():
    customer_dao = CustomerDAO()
    print('Choose folder where do you want to export customers')
    path = askdirectory()
    customer_dao.export_data(path)
    back_to_menu()


def export_orders():
    order_dao = OrderDAO()
    print('Choose folder where do you want to export orders')
    path = askdirectory()
    order_dao.export_data(path)
    back_to_menu()


def import_products():
    try:
        product_dao = ProductDAO()
        print('Choose csv file with products')
        path = askopenfilename(title='Choose products.csv', initialdir=os.getcwd(), filetypes=[("csv files", "*.csv")])
        product_dao.import_data(path)
        back_to_menu()
    except ProgrammingError:
        print('Invalid csv file')
        choose_import()


def import_customers():
    try:
        customer_dao = CustomerDAO()
        print('Choose csv file with customers')
        path = askopenfilename(title='Choose customers.csv', initialdir=os.getcwd(), filetypes=[("csv files", "*.csv")])
        customer_dao.import_data(path)
        back_to_menu()
    except ProgrammingError:
        print('Invalid csv file')
        choose_import()


def import_orders():
    order_dao = OrderDAO()
    try:
        print('Choose csv file with orders')
        order_path = askopenfilename(title='Choose orders.csv', initialdir=os.getcwd(),
                                     filetypes=[("csv files", "*.csv")])
        print('Choose csv file with order details')
        order_details_path = askopenfilename(title='Choose order_details.csv', initialdir=os.getcwd(),
                                             filetypes=[("csv files", "*.csv")])
        order_dao.import_data(order_path, order_details_path)
        back_to_menu()
    except ProgrammingError:
        print('Invalid csv file')
        choose_import()


def transfer_money():
    customer_dao = CustomerDAO()
    customers = customer_dao.get_all()
    from_customer = make_choice('Choose from customer: ', customers)
    to_customer = make_choice('Choose to customer: ', customers)
    money = input('Enter amount of money(float): ')
    assert float(money), 'Amount of money should be float number'
    print(f'Chosen customers: \nFrom customer:{from_customer}\nTo customer{to_customer}\nAmount to transfer: {money}')
    customer_dao.send_money_to_customer(from_customer, to_customer, float(money))
    back_to_menu()


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
    #order_details.remove(product)
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


def choose_create():
    create_p = Command('Create Product Row', create_product)
    create_c = Command('Create Customer Row', create_customer)
    create_o = Command('Create Order Row', create_order)
    commands = [create_p, create_c, create_o, back]
    choose_command(commands)


def choose_print():
    print_p = Command('Print Products', print_products)
    print_c = Command('Print Customers', print_customers)
    print_o = Command('Print Orders', print_orders)
    commands = [print_p, print_c, print_o, back]
    choose_command(commands)


def choose_update():
    update_p = Command('Update Product Row', update_product)
    update_c = Command('Update Customer Row', update_customer)
    update_o = Command('Update Order Row', update_order)
    commands = [update_p, update_c, update_o, back]
    choose_command(commands)


def choose_delete():
    delete_p = Command('Delete Product Row', delete_product)
    delete_c = Command('Delete Customer Row', delete_customer)
    delete_o = Command('Delete Order Row', delete_order)
    commands = [delete_p, delete_c, delete_o, back]
    choose_command(commands)


def choose_import():
    import_p = Command('Import Product Table Rows', import_products)
    import_c = Command('Import Customer Table Rows', import_customers)
    import_o = Command('Import Order Table Rows', import_orders)
    commands = [import_p, import_c, import_o, back]
    choose_command(commands)


def choose_export():
    export_p = Command('Export Product Table Rows', export_products)
    export_c = Command('Export Customer Table Rows', export_customers)
    export_o = Command('Export Order Table Rows', export_orders)
    commands = [export_p, export_c, export_o, back]
    choose_command(commands)


def choose_other_func():
    other_f_1 = Command('Transfer money from customer to another customer', transfer_money)
    other_f_2 = Command('Generate Aggregate Database Report', generate_report)
    commands = [other_f_1, other_f_2, back]
    choose_command(commands)


def choose_command(commands: list[Command]):
    cls()
    try:
        choices = dict(enumerate(commands, 1))
        for key in choices.keys():
            print(f'\033[1;35;40m[{key}] {choices[key].command_name}\033[0m\n')
        action = input(f'Choose option: ')
        if int(action) in choices.keys():
            choices[int(action)].method()
        else:
            raise ValueError
    except ValueError as e:
        print(e)
        print('Invalid input')
        choose_command(commands)


def menu():
    """
    Main Menu UI
    """
    try:
        cls()
        dao = OrderDAO()
        print('Shop Database Application')
        create_r = Command('Create Table Row', choose_create)
        print_r = Command('Print Table Rows', choose_print)
        update_r = Command('Update Table Row', choose_update)
        delete_r = Command('Delete Table Row', choose_delete)
        import_r = Command('Import Table Rows', choose_import)
        export_r = Command('Export Table Rows', choose_export)
        other_f = Command('Other Functions', choose_other_func)
        exit_p = Command('Exit', sys.exit)
        commands = [create_r, print_r, update_r, delete_r, import_r, export_r, other_f, exit_p]
        choose_command(commands)
    except Exception as e:
        exc_type, exc_name, ext_tb = exc_info()
        log_error(exc_type, exc_name, ext_tb)
        time.sleep(3)
        sys.exit()


if __name__ == '__main__':
    menu()
