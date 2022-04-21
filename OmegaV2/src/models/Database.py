import pyodbc
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import scripts.Configuration as config
database_connection = f'mssql://{config.database_login}:{config.database_password}' \
                      f'@{config.database_ip}/{config.database_name}' \
                      f'?driver={config.database_driver}'
engine = create_engine(database_connection)
Session = sessionmaker(bind=engine)
Base = declarative_base()


def create_db():
    """
    Creates database with configured connection
    To create db you have to have imported all needed tables
    """
    Base.metadata.create_all(engine)
