from sqlalchemy import Column, Integer, String
from DatabaseSingleton import DatabaseSingleton
from sqlalchemy.orm import relationship


DBConn = DatabaseSingleton()


class Genre(DBConn.Base):
    __tablename__ = 'genre'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    genres = relationship('genres')
