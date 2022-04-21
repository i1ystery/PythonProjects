from sys import exc_info
from PyQt5 import QtCore, QtGui, QtWidgets
from Windows.ErrorWindow import ErrorWindow
from Windows.DialogBox import DialogBox
import re


class RegisterWindow(object):

    def __init__(self, parent, window, session):
        """
        Initializes window and opens it
        :param window:
        :param parent: main window
        :param session: DB session
        """
        self.parent_window = parent
        self.window = window
        self.session = session
        self.main_ui()
        self.window.show()

    def main_ui(self):
        """
        Setups and loads window UI
        """
        try:
            self.window.resize(500, 500)
            self.window.setMaximumSize(QtCore.QSize(500, 500))
            self.window.setMinimumSize(QtCore.QSize(500, 500))

            # Central widget
            self.centralwidget = QtWidgets.QWidget(self.window)
            self.bg = QtWidgets.QFrame(self.centralwidget)
            self.bg.setGeometry(QtCore.QRect(-10, 0, 510, 510))
            self.bg.setStyleSheet("background-color: rgb(52, 52, 52)")
            self.bg.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.bg.setFrameShadow(QtWidgets.QFrame.Raised)

            # Login input box
            self.login_input = QtWidgets.QLineEdit(self.bg)
            self.login_input.setGeometry(QtCore.QRect(130, 130, 271, 41))
            font = QtGui.QFont()
            font.setFamily("Segoe UI Variable Display Semib")
            self.login_input.setStyleSheet(
                "color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\"")
            self.login_input.setFont(font)

            # Password input box
            self.pass_input = QtWidgets.QLineEdit(self.bg)
            self.pass_input.setGeometry(QtCore.QRect(130, 220, 271, 41))
            font = QtGui.QFont()
            font.setFamily("Segoe UI Variable Display Semib")
            self.pass_input.setStyleSheet(
                "color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\"")
            self.pass_input.setFont(font)
            self.pass_input.setInputMethodHints(QtCore.Qt.ImhSensitiveData)

            # Login label
            self.login_lbl = QtWidgets.QLabel(self.bg)
            self.login_lbl.setGeometry(QtCore.QRect(130, 100, 131, 31))
            self.login_lbl.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\"")

            # Password label
            self.pass_label = QtWidgets.QLabel(self.bg)
            self.pass_label.setGeometry(QtCore.QRect(130, 190, 131, 31))
            self.pass_label.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\"")

            # Create button
            self.create_btn_2 = QtWidgets.QPushButton(self.bg)
            self.create_btn_2.setGeometry(QtCore.QRect(270, 360, 130, 50))
            self.create_btn_2.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";background-color: rgb(27, 27, 45)")

            # Cancel button
            self.cancel = QtWidgets.QPushButton(self.bg)
            self.cancel.setGeometry(QtCore.QRect(130, 360, 130, 50))
            self.cancel.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";background-color: rgb(27, 27, 45)")

            # Error
            self.error_lbl = QtWidgets.QLabel(self.bg)
            self.error_lbl.setGeometry(QtCore.QRect(130, 330, 271, 21))
            font = QtGui.QFont()
            font.setFamily("Segoe UI Variable Display Semib")
            self.error_lbl.setFont(font)
            self.error_lbl.setStyleSheet(
                "color: red; font: 63 8pt \"Segoe UI Variable Display Semib\"")

            # Confirm password box
            self.pass_input_2 = QtWidgets.QLineEdit(self.bg)
            self.pass_input_2.setGeometry(QtCore.QRect(130, 290, 271, 41))
            font = QtGui.QFont()
            font.setFamily("Segoe UI Variable Display Semib")
            self.pass_input_2.setStyleSheet(
                "color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\"")
            self.pass_input_2.setFont(font)
            self.pass_input_2.setInputMethodHints(QtCore.Qt.ImhSensitiveData)

            # Confirm password label
            self.confirm_label = QtWidgets.QLabel(self.bg)
            self.confirm_label.setGeometry(QtCore.QRect(130, 260, 131, 31))
            self.confirm_label.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\"")

            # Registration label
            self.label = QtWidgets.QLabel(self.bg)
            self.label.setGeometry(QtCore.QRect(130, 40, 271, 61))
            self.label.setStyleSheet("color: rgb(255, 255, 255); font: 63 20pt \"Segoe UI Variable Display Semib\"")
            self.label.setAlignment(QtCore.Qt.AlignCenter)
            self.window.setCentralWidget(self.centralwidget)

            # Button bindings
            self.cancel.clicked.connect(lambda: self.close_window())
            self.create_btn_2.clicked.connect(self.register_account)

            self.load_ui()
            QtCore.QMetaObject.connectSlotsByName(self.window)
        except:
            self.err = ErrorWindow(exc_info())

    def load_ui(self):
        """
        Loads window UI
        """
        try:
            self.window.setWindowTitle("Registration")
            self.label.setText("Registration")
            self.login_lbl.setText("Login")
            self.pass_label.setText("Password")
            self.confirm_label.setText("Confirm Password")
            self.create_btn_2.setText("Create account")
            self.cancel.setText("Cancel")
        except:
            self.err = ErrorWindow(exc_info())

    def register_account(self):
        """
        Registers user
        """
        try:
            if re.fullmatch(r'[A-Za-z0-9]{3,}', self.login_input.text()):
                if re.fullmatch(r'[A-Za-z0-9@$#%^&+=]{4,}', self.pass_input.text()):
                    if self.pass_input.text() == self.pass_input_2.text():
                        from DBCommunication.UserInterface import add_new_user
                        result = add_new_user(self.session, self.login_input.text(), self.pass_input.text())
                        self.open_dialog(result)
                else:
                    self.error_lbl.setText('Password len > 4')
            else:
                self.error_lbl.setText('Login len > 4')
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

    def close_window(self):
        self.window.close()
