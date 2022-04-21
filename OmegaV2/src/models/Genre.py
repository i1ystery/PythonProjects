from sqlalchemy import Column, Integer, String, Table, ForeignKey
from models.Database import Base
from sqlalchemy.orm import relationship


class Genre(Base):
    """
    Database table genre
    """
    __tablename__ = 'genre'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name: str):
        self.name = name
