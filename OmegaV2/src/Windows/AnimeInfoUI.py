from sys import exc_info
import scripts.Configuration as config
from Windows.ErrorWindow import ErrorWindow
from PyQt5 import QtCore, QtGui, QtWidgets


def main_ui(anime_object):
    """
    Setups and loads window UI
    """
    try:
        anime_object.window.setObjectName("MainWindow")
        anime_object.window.resize(700, 580)
        anime_object.window.setMinimumSize(QtCore.QSize(700, 580))
        anime_object.window.setMaximumSize(QtCore.QSize(700, 580))

        # Central window
        anime_object.centralwidget = QtWidgets.QWidget(anime_object.window)
        anime_object.centralwidget.setObjectName("centralwidget")

        # Background
        anime_object.bg = QtWidgets.QFrame(anime_object.centralwidget)
        anime_object.bg.setGeometry(QtCore.QRect(0, 0, 700, 580))
        anime_object.bg.setStyleSheet("background-color: rgb(52, 52, 52)")
        anime_object.bg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        anime_object.bg.setFrameShadow(QtWidgets.QFrame.Raised)
        anime_object.bg.setObjectName("bg")

        # Image
        anime_object.image = QtWidgets.QLabel(anime_object.bg)
        anime_object.image.setGeometry(QtCore.QRect(20, 20, 150, 210))
        anime_object.image.setText("")
        anime_object.image.setPixmap(QtGui.QPixmap(""))
        anime_object.image.setScaledContents(True)
        anime_object.image.setObjectName("image")

        # Anime name
        anime_object.anime_name = QtWidgets.QLabel(anime_object.bg)
        anime_object.anime_name.setGeometry(QtCore.QRect(175, 20, 511, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display Semib")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        anime_object.anime_name.setFont(font)
        anime_object.anime_name.setStyleSheet("color: rgb(255, 255, 255); font: 63 14pt Segoe UI Variable Display Semib;")
        anime_object.anime_name.setObjectName("anime_name")

        # English title label
        anime_object.en_title = QtWidgets.QLabel(anime_object.bg)
        anime_object.en_title.setGeometry(QtCore.QRect(175, 60, 101, 21))
        anime_object.en_title.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
        anime_object.en_title.setObjectName("en_title")

        # English title
        anime_object.en_name = QtWidgets.QLabel(anime_object.bg)
        anime_object.en_name.setGeometry(QtCore.QRect(300, 60, 321, 21))
        anime_object.en_name.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
        anime_object.en_name.setObjectName("en_name")

        # Japanese title label
        anime_object.jp_title = QtWidgets.QLabel(anime_object.bg)
        anime_object.jp_title.setGeometry(QtCore.QRect(175, 90, 111, 21))
        anime_object.jp_title.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
        anime_object.jp_title.setObjectName("jp_title")

        # Japanese title
        anime_object.jp_name = QtWidgets.QLabel(anime_object.bg)
        anime_object.jp_name.setGeometry(QtCore.QRect(300, 90, 321, 21))
        anime_object.jp_name.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
        anime_object.jp_name.setObjectName("jp_name")

        # Score label
        anime_object.score = QtWidgets.QLabel(anime_object.bg)
        anime_object.score.setGeometry(QtCore.QRect(630, 60, 81, 21))
        anime_object.score.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
        anime_object.score.setObjectName("score")

        # Score
        anime_object.score_number = QtWidgets.QLabel(anime_object.bg)
        anime_object.score_number.setGeometry(QtCore.QRect(630, 90, 51, 21))
        anime_object.score_number.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
        anime_object.score_number.setAlignment(QtCore.Qt.AlignCenter)
        anime_object.score_number.setObjectName("score_number")

        # Show type label
        anime_object.show_name = QtWidgets.QLabel(anime_object.bg)
        anime_object.show_name.setGeometry(QtCore.QRect(20, 240, 111, 21))
        anime_object.show_name.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
        anime_object.show_name.setObjectName("show_name")

        # Show type
        anime_object.type_name = QtWidgets.QLabel(anime_object.bg)
        anime_object.type_name.setGeometry(QtCore.QRect(145, 240, 171, 21))
        anime_object.type_name.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
        anime_object.type_name.setObjectName("type_name")

        # Status
        anime_object.status_name = QtWidgets.QLabel(anime_object.bg)
        anime_object.status_name.setGeometry(QtCore.QRect(145, 270, 171, 21))
        anime_object.status_name.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
        anime_object.status_name.setObjectName("status_name")

        # Status label
        anime_object.current_status = QtWidgets.QLabel(anime_object.bg)
        anime_object.current_status.setGeometry(QtCore.QRect(20, 270, 111, 21))
        anime_object.current_status.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
        anime_object.current_status.setObjectName("current_status")

        # Aired from
        anime_object.aired_from_date = QtWidgets.QLabel(anime_object.bg)
        anime_object.aired_from_date.setGeometry(QtCore.QRect(145, 300, 171, 21))
        anime_object.aired_from_date.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
        anime_object.aired_from_date.setObjectName("aired_from_date")

        # Aired from label
        anime_object.aired_from = QtWidgets.QLabel(anime_object.bg)
        anime_object.aired_from.setGeometry(QtCore.QRect(20, 300, 111, 21))
        anime_object.aired_from.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
        anime_object.aired_from.setObjectName("aired_from")

        # Aired to
        anime_object.aired_to_date = QtWidgets.QLabel(anime_object.bg)
        anime_object.aired_to_date.setGeometry(QtCore.QRect(145, 330, 171, 21))
        anime_object.aired_to_date.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
        anime_object.aired_to_date.setObjectName("aired_to_date")

        # Aired to label
        anime_object.aired_to = QtWidgets.QLabel(anime_object.bg)
        anime_object.aired_to.setGeometry(QtCore.QRect(20, 330, 111, 21))
        anime_object.aired_to.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
        anime_object.aired_to.setObjectName("aired_to")

        # Number of episodes label
        anime_object.num_episodes = QtWidgets.QLabel(anime_object.bg)
        anime_object.num_episodes.setGeometry(QtCore.QRect(20, 360, 111, 41))
        anime_object.num_episodes.setAcceptDrops(False)
        anime_object.num_episodes.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
        anime_object.num_episodes.setScaledContents(False)
        anime_object.num_episodes.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        anime_object.num_episodes.setWordWrap(True)
        anime_object.num_episodes.setObjectName("num_episodes")

        # Number of episodes
        anime_object.num_eps = QtWidgets.QLabel(anime_object.bg)
        anime_object.num_eps.setGeometry(QtCore.QRect(145, 360, 111, 41))
        anime_object.num_eps.setAcceptDrops(False)
        anime_object.num_eps.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
        anime_object.num_eps.setScaledContents(False)
        anime_object.num_eps.setWordWrap(True)
        anime_object.num_eps.setObjectName("num_eps")

        # Episode duration label
        anime_object.episode_duration = QtWidgets.QLabel(anime_object.bg)
        anime_object.episode_duration.setGeometry(QtCore.QRect(20, 410, 111, 41))
        anime_object.episode_duration.setAcceptDrops(False)
        anime_object.episode_duration.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
        anime_object.episode_duration.setScaledContents(False)
        anime_object.episode_duration.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        anime_object.episode_duration.setWordWrap(True)
        anime_object.episode_duration.setObjectName("episode_duration")

        # Episode duration
        anime_object.dur_time = QtWidgets.QLabel(anime_object.bg)
        anime_object.dur_time.setGeometry(QtCore.QRect(145, 410, 111, 41))
        anime_object.dur_time.setAcceptDrops(False)
        anime_object.dur_time.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
        anime_object.dur_time.setScaledContents(False)
        anime_object.dur_time.setWordWrap(True)
        anime_object.dur_time.setObjectName("dur_time")

        # Genres label
        anime_object.genres = QtWidgets.QLabel(anime_object.bg)
        anime_object.genres.setGeometry(QtCore.QRect(300, 240, 111, 31))
        anime_object.genres.setAcceptDrops(False)
        anime_object.genres.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
        anime_object.genres.setScaledContents(False)
        anime_object.genres.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        anime_object.genres.setWordWrap(True)
        anime_object.genres.setObjectName("genres")

        # Genres
        anime_object.genres_names = QtWidgets.QLabel(anime_object.bg)
        anime_object.genres_names.setGeometry(QtCore.QRect(300, 280, 161, 91))
        anime_object.genres_names.setAcceptDrops(False)
        anime_object.genres_names.setStyleSheet("color: rgb(255, 255, 255); font: 63 10pt Segoe UI Variable Display Semib;")
        anime_object.genres_names.setScaledContents(False)
        anime_object.genres_names.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        anime_object.genres_names.setWordWrap(True)
        anime_object.genres_names.setObjectName("genres_names")

        # Themes label
        anime_object.themes = QtWidgets.QLabel(anime_object.bg)
        anime_object.themes.setGeometry(QtCore.QRect(480, 240, 111, 31))
        anime_object.themes.setAcceptDrops(False)
        anime_object.themes.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
        anime_object.themes.setScaledContents(False)
        anime_object.themes.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        anime_object.themes.setWordWrap(True)
        anime_object.themes.setObjectName("themes")

        # Themes
        anime_object.theme_names = QtWidgets.QLabel(anime_object.bg)
        anime_object.theme_names.setGeometry(QtCore.QRect(480, 280, 171, 91))
        anime_object.theme_names.setAcceptDrops(False)
        anime_object.theme_names.setStyleSheet("color: rgb(255, 255, 255); font: 63 10pt Segoe UI Variable Display Semib;")
        anime_object.theme_names.setScaledContents(False)
        anime_object.theme_names.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        anime_object.theme_names.setWordWrap(True)
        anime_object.theme_names.setObjectName("theme_names")

        # Add to list button
        anime_object.add_to_list = QtWidgets.QPushButton(anime_object.bg)
        anime_object.add_to_list.setGeometry(QtCore.QRect(10, 510, 441, 51))
        anime_object.add_to_list.setStyleSheet(
            "color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\"; background-color: rgb(27, 27, 45);")
        anime_object.add_to_list.setObjectName("add_to_list")

        # Back button
        anime_object.back_btn = QtWidgets.QPushButton(anime_object.bg)
        anime_object.back_btn.setGeometry(QtCore.QRect(560, 510, 131, 51))
        anime_object.back_btn.setStyleSheet(
            "color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\"; background-color: rgb(27, 27, 45);")
        anime_object.back_btn.setObjectName("back_btn")

        # Anime characters button
        anime_object.anime_characters = QtWidgets.QPushButton(anime_object.bg)
        anime_object.anime_characters.setGeometry(QtCore.QRect(540, 390, 151, 41))
        anime_object.anime_characters.setStyleSheet(
            "color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\"; background-color: rgb(27, 27, 45);")
        anime_object.anime_characters.setObjectName("anime_characters")

        # Broadcast time label
        anime_object.broadcast_time = QtWidgets.QLabel(anime_object.bg)
        anime_object.broadcast_time.setGeometry(QtCore.QRect(20, 460, 111, 21))
        anime_object.broadcast_time.setAcceptDrops(False)
        anime_object.broadcast_time.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
        anime_object.broadcast_time.setScaledContents(False)
        anime_object.broadcast_time.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        anime_object.broadcast_time.setWordWrap(True)
        anime_object.broadcast_time.setObjectName("broadcast_time")

        # Broadcast time
        anime_object.cast_time = QtWidgets.QLabel(anime_object.bg)
        anime_object.cast_time.setGeometry(QtCore.QRect(145, 455, 121, 31))
        anime_object.cast_time.setAcceptDrops(False)
        anime_object.cast_time.setStyleSheet("color: rgb(255, 255, 255); font: 63 9pt Segoe UI Variable Display Semib;")
        anime_object.cast_time.setScaledContents(False)
        anime_object.cast_time.setWordWrap(True)
        anime_object.cast_time.setObjectName("cast_time")

        # Episodes button
        anime_object.episodes = QtWidgets.QPushButton(anime_object.bg)
        anime_object.episodes.setGeometry(QtCore.QRect(540, 450, 151, 41))
        anime_object.episodes.setStyleSheet(
            "color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\"; background-color: rgb(27, 27, 45);")
        anime_object.episodes.setObjectName("episodes")

        # Character dropdown
        anime_object.character_drop = QtWidgets.QComboBox(anime_object.bg)
        anime_object.character_drop.setGeometry(QtCore.QRect(280, 390, 251, 41))
        anime_object.character_drop.setMinimumSize(QtCore.QSize(0, 40))
        anime_object.character_drop.setStyleSheet(
            "color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";background-color: rgb(27, 27, 45)")
        anime_object.character_drop.setObjectName("character_drop")

        # Episodes dropdown
        anime_object.episode_drop = QtWidgets.QComboBox(anime_object.bg)
        anime_object.episode_drop.setGeometry(QtCore.QRect(280, 450, 251, 41))
        anime_object.episode_drop.setMinimumSize(QtCore.QSize(0, 40))
        anime_object.episode_drop.setStyleSheet(
            "color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";background-color: rgb(27, 27, 45)")
        anime_object.episode_drop.setObjectName("episode_drop")

        # Button bindings
        anime_object.anime_characters.clicked.connect(anime_object.character_info)
        anime_object.episodes.clicked.connect(anime_object.episode_info)
        anime_object.add_to_list.clicked.connect(anime_object.add_list)
        anime_object.back_btn.clicked.connect(lambda: anime_object.close())
        anime_object.window.setCentralWidget(anime_object.centralwidget)
        anime_object.window.closeEvent = anime_object.close_event

        load_ui(anime_object)
        QtCore.QMetaObject.connectSlotsByName(anime_object.window)
    except:
        anime_object.err = ErrorWindow(exc_info())


def load_ui(anime_object):
    """
    Loads UI
    """
    try:
        anime_object.window.setWindowTitle(anime_object.anime.title)
        anime_object.image.setPixmap(QtGui.QPixmap(f"{config.images_path}/Items/{anime_object.anime.id}.jpg"))
        anime_object.anime_name.setText(anime_object.anime.title)
        anime_object.en_title.setText("English Name:")
        anime_object.en_name.setText(anime_object.anime.title_english if anime_object.anime.title_english else anime_object.anime.title)
        anime_object.jp_title.setText("Japanese Name:")
        anime_object.jp_name.setText(anime_object.anime.title_japanese)
        anime_object.score.setText("SCORE")
        anime_object.score_number.setText(str(anime_object.anime.score))
        anime_object.show_name.setText("Show type")
        anime_object.type_name.setText(anime_object.anime.show_type)
        anime_object.current_status.setText("Current status")
        anime_object.status_name.setText(anime_object.anime.status)
        anime_object.aired_from_date.setText(str(anime_object.anime.aired_from))
        anime_object.aired_from.setText("Aired from")
        anime_object.aired_to_date.setText(str(anime_object.anime.aired_to) if anime_object.anime.aired_to else 'Ongoing')
        anime_object.aired_to.setText("Aired to")
        anime_object.num_episodes.setText("Number of episodes")
        anime_object.num_eps.setText(str(anime_object.anime.num_episodes))
        anime_object.episode_duration.setText("Episode duration")
        anime_object.dur_time.setText(str(anime_object.anime.episode_duration))
        anime_object.genres.setText("Genres")
        anime_object.genres_names.setText(anime_object.get_genres())
        anime_object.themes.setText("Themes")
        anime_object.theme_names.setText(anime_object.get_themes())
        anime_object.add_to_list.setText("Add to my list")
        anime_object.back_btn.setText("Close")
        anime_object.anime_characters.setText("Show Character Info")
        anime_object.broadcast_time.setText("Broadcast time")
        anime_object.cast_time.setText(repr(anime_object.anime.broadcast_time[0]))
        anime_object.episodes.setText("Show Episode Info")
        if not anime_object.user:
            anime_object.add_to_list.setVisible(False)
        anime_object.set_episode_dropdown()
        anime_object.set_character_dropdown()
    except:
        anime_object.err = ErrorWindow(exc_info())
