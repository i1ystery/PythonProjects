from sqlalchemy import Column, ForeignKey, Integer, String, Date, Float, Boolean
from DatabaseSingleton import DatabaseSingleton

DBConn = DatabaseSingleton()


class AnimeEpisode(DBConn.Base):
    __tablename__ = 'anime_episodes'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    title_japanese = Column(String, nullable=True)
    duration = Column(Float)
    aired = Column(Date)
    is_filler = Column(Boolean)
    is_recap = Column(Boolean)
    watch_link = Column(String, nullable=True)
    anime = Column(Integer, ForeignKey('anime.id'))
