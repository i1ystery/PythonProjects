from sys import exc_info

from PyQt5 import QtCore, QtGui, QtWidgets

from Windows.ErrorWindow import ErrorWindow
from models.AnimeCharacter import AnimeCharacter
from models.MangaCharacter import MangaCharacter
from scripts.ImageOperations import get_image
import scripts.Configuration as config
from typing import Union


class CharacterWindow(object):

    def __init__(self, window, character: Union[AnimeCharacter, MangaCharacter]):
        """
        Initializes window and opens it
        :param window:
        :param character:
        """
        self.character = character
        self.window = window
        self.main_ui()
        self.window.show()

    def main_ui(self):
        """
        Setups and loads window UI
        """
        try:
            self.window.resize(640, 480)
            self.window.setMinimumSize(QtCore.QSize(640, 480))
            self.window.setMaximumSize(QtCore.QSize(640, 480))

            # Central widget
            self.centralwidget = QtWidgets.QWidget(self.window)
            self.centralwidget.setStyleSheet("background-color: rgb(52, 52, 52)")

            # Grid layout
            self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)

            # Character role
            self.role = QtWidgets.QLabel(self.centralwidget)
            self.role.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";")
            self.gridLayout.addWidget(self.role, 1, 2, 1, 1)

            # Character role label
            self.role_lbl = QtWidgets.QLabel(self.centralwidget)
            self.role_lbl.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";")
            self.gridLayout.addWidget(self.role_lbl, 1, 1, 1, 1)

            # Character name
            self.name = QtWidgets.QLabel(self.centralwidget)
            self.name.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";")
            self.gridLayout.addWidget(self.name, 0, 2, 1, 1)

            # Character name label
            self.name_lbl = QtWidgets.QLabel(self.centralwidget)
            self.name_lbl.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";")
            self.gridLayout.addWidget(self.name_lbl, 0, 1, 1, 1)

            # English VA label
            self.en_voice_actor = QtWidgets.QLabel(self.centralwidget)
            self.en_voice_actor.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";")
            self.gridLayout.addWidget(self.en_voice_actor, 3, 1, 1, 1)

            # Japanese VA label
            self.jp_voice_actor = QtWidgets.QLabel(self.centralwidget)
            self.jp_voice_actor.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";")
            self.gridLayout.addWidget(self.jp_voice_actor, 2, 1, 1, 1)

            # Japanese VA name
            self.jp_name = QtWidgets.QLabel(self.centralwidget)
            self.jp_name.setWordWrap(True)
            self.jp_name.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";")
            self.gridLayout.addWidget(self.jp_name, 2, 2, 1, 1)

            # English VA name
            self.en_name = QtWidgets.QLabel(self.centralwidget)
            self.en_name.setWordWrap(True)
            self.en_name.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";")
            self.gridLayout.addWidget(self.en_name, 3, 2, 1, 1)

            # Image
            self.image = QtWidgets.QLabel(self.centralwidget)
            self.image.setMaximumSize(QtCore.QSize(300, 16777215))
            self.image.setPixmap(QtGui.QPixmap(""))
            self.image.setScaledContents(True)
            self.gridLayout.addWidget(self.image, 0, 0, 4, 1)
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
            self.window.setWindowTitle(self.character.name)
            self.name_lbl.setText("Name")
            self.name.setText(self.character.name)
            self.role_lbl.setText("Role")
            self.role.setText(self.character.role)
            if isinstance(self.character, AnimeCharacter):
                if self.character.voice_actors:
                    try:
                        self.en_voice_actor.setText("EN Voice Actor")
                        self.en_name.setText(self.character.voice_actors[1].full_name)
                    except:
                        pass
                    try:
                        self.jp_voice_actor.setText("JP Voice Actor")
                        self.jp_name.setText(self.character.voice_actors[0].full_name)
                    except:
                        pass
            get_image(self.character)
            self.image.setPixmap(QtGui.QPixmap(f"{config.images_path}/Characters/{self.character.name}.jpg"))
        except:
            self.err = ErrorWindow(exc_info())

