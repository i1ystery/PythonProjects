import requests
import AnimeEntry
import MangaEntry

#MAL API
ANIME_LIST = 'https://api.myanimelist.net/v2/users/{}/animelist?fields=list_status&limit={}'
UPDATE_ALIST = 'https://api.myanimelist.net/v2/anime/{}/my_list_status'
DELETE_ALIST = 'https://api.myanimelist.net/v2/anime/{}/my_list_status'
ANIME = 'https://api.myanimelist.net/v2/anime/{}?fields=id,title,main_picture,alternative_titles,start_date,end_date,' \
        'synopsis,mean,rank,popularity,num_list_users,num_scoring_users,nsfw,created_at,updated_at,media_type,status,genres,' \
        'my_list_status,num_episodes,start_season,broadcast,source,average_episode_duration,rating,pictures,background,' \
        'related_anime,related_manga,recommendations,studios,statistics'
FIND_ANIME = 'https://api.myanimelist.net/v2/anime/?q={}'

MAL_USER_INFO = 'https://api.myanimelist.net/v2/users/@me?fields=anime_statistics'

MANGA_LIST = 'https://api.myanimelist.net/v2/users/@me/mangalist?fields=list_status&limit={}'
UPDATE_MLIST = 'https://api.myanimelist.net/v2/manga/{}/my_list_status'
DELETE_MLIST = 'https://api.myanimelist.net/v2/manga/{}/my_list_status'
MANGA = ''

#Jikan MAL API


def get_usr_anime_list(access_token: str, anime_count: int = 100) -> dict:
    response = requests.get(ANIME_LIST.format('@me', anime_count),
                            headers={'Authentication': f'Bearer {access_token}'})
    response.raise_for_status()
    return response.json()


def get_user_info(access_token: str) -> dict:
    response = requests.get(MAL_USER_INFO, headers={'Authentication': f'Bearer {access_token}'})
    response.raise_for_status()
    return response.json()


def get_anime(access_token: str, anime_id: int) -> dict:
    response = requests.get(ANIME.format(anime_id),
                            headers={'Authentication': f'Bearer {access_token}'})
    response.raise_for_status()
    return response.json()