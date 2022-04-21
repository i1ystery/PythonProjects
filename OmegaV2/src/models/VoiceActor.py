from sqlalchemy import Column, String, Integer, Table, ForeignKey
from models.Database import Base


class VoiceActor(Base):
    """
    Database table voice_actor
    """
    __tablename__ = 'voice_actor'

    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    language = Column(String)

    def __init__(self, full_name: str, language: str):
        self.full_name = full_name
        self.language = language
