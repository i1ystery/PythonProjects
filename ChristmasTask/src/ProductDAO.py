from datetime import datetime
from enum import Enum
import pandas as pd
from DBConnection import DBConnection
import csv


class ProductCategory(Enum):
    CONVENIENCE = 1
    SHOPPING = 2
    SPECIALTY = 3


class Product:
    def __init__(self, product_name, product_price, is_edible, expiration_date, product_category: ProductCategory, product_id=None):
        assert isinstance(product_name, str) and len(product_name) <= 50, 'Incorrect product name'
        assert datetime.strptime(expiration_date, '%Y-%m-%d'), 'Incorrect expiration date'
        assert isinstance(product_category, ProductCategory)
        assert isinstance(is_edible, bool)
        assert isinstance(product_price, float) and product_price > 0, 'Incorrect product price'
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price
        self.is_edible = is_edible
        self.expiration_date = expiration_date
        self.product_category = product_category

    def __str__(self):
        return f'ID: {self.product_id}\nName: {self.product_name}\nProduct price: {self.product_price}\nIs edible: {self.is_edible}\nExpiration date: {self.expiration_date}\nType: {self.product_category.name}'


class ProductDAO(object):
    def __init__(self):
        self.conn = DBConnection()
        self.auto_commit = True

    def get_all_products(self):
        raw_products = self.conn.execute_command("SELECT * from Products").fetchall()
        products = []
        for raw_product in raw_products:
            products.append(Product(raw_product[1], raw_product[2], bool(raw_product[3]), raw_product[5], ProductCategory(raw_product[4]), raw_product[0]))
        return products

    def get_product_by_id(self, product_id):
        raw_product = self.conn.execute_command("SELECT * from Products where product_id = ?", product_id).fetchone()
        return Product(raw_product[1], raw_product[2], bool(raw_product[3]), raw_product[5], ProductCategory(raw_product[4]), raw_product[0])

    def get_product_by_name(self, product_name):
        raw_product = self.conn.execute_command("SELECT * from Products where product_name = ?", product_name).fetchone()
        return Product(raw_product[1], raw_product[2], bool(raw_product[3]), raw_product[5],
                       ProductCategory(raw_product[4]), raw_product[0])

    def save(self, product: Product):
        data = [product.product_name, product.product_price, product.is_edible, product.product_category.value, product.expiration_date]
        if product.product_id is None:
            self.conn.execute_command("INSERT INTO Products values (?, ?, ?, ?, ?)", data, self.auto_commit)
            product.product_id = self.conn.execute_command('SELECT TOP(1) product_id FROM Products ORDER BY product_id DESC').fetchone()[0]
        else:
            data.append(product.product_id)
            self.conn.execute_command("UPDATE Products set product_name = ?, product_price = ?, is_edible = ?, product_category = ?, expiration_date = ? where product_id = ?",
                                      data, self.auto_commit)

    def delete_customer(self, product: Product):
        self.conn.execute_command("DELETE FROM Products where product_id = ?", product.product_id, self.auto_commit)

    def import_products(self):
        try:
            self.auto_commit = False
            with open(self.conn.config['EXPORT_PATH'] + '/products.csv', 'r') as file:
                reader = csv.reader(file)
                next(reader)
                self.conn.execute_command("SET IDENTITY_INSERT Products ON")
                for row in reader:
                    self.conn.execute_command("INSERT INTO Users values (?, ?, ?, ?, ?, ?)", row, self.auto_commit)
                self.conn.execute_command("SET IDENTITY_INSERT Products OFF")
            self.conn.commit()
            self.auto_commit = True
        except Exception as e:
            print(e)
            self.conn.rollback()
            self.auto_commit = True

    def export_products(self):
        pd.DataFrame(pd.read_sql_query("SELECT * from Products", self.conn.con)).to_csv(self.conn.config['EXPORT_PATH'] + '/products.csv', index=False)
