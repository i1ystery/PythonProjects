from sqlalchemy import Column, ForeignKey, Integer, String
from DatabaseSingleton import DatabaseSingleton
from sqlalchemy.orm import relationship


DBConn = DatabaseSingleton()


class AnimeCharacter(DBConn.Base):
    __tablename__ = 'anime_characters'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    image = Column(String, nullable=True)
    role = Column(String)
    anime = Column(Integer, ForeignKey('anime.id'))
    voice_actors = relationship('character_va')


class CharacterVoiceActor(DBConn.Base):
    __tablename__ = 'character_va'

    id = Column(Integer, primary_key=True)
    character = Column(Integer, ForeignKey('anime_character.id'))
    voice_actor = Column(Integer, ForeignKey('voice_actor.id'))
