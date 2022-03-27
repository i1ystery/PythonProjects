from sqlalchemy import Column, ForeignKey, Integer, String, Date, Float
from DatabaseSingleton import DatabaseSingleton
from sqlalchemy.orm import relationship


DBConn = DatabaseSingleton()


class Manga(DBConn.Base):
    __tablename__ = 'manga'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    title_english = Column(String)
    title_japanese = Column(String)
    image = Column(String, nullable=True)
    chapters = Column(Integer)
    volumes = Column(Integer)
    status = Column(String)
    published_from = Column(Date)
    published_to = Column(Date, nullable=True)
    score = Column(Float)
    authors = relationship('manga_author')
    genres = relationship('manga_genres')
    themes = relationship('manga_themes')
    characters = relationship('manga_character')


class MangaAuthor(DBConn.Base):
    __tablename__ = 'manga_author'

    id = Column(Integer, primary_key=True)
    author = Column(Integer, ForeignKey('author'))
    manga = Column(Integer, ForeignKey('manga'))


class MangaGenres(DBConn.Base):
    __tablename__ = 'manga_genres'

    id = Column(Integer, primary_key=True)
    genre = Column(Integer, ForeignKey('genre.id'))
    manga = Column(Integer, ForeignKey('manga.id'))


class MangaThemes(DBConn.Base):
    __tablename__ = 'manga_themes'

    id = Column(Integer, primary_key=True)
    theme = Column(Integer, ForeignKey('theme.id'))
    manga = Column(Integer, ForeignKey('manga.id'))


