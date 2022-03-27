from sqlalchemy import Column, ForeignKey, Integer, String
from DatabaseSingleton import DatabaseSingleton
from sqlalchemy.orm import relationship


DBConn = DatabaseSingleton()


class MangaCharacter(DBConn.Base):
    __tablename__ = 'manga_character'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    image = Column(String, nullable=True)
    role = Column(String)
