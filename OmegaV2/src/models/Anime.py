from datetime import date, time
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Float, Time, Table, Unicode
from models.Database import Base
from models.BroadcastTime import BroadcastTime
from sqlalchemy.orm import relationship
from models.Genre import Genre
from models.Theme import Theme
from models.AnimeEpisode import AnimeEpisode
from models.AnimeCharacter import AnimeCharacter
from models.VoiceActor import VoiceActor
from models.User import UserAnimeListItem


genre_association = Table('an_genre_association', Base.metadata,
                          Column('anime_id', Integer, ForeignKey('anime.id')),
                          Column('genre_id', Integer, ForeignKey('genre.id'))
                          )


theme_association = Table('an_theme_association', Base.metadata,
                          Column('anime_id', Integer, ForeignKey('anime.id')),
                          Column('theme_id', Integer, ForeignKey('theme.id'))
                          )


class Anime(Base):
    """
    Database table anime
    """
    __tablename__ = 'anime'

    id = Column(Integer, primary_key=True)
    title = Column(Unicode)
    title_english = Column(String)
    title_japanese = Column(Unicode)
    synopsis = Column(Unicode)
    image = Column(String, nullable=True)
    show_type = Column(String)
    num_episodes = Column(Integer)
    status = Column(String)
    aired_from = Column(Date)
    aired_to = Column(Date, nullable=True)
    episode_duration = Column(String)
    score = Column(Float, nullable=True)
    broadcast_time = relationship('BroadcastTime')
    genres = relationship('Genre', secondary=genre_association)
    themes = relationship('Theme', secondary=theme_association)
    episodes = relationship('AnimeEpisode')
    anime_characters = relationship('AnimeCharacter')
    users_a_lists = relationship('UserAnimeListItem', back_populates="anime")

    def __init__(self, title: str, title_english: str, title_japanese: str, synopsis: str, image: str, show_type: str,
                 num_episodes: int, status: str, aired_from: date, aired_to: date, episode_duration: int,
                 score: float):
        self.title = title
        self.title_english = title_english
        self.title_japanese = title_japanese
        self.synopsis = synopsis
        self.image = image
        self.show_type = show_type
        self.num_episodes = num_episodes
        self.status = status
        self.aired_from = aired_from
        self.aired_to = aired_to
        self.episode_duration = episode_duration
        self.score = score
