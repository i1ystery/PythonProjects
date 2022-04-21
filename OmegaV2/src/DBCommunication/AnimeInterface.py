import datetime
import requests

from models.Anime import Anime, BroadcastTime
from models.Manga import Manga
from models.AnimeEpisode import AnimeEpisode
from models.AnimeCharacter import AnimeCharacter
from models.VoiceActor import VoiceActor
from models.Theme import Theme
from models.Genre import Genre


def insert_anime_by_name_jikan(anime_name: str, session) -> str:
    """
    Adds anime to database by name using jikan API
    :param anime_name:
    :param session: Database session
    :return: Completion status
    """
    try:
        link = "https://api.jikan.moe/v4/anime"
        request = requests.get(link + f'?q={anime_name}')
        response = request.json()
        if not response['data']:
            return 'Anime not found'
        anime_data = response['data'][0]
        mal_id = anime_data['mal_id']
        title = anime_data['title']
        if session.query(Anime).where(Anime.title == title).first():
            return 'Anime is already in database'
        title_en = anime_data['title_english']
        title_jp = anime_data['title_japanese']
        synopsis = anime_data['synopsis']
        image = anime_data['images']['jpg']['image_url']
        show_type = anime_data['type']
        num_episodes = anime_data['episodes']
        status = anime_data['status']
        aired_from = anime_data['aired']['from']
        aired_to = anime_data['aired']['to']
        episode_duration = anime_data['duration']
        score = anime_data['score']
        broadcast_d = anime_data['broadcast']['day']
        broadcast_t = anime_data['broadcast']['time']
        broadcast_tz = anime_data['broadcast']['timezone']
        genres = anime_data['genres']
        themes = anime_data['themes']
        if aired_from:
            aired_from = datetime.datetime.strptime(aired_from.split('T')[0], '%Y-%m-%d').date()
        if aired_to:
            aired_to = datetime.datetime.strptime(aired_to.split('T')[0], '%Y-%m-%d').date()
        if broadcast_t:
            broadcast_t = datetime.datetime.strptime(broadcast_t, '%H:%M').time()
        broadcast = BroadcastTime(broadcast_d, broadcast_t, broadcast_tz)
        session.add(broadcast)
        session.commit()
        anime = Anime(title, title_en, title_jp, synopsis, image, show_type, num_episodes, status, aired_from, aired_to, episode_duration, score)
        anime.broadcast_time.append(broadcast)
        session.add(anime)
        session.commit()
        add_episodes_to_anime(mal_id, anime, session)
        add_characters_to_anime(mal_id, anime, session)
        add_genres_to_anime(genres, anime, session)
        add_themes_to_anime(themes, anime, session)
        session.commit()
        return f'Successfully added\n{title}'
    except:
        session.rollback()
        raise


def add_episodes_to_anime(mal_id, anime: Anime, session):
    """
    Helping method for insert_anime_by_name_jikan method
    Is not used separately
    """
    try:
        link = f"https://api.jikan.moe/v4/anime/{mal_id}/episodes"
        request = requests.get(link)
        response = request.json()
        episode_data = response['data']
        for episode in episode_data:
            ep_title = episode['title']
            ep_title_jp = episode['title_japanese']
            ep_aired = episode['aired']
            is_filler = episode['filler']
            is_recap = episode['recap']
            watch_link = None
            episode = AnimeEpisode(ep_title, ep_title_jp, ep_aired, is_filler, is_recap, watch_link, anime.id)
            session.add(episode)
    except:
        session.rollback()
        raise


def add_characters_to_anime(mal_id, anime: Anime, session):
    """
    Helping method for insert_anime_by_name_jikan method
    Is not used separately
    """
    try:
        link = f"https://api.jikan.moe/v4/anime/{mal_id}/characters"
        request = requests.get(link)
        response = request.json()
        characters = response['data']
        for character_data in characters:
            character_name = character_data['character']['name']
            character_image = character_data['character']['images']['jpg']['image_url']
            character_role = character_data['role']
            voice_actors = character_data['voice_actors']
            character = AnimeCharacter(character_name, character_image, character_role, anime.id)
            session.add(character)
            add_voice_actors_to_char(voice_actors, character, session)
    except:
        session.rollback()
        raise


def add_voice_actors_to_char(actors: dict, character: AnimeCharacter, session):
    """
    Helping method for insert_anime_by_name_jikan method
    Is not used separately
    """
    try:
        for actor in actors:
            actor_language = actor['language']
            actor_name = actor['person']['name']
            if actor_language in ['Japanese', 'English']:
                actor_db = session.query(VoiceActor).filter(VoiceActor.full_name == actor_name).first()
                if actor_db:
                    character.voice_actors.append(actor_db)
                else:
                    actor_db = VoiceActor(actor_name, actor_language)
                    session.add(actor_db)
                    character.voice_actors.append(actor_db)
    except:
        session.rollback()
        raise


def add_genres_to_anime(genres: dict, anime: Anime, session):
    """
    Helping method for insert_anime_by_name_jikan method
    Is not used separately
    """
    try:
        for genre in genres:
            genre_name = genre['name']
            genre_db = session.query(Genre).filter(Genre.name == genre_name).first()
            if genre_db:
                anime.genres.append(genre_db)
            else:
                genre_db = Genre(genre_name)
                session.add(genre_db)
                anime.genres.append(genre_db)
    except:
        session.rollback()
        raise


def add_themes_to_anime(themes: dict, anime: Anime, session):
    """
    Helping method for insert_anime_by_name_jikan method
    Is not used separately
    """
    try:
        for theme in themes:
            theme_name = theme['name']
            theme_db = session.query(Theme).filter(Theme.name == theme_name).first()
            if theme_db:
                anime.themes.append(theme_db)
            else:
                theme_db = Theme(theme_name)
                session.add(theme_db)
                anime.themes.append(theme_db)
    except:
        session.rollback()
        raise
