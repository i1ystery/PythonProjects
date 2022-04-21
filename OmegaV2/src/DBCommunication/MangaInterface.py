import datetime
import requests

from models.Database import *
from models.Author import Author
from models.MangaCharacter import MangaCharacter
from models.Manga import Manga
from models.Anime import Anime
from models.Theme import Theme
from models.Genre import Genre


def insert_manga_by_name_jikan(manga_name: str, session):
    """
    Adds manga to database by name using jikan API
    :param manga_name:
    :param session: Database session
    :return: Completion status
    """
    try:
        link = "https://api.jikan.moe/v4/manga"
        request = requests.get(link + f'?q={manga_name}')
        response = request.json()
        if not response['data']:
            return 'Manga not found'
        manga_data = response['data'][0]
        mal_id = manga_data['mal_id']
        title = manga_data['title']
        if session.query(Manga).where(Manga.title == title).first():
            return 'Manga is already in database'
        title_en = manga_data['title_english']
        title_jp = manga_data['title_japanese']
        synopsis = manga_data['synopsis']
        image = manga_data['images']['jpg']['image_url']
        manga_type = manga_data['type']
        chapters = manga_data['chapters']
        volumes = manga_data['volumes']
        status = manga_data['status']
        published_from = manga_data['published']['from']
        published_to = manga_data['published']['to']
        if published_from:
            published_from = datetime.datetime.strptime(published_from.split('T')[0], '%Y-%m-%d').date()
        if published_to:
            published_to = datetime.datetime.strptime(published_to.split('T')[0], '%Y-%m-%d').date()
        score = manga_data['score']
        authors = manga_data['authors']
        genres = manga_data['genres']
        themes = manga_data['themes']
        manga = Manga(title, title_jp, title_en, synopsis, image, manga_type, chapters, volumes, status, published_from, published_to, score)
        session.add(manga)
        session.commit()
        add_authors_to_manga(authors, manga, session)
        add_genres_to_manga(genres, manga, session)
        add_themes_to_manga(themes, manga, session)
        add_characters_to_manga(mal_id, manga, session)
        session.commit()
        return f'Successfully added\n{title}'
    except Exception as e:
        session.rollback()
        raise e


def add_authors_to_manga(authors: dict, manga: Manga, session):
    """
    Helping method for insert_manga_by_name_jikan method
    Is not used separately
    """
    try:
        for author in authors:
            author_name = author['name']
            author_db = session.query(Author).filter(Author.full_name == author_name).first()
            if author_db:
                manga.authors.append(author_db)
            else:
                author_db = Author(author_name)
                session.add(author_db)
                manga.authors.append(author_db)
    except:
        session.rollback()
        raise


def add_characters_to_manga(mal_id: int, manga: Manga, session):
    """
    Helping method for insert_manga_by_name_jikan method
    Is not used separately
    """
    try:
        link = f"https://api.jikan.moe/v4/manga/{mal_id}/characters"
        request = requests.get(link)
        response = request.json()
        characters = response['data']
        for character_data in characters:
            character_name = character_data['character']['name']
            character_image = character_data['character']['images']['jpg']['image_url']
            character_role = character_data['role']
            character = MangaCharacter(character_name, character_image, character_role, manga.id)
            session.add(character)
    except:
        session.rollback()
        raise


def add_genres_to_manga(genres: dict, manga: Manga, session):
    """
    Helping method for insert_manga_by_name_jikan method
    Is not used separately
    """
    try:
        for genre in genres:
            genre_name = genre['name']
            genre_db = session.query(Genre).filter(Genre.name == genre_name).first()
            if genre_db:
                manga.genres.append(genre_db)
            else:
                genre_db = Genre(genre_name)
                session.add(genre_db)
                manga.genres.append(genre_db)
    except:
        session.rollback()
        raise


def add_themes_to_manga(themes: dict, manga: Manga, session):
    """
    Helping method for insert_manga_by_name_jikan method
    Is not used separately
    """
    try:
        for theme in themes:
            theme_name = theme['name']
            theme_db = session.query(Theme).filter(Theme.name == theme_name).first()
            if theme_db:
                manga.themes.append(theme_db)
            else:
                theme_db = Theme(theme_name)
                session.add(theme_db)
                manga.themes.append(theme_db)
    except:
        session.rollback()
        raise
