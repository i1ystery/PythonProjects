from PyQt5 import QtCore, QtGui, QtWidgets
from register import *


class LoginWindow(object):
    def __init__(self, parent):
        self.parent_window = parent

    def main_ui(self, login_window):
        login_window.resize(500, 500)
        self.centralwidget = QtWidgets.QWidget(login_window)
        self.bg = QtWidgets.QFrame(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(-10, 0, 510, 510))
        self.bg.setStyleSheet("background-color: rgb(52, 52, 52)")
        self.bg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_input = QtWidgets.QLineEdit(self.bg)
        self.login_input.setGeometry(QtCore.QRect(130, 130, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display Semib")
        self.login_input.setFont(font)
        self.pass_input = QtWidgets.QLineEdit(self.bg)
        self.pass_input.setGeometry(QtCore.QRect(130, 220, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display Semib")
        self.pass_input.setFont(font)
        self.login_lbl = QtWidgets.QLabel(self.bg)
        self.login_lbl.setGeometry(QtCore.QRect(130, 100, 131, 31))
        self.login_lbl.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\"")
        self.pass_label = QtWidgets.QLabel(self.bg)
        self.pass_label.setGeometry(QtCore.QRect(130, 190, 131, 31))
        self.pass_label.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\"")
        self.login_btn = QtWidgets.QPushButton(self.bg)
        self.login_btn.setGeometry(QtCore.QRect(270, 300, 130, 50))
        self.login_btn.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";background-color: rgb(27, 27, 45)")
        self.create_btn = QtWidgets.QPushButton(self.bg)
        self.create_btn.setGeometry(QtCore.QRect(130, 300, 130, 50))
        self.create_btn.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";background-color: rgb(27, 27, 45)")
        self.label = QtWidgets.QLabel(self.bg)
        self.label.setGeometry(QtCore.QRect(130, 270, 271, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display Semib")
        self.label.setFont(font)
        self.login_btn.clicked.connect(lambda: self.login(login_window))
        self.create_btn.clicked.connect(lambda: self.register(login_window))
        login_window.setCentralWidget(self.centralwidget)
        self.load_ui(login_window)
        QtCore.QMetaObject.connectSlotsByName(login_window)

    def login(self, login_window):
        if self.login_input.text() and self.pass_input.text():
            if self.login_input.text() == self.pass_input.text():
                username = self.login_input.text()
                self.parent_window.logged_in_ui(username)
                login_window.close()

    def register(self, login_window):
        self.register_window = QtWidgets.QMainWindow()
        self.register_ui = RegisterWindow()
        self.register_ui.main_ui(self.register_window)
        self.register_window.show()
        login_window.close()

    def load_ui(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.login_lbl.setText(_translate("MainWindow", "Login"))
        self.pass_label.setText(_translate("MainWindow", "Password"))
        self.login_btn.setText(_translate("MainWindow", "Login"))
        self.create_btn.setText(_translate("MainWindow", "Create account"))


