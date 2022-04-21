from typing import Union
from models.User import User
from models.Anime import Anime
from models.Manga import Manga
from models.User import UserAnimeListItem
from models.User import UserMangaListItem


def add_new_user(session, username: str, password: str, is_admin=False):
    """
    Adds new user to database
    :param session: DB session
    :param username:
    :param password:
    :param is_admin:
    :return: Completion status
    """
    try:
        check_existing = session.query(User).filter(User.username == username).first()
        if check_existing:
            return 'User already exists'
        user = User(username, password, is_admin)
        session.add(user)
        session.commit()
        return 'Successfully registered'
    except Exception as e:
        session.rollback()
        raise e


def check_login(session, username: str, password: str) -> Union[User, str]:
    """
    Checks login:password combination
    :param session: DB session
    :param username:
    :param password:
    :return: If user exists returns User object else returns string Completion status
    """
    try:
        check_existing_user = session.query(User).filter(User.username == username).first()
        if check_existing_user:
            user = session.query(User).filter(User.username == username, User.password == password).first()
            if user:
                return user
            else:
                return 'Invalid password'
        else:
            return 'User does not exist'
    except Exception as e:
        raise e


def add_anime_to_user_list(session, user: User, anime: Anime, status: str, score: int, ep_watched: int):
    """
    Adds given anime to user's list
    :param session: DB session
    :param user:
    :param anime:
    :param status:
    :param score:
    :param ep_watched:
    :return: Completion status
    """
    try:
        if session.query(UserAnimeListItem).where(
                UserAnimeListItem.user_id == user.id,
                UserAnimeListItem.anime_id == anime.id
        ).first():
            return 'You already have anime in your list'
        anime_list_item = UserAnimeListItem(user=user, anime=anime, status=status, score=score, episodes_watched=ep_watched)
        session.add(anime_list_item)
        session.commit()
        return 'Successfully added'
    except Exception as e:
        session.rollback()
        raise e


def add_manga_to_user_list(session, user: User, manga: Manga, status: str, score: int, chapters_read: int, volumes_read: int):
    """
    Adds given manga to user's list
    :param session: DB session
    :param user:
    :param manga:
    :param status:
    :param score:
    :param chapters_read:
    :param volumes_read:
    :return: Completion status
    """
    try:
        if session.query(UserMangaListItem).where(
                UserMangaListItem.user_id == user.id,
                UserMangaListItem.manga_id == manga.id
        ).first():
            return 'You already have manga in your list'
        manga_list_item = UserMangaListItem(
            user=user, manga=manga, status=status, score=score, chapters_read=chapters_read, volumes_read=volumes_read
        )
        session.add(manga_list_item)
        session.commit()
        return 'Successfully added'
    except Exception as e:
        session.rollback()
        raise e


def update_user_anime(session, user_anime_item: UserAnimeListItem, status: str, score: int, episodes_watched: int):
    """
    Updates data User's Anime Item data
    :param session: DB session
    :param user_anime_item:
    :param status:
    :param score:
    :param episodes_watched:
    :return: Completion status
    """
    try:
        user_anime_item.status = status
        user_anime_item.score = score
        user_anime_item.episodes_watched = episodes_watched
        session.commit()
        return 'Successfully updated'
    except Exception as e:
        session.rollback()
        raise e


def update_user_manga(session, user_manga_item: UserMangaListItem, status: str, score: int, chapters_read: int, volumes_read: int):
    """
    Updates data User's Manga Item data
    :param session: DB session
    :param user_manga_item:
    :param status:
    :param score:
    :param chapters_read:
    :param volumes_read:
    :return: Completion status
    """
    try:
        user_manga_item.status = status
        user_manga_item.score = score
        user_manga_item.chapters_read = chapters_read
        user_manga_item.volumes_read = volumes_read
        session.commit()
        return 'Successfully updated'
    except Exception as e:
        session.rollback()
        raise e


def delete_user_item(session, user_anime_item: Union[UserAnimeListItem, UserMangaListItem]):
    """
    Deletes item from user's list
    :param session: DB session
    :param user_anime_item:
    :return: Completion status
    """
    try:
        session.delete(user_anime_item)
        if isinstance(user_anime_item, UserAnimeListItem):
            session.execute(f"DBCC CHECKIDENT('user_anime_list_item', RESEED, {user_anime_item.id - 1})")
        else:
            session.execute(f"DBCC CHECKIDENT('user_manga_list_item', RESEED, {user_anime_item.id - 1})")
        session.commit()
        return 'Successfully deleted'
    except Exception as e:
        session.rollback()
        raise e
