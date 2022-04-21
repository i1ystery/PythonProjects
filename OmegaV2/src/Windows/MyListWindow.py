from sys import exc_info
from typing import Union
from PyQt5 import QtCore, QtGui, QtWidgets

from Windows.AddAnimeToList import AddAnimeWindow
from Windows.AddMangaToList import AddMangaWindow
from Windows.AnimeInfo import AnimeInfo
from Windows.ErrorWindow import ErrorWindow
from Windows.MangaInfo import MangaInfo
from Windows.Mode import Mode
from models.User import User, UserAnimeListItem, UserMangaListItem
import scripts.Configuration as config
from scripts.ImageOperations import get_image, remove_old_images
from DBCommunication.DBRetrievePages import get_user_anime_page, get_user_manga_page
from DBCommunication.UserInterface import delete_user_item
from models.Status import Status
from Windows.MyListWindowUI import main_ui


class MyListWindow(object):

    def __init__(self, parent, window):
        """
        Initializes window and opens it
        :param window:
        :param parent: main window
        """
        self.parent = parent
        self.parent.window.hide()
        self.window = window
        self.current_page = 1
        self.first_item = None
        self.second_item = None
        self.third_item = None
        # LOAD WINDOW UI FROM MyListWindowUI MODULE
        main_ui(self)
        self.window.show()

    def delete_item(self, item):
        """
        Deletes item from user's list
        :param item:
        """
        delete_user_item(self.parent.session, item)
        self.load_page()

    def filter_items(self):
        """
        Filters shown items
        """
        try:
            self.load_page(Status(self.filter_box.currentText()))
        except:
            self.err = ErrorWindow(exc_info())

    def back_to_menu(self):
        """
        Returns user to menu
        """
        try:
            self.window.close()
            self.parent.load_page()
            self.parent.window.show()
        except:
            self.err = ErrorWindow(exc_info())

    def switch_modes(self):
        """
        Switches current mode to ANIME/MANGA
        """
        try:
            if self.parent.mode == Mode.ANIME:
                self.parent.mode = Mode.MANGA
            else:
                self.parent.mode = Mode.ANIME
            self.current_page = 1
            self.load_page()
        except:
            self.err = ErrorWindow(exc_info())

    def item_info(self, item):
        """
        Opens chosen item info window
        :param item:
        """
        try:
            self.item_info_window = QtWidgets.QMainWindow()
            if self.parent.mode == Mode.ANIME:
                self.item_info_ui = AnimeInfo(self.item_info_window, item.anime, None, self.parent.session)
            else:
                self.item_info_ui = MangaInfo(self.item_info_window, item.manga, None, self.parent.session)
        except:
            self.err = ErrorWindow(exc_info())

    def update_item(self, item: Union[UserAnimeListItem, UserMangaListItem]):
        """
        Opens update window for chosen item
        :param item:
        :return:
        """
        try:
            self.add_to_list_window = QtWidgets.QMainWindow()
            if self.parent.mode == Mode.ANIME:
                self.add_to_list_ui = AddAnimeWindow(self.add_to_list_window, item, self.parent.session)
            else:
                self.add_to_list_ui = AddMangaWindow(self.add_to_list_window, item, self.parent.session)
        except:
            self.err = ErrorWindow(exc_info())

    def load_page(self, item_filter: Status = Status.ALL, load_mode: int = 0):
        """
        Loads user's anime or manga page
        :param item_filter: filter, by default set to ALL
        :param load_mode: 0 - first page, -1 - previous page, 1 - next page
        """
        try:
            self.switch_mode.setText(
                f"Switch to {Mode.MANGA.value if self.parent.mode == Mode.ANIME else Mode.ANIME.value}")
            self.filter_box.setItemText(3, Status.PLAN_TO_WATCH.value if self.parent.mode == Mode.ANIME else Status.PLAN_TO_READ.value)
            self.filter_box.setItemText(4, Status.WATCHING.value if self.parent.mode == Mode.ANIME else Status.READING.value)
            # MODE 0 = FIRST PAGE
            if load_mode == 0:
                if self.parent.mode == Mode.ANIME:
                    items = get_user_anime_page(
                        self.parent.session, self.parent.logged_user,
                        item_filter=item_filter, mode=load_mode
                    )
                elif self.parent.mode == Mode.MANGA:
                    items = get_user_manga_page(
                        self.parent.session, self.parent.logged_user,
                        item_filter=item_filter, mode=load_mode
                    )
                self.items_setup(items)
                self.current_page = 1
            # MODE 1 = NEXT PAGE
            if load_mode == 1:
                if self.third_item:
                    if self.parent.mode == Mode.ANIME:
                        items = get_user_anime_page(
                            self.parent.session, self.parent.logged_user,
                            user_anime_id=self.third_item.id, item_filter=item_filter, mode=load_mode
                        )
                    elif self.parent.mode == Mode.MANGA:
                        items = get_user_manga_page(
                            self.parent.session, self.parent.logged_user,
                            user_manga_id=self.third_item.id, item_filter=item_filter, mode=load_mode
                        )
                    if items:
                        self.items_setup(items)
                        self.current_page += 1
            # MODE -1 = PREVIOUS PAGE
            if load_mode == -1:
                if self.current_page > 1:
                    if self.parent.mode == Mode.ANIME:
                        items = get_user_anime_page(
                            self.parent.session, self.parent.logged_user,
                            user_anime_id=self.first_item.id, mode=load_mode, item_filter=item_filter
                        )
                    elif self.parent.mode == Mode.MANGA:
                        items = get_user_manga_page(
                            self.parent.session, self.parent.logged_user,
                            user_manga_id=self.first_item.id, item_filter=item_filter, mode=load_mode
                        )
                    if items:
                        self.items_setup(items)
                        self.current_page -= 1
        except:
            self.err = ErrorWindow(exc_info())

    def items_setup(self, items: list):
        """
        Sets loaded anime/manga data
        :param items:
        """
        try:
            self.first_item = items[0]
            remove_old_images()
            self.set_first_item()
            self.first_item_bg.setVisible(True)
        except:
            self.first_item_bg.setVisible(False)
            self.first_item = None
        try:
            self.second_item = items[1]
            self.set_second_item()
            self.second_item_bg.setVisible(True)
        except:
            self.second_item_bg.setVisible(False)
            self.second_item = None
        try:
            self.third_item = items[2]
            self.set_third_item()
            self.third_item_bg.setVisible(True)
        except:
            self.third_item_bg.setVisible(False)
            self.third_item = None

    def set_first_item(self):
        """
        Sets first anime/manga data
        """
        try:
            self.first_item_status_value.setText(self.first_item.status)
            self.first_item_score_value.setText(str(self.first_item.score))
            if isinstance(self.first_item, UserAnimeListItem):
                get_image(self.first_item.anime)
                self.first_item_img.setPixmap(QtGui.QPixmap(f"{config.images_path}/Items/{self.first_item.anime.id}.jpg"))
                self.first_item_title.setText(self.first_item.anime.title)
                self.first_item_counter1.setText("Episodes")
                self.first_item_counter2.setVisible(False)
                self.first_item_counter2_value.setVisible(False)
                self.first_item_counter1_value.setText(str(self.first_item.episodes_watched))
            elif isinstance(self.first_item, UserMangaListItem):
                get_image(self.first_item.manga)
                self.first_item_img.setPixmap(QtGui.QPixmap(f"{config.images_path}/Items/{self.first_item.manga.id}.jpg"))
                self.first_item_title.setText(self.first_item.manga.title)
                self.first_item_counter1.setText("Chapters")
                self.first_item_counter2.setVisible(True)
                self.first_item_counter2_value.setVisible(True)
                self.first_item_counter1_value.setText(str(self.first_item.chapters_read))
                self.first_item_counter2_value.setText(str(self.first_item.volumes_read))
        except:
            self.err = ErrorWindow(exc_info())

    def set_second_item(self):
        """
        Sets second anime/manga data
        """
        try:
            self.second_item_status_value.setText(self.second_item.status)
            self.second_item_score_value.setText(str(self.second_item.score))
            if isinstance(self.second_item, UserAnimeListItem):
                get_image(self.second_item.anime)
                self.second_item_img.setPixmap(QtGui.QPixmap(f"{config.images_path}/Items/{self.second_item.anime.id}.jpg"))
                self.second_item_title.setText(self.second_item.anime.title)
                self.second_item_counter1.setText("Episodes")
                self.second_item_counter2.setVisible(False)
                self.second_item_counter2_value.setVisible(False)
                self.second_item_counter1_value.setText(str(self.second_item.episodes_watched))
            elif isinstance(self.second_item, UserMangaListItem):
                get_image(self.second_item.manga)
                self.second_item_img.setPixmap(QtGui.QPixmap(f"{config.images_path}/Items/{self.second_item.manga.id}.jpg"))
                self.second_item_title.setText(self.second_item.manga.title)
                self.second_item_counter1.setText("Chapters")
                self.second_item_counter2.setVisible(True)
                self.second_item_counter2_value.setVisible(True)
                self.second_item_counter1_value.setText(str(self.second_item.chapters_read))
                self.second_item_counter2_value.setText(str(self.second_item.volumes_read))
        except:
            self.err = ErrorWindow(exc_info())

    def set_third_item(self):
        """
        Sets third anime/manga data
        """
        try:
            self.third_item_status_value.setText(self.third_item.status)
            self.third_item_score_value.setText(str(self.third_item.score))
            if isinstance(self.third_item, UserAnimeListItem):
                get_image(self.third_item.anime)
                self.third_item_img.setPixmap(QtGui.QPixmap(f"{config.images_path}/Items/{self.third_item.anime.id}.jpg"))
                self.third_item_title.setText(self.third_item.anime.title)
                self.third_item_counter1.setText("Episodes")
                self.third_item_counter2.setVisible(False)
                self.third_item_counter2_value.setVisible(False)
                self.third_item_counter1_value.setText(str(self.third_item.episodes_watched))
            elif isinstance(self.third_item, UserMangaListItem):
                get_image(self.third_item.manga)
                self.third_item_img.setPixmap(QtGui.QPixmap(f"{config.images_path}/Items/{self.third_item.manga.id}.jpg"))
                self.third_item_title.setText(self.third_item.manga.title)
                self.third_item_counter1.setText("Chapters")
                self.third_item_counter2.setVisible(True)
                self.third_item_counter2_value.setVisible(True)
                self.third_item_counter1_value.setText(str(self.third_item.chapters_read))
                self.third_item_counter2_value.setText(str(self.third_item.volumes_read))
        except:
            self.err = ErrorWindow(exc_info())
