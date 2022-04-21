from models.Anime import Anime
from models.Manga import Manga
from models.Status import Status
from models.User import UserAnimeListItem, UserMangaListItem, User
from typing import Union
import random


def get_anime_page(session, anime_id: int = 0, mode: int = 0) -> list[Anime]:
    """
    Loads 3 animes from database and returns it as list
    Method modes:
        0 load first 3 from db
        1 load 3 after given anime_id
        -1 load previous 3 before given anime_id
    :param session: DB session
    :param mode: Default 0
    :return: list of Animes
    """
    if mode == 0 or mode == 1:
        animes = session.query(Anime).where(Anime.id > anime_id).limit(3).all()
    elif mode == -1 and anime_id - 3 >= 1:
        animes = session.query(Anime).where(Anime.id >= anime_id - 4).limit(3).all()
    return animes


def get_manga_page(session, manga_id: int = 0, mode: int = 0) -> list[Manga]:
    """
    Loads 3 mangas from database and returns it as list
    Method modes:
        0 load first 3 from db
        1 load 3 after given manga_id
        -1 load previous 3 before given manga_id
    :param session: DB session
    :param mode: Default 0
    :return: list of Mangas
    """
    if mode == 0 or mode == 1:
        mangas = session.query(Manga).where(Manga.id > manga_id).limit(3).all()
    elif mode == -1 and manga_id - 3 >= 1:
        mangas = session.query(Manga).where(Manga.id >= manga_id - 4).limit(3).all()
    return mangas


def get_anime(session) -> list[Anime]:
    """
    Loads all animes from DB
    :param session: DB session
    :return: full list of Animes
    """
    return session.query(Anime).all()


def get_manga(session) -> list[Manga]:
    """
   Loads all manga from DB
   :param session: DB session
   :return: full list of Manga
    """
    return session.query(Manga).all()


def get_user_anime_page(session, user: User, item_filter: Status, user_anime_id: int = 0, mode: int = 0) -> list[UserAnimeListItem]:
    """
    Loads 3 USER animes from database and returns it as list
    Method modes:
        0 load first 3 from db
        1 load 3 after given user_anime_id
        -1 load previous 3 before given user_anime_id
    :param session: DB session
    :param item_filter: Status ENUM
    :return: page of UserAnimes as list
    """
    if mode == 0 or mode == 1:
        if item_filter == Status.ALL:
            animes = session.query(UserAnimeListItem).join(User).where(User.id == user.id, UserAnimeListItem.id > user_anime_id,).limit(3).all()
        else:
            animes = session.query(UserAnimeListItem).join(User).where(User.id == user.id,
                                                                       UserAnimeListItem.id > user_anime_id,
                                                                       UserAnimeListItem.status == item_filter.value
                                                                       ).limit(3).all()
    elif mode == - 1 and user_anime_id - 3 >= 1:
        if item_filter == Status.ALL:
            animes = session.query(UserAnimeListItem).join(User).where(User.id == user.id, UserAnimeListItem.id >= user_anime_id - 4).limit(3).all()
        else:
            animes = session.query(UserAnimeListItem).join(User).where(User.id == user.id,
                                                                       UserAnimeListItem.id >= user_anime_id - 4,
                                                                       UserAnimeListItem.status == item_filter.value
                                                                       ).limit(3).all()
    return animes


def get_user_manga_page(session, user: User, item_filter: Status, user_manga_id: int = 0, mode: int = 0) -> list[UserMangaListItem]:
    """
    Loads 3 USER manga from database and returns it as list
    Method modes:
        0 load first 3 from db
        1 load 3 after given manga_id
        -1 load previous 3 before given manga_id
    :param session: DB session
    :param item_filter: Status ENUM
    :return: page of UsesManga as list
    """
    if mode == 0 or mode == 1:
        if item_filter == Status.ALL:
            mangas = session.query(UserMangaListItem).join(User).where(User.id == user.id, UserMangaListItem.id > user_manga_id).limit(3).all()
        else:
            mangas = session.query(UserMangaListItem).join(User).where(User.id == user.id,
                                                                       UserMangaListItem.id > user_manga_id,
                                                                       UserMangaListItem.status == item_filter.value
                                                                       ).limit(3).all()
    elif mode == - 1 and user_manga_id - 3 >= 1:
        if item_filter == Status.ALL:
            mangas = session.query(UserMangaListItem).join(User).where(User.id == user.id, UserMangaListItem.id >= user_manga_id - 4).limit(3).all()
        else:
            mangas = session.query(UserMangaListItem).join(User).where(User.id == user.id,
                                                                       UserMangaListItem.id >= user_manga_id - 4,
                                                                       UserMangaListItem.status == item_filter.value
                                                                       ).limit(3).all()
    return mangas


def get_random_anime(session) -> Union[Anime, None]:
    """
   Loads random anime from DB
   :param session: DB session
   :return: Anime object
    """
    count = session.query(Anime).count()
    if count > 0:
        rng = random.randint(1, count)
        return session.query(Anime).filter(Anime.id == rng).first()
    return None


def get_random_manga(session) -> Union[Manga, None]:
    """
   Loads random manga from DB
   :param session: DB session
   :return: Manga object
    """
    count = session.query(Manga).count()
    if count > 0:
        rng = random.randint(1, count)
        return session.query(Manga).filter(Manga.id == rng).first()
    return None
