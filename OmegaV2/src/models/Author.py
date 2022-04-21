from sqlalchemy import Column, Integer, Unicode
from models.Database import Base


class Author(Base):
    """
    Database table author
    """
    __tablename__ = 'author'

    id = Column(Integer, primary_key=True)
    full_name = Column(Unicode)

    def __init__(self, full_name: str):
        self.full_name = full_name
