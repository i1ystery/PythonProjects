import json
import os.path
import pyodbc


class DBConnection:
    instance = None
    con = None

    def __init__(self):
        if DBConnection.con is None:
            self.config = self.load_config()
            self.con = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={self.config["SERVER"]};DATABASE={self.config["DATABASE"]};UID={self.config["UID"]};PWD={self.config["PWD"]}')
            print('Database connection opened.')

    def __new__(cls):
        if cls.instance is None:
            cls.instance = object.__new__(cls)
        return cls.instance

    def __del__(self):
        if self.con is not None:
            self.con.close()
            print('Database connection closed.')

    def load_config(self):
        if os.path.exists('../cfg/config.json'):
            with open('../cfg/config.json', 'r') as file:
                return json.load(file)
        else:
            raise FileNotFoundError('Config not found')

    def commit(self):
        self.con.commit()

    def rollback(self):
        self.con.rollback()

    def execute_command(self, query, params=None, commit=False):
        cursor = self.con.cursor()
        if params is not None:
            cursor.execute(query, params)
            if commit:
                self.con.commit()
        else:
            cursor.execute(query)
        return cursor