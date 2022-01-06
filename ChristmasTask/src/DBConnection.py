import json
import os.path
import pyodbc


class DBConnection:
    instance = None
    con = None

    def __init__(self):
        """
        Loads config and creates connection to MSSQL Server
        """
        if DBConnection.con is None:
            print('Loading...')
            self.config = self.load_config()
            DBConnection.con = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={self.config["SERVER"]};DATABASE={self.config["DATABASE"]};UID={self.config["UID"]};PWD={self.config["PWD"]}')

    def __new__(cls) -> pyodbc.Connection:
        """
        Connection singleton
        :return: MSSQL Server connection object
        """
        if DBConnection.instance is None:
            DBConnection.instance = object.__new__(cls)
        return DBConnection.instance

    def __del__(self):
        if DBConnection.con is not None:
            DBConnection.con.close()

    def load_config(self) -> dict:
        """
        Loads connection config from file.
        :return: loaded config as dictionary
        """
        config_path = os.path.abspath(os.path.join(os.getcwd(), '../cfg/config.json'))
        if os.path.exists(config_path):
            with open(config_path, 'r') as file:
                return json.load(file)
        else:
            raise FileNotFoundError('Config not found')

    def commit(self):
        DBConnection.con.commit()

    def rollback(self):
        DBConnection.con.rollback()

    def execute_command(self, query: str, params=None, commit=False) -> pyodbc.Cursor:
        """
        Executes sql query with parameters. If no parameters given, executes query
        :param query: sql query
        :param params: bind parameters for sql query
        :param commit:  autocommit variable
        :return: cursor with database output
        """
        cursor = DBConnection.con.cursor()
        if params is not None:
            cursor.execute(query, params)
            if commit:
                DBConnection.con.commit()
        else:
            cursor.execute(query)
        return cursor
