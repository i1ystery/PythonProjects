from sqlalchemy import Column, Integer, String
from DatabaseSingleton import DatabaseSingleton
from sqlalchemy.orm import relationship


DBConn = DatabaseSingleton()


class Author(DBConn.Base):
    __tablename__ = 'author'

    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    image = Column(String, nullable=True)
    manga_author = relationship('manga_author')
