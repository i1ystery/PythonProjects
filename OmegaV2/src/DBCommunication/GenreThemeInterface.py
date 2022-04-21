import requests as requests

from models.Genre import Genre
from models.Theme import Theme


def insert_genres_jikan(session):
    """
    Inserts all genres from jikan API into DB
    :param session: DB session
    :return: Completion status
    """
    try:
        link = "https://api.jikan.moe/v4/genres/anime?filter=genres,explicit_genres"
        request = requests.get(link)
        response = request.json()
        genres_data = response['data']
        for genre in genres_data:
            genre = Genre(genre['name'])
            session.add(genre)
        session.commit()
        return 'Successfully added genres'
    except:
        session.rollback()
        raise


def insert_themes_jikan(session):
    """
    Inserts all themes from jikan API into DB
    :param session: DB session
    :return: Completion status
    """
    try:
        link = "https://api.jikan.moe/v4/genres/anime?filter=themes"
        request = requests.get(link)
        response = request.json()
        themes_data = response['data']
        for theme in themes_data:
            theme = Theme(theme['name'])
            session.add(theme)
        session.commit()
        return 'Successfully added themes'
    except:
        session.rollback()
        raise

