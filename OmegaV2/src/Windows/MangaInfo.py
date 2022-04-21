from sys import exc_info

from PyQt5 import QtCore, QtGui, QtWidgets
from Windows.AddMangaToList import AddMangaWindow
from Windows.CharacterWindow import CharacterWindow
from Windows.ErrorWindow import ErrorWindow
from models.Manga import Manga
import scripts.Configuration as config
from typing import Union
from models.User import User


class MangaInfo(object):

    def __init__(self, window, manga: Manga, user: Union[User, None], session):
        """
        Initializes window and opens it
        :param window:
        :param manga:
        :param user:
        :param session:
        """
        self.manga = manga
        self.window = window
        self.user = user
        self.session = session
        self.main_ui()
        self.window.show()

    def main_ui(self):
        """
        Setups and loads window UI
        """
        try:
            self.window.setObjectName("MainWindow")
            self.window.resize(630, 570)
            self.window.setMinimumSize(QtCore.QSize(630, 570))
            self.window.setMaximumSize(QtCore.QSize(630, 570))

            # Central widgget
            self.centralwidget = QtWidgets.QWidget(self.window)
            self.centralwidget.setObjectName("centralwidget")\

            # Background
            self.bg = QtWidgets.QFrame(self.centralwidget)
            self.bg.setGeometry(QtCore.QRect(0, 0, 630, 570))
            self.bg.setStyleSheet("background-color: rgb(52, 52, 52)")
            self.bg.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.bg.setFrameShadow(QtWidgets.QFrame.Raised)
            self.bg.setObjectName("bg")

            # Image
            self.image = QtWidgets.QLabel(self.bg)
            self.image.setGeometry(QtCore.QRect(20, 20, 150, 210))
            self.image.setText("")
            self.image.setPixmap(QtGui.QPixmap(""))
            self.image.setScaledContents(True)
            self.image.setObjectName("image")

            # Manga name
            self.manga_name = QtWidgets.QLabel(self.bg)
            self.manga_name.setGeometry(QtCore.QRect(175, 20, 461, 41))
            font = QtGui.QFont()
            font.setFamily("Segoe UI Variable Display Semib")
            font.setPointSize(14)
            font.setBold(False)
            font.setItalic(False)
            font.setWeight(7)
            self.manga_name.setFont(font)
            self.manga_name.setStyleSheet("color: rgb(255, 255, 255); font: 63 14pt Segoe UI Variable Display Semib;")
            self.manga_name.setObjectName("manga_name")

            # English title label
            self.en_title = QtWidgets.QLabel(self.bg)
            self.en_title.setGeometry(QtCore.QRect(175, 60, 101, 21))
            self.en_title.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
            self.en_title.setObjectName("en_title")

            # English name
            self.en_name = QtWidgets.QLabel(self.bg)
            self.en_name.setGeometry(QtCore.QRect(300, 60, 321, 21))
            self.en_name.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
            self.en_name.setObjectName("en_name")

            # Japanese title label
            self.jp_title = QtWidgets.QLabel(self.bg)
            self.jp_title.setGeometry(QtCore.QRect(175, 90, 111, 21))
            self.jp_title.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
            self.jp_title.setObjectName("jp_title")

            # Japanese title
            self.jp_name = QtWidgets.QLabel(self.bg)
            self.jp_name.setGeometry(QtCore.QRect(300, 90, 321, 21))
            self.jp_name.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
            self.jp_name.setObjectName("jp_name")

            # Score label
            self.score = QtWidgets.QLabel(self.bg)
            self.score.setGeometry(QtCore.QRect(501, 130, 81, 21))
            self.score.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
            self.score.setObjectName("score")

            # Score
            self.score_number = QtWidgets.QLabel(self.bg)
            self.score_number.setGeometry(QtCore.QRect(500, 160, 51, 21))
            self.score_number.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
            self.score_number.setAlignment(QtCore.Qt.AlignCenter)
            self.score_number.setObjectName("score_number")

            # Status label
            self.status_name = QtWidgets.QLabel(self.bg)
            self.status_name.setGeometry(QtCore.QRect(145, 240, 151, 21))
            self.status_name.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
            self.status_name.setObjectName("status_name")

            # Status
            self.current_status = QtWidgets.QLabel(self.bg)
            self.current_status.setGeometry(QtCore.QRect(20, 240, 111, 21))
            self.current_status.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
            self.current_status.setObjectName("current_status")

            # Published from
            self.published_from_date = QtWidgets.QLabel(self.bg)
            self.published_from_date.setGeometry(QtCore.QRect(145, 270, 151, 21))
            self.published_from_date.setStyleSheet(
                "color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
            self.published_from_date.setObjectName("published_from_date")

            # Published from label
            self.published_from = QtWidgets.QLabel(self.bg)
            self.published_from.setGeometry(QtCore.QRect(20, 270, 111, 21))
            self.published_from.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
            self.published_from.setObjectName("published_from")

            # Published to
            self.published_to_date = QtWidgets.QLabel(self.bg)
            self.published_to_date.setGeometry(QtCore.QRect(145, 300, 151, 21))
            self.published_to_date.setStyleSheet(
                "color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
            self.published_to_date.setObjectName("published_to_date")

            # Published to label
            self.published_to = QtWidgets.QLabel(self.bg)
            self.published_to.setGeometry(QtCore.QRect(20, 300, 111, 21))
            self.published_to.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
            self.published_to.setObjectName("published_to")

            # Chapters label
            self.chapters = QtWidgets.QLabel(self.bg)
            self.chapters.setGeometry(QtCore.QRect(20, 330, 111, 21))
            self.chapters.setAcceptDrops(False)
            self.chapters.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
            self.chapters.setScaledContents(False)
            self.chapters.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
            self.chapters.setWordWrap(True)
            self.chapters.setObjectName("chapters")

            # Chapters
            self.episodes_cnt = QtWidgets.QLabel(self.bg)
            self.episodes_cnt.setGeometry(QtCore.QRect(145, 330, 111, 21))
            self.episodes_cnt.setAcceptDrops(False)
            self.episodes_cnt.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
            self.episodes_cnt.setScaledContents(False)
            self.episodes_cnt.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
            self.episodes_cnt.setWordWrap(True)
            self.episodes_cnt.setObjectName("episodes_cnt")

            # Volumes label
            self.volumes = QtWidgets.QLabel(self.bg)
            self.volumes.setGeometry(QtCore.QRect(20, 360, 111, 21))
            self.volumes.setAcceptDrops(False)
            self.volumes.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
            self.volumes.setScaledContents(False)
            self.volumes.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
            self.volumes.setWordWrap(True)
            self.volumes.setObjectName("volumes")

            # Volumes
            self.volumes_cnt = QtWidgets.QLabel(self.bg)
            self.volumes_cnt.setGeometry(QtCore.QRect(145, 360, 111, 21))
            self.volumes_cnt.setAcceptDrops(False)
            self.volumes_cnt.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
            self.volumes_cnt.setScaledContents(False)
            self.volumes_cnt.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
            self.volumes_cnt.setWordWrap(True)
            self.volumes_cnt.setObjectName("volumes_cnt")

            # Genres label
            self.genres = QtWidgets.QLabel(self.bg)
            self.genres.setGeometry(QtCore.QRect(300, 240, 111, 31))
            self.genres.setAcceptDrops(False)
            self.genres.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
            self.genres.setScaledContents(False)
            self.genres.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
            self.genres.setWordWrap(True)
            self.genres.setObjectName("genres")

            # Genres
            self.genres_names = QtWidgets.QLabel(self.bg)
            self.genres_names.setGeometry(QtCore.QRect(300, 260, 161, 101))
            self.genres_names.setAcceptDrops(False)
            self.genres_names.setStyleSheet("color: rgb(255, 255, 255); font: 63 10pt Segoe UI Variable Display Semib;")
            self.genres_names.setScaledContents(False)
            self.genres_names.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
            self.genres_names.setWordWrap(True)
            self.genres_names.setObjectName("genres_names")

            # Themes label
            self.themes = QtWidgets.QLabel(self.bg)
            self.themes.setGeometry(QtCore.QRect(480, 240, 111, 31))
            self.themes.setAcceptDrops(False)
            self.themes.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
            self.themes.setScaledContents(False)
            self.themes.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
            self.themes.setWordWrap(True)
            self.themes.setObjectName("themes")

            # Themes
            self.theme_names = QtWidgets.QLabel(self.bg)
            self.theme_names.setGeometry(QtCore.QRect(480, 260, 171, 101))
            self.theme_names.setAcceptDrops(False)
            self.theme_names.setStyleSheet("color: rgb(255, 255, 255); font: 63 10pt Segoe UI Variable Display Semib;")
            self.theme_names.setScaledContents(False)
            self.theme_names.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
            self.theme_names.setWordWrap(True)
            self.theme_names.setObjectName("theme_names")

            # Add to list button
            self.add_to_list = QtWidgets.QPushButton(self.bg)
            self.add_to_list.setGeometry(QtCore.QRect(20, 510, 441, 51))
            self.add_to_list.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\"; "
                                           "background-color: rgb(27, 27, 45);")
            self.add_to_list.setObjectName("add_to_list")

            # Close button
            self.close_button = QtWidgets.QPushButton(self.bg)
            self.close_button.setGeometry(QtCore.QRect(470, 510, 141, 51))
            self.close_button.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\"; "
                                            "background-color: rgb(27, 27, 45);")
            self.close_button.setObjectName("close_btn")

            # Authors dropdown
            self.authors_drop = QtWidgets.QComboBox(self.bg)
            self.authors_drop.setGeometry(QtCore.QRect(20, 390, 251, 41))
            self.authors_drop.setMinimumSize(QtCore.QSize(0, 40))
            self.authors_drop.setStyleSheet(
                "color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";background-color: rgb(27, 27, 45)")
            self.authors_drop.setObjectName("authors_drop")

            # Character dropdown
            self.character_drop = QtWidgets.QComboBox(self.bg)
            self.character_drop.setGeometry(QtCore.QRect(20, 450, 251, 41))
            self.character_drop.setMinimumSize(QtCore.QSize(0, 40))
            self.character_drop.setStyleSheet(
                "color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";background-color: rgb(27, 27, 45)")
            self.character_drop.setObjectName("character_drop")

            # Characters button
            self.manga_characters = QtWidgets.QPushButton(self.bg)
            self.manga_characters.setGeometry(QtCore.QRect(280, 450, 151, 41))
            self.manga_characters.setStyleSheet(
                "color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\"; background-color: rgb(27, 27, 45);")
            self.manga_characters.setObjectName("anime_characters")

            # Authors button not clickable
            self.authors_button = QtWidgets.QPushButton(self.bg)
            self.authors_button.setEnabled(False)
            self.authors_button.setGeometry(QtCore.QRect(280, 390, 151, 41))
            self.authors_button.setStyleSheet(
                "color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\"; background-color: rgb(27, 27, 45);")
            self.authors_button.setCheckable(False)
            self.authors_button.setAutoDefault(False)
            self.authors_button.setDefault(False)
            self.authors_button.setFlat(False)
            self.authors_button.setObjectName("authors_button")
            self.window.setCentralWidget(self.centralwidget)

            # Button bindings
            self.add_to_list.clicked.connect(self.add_list)
            self.close_button.clicked.connect(self.close)
            self.manga_characters.clicked.connect(self.character_info)

            self.load_ui()
            QtCore.QMetaObject.connectSlotsByName(self.window)
        except:
            self.err = ErrorWindow(exc_info())

    def load_ui(self):
        """
        Loads UI
        """
        try:
            self.manga_name.setText(self.manga.title)
            self.image.setPixmap(QtGui.QPixmap(f"{config.images_path}/Items/{self.manga.id}.jpg"))
            self.window.setWindowTitle(self.manga.title)
            self.en_title.setText("English Name:")
            self.en_name.setText(self.manga.title_english)
            self.jp_title.setText("Japanese Name:")
            self.jp_name.setText(self.manga.title_japanese)
            self.score.setText("SCORE")
            self.score_number.setText(str(self.manga.score))
            self.current_status.setText("Current status")
            self.status_name.setText(self.manga.status)
            self.published_from.setText("Published from")
            self.published_from_date.setText(str(self.manga.published_from))
            self.published_to.setText("Published to")
            self.published_to_date.setText(str(self.manga.published_to))
            self.chapters.setText("Chapters")
            self.episodes_cnt.setText(str(self.manga.chapters) if self.manga.chapters else 'Unknown')
            self.volumes.setText("Volumes")
            self.volumes_cnt.setText(str(self.manga.volumes) if self.manga.volumes else 'Unknown')
            self.genres.setText("Genres")
            self.genres_names.setText(self.get_genres())
            self.themes.setText("Themes")
            self.theme_names.setText(self.get_themes())
            self.add_to_list.setText("Add to my list")
            self.close_button.setText("Close")
            self.authors_button.setText("Authors")
            self.manga_characters.setText("Show Character Info")
            if not self.user:
                self.add_to_list.setVisible(False)
            self.set_author_dropdown()
            self.set_character_dropdown()
        except:
            self.err = ErrorWindow(exc_info())

    def character_info(self):
        """
        Opens chosen character info window from dropdown list
        """
        try:
            try:
                chosen_character = self.manga.characters[self.character_drop.currentIndex()]
                self.char_info = QtWidgets.QMainWindow()
                self.char_info_ui = CharacterWindow(self.char_info, chosen_character)
            except:
                pass
        except:
            self.err = ErrorWindow(exc_info())

    def add_list(self):
        """
        Opens add to manga list window
        """
        try:
            self.add_to_list_window = QtWidgets.QMainWindow()
            self.add_to_list_ui = AddMangaWindow(self.add_to_list_window, self.manga, self.session, self.user)
        except:
            self.err = ErrorWindow(exc_info())

    def close(self):
        self.window.close()

    def set_author_dropdown(self):
        """
        Sets author dropdown
        """
        try:
            authors = self.manga.authors
            for author in authors:
                self.authors_drop.addItem(author.full_name)
        except:
            self.err = ErrorWindow(exc_info())

    def set_character_dropdown(self):
        """
        Sets choices for character dropdown
        """
        try:
            characters = self.manga.characters
            for character in characters:
                self.character_drop.addItem(character.name)
        except:
            self.err = ErrorWindow(exc_info())

    def get_genres(self) -> str:
        """
        Gets all current manga genres
        :return: genres as string
        """
        try:
            manga_genres = self.manga.genres
            genres = ''
            for genre in manga_genres:
                genres += f'{genre.name}\n'
            return genres
        except:
            self.err = ErrorWindow(exc_info())

    def get_themes(self) -> str:
        """
        Gets all current manga themes
        :return: themes as string
        """
        try:
            manga_themes = self.manga.themes
            themes = ''
            for theme in manga_themes:
                themes += f'{theme.name}\n'
            return themes
        except:
            self.err = ErrorWindow(exc_info())
