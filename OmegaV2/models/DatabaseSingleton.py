import json
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def load_cfg():
    with open('../config/config.json', 'r') as file:
        return json.load(file)


class DatabaseSingleton:
    instance = None

    def __init__(self):
        self.config = load_cfg()
        self.database_name = self.config['DATABASE_NAME']
        self.engine = create_engine(f'sqlite:///{self.database_name}')
        self.Session = sessionmaker(bind=self.engine)
        self.Base = declarative_base()

    def __new__(cls):
        if DatabaseSingleton.instance is None:
            DatabaseSingleton.instance = object.__new__(cls)
        return DatabaseSingleton.instance

    def create_db(self):
        self.Base.metadata.create_all(self.engine)
