import csv
import json
import os.path
import pyodbc


def load_config():
    if os.path.exists('config.json'):
        with open('config.json', 'r') as file:
            return json.load(file)


class DBConnection:
    instance = None
    con = None

    def __init__(self):
        if DBConnection.con is None:
            try:
                config = load_config()
                DBConnection.con = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={config["SERVER"]};DATABASE={config["DATABASE"]};UID={config["UID"]};PWD={config["PWD"]}')
                print('Database connection opened.')
            except Exception as e:
                print("Error :\n{0}".format(e))

    def __new__(cls):
        if DBConnection.instance is None:
            DBConnection.instance = object.__new__(cls)
        return DBConnection.instance

    def __del__(self):
        if DBConnection.con is not None:
            DBConnection.con.close()
            print('Database connection closed.')

    def commit(self):
        DBConnection.con.commit()

    def rollback(self):
        DBConnection.con.rollback()

    def execute_command(self, query, params, commit=False):
        cursor = DBConnection.con.cursor()
        cursor.execute(query, params)
        if commit:
            DBConnection.con.commit()
        return cursor

    def execute_query(self, query, params):
        cursor = DBConnection.con.cursor()
        try:
            if params is not None:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor
        except Exception as a:
            print(a)


class UserDAO(object):

    def __init__(self):
        self.conn = DBConnection()

    def get_all_users(self):
        return self.conn.execute_query("SELECT * from Users", None).fetchall()

    def get_users_by_username(self, username):
        return self.conn.execute_query("SELECT * from Users where username = ?", username).fetchall()

    def insert_user(self, username, favorite_number, favorite_color):
        assert isinstance(username, str) and len(username) <= 40
        assert isinstance(favorite_number, int)
        assert isinstance(favorite_color, str) and len(favorite_color) <= 40
        self.conn.execute_command("INSERT INTO Users values (?, ?, ?)", (username, favorite_number, favorite_color))

    def update_users_color(self, username, favorite_color):
        self.conn.execute_command("UPDATE Users set favorite_color = ? where username = ?", (favorite_color, username))

    def delete_user(self, username):
        self.conn.execute_command("DELETE FROM Users where username = ?", username)

    def import_users(self, path):
        try:
            with open(path, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)
                    self.insert_user(*row)
            #self.conn.commit()
        except Exception as e:
            print(e)
            #self.conn.rollback()



if __name__ == '__main__':
    a = UserDAO()
    # print(a.get_all_users())
    # print(a.get_users_by_username('Matej'))
    # a.insert_user('Dima', 6853368, 'Slepa')
    # print(a.get_all_users())
    # a.update_users_color('Dima', 'Bloody Red')
    # print(a.get_all_users())
    # a.delete_user('Dima')
    # print(a.get_all_users())
    a.import_users('insert.csv')
    print(a.get_all_users())
