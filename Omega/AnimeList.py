from API_Client import *


class AnimeList:
    def __init__(self):
        self.animes = list()
        self.user_stats = None

    def load_list(self, token: dict):
        access_token = token['access_token']
        user_info_data = get_user_info(access_token)
        user_stats = AnimeListUserStats(user_info_data)
        anime_list_data = get_usr_anime_list(access_token, user_stats.overall_count)
        anime_list = list()
        for anime in anime_list_data['data']:
            anime_list.append(AnimeListEntry(anime))
        self.animes = anime_list
        self.user_stats = user_stats


class AnimeListUserStats:
    def __init__(self, data: dict):
        stats = data['anime_statistics']
        self.watching = stats['num_items_watching']
        self.completed = stats['num_items_completed']
        self.on_hold = stats['num_items_on_hold']
        self.dropped = stats['num_items_dropped']
        self.plan_to_watch = stats['num_items_plan_to_watch']
        self.overall_count = stats['num_items']
        self.total_episodes_watched = ['num_episodes']
        self.rewatched_anime_count = ['num_times_rewatched']
        self.mean_score = ['mean_score']


class AnimeListEntry:
    def __init__(self, data: dict):
        anime = data['node']
        user_list_status = data['list_status']
        self.anime_id = anime['id']
        self.anime_title = anime['title']
        self.anime_image = anime['main_picture']['medium']
        self.user_status = user_list_status['status']
        self.user_score = user_list_status['score']
        self.user_watched_episodes = user_list_status['num_episodes_watched']
        self.user_rewatching = True if user_list_status['is_rewatching'] == 'true' else False
        self.user_last_upd = user_list_status['updated_at']

