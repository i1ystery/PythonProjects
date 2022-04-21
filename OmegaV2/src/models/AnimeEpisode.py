from datetime import date

from sqlalchemy import Column, ForeignKey, Integer, String, Date, Unicode, Boolean
from models.Database import Base


class AnimeEpisode(Base):
    """
    Database table anime_episodes
    """
    __tablename__ = 'anime_episodes'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    title_japanese = Column(Unicode, nullable=True)
    aired = Column(Date)
    is_filler = Column(Boolean)
    is_recap = Column(Boolean)
    watch_link = Column(String, nullable=True)
    anime = Column(Integer, ForeignKey('anime.id'))

    def __init__(self, title: str, title_japanese: str, aired_date: date, is_filler: bool, is_recap: bool,
                 watch_link: 'str or None', anime_id: int):
        self.title = title
        self.title_japanese = title_japanese
        self.aired = aired_date
        self.is_filler = is_filler
        self.is_recap = is_recap
        self.watch_link = watch_link
        self.anime = anime_id
