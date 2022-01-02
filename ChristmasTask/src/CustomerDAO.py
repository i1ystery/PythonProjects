import pandas as pd
from DBConnection import DBConnection
import csv


class Customer:
    def __init__(self, customer_name, customer_lastname, city, phone_number, email, money, customer_id=None):
        assert isinstance(customer_name, str) and len(customer_name) <= 25
        assert isinstance(customer_name, str) and len(customer_name) <= 25
        assert isinstance(city, str) and len(city) <= 25
        assert isinstance(phone_number, int)
        assert isinstance(email, str) and len(email) <= 25
        assert isinstance(money, float)
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.customer_lastname = customer_lastname
        self.city = city
        self.phone_number = phone_number
        self.email = email
        self.money = money

    def __str__(self):
        return f'ID: {self.customer_id}\nName: {self.customer_name}\nLastname: {self.customer_lastname}\nCity: {self.city}\nPhone number: {self.phone_number}\nEmail: {self.email}\nMoney: {self.money}'


class CustomerDAO(object):
    def __init__(self):
        self.conn = DBConnection()
        self.auto_commit = True

    def get_all_customers(self):
        raw_customers = self.conn.execute_command("SELECT * from Customers").fetchall()
        customers = []
        for raw_customer in raw_customers:
            data = (*raw_customer[1:], raw_customer[0])
            customers.append(Customer(*data))
        return customers

    def get_customer_by_id(self, customer_id):
        raw_customer = self.conn.execute_command("SELECT * from Customers where customer_id = ?", customer_id).fetchone()
        data = (*raw_customer[1:], raw_customer[0])
        return Customer(*data)

    def get_customer_by_fullname(self, name, lastname):
        raw_customer = self.conn.execute_command("SELECT * from Customers where customer_name = ? and customer_lastname = ?", (name, lastname)).fetchone()
        data = (*raw_customer[1:], raw_customer[0])
        return Customer(*data)

    def save(self, customer: Customer):
        data = [customer.customer_name, customer.customer_lastname, customer.city, customer.phone_number, customer.email, customer.money]
        if customer.customer_id is None:
            self.conn.execute_command("INSERT INTO Customers values (?, ?, ?, ?, ?, ?)", data,
                                      self.auto_commit)
            customer.customer_id = self.conn.execute_command('SELECT TOP(1) customer_id FROM Customers ORDER BY customer_id DESC').fetchone()[0]
        else:
            data.append(customer.customer_id)
            self.conn.execute_command("UPDATE Customers set customer_name = ?,customer_lastname = ?, city = ?, phone_number = ?, email = ?, money = ? where customer_id = ?",
                                      data, self.auto_commit)

    def delete_customer(self, customer: Customer):
        self.conn.execute_command("DELETE FROM Customers where customer_id = ?", customer.customer_id, self.auto_commit)

    def send_money_to_customer(self, from_customer: Customer, to_customer: Customer, amount: float):
        try:
            self.auto_commit = False
            assert from_customer.money >= amount
            self.conn.execute_command('UPDATE Customers set money = money - ? where customer_id = ?', (amount, from_customer.customer_id))
            self.conn.execute_command('UPDATE Customers set money = money + ? where customer_id = ?', (amount, to_customer.customer_id))
            self.auto_commit = True
        except Exception as e:
            print(e)
            self.conn.rollback()
            self.auto_commit = True

    def import_customers(self):
        try:
            self.auto_commit = False
            with open(self.conn.config['EXPORT_PATH'] + '/customers.csv', 'r') as file:
                reader = csv.reader(file)
                next(reader)
                self.conn.execute_command("SET IDENTITY_INSERT Customers ON")
                for row in reader:
                    self.conn.execute_command('INSERT INTO Customers values (?, ?, ?, ?, ?, ?, ?)', row, self.auto_commit)
                self.conn.execute_command("SET IDENTITY_INSERT Customers OFF")
            self.conn.commit()
            self.auto_commit = True
        except Exception as e:
            print(e)
            self.conn.rollback()
            self.auto_commit = True

    def export_customers(self):
        pd.DataFrame(pd.read_sql_query("SELECT * from Customers", self.conn.con)).to_csv(self.conn.config['EXPORT_PATH'] + '/customers.csv', index=False)

