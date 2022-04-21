from sys import exc_info
from PyQt5 import QtCore, QtGui, QtWidgets
from models.Anime import Anime
from models.Status import Status
from models.User import User, UserAnimeListItem
from Windows.DialogBox import DialogBox
from Windows.ErrorWindow import ErrorWindow
from typing import Union


class AddAnimeWindow(object):

    def __init__(self, window, anime: Union[Anime, UserAnimeListItem], session, user: User = None):
        """
        Initializes window and opens it
        :param window:
        :param anime:
        :param session:
        :param user:
        """
        self.anime = anime
        self.window = window
        self.user = user
        self.session = session
        self.main_ui()
        self.window.show()

    def main_ui(self):
        """
        Setups and loads window UI
        :return:
        """
        try:
            self.window.resize(600, 200)
            self.window.setMaximumSize(QtCore.QSize(600, 200))
            self.window.setMinimumSize(QtCore.QSize(600, 200))
            # Central widget
            self.centralwidget = QtWidgets.QWidget(self.window)
            self.centralwidget.setMaximumSize(QtCore.QSize(600, 200))
            self.centralwidget.setMinimumSize(QtCore.QSize(600, 200))
            self.centralwidget.setStyleSheet("background-color: rgb(52, 52, 52)")

            # Layout
            self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)

            # Score dropdown
            self.score_dropdown = QtWidgets.QComboBox(self.centralwidget)
            self.score_dropdown.setMinimumSize(QtCore.QSize(0, 40))
            self.score_dropdown.setStyleSheet(
                "color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";background-color: rgb(27, 27, 45)")
            self.gridLayout_2.addWidget(self.score_dropdown, 2, 1, 1, 1)

            # Anime name
            self.anime_name = QtWidgets.QLabel(self.centralwidget)
            self.anime_name.setMinimumSize(QtCore.QSize(0, 40))
            self.anime_name.setStyleSheet("color: rgb(255, 255, 255); font: 63 20pt \"Segoe UI Variable Display Semib\";")
            self.anime_name.setAlignment(QtCore.Qt.AlignCenter)
            self.gridLayout_2.addWidget(self.anime_name, 0, 0, 1, 4)

            # Score label
            self.score_lbl = QtWidgets.QLabel(self.centralwidget)
            self.score_lbl.setMinimumSize(QtCore.QSize(0, 20))
            self.score_lbl.setStyleSheet("color: rgb(255, 255, 255); font: 63 13pt \"Segoe UI Variable Display Semib\";")
            self.gridLayout_2.addWidget(self.score_lbl, 1, 1, 1, 1)

            # Episodes label
            self.episodes_lbl = QtWidgets.QLabel(self.centralwidget)
            self.episodes_lbl.setMinimumSize(QtCore.QSize(0, 15))
            self.episodes_lbl.setMaximumSize(QtCore.QSize(16777215, 15))
            self.episodes_lbl.setStyleSheet("color: rgb(255, 255, 255); font: 63 13pt \"Segoe UI Variable Display Semib\";")
            self.gridLayout_2.addWidget(self.episodes_lbl, 1, 2, 1, 1)

            # Status dropdown
            self.status_dropdown = QtWidgets.QComboBox(self.centralwidget)
            self.status_dropdown.setMinimumSize(QtCore.QSize(160, 40))
            self.status_dropdown.setStyleSheet(
                "color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";background-color: rgb(27, 27, 45)")
            self.gridLayout_2.addWidget(self.status_dropdown, 2, 0, 1, 1)

            # Status label
            self.status_lbl = QtWidgets.QLabel(self.centralwidget)
            self.status_lbl.setMinimumSize(QtCore.QSize(0, 20))
            self.status_lbl.setStyleSheet("color: rgb(255, 255, 255); font: 63 13pt \"Segoe UI Variable Display Semib\";")
            self.gridLayout_2.addWidget(self.status_lbl, 1, 0, 1, 1)

            # Episodes dropdown
            self.episodes_dropdown = QtWidgets.QComboBox(self.centralwidget)
            self.episodes_dropdown.setMinimumSize(QtCore.QSize(0, 40))
            self.episodes_dropdown.setMaximumSize(QtCore.QSize(16777215, 60))
            self.episodes_dropdown.setStyleSheet(
                "color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";background-color: rgb(27, 27, 45)")
            self.gridLayout_2.addWidget(self.episodes_dropdown, 2, 2, 1, 1)

            # Save button
            self.save_btn = QtWidgets.QPushButton(self.centralwidget)
            self.save_btn.setMinimumSize(QtCore.QSize(0, 70))
            self.save_btn.setStyleSheet(
                "color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";background-color: rgb(27, 27, 45)")
            self.gridLayout_2.addWidget(self.save_btn, 1, 3, 2, 1)
            self.window.setCentralWidget(self.centralwidget)

            # UI load
            self.load_ui()
            QtCore.QMetaObject.connectSlotsByName(self.window)
        except:
            self.err = ErrorWindow(exc_info())

    def load_ui(self):
        """
        Loads UI
        :return:
        """
        try:
            self.score_lbl.setText("Your score")
            self.score_dropdown.addItem("1")
            self.score_dropdown.addItem("2")
            self.score_dropdown.addItem("3")
            self.score_dropdown.addItem("4")
            self.score_dropdown.addItem("5")
            self.score_dropdown.addItem("6")
            self.score_dropdown.addItem("7")
            self.score_dropdown.addItem("8")
            self.score_dropdown.addItem("9")
            self.score_dropdown.addItem("10")
            self.status_lbl.setText("Status")
            self.status_dropdown.addItem(Status.PLAN_TO_WATCH.value)
            self.status_dropdown.addItem(Status.COMPLETED.value)
            self.status_dropdown.addItem(Status.WATCHING.value)
            self.status_dropdown.addItem(Status.DROPPED.value)
            self.episodes_lbl.setText("Episodes watched")
            self.save_btn.setText("Save")

            # If class anime item type is UserAnimeList item
            # Set ui for item update
            if isinstance(self.anime, UserAnimeListItem):
                self.window.setWindowTitle(self.anime.anime.title)
                self.anime_name.setText(self.anime.anime.title)
                self.save_btn.clicked.connect(self.update_anime)
                self.set_episodes_dropdown(self.anime.anime)
            else:
                self.window.setWindowTitle(self.anime.title)
                self.anime_name.setText(self.anime.title)
                self.save_btn.clicked.connect(self.add_to_list)
                self.set_episodes_dropdown(self.anime)
        except:
            self.err = ErrorWindow(exc_info())

    def set_episodes_dropdown(self, anime: Anime):
        """
        Sets choices for episodes dropdown
        :param anime:
        """
        try:
            if anime.num_episodes:
                for i in range(anime.num_episodes + 1):
                    self.episodes_dropdown.addItem(f'{i}')
            else:
                self.episodes_dropdown.addItem('Currently no episodes')
        except:
            self.err = ErrorWindow(exc_info())

    def update_anime(self):
        """
        Updates anime item in users list
        :return:
        """
        try:
            from DBCommunication.UserInterface import update_user_anime
            status = self.status_dropdown.currentText()
            score = self.score_dropdown.currentIndex() + 1
            episodes = self.episodes_dropdown.currentIndex()
            result = update_user_anime(self.session, self.anime, status, score, episodes)
            self.open_dialog(result)
        except:
            self.err = ErrorWindow(exc_info())

    def add_to_list(self):
        """
        Adds anime item to users list
        :return:
        """
        try:
            from DBCommunication.UserInterface import add_anime_to_user_list
            status = self.status_dropdown.currentText()
            score = self.score_dropdown.currentIndex() + 1
            episodes = self.episodes_dropdown.currentIndex()
            result = add_anime_to_user_list(self.session, self.user, self.anime, status, score, episodes)
            self.open_dialog(result)
        except:
            self.err = ErrorWindow(exc_info())

    def open_dialog(self, message):
        """
        Opens dialog window with given message
        :param message:
        """
        try:
            self.current_window = QtWidgets.QDialog()
            self.ui = DialogBox(self.window, self.current_window)
            self.ui.main_ui(message)
            self.current_window.show()
        except:
            self.err = ErrorWindow(exc_info())
