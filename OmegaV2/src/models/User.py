from sqlalchemy import Column, Integer, String, Boolean, Table, ForeignKey
from sqlalchemy.orm import relationship
from models.Database import Base


class User(Base):
    """
    Database table user
    """
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    is_admin = Column(Boolean)
    anime_list = relationship('UserAnimeListItem', back_populates="user")
    manga_list = relationship('UserMangaListItem', back_populates="user")

    def __init__(self, username: str, password: str, is_admin=False):
        self.username = username
        self.password = password
        self.is_admin = is_admin


class UserAnimeListItem(Base):
    __tablename__ = 'user_anime_list_item'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    anime_id = Column(Integer, ForeignKey('anime.id'), primary_key=True)
    status = Column(String)
    score = Column(Integer)
    episodes_watched = Column(Integer)
    user = relationship('User', back_populates="anime_list")
    anime = relationship('Anime', back_populates="users_a_lists")


class UserMangaListItem(Base):
    __tablename__ = 'user_manga_list_item'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    manga_id = Column(Integer, ForeignKey('manga.id'), primary_key=True)
    status = Column(String)
    score = Column(Integer)
    chapters_read = Column(Integer)
    volumes_read = Column(Integer)
    user = relationship('User', back_populates="manga_list")
    manga = relationship("Manga", back_populates="users_m_lists")




