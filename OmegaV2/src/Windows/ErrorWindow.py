import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from scripts.FileOperations import save_error


class ErrorWindow(object):
    def __init__(self, exception_data: tuple):
        """
        Initializes window and opens it
        :param exception_data:
        """
        self.exception = exception_data
        self.window = QtWidgets.QMainWindow()
        self.main_ui()
        self.window.show()

    def main_ui(self):
        """
        Setups and loads window UI
        """
        self.window.setObjectName("Dialog")
        self.window.resize(400, 250)
        self.window.setMinimumSize(QtCore.QSize(400, 250))
        self.window.setMaximumSize(QtCore.QSize(400, 250))

        # Background
        self.frame = QtWidgets.QFrame(self.window)
        self.frame.setGeometry(QtCore.QRect(0, 0, 400, 250))
        self.frame.setStyleSheet("background-color: rgb(52, 52, 52)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        # Ok button
        self.ok = QtWidgets.QPushButton(self.frame)
        self.ok.setGeometry(QtCore.QRect(20, 190, 150, 50))
        self.ok.setMinimumSize(QtCore.QSize(0, 50))
        self.ok.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";background-color: rgb(27, 27, 45)")
        self.ok.setObjectName("ok")

        # Save error button
        self.save_error = QtWidgets.QPushButton(self.frame)
        self.save_error.setGeometry(QtCore.QRect(230, 190, 150, 50))
        self.save_error.setMinimumSize(QtCore.QSize(0, 50))
        self.save_error.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";background-color: rgb(27, 27, 45)")
        self.save_error.setObjectName("save_error")

        # Text
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 20, 351, 171))
        self.label.setStyleSheet("color: rgb(255, 255, 255); font: 63 13pt \"Segoe UI Variable Display Semib\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        # Button bindings
        self.save_error.clicked.connect(self.log_error)
        self.ok.clicked.connect(self.window.close)

        self.load_ui()
        QtCore.QMetaObject.connectSlotsByName(self.window)

    def load_ui(self):
        """
        Loads UI
        """
        self.window.setWindowTitle("Error occurred")
        self.ok.setText("OK")
        self.save_error.setText("Save Error")
        self.label.setText("Unexpected error\nUse save error button to save error log")

    def log_error(self):
        """
        Logs error to file and closes the window
        """
        save_error(self.exception[0], self.exception[1], self.exception[2])
        self.window.close()

