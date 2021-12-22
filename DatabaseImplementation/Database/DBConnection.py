import json
import os.path
import pyodbc


class DBConnection:
    instance = None
    con = None

    def __init__(self):
        if DBConnection.con is None:
            try:
                config = self.load_config()
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

    def load_config(self):
        if os.path.exists('./config.json'):
            with open('./config.json', 'r') as file:
                return json.load(file)

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
