from sqlalchemy import Column, ForeignKey, Integer, String, Date, Float, Enum, Time
from DatabaseSingleton import DatabaseSingleton
from sqlalchemy.orm import relationship


DBConn = DatabaseSingleton()


class DayOfWeek(Enum):
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6
    Sunday = 7


class Anime(DBConn.Base):
    __tablename__ = 'anime'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    title_english = Column(String)
    title_japanese = Column(String)
    image = Column(String, nullable=True)
    show_type = Column(String)
    num_episodes = Column(Integer)
    status = Column(String)
    aired_from = Column(Date)
    aired_to = Column(Date, nullable=True)
    episode_duration = Column(Integer)
    score = Column(Float, nullable=True)
    broadcast_time = Column(Integer, ForeignKey('broadcast_time.id'))
    genres = relationship('anime_genres')
    themes = relationship('anime_themes')
    episode = relationship('anime_episode')
    anime_characters = relationship('anime_characters')


class BroadcastTime(DBConn.Base):
    __tablename__ = 'broadcast_time'

    id = Column(Integer, primary_key=True)
    day_of_week = Column(Enum(DayOfWeek))
    time = Column(Time)
    timezone = Column(String)
    anime = relationship('anime')


class Genres(DBConn.Base):
    __tablename__ = 'anime_genres'

    id = Column(Integer, primary_key=True)
    genre = Column(Integer, ForeignKey('genre.id'))
    anime = Column(Integer, ForeignKey('anime.id'))


class Themes(DBConn.Base):
    __tablename__ = 'anime_themes'

    id = Column(Integer, primary_key=True)
    theme = Column(Integer, ForeignKey('theme.id'))
    anime = Column(Integer, ForeignKey('anime.id'))
