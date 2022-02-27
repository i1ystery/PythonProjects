from API_Client import *


class MangaList:
    def __init__(self):
        self.mangas = list()

    def load_list(self, token: dict):
        access_token = token['access_token']
        manga_list_data = get_usr_manga_list(access_token)
        manga_list = list()
        for manga in manga_list_data['data']:
            manga_list.append(MangaListEntry(manga))
        self.mangas = manga_list


class MangaListEntry:
    def __init__(self, manga_data: dict):
        manga = manga_data['node']
        user_list_status = manga_data['list_status']
        self.manga_id = manga['id']
        self.title = manga['title']
        self.manga_image = manga['main_picture']['medium']
        self.user_status = user_list_status['status']
        self.is_rereading = True if user_list_status['is_rereading'] == 'true' else False
        self.volumes_read = user_list_status['num_volumes_read']
        self.chapters_read = user_list_status['num_chapters_read']
        self.score = user_list_status['score']
