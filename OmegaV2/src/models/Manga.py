from datetime import date
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Float, Table, Unicode
from sqlalchemy.orm import relationship
from models.Database import Base
from models.Author import Author
from models.Genre import Genre
from models.Theme import Theme
from models.MangaCharacter import MangaCharacter
from models.User import UserMangaListItem


author_association = Table('author_association', Base.metadata,
                           Column('manga_id', Integer, ForeignKey('manga.id')),
                           Column('author_id', Integer, ForeignKey('author.id'))
                           )


genre_association = Table('mg_genre_association', Base.metadata,
                          Column('manga_id', Integer, ForeignKey('manga.id')),
                          Column('genre_id', Integer, ForeignKey('genre.id'))
                          )


theme_association = Table('mg_theme_association', Base.metadata,
                          Column('manga_id', Integer, ForeignKey('manga.id')),
                          Column('theme_id', Integer, ForeignKey('theme.id'))
                          )


class Manga(Base):
    """
    Database table manga
    """
    __tablename__ = 'manga'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode)
    title_english = Column(String)
    title_japanese = Column(Unicode)
    synopsis = Column(Unicode)
    image = Column(String, nullable=True)
    manga_type = Column(String)
    chapters = Column(Integer)
    volumes = Column(Integer)
    status = Column(String)
    published_from = Column(Date)
    published_to = Column(Date, nullable=True)
    score = Column(Float)
    authors = relationship('Author', secondary=author_association)
    genres = relationship('Genre', secondary=genre_association)
    themes = relationship('Theme', secondary=theme_association)
    characters = relationship('MangaCharacter')
    users_m_lists = relationship('UserMangaListItem', back_populates="manga")

    def __init__(self, title: str, title_japanese: str, title_english: str, synopsis: str, image: 'string or None', manga_type: str, chapters: int, volumes: int,
                 status: str, published_from: date, published_to: date, score: float):
        self.title = title
        self.title_japanese = title_japanese
        self.title_english = title_english
        self.synopsis = synopsis
        self.image = image
        self.manga_type = manga_type
        self.chapters = chapters
        self.volumes = volumes
        self.status = status
        self.published_from = published_from
        self.published_to = published_to
        self.score = score

