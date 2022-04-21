from models.Database import *
from models.Anime import Anime
from models.AnimeCharacter import AnimeCharacter
from models.AnimeEpisode import AnimeEpisode
from models.Author import Author
from models.Genre import Genre
from models.Theme import Theme
from models.Manga import Manga
from models.MangaCharacter import MangaCharacter
from models.User import User
from models.VoiceActor import VoiceActor


def make_new_db():
    """
    Use this to create database if not created
    :return:
    """
    create_db()


# For TESTING
# def remove_last():
#     session = Session()
#     a = session.query(Anime).all()
#     last = a[len(a) - 1]
#     print(last.title)
#     a = last.id
#     print(a)
#     session.delete(last)
#     session.execute(f"DBCC CHECKIDENT('anime', RESEED, {a - 1})")
#     session.commit()
