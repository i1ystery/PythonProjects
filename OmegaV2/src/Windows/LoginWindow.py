from Windows.RegisterWindow import *
from models.User import User


class LoginWindow(object):

    def __init__(self, parent_window, window):
        """
        Initializes window and opens it
        :param window:
        :param parent_window:
        """
        self.parent_window = parent_window
        self.window = window
        self.main_ui()
        self.window.show()

    def main_ui(self):
        """
        Setups and loads window UI
        """
        try:
            self.window.resize(500, 500)
            self.window.setMinimumSize(QtCore.QSize(500, 500))
            self.window.setMaximumSize(QtCore.QSize(500, 500))
            self.centralwidget = QtWidgets.QWidget(self.window)

            # Background
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
            self.login_input.setFont(font)
            self.login_input.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\"")

            # Password input box
            self.pass_input = QtWidgets.QLineEdit(self.bg)
            self.pass_input.setGeometry(QtCore.QRect(130, 220, 271, 41))
            font = QtGui.QFont()
            font.setFamily("Segoe UI Variable Display Semib")
            self.pass_input.setFont(font)
            self.pass_input.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\"")

            # Login label
            self.login_lbl = QtWidgets.QLabel(self.bg)
            self.login_lbl.setGeometry(QtCore.QRect(130, 100, 131, 31))
            self.login_lbl.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\"")

            # Password label
            self.pass_label = QtWidgets.QLabel(self.bg)
            self.pass_label.setGeometry(QtCore.QRect(130, 190, 131, 31))
            self.pass_label.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\"")

            # Login button
            self.login_btn = QtWidgets.QPushButton(self.bg)
            self.login_btn.setGeometry(QtCore.QRect(270, 300, 130, 50))
            self.login_btn.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";background-color: rgb(27, 27, 45)")

            # Create button
            self.create_btn = QtWidgets.QPushButton(self.bg)
            self.create_btn.setGeometry(QtCore.QRect(130, 300, 130, 50))
            self.create_btn.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";background-color: rgb(27, 27, 45)")

            # Error
            self.error = QtWidgets.QLabel(self.bg)
            self.error.setGeometry(QtCore.QRect(130, 270, 271, 21))
            font = QtGui.QFont()
            font.setFamily("Segoe UI Variable Display Semib")
            self.error.setFont(font)
            self.error.setStyleSheet(
                "color: red; font: 63 8pt \"Segoe UI Variable Display Semib\"")
            self.window.setCentralWidget(self.centralwidget)

            # Button bindings
            self.login_btn.clicked.connect(lambda: self.login(self.login_input.text(), self.pass_input.text()))
            self.create_btn.clicked.connect(lambda: self.register())

            self.load_ui()
            QtCore.QMetaObject.connectSlotsByName(self.window)
        except:
            self.err = ErrorWindow(exc_info())

    def load_ui(self):
        """
        Loads UI
        """
        try:
            self.window.setWindowTitle("Login")
            self.login_lbl.setText("Login")
            self.pass_label.setText("Password")
            self.login_btn.setText("Login")
            self.create_btn.setText("Create account")
        except:
            self.err = ErrorWindow(exc_info())

    def login(self, login: str, passw: str):
        """
        Logins user
        :param login:
        :param passw:
        """
        try:
            from DBCommunication.UserInterface import check_login
            user = check_login(self.parent_window.session, login, passw)
            if isinstance(user, User):
                self.parent_window.logged_in_ui(user)
                self.window.close()
            else:
                self.error.setText(user)
        except:
            self.err = ErrorWindow(exc_info())

    def register(self):
        """
        Opens registration window
        """
        try:
            self.register_window = QtWidgets.QMainWindow()
            self.register_ui = RegisterWindow(self.window, self.register_window, self.parent_window.session)
            self.window.close()
        except:
            self.err = ErrorWindow(exc_info())

