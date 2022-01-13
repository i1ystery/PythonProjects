import csv
import pandas as pd
from DBConnection import DBConnection
from IDBTable import IDBTable


class Customer:
    def __init__(self, customer_name: str, customer_lastname: str, city: str, phone_number: str, email: str, money: str, customer_id=None):
        assert isinstance(customer_name, str) and len(customer_name) <= 25, 'Incorrect customer name'
        assert isinstance(customer_name, str) and len(customer_name) <= 25, 'Incorrect customer lastname'
        assert isinstance(city, str) and len(city) <= 25, 'Incorrect city'
        assert phone_number.isnumeric() and 2 < len(phone_number) < 16, 'Incorrect phone number'
        assert isinstance(email, str) and len(email) <= 25, 'Incorrect email'
        try:
            self.money = float(money)
            assert 0 <= self.money < 1.7976931348623157e+308, 'Incorrect product price'
        except ValueError:
            raise AssertionError('Incorrect product price')
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.customer_lastname = customer_lastname
        self.city = city
        self.phone_number = phone_number
        self.email = email
        self.money = money

    def __str__(self):
        return f'ID: {self.customer_id}\nName: {self.customer_name}\nLastname: {self.customer_lastname}\nCity: {self.city}\nPhone number: {self.phone_number}\nEmail: {self.email}\nMoney: {self.money}'


class CustomerDAO(IDBTable):
    def __init__(self):
        self.conn = DBConnection()
        self.auto_commit = True

    def get_all(self):
        """
        Selects all Customers from the database and returns them
        :return: List with Customers Objects
        """
        raw_customers = self.conn.execute_command("SELECT * from Customers").fetchall()
        customers = []
        for raw_customer in raw_customers:
            data = (*raw_customer[1:], raw_customer[0])
            customers.append(Customer(*data))
        return customers

    def get_by_id(self, customer_id):
        """
        Selects customer by given id
        :return: Customer Object
        """
        raw_customer = self.conn.execute_command("SELECT * from Customers where customer_id = ?", customer_id).fetchone()
        data = (*raw_customer[1:], raw_customer[0])
        return Customer(*data)

    def save(self, customer: Customer):
        """
        Inserts new/Updates existing Customer in the DB
        """
        data = [customer.customer_name, customer.customer_lastname, customer.city, customer.phone_number, customer.email, customer.money]
        if customer.customer_id is None:
            self.conn.execute_command("INSERT INTO Customers values (?, ?, ?, ?, ?, ?)", data,
                                      self.auto_commit)
            customer.customer_id = self.conn.execute_command('SELECT TOP(1) customer_id FROM Customers ORDER BY customer_id DESC').fetchone()[0]
        else:
            data.append(customer.customer_id)
            self.conn.execute_command("UPDATE Customers set customer_name = ?,customer_lastname = ?, city = ?, phone_number = ?, email = ?, money = ? where customer_id = ?",
                                      data, self.auto_commit)

    def delete(self, customer: Customer):
        """
        Deletes given Customer from the DB
        """
        self.conn.execute_command("DELETE FROM Customers where customer_id = ?", customer.customer_id, self.auto_commit)

    def send_money_to_customer(self, from_customer: Customer, to_customer: Customer, amount: float):
        """
        Transfers money from customer to customer
        :param from_customer: Customer Object
        :param to_customer: Customer Object
        :param amount: Amount of money to transfer
        """
        try:
            self.auto_commit = False
            assert from_customer.money >= amount, 'You can\'t transfer more that customer have'
            self.conn.execute_command('UPDATE Customers set money = money - ? where customer_id = ?', (amount, from_customer.customer_id))
            self.conn.execute_command('UPDATE Customers set money = money + ? where customer_id = ?', (amount, to_customer.customer_id))
            self.auto_commit = True
        except Exception:
            self.conn.rollback()
            self.auto_commit = True
            raise

    def import_data(self, file_path):
        """
        Imports Customers from given .csv file
        :param file_path: path to .csv file with Customers
        """
        try:
            self.auto_commit = False
            with open(file_path, 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    print(row)
                    self.conn.execute_command('INSERT INTO Customers values (?, ?, ?, ?, ?, ?)', row, self.auto_commit)
            self.conn.commit()
            self.auto_commit = True
        except Exception as e:
            self.conn.rollback()
            self.auto_commit = True
            raise

    def export_data(self, path):
        """
        Exports all rows from Customers in the database as .csv file at the specified path.
        :param path: Path that the .csv file will be saved
        """
        pd.DataFrame(pd.read_sql_query("SELECT * from CustomersExport", self.conn.con)).to_csv(path + '/customers.csv', index=False)

