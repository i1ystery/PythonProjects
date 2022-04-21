from datetime import time
from sqlalchemy import Column, Integer, String, Date, Time
from sqlalchemy.sql.schema import ForeignKey
from models.Database import Base


class BroadcastTime(Base):
    """
    Database table broadcast_time
    """
    __tablename__ = 'broadcast_time'

    id = Column(Integer, primary_key=True)
    day_of_week = Column(String)
    broadcast_time = Column(Time)
    timezone = Column(String)
    anime = Column(Integer, ForeignKey('anime.id'))

    def __init__(self, day_of_week: str, br_time: time, timezone: str):
        self.day_of_week = day_of_week
        self.broadcast_time = br_time
        self.timezone = timezone

    def __repr__(self):
        return f'{self.day_of_week} {self.broadcast_time} {self.timezone}'
