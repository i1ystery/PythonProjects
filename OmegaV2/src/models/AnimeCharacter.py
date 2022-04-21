from sqlalchemy import Column, ForeignKey, Integer, String, Table
from models.Database import Base
from sqlalchemy.orm import relationship


va_association = Table('va_association', Base.metadata,
                       Column('va_id', Integer, ForeignKey('voice_actor.id')),
                       Column('character_id', Integer, ForeignKey('anime_character.id'))
                       )


class AnimeCharacter(Base):
    """
    Database table anime_character
    """
    __tablename__ = 'anime_character'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    image = Column(String, nullable=True)
    role = Column(String)
    anime = Column(Integer, ForeignKey('anime.id'))
    voice_actors = relationship('VoiceActor', secondary=va_association)

    def __init__(self, name: str, image: 'string or None', role: str, anime_id: int):
        self.name = name
        self.image = image
        self.role = role
        self.anime = anime_id
