from CustomerDAO import *
from ProductDAO import *
import pandas as pd
import csv

class OrderDetails:
    def __init__(self, product: Product, quantity: int, details_id=None, order_id=None, final_price=None):
        self.details_id = details_id
        self.product = product
        self.order_id = order_id
        self.quantity = quantity
        if final_price is None:
            self.final_price = product.product_price * quantity
        else:
            self.final_price = final_price

    def __str__(self):
        return f'Details ID: {self.details_id}\nProduct: {self.product.product_name}\nQuantity: {self.quantity}\nFinal price: {self.final_price}'

    def return_as_insert_list(self):
        """
        Returns OrderDetail object as list with all attributes for insert into the DB
        :return:
        """
        return self.product.product_id, self.order_id, self.quantity, self.final_price


class Order:
    def __init__(self, customer: Customer, order_date: str, ship_name: str, ship_city: str, ship_address: str, ship_zip: int, tracking: str, order_id=None, order_details=None):
        assert isinstance(customer, Customer), 'Incorrect customer'
        assert datetime.strptime(str(order_date), '%Y-%m-%d %H:%M:%S'), 'Incorrect order date'
        assert isinstance(ship_name, str) and len(ship_name) <= 50, 'Incorrect shipment name'
        assert isinstance(ship_city, str) and len(ship_city) <= 25, 'Incorrect shipment city'
        assert isinstance(ship_address, str) and len(ship_address) <= 100, 'Incorrect shipment address'
        assert isinstance(ship_zip, int), 'Incorrect shipment zip'
        assert isinstance(tracking, str) and len(tracking) <= 50, 'Incorrect tracking code'
        self.order_id = order_id
        self.customer = customer
        self.order_date = order_date
        self.ship_name = ship_name
        self.ship_city = ship_city
        self.ship_address = ship_address
        self.ship_zip = ship_zip
        self.tracking = tracking
        if not order_details:
            self.order_details = []
        else:
            self.order_details = order_details

    def add_product(self, product: Product, quantity: int):
        """
        Creates OrderDetails object with given product and it's quantity.
        Afterwards adds it to the order
        """
        assert isinstance(product, Product), 'Incorrect product'
        assert isinstance(quantity, int) and quantity > 0, 'Incorrect quantity'
        ord_det = OrderDetails(product, quantity)
        self.order_details.append(ord_det)

    def remove_product(self, order_detail: OrderDetails):
        """
        Removes given OrderDetails Object from an order
        """
        self.order_details.remove(order_detail)

    def __str__(self):
        s = f'Order ID: {self.order_id}\nCustomer: {self.customer}\nOrder date: {self.order_date }\nShipment name: {self.ship_name}' \
               f'\nShipment city: {self.ship_city}\nShipment address: {self.ship_address}\nShipment zip: {self.ship_zip}\nTracking code: {self.tracking}\nProducts:\n'
        for products in self.order_details:
            s += products.__str__() + '\n'
        return s


class OrderDAO(object):
    def __init__(self):
        self.conn = DBConnection()
        self.auto_commit = True

    def get_all_orders(self) -> list[Order]:
        """
        Selects all Orders from the database and returns them
        :return: List with Order Objects
        """
        raw_orders = self.conn.execute_command("SELECT * from Orders").fetchall()
        orders = []
        for raw_order in raw_orders:
            cust_dao = CustomerDAO()
            cust = cust_dao.get_customer_by_id(customer_id=raw_order[1])
            order = Order(cust, raw_order[2], raw_order[3], raw_order[4], raw_order[5], raw_order[6], raw_order[7], raw_order[0])
            order.order_details.extend(self.get_order_det_by_id(raw_order[0]))
            orders.append(order)
        return orders

    def get_order_det_by_id(self, order_id: int) -> list[OrderDetails]:
        """
        Selects all OrderDetails associated with Order that the given order_id belongs to
        :return: List with OrderDetails Objects
        """
        raw_details = self.conn.execute_command("SELECT * from OrderDetails where order_id = ?", order_id).fetchall()
        details = []
        for raw_detail in raw_details:
            prod_dao = ProductDAO()
            product = prod_dao.get_product_by_id(raw_detail[1])
            details.append(OrderDetails(product, raw_detail[3], raw_detail[0], raw_detail[2], raw_detail[4]))
        return details

    def save(self, order: Order):
        """
        Inserts new/Updates existing Order in the DB
        """
        assert order.order_details
        order_data = [order.customer.customer_id, order.order_date, order.ship_name, order.ship_city, order.ship_address, order.ship_zip, order.tracking]
        if order.order_id is None:
            self.conn.execute_command("INSERT INTO Orders values (?, ?, ?, ?, ?, ?, ?)", order_data, self.auto_commit)
            order.order_id = self.conn.execute_command('SELECT TOP(1) order_id FROM Orders ORDER BY order_id DESC').fetchone()[0]
            for product_details in order.order_details:
                product_details.order_id = order.order_id
                self.conn.execute_command("INSERT INTO OrderDetails values (?, ?, ?, ?)", product_details.return_as_insert_list(), self.auto_commit)
                product_details.details_id = self.conn.execute_command('SELECT TOP(1) details_id FROM OrderDetails ORDER BY details_id DESC').fetchone()[0]
        else:
            order_data.append(order.order_id)
            self.conn.execute_command("UPDATE Orders set order_customer = ?, order_datetime = ?, ship_name = ?, ship_city = ?, ship_address = ?, ship_zip = ?, order_tracking = ? where order_id = ?",
                                      order_data, self.auto_commit)
            db_details = self.conn.execute_command("SELECT details_id from OrderDetails where order_id = ?", order.order_id).fetchall()
            for details in order.order_details:
                if details.details_id is None:
                    details.order_id = order.order_id
                    self.conn.execute_command("INSERT INTO OrderDetails values (?, ?, ?, ?)", details.return_as_insert_list(), self.auto_commit)
                    details.details_id = self.conn.execute_command('SELECT TOP(1) details_id FROM OrderDetails ORDER BY details_id DESC').fetchone()[0]
                    continue
                if details.details_id in db_details:
                    db_details.remove(details.details_id)
            if db_details:
                for details_id in db_details:
                    self.conn.execute_command("DELETE from OrderDetails where details_id = ?", details_id, self.auto_commit)

    def delete_order(self, order: Order):
        """
        Deletes given Order from the DB
        """
        try:
            self.auto_commit = False
            for details in order.order_details:
                self.conn.execute_command("DELETE from OrderDetails where order_id = ?", order.order_id, self.auto_commit)
            self.conn.execute_command("DELETE from Orders where order_id = ?", order.order_id, self.auto_commit)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            self.auto_commit = True
            raise e

    def get_report(self):
        """
        Executes stored procedure in the DB that generates Database Aggregate Report
        :return: Aggregate report as pandas DataFrames
        """
        return pd.read_sql('EXEC AggregateReport', self.conn.con)

    def import_orders(self, order_path, order_details_path):
        """
        Imports Orders and OrdersDetails from given .csv files
        :param order_path: path to .csv file with Orders
        :param order_details_path: path to .csv file with OrderDetails
        """
        try:
            self.auto_commit = False
            with open(order_path, 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    self.conn.execute_command('INSERT INTO Orders values (?, ?, ?, ?, ?, ?, ?)', row, self.auto_commit)
            with open(order_details_path, 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    self.conn.execute_command('INSERT INTO OrderDetails values (? ,?, ?, ?)', row, self.auto_commit)
            self.conn.commit()
            self.auto_commit = True
        except Exception as e:
            self.conn.rollback()
            self.auto_commit = True
            raise

    def export_orders(self, path):
        """
        Exports all rows from the Orders and Order Details tables in the database as .csv files at the specified path.
        :param path: Path that the .csv file will be saved
        """
        pd.DataFrame(pd.read_sql_query("SELECT * from OrdersExport", self.conn.con)).to_csv(path+'/orders.csv', index=False)
        pd.DataFrame(pd.read_sql_query("SELECT * from OrderDetailsExport", self.conn.con)).to_csv(path + '/order_details.csv', index=False)
