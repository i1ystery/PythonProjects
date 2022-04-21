from sys import exc_info

from PyQt5 import QtCore, QtGui, QtWidgets
from Windows.CharacterWindow import CharacterWindow
from Windows.EpisodeWindow import EpisodeWindow
from Windows.AddAnimeToList import AddAnimeWindow
from Windows.ErrorWindow import ErrorWindow
from Windows.AnimeInfoUI import main_ui
from models.Anime import Anime
from scripts.ImageOperations import remove_old_images
import scripts.Configuration as config
from typing import Union


from models.User import User


class AnimeInfo(object):

    def __init__(self, window, anime: Anime, user: Union[User, None], session):
        """
        Initializes window and opens it
        :param window:
        :param anime:
        :param user:
        :param session:
        """
        self.anime = anime
        self.window = window
        self.user = user
        self.session = session
        # LOAD WINDOW UI FROM AnimeInfoUI MODULE
        main_ui(self)
        self.window.show()

    def close_event(self, event):
        """
        On close event removes images and closes the window
        :param event:
        """
        try:
            remove_old_images(f'{config.images_path}/Characters')
            event.accept()  # let the window close
        except:
            self.err = ErrorWindow(exc_info())

    def close(self):
        self.window.close()

    def character_info(self):
        """
        Opens chosen character info window from dropdown list
        """
        try:
            try:
                chosen_character = self.anime.anime_characters[self.character_drop.currentIndex()]
                self.char_info = QtWidgets.QMainWindow()
                self.char_info_ui = CharacterWindow(self.char_info, chosen_character)
            except:
                pass
        except:
            self.err = ErrorWindow(exc_info())

    def episode_info(self):
        """
        Opens chosen episode info window from dropdown list
        """
        try:
            try:
                chosen_episode = self.anime.episodes[self.episode_drop.currentIndex()]
                self.episode_info = QtWidgets.QMainWindow()
                self.episode_info_ui = EpisodeWindow(self.episode_info, chosen_episode, self.anime)
            except:
                pass
        except:
            self.err = ErrorWindow(exc_info())

    def add_list(self):
        """
        Opens add to anime list window
        """
        try:
            self.add_to_list_window = QtWidgets.QMainWindow()
            self.add_to_list_ui = AddAnimeWindow(self.add_to_list_window, self.anime, self.session, self.user)
        except:
            self.err = ErrorWindow(exc_info())

    def set_character_dropdown(self):
        """
        Sets choices for character dropdown
        """
        try:
            characters = self.anime.anime_characters
            for character in characters:
                self.character_drop.addItem(character.name)
        except:
            self.err = ErrorWindow(exc_info())

    def set_episode_dropdown(self):
        """
        Sets choices for episode dropdown
        """
        try:
            episodes = self.anime.episodes
            for episode in episodes:
                self.episode_drop.addItem(episode.title)
        except:
            self.err = ErrorWindow(exc_info())

    def get_genres(self) -> str:
        """
        Gets all current anime genres
        :return: genres as string
        """
        try:
            anime_genres = self.anime.genres
            genres = ''
            for genre in anime_genres:
                genres += f'{genre.name}\n'
            return genres
        except:
            self.err = ErrorWindow(exc_info())

    def get_themes(self) -> str:
        """
        Gets all current anime themes
        :return: themes as string
        """
        try:
            anime_themes = self.anime.themes
            themes = ''
            for theme in anime_themes:
                themes += f'{theme.name}\n'
            return themes
        except:
            self.err = ErrorWindow(exc_info())
