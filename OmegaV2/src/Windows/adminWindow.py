from sys import exc_info

from PyQt5 import QtCore, QtGui, QtWidgets

from DBCommunication.AnimeInterface import insert_anime_by_name_jikan
from DBCommunication.GenreThemeInterface import insert_genres_jikan, insert_themes_jikan
from DBCommunication.MangaInterface import insert_manga_by_name_jikan
from Windows.DialogBox import DialogBox
from Windows.ErrorWindow import ErrorWindow


class AdminWindow(object):

    def __init__(self, session, window, parent):
        """
        Initializes window and opens it
        :param session:
        :param window:
        :param parent:
        """
        self.window = window
        self.session = session
        self.parent = parent
        self.main_ui()
        self.parent.window.hide()
        self.window.show()

    def main_ui(self):
        """
        Setups and loads window UI
        :return:
        """
        try:
            self.window.setObjectName("MainWindow")
            self.window.resize(600, 350)
            self.window.setMinimumSize(QtCore.QSize(600, 350))
            self.window.setMaximumSize(QtCore.QSize(600, 350))

            # Central widget
            self.centralwidget = QtWidgets.QWidget(self.window)
            self.centralwidget.setObjectName("centralwidget")

            # Self background
            self.bg = QtWidgets.QFrame(self.centralwidget)
            self.bg.setEnabled(True)
            self.bg.setGeometry(QtCore.QRect(0, 0, 600, 350))
            self.bg.setStyleSheet("background-color: rgb(52, 52, 52)")
            self.bg.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.bg.setFrameShadow(QtWidgets.QFrame.Raised)
            self.bg.setObjectName("bg")

            # Add genres button
            self.add_genres_button = QtWidgets.QPushButton(self.bg)
            self.add_genres_button.setGeometry(QtCore.QRect(10, 260, 290, 50))
            self.add_genres_button.setStyleSheet("color: rgb(255, 255, 255);font: 63 11pt "
                                                 "\"Segoe UI Variable Display Semib\";background-color: rgb(27, 27, 45)")
            self.add_genres_button.setDefault(False)
            self.add_genres_button.setFlat(False)
            self.add_genres_button.setObjectName("add_genres_button")

            # Add themes button
            self.add_themes_button = QtWidgets.QPushButton(self.bg)
            self.add_themes_button.setGeometry(QtCore.QRect(300, 260, 290, 50))
            self.add_themes_button.setStyleSheet("color: rgb(255, 255, 255);font: 63 11pt "
                                                 "\"Segoe UI Variable Display Semib\";background-color: rgb(27, 27, 45)")
            self.add_themes_button.setDefault(False)
            self.add_themes_button.setFlat(False)
            self.add_themes_button.setObjectName("add_themes_button")

            # Add manga button
            self.add_manga_button = QtWidgets.QPushButton(self.bg)
            self.add_manga_button.setGeometry(QtCore.QRect(330, 180, 260, 50))
            self.add_manga_button.setStyleSheet("color: rgb(255, 255, 255);font: 63 11pt "
                                                "\"Segoe UI Variable Display Semib\";background-color: rgb(27, 27, 45)")
            self.add_manga_button.setDefault(False)
            self.add_manga_button.setFlat(False)
            self.add_manga_button.setObjectName("add_manga_button")

            # Add anime button
            self.add_anime_button = QtWidgets.QPushButton(self.bg)
            self.add_anime_button.setGeometry(QtCore.QRect(330, 100, 260, 50))
            self.add_anime_button.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt "
                                                "\"Segoe UI Variable Display Semib\";background-color: rgb(27, 27, 45)")
            self.add_anime_button.setDefault(False)
            self.add_anime_button.setFlat(False)
            self.add_anime_button.setObjectName("add_anime_button")

            # Admin Panel label
            self.label = QtWidgets.QLabel(self.bg)
            self.label.setGeometry(QtCore.QRect(10, 10, 580, 80))
            self.label.setStyleSheet("color: rgb(255, 255, 255); font: 63 20pt \"Segoe UI Variable Display Semib\";")
            self.label.setAlignment(QtCore.Qt.AlignCenter)
            self.label.setObjectName("label")

            # Anime input box
            self.anime_input = QtWidgets.QLineEdit(self.bg)
            self.anime_input.setGeometry(QtCore.QRect(10, 100, 310, 50))
            self.anime_input.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt "
                                           "\"Segoe UI Variable Display Semib\";background-color: rgb(27, 27, 45)")
            self.anime_input.setObjectName("anime_input")

            # Manga input box
            self.manga_input = QtWidgets.QLineEdit(self.bg)
            self.manga_input.setGeometry(QtCore.QRect(10, 180, 310, 50))
            self.manga_input.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt "
                                           "\"Segoe UI Variable Display Semib\";background-color: rgb(27, 27, 45)")
            self.manga_input.setObjectName("manga_input")

            self.window.setCentralWidget(self.centralwidget)
            self.window.closeEvent = self.close_event

            # Button bindings
            self.add_genres_button.clicked.connect(self.add_genres)
            self.add_themes_button.clicked.connect(self.add_themes)
            self.add_anime_button.clicked.connect(self.add_anime)
            self.add_manga_button.clicked.connect(self.add_manga)

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
            self.window.setWindowTitle("ADMIN PANEL")
            self.add_genres_button.setText("Add genres")
            self.add_themes_button.setText("Add themes")
            self.add_manga_button.setText("Add Manga")
            self.add_anime_button.setText("Add Anime")
            self.label.setText("ADMIN PANEL")
            self.anime_input.setPlaceholderText("Anime full name")
            self.manga_input.setPlaceholderText("Manga full name")
        except:
            self.err = ErrorWindow(exc_info())

    def open_dialog(self, message):
        """
        Opens dialog window with given message
        :param message:
        """
        try:
            self.dialog = QtWidgets.QDialog()
            self.dialog_ui = DialogBox(None, self.dialog)
            self.dialog_ui.main_ui(message)
            self.dialog.show()
        except:
            self.err = ErrorWindow(exc_info())

    def close_event(self, event):
        """
        On close event load previous window and close current window
        :param event:
        :return:
        """
        self.parent.load_page()
        self.parent.window.show()
        event.accept()

    def add_anime(self):
        """
        Adds anime from input box to database
        :return:
        """
        try:
            if len(self.anime_input.text()) > 2:
                result = insert_anime_by_name_jikan(self.anime_input.text(), self.session)
                self.open_dialog(result)
        except:
            self.err = ErrorWindow(exc_info())

    def add_manga(self):
        """
        Adds manga from input box to database
        :return:
        """
        try:
            if len(self.manga_input.text()) > 2:
                result = insert_manga_by_name_jikan(self.manga_input.text(), self.session)
                self.open_dialog(result)
        except:
            self.err = ErrorWindow(exc_info())

    def add_genres(self):
        """
        Adds genres to database
        :return:
        """
        try:
            result = insert_genres_jikan(self.session)
            self.open_dialog(result)
        except:
            self.err = ErrorWindow(exc_info())

    def add_themes(self):
        """
        Adds themes to database
        :return:
        """
        try:
            result = insert_themes_jikan(self.session)
            self.open_dialog(result)
        except:
            self.err = ErrorWindow(exc_info())
