from sqlalchemy import Column, ForeignKey, Integer, String
from models.Database import Base


class MangaCharacter(Base):
    """
    Database table manga_character
    """
    __tablename__ = 'manga_character'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    image = Column(String, nullable=True)
    role = Column(String)
    manga = Column(Integer, ForeignKey('manga.id'))

    def __init__(self, name: str, image: 'string or None', role: str, manga_id: int):
        self.name = name
        self.image = image
        self.role = role
        self.manga = manga_id
