from sqlalchemy import Column, String, Integer, Table, ForeignKey
from models.Database import Base


class Theme(Base):
    """
    Database table theme
    """
    __tablename__ = 'theme'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name: str):
        self.name = name
