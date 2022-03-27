from sqlalchemy import Column, String
from DatabaseSingleton import DatabaseSingleton
from sqlalchemy.orm import relationship


DBConn = DatabaseSingleton()


class VoiceActor(DBConn.Base):
    __tablename__ = 'voice_actor'
    full_name = Column(String)
    language = Column(String)
    character_va = relationship('character_va')
