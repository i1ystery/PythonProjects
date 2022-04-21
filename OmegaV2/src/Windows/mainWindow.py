from PyQt5 import QtCore, QtGui, QtWidgets
from Windows.ErrorWindow import ErrorWindow
from Windows.adminWindow import AdminWindow
from models.Database import Session
from Windows.LoginWindow import *
from Windows.AnimeInfo import *
from Windows.MangaInfo import *
from Windows.MyListWindow import *
from Windows.Mode import Mode
from Windows.mainWindowUI import main_ui
import scripts.Configuration as config
from scripts.ImageOperations import load_images
from models.User import User
from DBCommunication.DBRetrievePages import get_anime_page, get_manga_page, get_random_anime, get_random_manga
from sys import exc_info


class MainPage(object):

    def __init__(self, current_window):
        """
        Initializes window and opens it
        :param current_window:
        """
        self.window = current_window
        self.logged_user = None
        self.mode = Mode.ANIME
        self.current_page = 1
        self.session = Session()
        self.first_item = None
        self.second_item = None
        self.third_item = None
        # LOAD UI FROM mainWindowUI MODULE
        main_ui(self)
        self.window.show()

    def load_random(self):
        """
        Gets random anime and opens Anime Info window
        :return:
        """
        try:
            if self.mode == Mode.ANIME:
                item = get_random_anime(self.session)
            elif self.mode == Mode.MANGA:
                item = get_random_manga(self.session)
            if item:
                get_image(item)
                self.item_info(item)
        except:
            self.err = ErrorWindow(exc_info())

    def load_page(self, load_mode: int = 0):
        """
        Loads anime or manga page
        :param load_mode: 0 - first page, -1 - previous page, 1 - next page
        """
        try:
            self.switch_mode.setText(f"Switch to {Mode.MANGA.value if self.mode == Mode.ANIME else Mode.ANIME.value}")
            self.random_item.setText(f"Random {Mode.ANIME.value if self.mode == Mode.ANIME else Mode.MANGA.value}")
            # MODE 0 = FIRST PAGE
            if load_mode == 0:
                if self.mode == Mode.ANIME:
                    items = get_anime_page(self.session, mode=load_mode)
                elif self.mode == Mode.MANGA:
                    items = get_manga_page(self.session, mode=load_mode)
                self.items_setup(items)
                self.current_page = 1
            # MODE 1 = NEXT PAGE
            if load_mode == 1:
                if self.third_item:
                    if self.mode == Mode.ANIME:
                        items = get_anime_page(self.session, self.third_item.id, mode=load_mode)
                    elif self.mode == Mode.MANGA:
                        items = get_manga_page(self.session, self.third_item.id, mode=load_mode)
                    if items:
                        self.items_setup(items)
                        self.current_page += 1
            # MODE -1 = PREVIOUS PAGE
            if load_mode == -1:
                if self.current_page > 1:
                    if self.mode == Mode.ANIME:
                        items = get_anime_page(self.session, self.first_item.id, mode=load_mode)
                    elif self.mode == Mode.MANGA:
                        items = get_manga_page(self.session, self.first_item.id, mode=load_mode)
                    if items:
                        self.items_setup(items)
                        self.current_page -= 1
        except:
            self.err = ErrorWindow(exc_info())

    def admin_window(self):
        """
        Opens admin window
        """
        try:
            self.admin = QtWidgets.QMainWindow()
            self.admin = AdminWindow(self.session, self.admin, self)
        except:
            self.err = ErrorWindow(exc_info())

    def items_setup(self, items: list):
        """
        Sets loaded anime/manga data
        :param items:
        """
        try:
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
        except:
            self.err = ErrorWindow(exc_info())

    def set_first_item(self):
        """
        Sets first anime/manga data
        """
        if self.first_item:
            get_image(self.first_item)
            self.first_item_title.setText(self.first_item.title)
            self.first_item_synopsis.setText(self.first_item.synopsis)
            self.first_item_img.setPixmap(QtGui.QPixmap(f"{config.images_path}/Items/{self.first_item.id}.jpg"))

    def set_second_item(self):
        """
        Sets second anime/manga data
        """
        if self.second_item:
            get_image(self.second_item)
            self.second_item_title.setText(self.second_item.title)
            self.second_item_synopsis.setText(self.second_item.synopsis)
            self.second_item_img.setPixmap(QtGui.QPixmap(f"{config.images_path}/Items/{self.second_item.id}.jpg"))

    def set_third_item(self):
        """
        Sets third anime/manga data
        """
        if self.third_item:
            get_image(self.third_item)
            self.third_item_title.setText(self.third_item.title)
            self.third_item_synopsis.setText(self.third_item.synopsis)
            self.third_item_img.setPixmap(QtGui.QPixmap(f"{config.images_path}/Items/{self.third_item.id}.jpg"))

    def login(self):
        """
        Opens login window
        """
        try:
            self.login_window = QtWidgets.QMainWindow()
            self.login_ui = LoginWindow(self, self.login_window)
        except:
            self.err = ErrorWindow(exc_info())

    def logout(self):
        """
        Method used to log out user
        """
        try:
            self.logged_as.hide()
            self.my_list_button.hide()
            self.admin_button.hide()
            self.logged_user = None
            self.login_button.setText('Login')
            self.load_page()
            self.login_button.clicked.connect(self.login)
            self.login_button.clicked.disconnect(self.logout)
        except:
            self.err = ErrorWindow(exc_info())

    def logged_in_ui(self, user: User):
        """
        Sets windows UI for logged user
        :param user:
        """
        try:
            self.logged_user = user
            self.logged_as.show()
            self.my_list_button.show()
            if self.logged_user.is_admin:
                self.admin_button.show()
            self.logged_as.setText(f'Logged as {self.logged_user.username}')
            self.login_button.setText('Logout')
            self.load_page()
            self.login_button.clicked.disconnect(self.login)
            self.login_button.clicked.connect(self.logout)
        except:
            self.err = ErrorWindow(exc_info())

    def open_my_list(self):
        """
        Opens MyList window
        """
        try:
            self.my_list = QtWidgets.QMainWindow()
            self.my_list_ui = MyListWindow(self, self.my_list)
        except:
            self.err = ErrorWindow(exc_info())

    def item_info(self, item):
        """
        Opens item info window
        :param item:
        """
        try:
            self.item_info_window = QtWidgets.QMainWindow()
            if self.mode == Mode.ANIME:
                self.item_info_ui = AnimeInfo(self.item_info_window, item, self.logged_user, self.session)
            else:
                self.item_info_ui = MangaInfo(self.item_info_window, item, self.logged_user, self.session)
        except:
            self.err = ErrorWindow(exc_info())

    def switch_modes(self):
        """
        Switches current mode to ANIME/MANGA
        """
        try:
            if self.mode == Mode.ANIME:
                self.mode = Mode.MANGA
            else:
                self.mode = Mode.ANIME
            self.current_page = 1
            self.load_page()
        except:
            self.err = ErrorWindow(exc_info())


def run():
    """
    Method used to run application
    :return:
    """
    import sys
    try:
        app = QtWidgets.QApplication(sys.argv)
        main_window = QtWidgets.QMainWindow()
        MainPage(main_window)
    except:
        exc_type, exc_name, ext_tb = exc_info()
        ErrorWindow((exc_type, exc_name, ext_tb))
    finally:
        sys.exit(app.exec_())


