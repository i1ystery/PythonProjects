from sys import exc_info

from PyQt5 import QtCore, QtGui, QtWidgets

from Windows.ErrorWindow import ErrorWindow


class DialogBox(object):
    def __init__(self, parent, window):
        """
        Initializes window
        :param window:
        :param parent: parent window
        """
        self.window = window
        self.parent_window = parent

    def main_ui(self, message):
        """
        Setups and loads window UI
        """
        self.window.setObjectName("Dialog")
        self.window.resize(340, 150)
        self.window.setMaximumSize(QtCore.QSize(340, 150))
        self.window.setMinimumSize(QtCore.QSize(340, 150))
        self.window.setStyleSheet("background-color: rgb(52, 52, 52)")

        # Background
        self.bg = QtWidgets.QFrame(self.window)
        self.bg.setGeometry(QtCore.QRect(0, 0, 340, 150))
        self.bg.setAutoFillBackground(False)
        self.bg.setStyleSheet("background-color: rgb(52, 52, 52)")
        self.bg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bg.setObjectName("bg")

        # Message
        self.message = QtWidgets.QLabel(self.bg)
        self.message.setGeometry(QtCore.QRect(10, 20, 320, 61))
        self.message.setMinimumSize(QtCore.QSize(0, 20))
        self.message.setStyleSheet("color: rgb(255, 255, 255); font: 63 13pt \"Segoe UI Variable Display Semib\";")
        self.message.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.message.setWordWrap(True)
        self.message.setObjectName("message")

        # OK button
        self.ok = QtWidgets.QPushButton(self.bg)
        self.ok.setGeometry(QtCore.QRect(95, 90, 150, 50))
        self.ok.setMinimumSize(QtCore.QSize(0, 50))
        self.ok.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";background-color: rgb(27, 27, 45)")
        self.ok.setObjectName("ok")

        # Button bindings
        self.ok.clicked.connect(self.close)

        self.load_ui(message)
        QtCore.QMetaObject.connectSlotsByName(self.window)

    def load_ui(self, message=None):
        """
        Loads UI
        """
        self.window.setWindowTitle("Dialog")
        self.message.setText(message)
        self.ok.setText("OK")

    def close(self):
        """
        Closes dialog box
        If parent is set closes parent too
        :return:
        """
        try:
            self.window.close()
            if self.parent_window:
                self.parent_window.close()
        except:
            self.err = ErrorWindow(exc_info())
