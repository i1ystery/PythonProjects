from sys import exc_info
from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser
from Windows.ErrorWindow import ErrorWindow
from models.AnimeEpisode import AnimeEpisode
from models.Anime import Anime


class EpisodeWindow(object):

    def __init__(self, window, episode: AnimeEpisode, anime: Anime):
        """
        Initializes window and opens it
        :param window:
        :param episode:
        :param anime:
        """
        self.episode = episode
        self.window = window
        self.anime = anime
        self.main_ui()
        self.window.show()

    def main_ui(self):
        """
        Setups and loads window UI
        """
        try:
            self.window .resize(640, 532)
            self.window.setMinimumSize(QtCore.QSize(640, 532))
            self.window.setMaximumSize(QtCore.QSize(640, 532))

            # Central widget
            self.centralwidget = QtWidgets.QWidget(self.window)
            self.centralwidget.setStyleSheet("background-color: rgb(52, 52, 52)")

            # Grid layout
            self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)

            # Recap label
            self.recap = QtWidgets.QLabel(self.centralwidget)
            self.recap.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";")
            self.gridLayout.addWidget(self.recap, 5, 0, 1, 1)

            # Recap
            self.recap_data = QtWidgets.QLabel(self.centralwidget)
            self.recap_data.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";")
            self.gridLayout.addWidget(self.recap_data, 5, 1, 1, 1)

            # Filler label
            self.filler = QtWidgets.QLabel(self.centralwidget)
            self.filler.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";")
            self.gridLayout.addWidget(self.filler, 4, 0, 1, 1)

            # Filler
            self.filler_data = QtWidgets.QLabel(self.centralwidget)
            self.filler_data.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";")
            self.gridLayout.addWidget(self.filler_data, 4, 1, 1, 1)

            # Aired
            self.aired_date = QtWidgets.QLabel(self.centralwidget)
            self.aired_date.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";")
            self.aired_date.setWordWrap(True)
            self.gridLayout.addWidget(self.aired_date, 3, 1, 1, 1)

            # Aired label
            self.aired = QtWidgets.QLabel(self.centralwidget)
            self.aired.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";")
            self.gridLayout.addWidget(self.aired, 3, 0, 1, 1)

            # Duration label
            self.duration = QtWidgets.QLabel(self.centralwidget)
            self.duration.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";")
            self.gridLayout.addWidget(self.duration, 2, 0, 1, 1)

            # Duration
            self.duration_time = QtWidgets.QLabel(self.centralwidget)
            self.duration_time.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";")
            self.duration_time.setWordWrap(True)
            self.gridLayout.addWidget(self.duration_time, 2, 1, 1, 1)

            # English title
            self.en_title_name = QtWidgets.QLabel(self.centralwidget)
            self.en_title_name.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";")
            self.en_title_name.setWordWrap(True)
            self.gridLayout.addWidget(self.en_title_name, 0, 1, 1, 1)

            # English title label
            self.en_title = QtWidgets.QLabel(self.centralwidget)
            self.en_title.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";")
            self.gridLayout.addWidget(self.en_title, 0, 0, 1, 1)

            # Japanese title
            self.jp_title_name = QtWidgets.QLabel(self.centralwidget)
            self.jp_title_name.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";")
            self.jp_title_name.setWordWrap(True)
            self.gridLayout.addWidget(self.jp_title_name, 1, 1, 1, 1)

            # Japanese title label
            self.jp_title = QtWidgets.QLabel(self.centralwidget)
            self.jp_title.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";")
            self.gridLayout.addWidget(self.jp_title, 1, 0, 1, 1)

            # Watch in english button
            self.watch_en = QtWidgets.QPushButton(self.centralwidget)
            self.watch_en.setMinimumSize(QtCore.QSize(0, 50))
            self.watch_en.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\"; background-color: rgb(27, 27, 45);")
            self.gridLayout.addWidget(self.watch_en, 6, 0, 1, 1)
            self.window.setCentralWidget(self.centralwidget)

            # Watch in russian button
            self.watch_ru = QtWidgets.QPushButton(self.centralwidget)
            self.watch_ru.setMinimumSize(QtCore.QSize(0, 50))
            self.watch_ru.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\"; background-color: rgb(27, 27, 45);")
            self.gridLayout.addWidget(self.watch_ru, 6, 1, 1, 1)

            # Button bindings
            self.watch_en.clicked.connect(self.watch_english)
            self.watch_ru.clicked.connect(self.watch_russian)

            self.load_ui()
            QtCore.QMetaObject.connectSlotsByName(self.window)
        except:
            self.err = ErrorWindow(exc_info())

    def load_ui(self):
        """
        Loads UI
        """
        try:
            self.window.setWindowTitle(self.episode.title)
            self.recap.setText("Recap episode")
            self.recap_data.setText('Yes' if self.episode.is_recap else 'No')
            self.filler.setText("Filler episode")
            self.filler_data.setText('Yes' if self.episode.is_filler else 'No')
            self.en_title.setText("Episode title")
            self.en_title_name.setText(self.episode.title)
            self.aired.setText("Aired")
            self.aired_date.setText(str(self.episode.aired))
            self.duration.setText("Duration")
            self.duration_time.setText('24 minutes')
            self.jp_title.setText("Japanese title")
            self.jp_title_name.setText(self.episode.title_japanese)
            self.watch_en.setText("Watch in English")
            self.watch_ru.setText("Watch in Russian")
        except:
            self.err = ErrorWindow(exc_info())

    def watch_russian(self):
        webbrowser.open(f'https://animego.org/search/all?q={self.anime.title}')

    def watch_english(self):
        webbrowser.open(f'https://9anime.vc/search?keyword={self.anime.title}')

