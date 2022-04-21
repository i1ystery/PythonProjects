from sys import exc_info

from PyQt5 import QtCore, QtGui, QtWidgets

from Windows.ErrorWindow import ErrorWindow
from models.Manga import Manga
from models.Status import Status
from models.User import User, UserMangaListItem
from Windows.DialogBox import DialogBox
from typing import Union


class AddMangaWindow(object):

    def __init__(self, window, manga: Union[Manga, UserMangaListItem], session, user: User = None):
        """
        Initializes window and opens it
        :param window:
        :param manga:
        :param session:
        :param user:
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
        :return:
        """
        try:
            self.window.resize(800, 200)
            self.window.setMaximumSize(QtCore.QSize(800, 200))
            self.window.setMinimumSize(QtCore.QSize(800, 200))

            # Central window
            self.centralwidget = QtWidgets.QWidget(self.window)
            self.centralwidget.setMaximumSize(QtCore.QSize(800, 200))
            self.centralwidget.setMinimumSize(QtCore.QSize(800, 200))
            self.centralwidget.setStyleSheet("background-color: rgb(52, 52, 52)")

            # Grid layout
            self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)

            # Score dropdown
            self.score_dropdown = QtWidgets.QComboBox(self.centralwidget)
            self.score_dropdown.setMinimumSize(QtCore.QSize(0, 40))
            self.score_dropdown.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";background-color: rgb(27, 27, 45)")
            self.gridLayout_2.addWidget(self.score_dropdown, 2, 1, 1, 1)

            # Manga name
            self.manga_name = QtWidgets.QLabel(self.centralwidget)
            self.manga_name.setMinimumSize(QtCore.QSize(0, 40))
            self.manga_name.setStyleSheet("color: rgb(255, 255, 255); font: 63 20pt \"Segoe UI Variable Display Semib\";")
            self.manga_name.setAlignment(QtCore.Qt.AlignCenter)
            self.gridLayout_2.addWidget(self.manga_name, 0, 0, 1, 5)

            # Score label
            self.score_lbl = QtWidgets.QLabel(self.centralwidget)
            self.score_lbl.setMinimumSize(QtCore.QSize(0, 20))
            self.score_lbl.setStyleSheet("color: rgb(255, 255, 255); font: 63 13pt \"Segoe UI Variable Display Semib\";")
            self.gridLayout_2.addWidget(self.score_lbl, 1, 1, 1, 1)

            # Chapters label
            self.chapters_lbl = QtWidgets.QLabel(self.centralwidget)
            self.chapters_lbl.setMinimumSize(QtCore.QSize(0, 20))
            self.chapters_lbl.setMaximumSize(QtCore.QSize(16777215, 15))
            self.chapters_lbl.setStyleSheet("color: rgb(255, 255, 255); font: 63 13pt \"Segoe UI Variable Display Semib\";")
            self.gridLayout_2.addWidget(self.chapters_lbl, 1, 2, 1, 1)

            # Save button
            self.save_btn = QtWidgets.QPushButton(self.centralwidget)
            self.save_btn.setMinimumSize(QtCore.QSize(0, 70))
            self.save_btn.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";background-color: rgb(27, 27, 45)")
            self.gridLayout_2.addWidget(self.save_btn, 1, 4, 2, 1)

            # Status dropdown
            self.status_dropdown = QtWidgets.QComboBox(self.centralwidget)
            self.status_dropdown.setMinimumSize(QtCore.QSize(160, 40))
            self.status_dropdown.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";background-color: rgb(27, 27, 45)")
            self.gridLayout_2.addWidget(self.status_dropdown, 2, 0, 1, 1)

            # Status label
            self.status_lbl = QtWidgets.QLabel(self.centralwidget)
            self.status_lbl.setMinimumSize(QtCore.QSize(0, 20))
            self.status_lbl.setStyleSheet("color: rgb(255, 255, 255); font: 63 13pt \"Segoe UI Variable Display Semib\";")
            self.gridLayout_2.addWidget(self.status_lbl, 1, 0, 1, 1)

            # Chapters dropdown
            self.chapters_dropdown = QtWidgets.QComboBox(self.centralwidget)
            self.chapters_dropdown.setMinimumSize(QtCore.QSize(0, 40))
            self.chapters_dropdown.setMaximumSize(QtCore.QSize(16777215, 60))
            self.chapters_dropdown.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";background-color: rgb(27, 27, 45)")
            self.gridLayout_2.addWidget(self.chapters_dropdown, 2, 2, 1, 1)

            # Volumes label
            self.volumes_lbl = QtWidgets.QLabel(self.centralwidget)
            self.volumes_lbl.setMinimumSize(QtCore.QSize(0, 20))
            self.volumes_lbl.setStyleSheet("color: rgb(255, 255, 255); font: 63 13pt \"Segoe UI Variable Display Semib\";")
            self.gridLayout_2.addWidget(self.volumes_lbl, 1, 3, 1, 1)

            # Volumes dropdown
            self.volumes_dropdown = QtWidgets.QComboBox(self.centralwidget)
            self.volumes_dropdown.setMinimumSize(QtCore.QSize(0, 40))
            self.volumes_dropdown.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";background-color: rgb(27, 27, 45)")
            self.gridLayout_2.addWidget(self.volumes_dropdown, 2, 3, 1, 1)
            self.window.setCentralWidget(self.centralwidget)

            self.load_ui()
            QtCore.QMetaObject.connectSlotsByName(self.window)
        except:
            self.err = ErrorWindow(exc_info())

    def load_ui(self):
        """
        Loads UI
        """
        try:
            self.save_btn.setText("Save")
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
            self.status_dropdown.addItem(Status.PLAN_TO_READ.value)
            self.status_dropdown.addItem(Status.COMPLETED.value)
            self.status_dropdown.addItem(Status.READING.value)
            self.status_dropdown.addItem(Status.DROPPED.value)
            self.chapters_lbl.setText("Chapters read")
            self.volumes_lbl.setText("Volumes read")
            if isinstance(self.manga, UserMangaListItem):
                self.window.setWindowTitle(self.manga.manga.title)
                self.manga_name.setText(self.manga.manga.title)
                self.save_btn.clicked.connect(self.update_manga)
                self.set_chapters_dropdown(self.manga.manga)
                self.set_volumes_dropdown(self.manga.manga)
            else:
                self.window.setWindowTitle(self.manga.title)
                self.manga_name.setText(self.manga.title)
                self.save_btn.clicked.connect(self.add_to_list)
                self.set_chapters_dropdown(self.manga)
                self.set_volumes_dropdown(self.manga)
        except:
            self.err = ErrorWindow(exc_info())

    def set_chapters_dropdown(self, manga: Manga):
        """
        Sets choices for chapters dropdown
        :param manga:
        """
        try:
            if manga.chapters:
                for i in range(manga.chapters + 1):
                    self.chapters_dropdown.addItem(f'{i}')
            else:
                self.chapters_dropdown.addItem('Currently no chapters')
        except:
            self.err = ErrorWindow(exc_info())

    def set_volumes_dropdown(self, manga: Manga):
        """
        Sets choices for volumes dropdown
        :param manga:
        """
        try:
            if manga.volumes:
                for i in range(manga.volumes + 1):
                    self.volumes_dropdown.addItem(f'{i}')
            else:
                self.volumes_dropdown.addItem('Currently no volumes')
        except:
            self.err = ErrorWindow(exc_info())

    def update_manga(self):
        """
        Updates manga item in users list
        :return:
        """
        try:
            from DBCommunication.UserInterface import update_user_manga
            status = self.status_dropdown.currentText()
            score = self.score_dropdown.currentIndex() + 1
            chapters = self.chapters_dropdown.currentIndex()
            volumes = self.volumes_dropdown.currentIndex()
            result = update_user_manga(self.session, self.manga, status, score, chapters, volumes)
            self.open_dialog(result)
        except:
            self.err = ErrorWindow(exc_info())

    def add_to_list(self):
        """
        Adds manga item in users list
        :return:
        """
        try:
            from DBCommunication.UserInterface import add_manga_to_user_list
            status = self.status_dropdown.currentText()
            score = self.score_dropdown.currentIndex() + 1
            chapters = self.chapters_dropdown.currentIndex()
            volumes = self.volumes_dropdown.currentIndex()
            result = add_manga_to_user_list(self.session, self.user, self.manga, status, score, chapters, volumes)
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
