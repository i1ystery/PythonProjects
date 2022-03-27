class Anime:
    def __init__(self, anime_data: dict):
        self.anime_id = anime_data['id']
        self.anime_title = anime_data['title']
        self.media_type = anime_data['media_type']
        self.start_date = anime_data['start_date']
        self.end_date = anime_data['end_date']
        self.synopsis = anime_data['synopsis']
        self.mean_score = anime_data['mean']
        self.popularity = anime_data['popularity']
        self.status = anime_data['status']
        self.genres = list()
        for genre in anime_data['genres']:
            self.genres.append(genre['name'])
        self.anime_image = anime_data['main_picture']['medium']
        self.user_watched_episodes = anime_data['my_list_status']['num_episodes_watched']
        self.user_score = anime_data['my_list_status']['score']
        self.user_status = anime_data['my_list_status']['status']
        self.user_rewatching = True if anime_data['my_list_status']['is_rewatching'] == 'true' else False


    def __str__(self):
        return f'Anime: {self.anime_title}\n'