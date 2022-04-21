from sys import exc_info
from PyQt5 import QtCore, QtGui, QtWidgets
from Windows.ErrorWindow import ErrorWindow
from Windows.Mode import Mode


def main_ui(main_object):
    """
    Setups and loads window UI
    """
    try:
        main_object.window.setEnabled(True)
        main_object.window.resize(1024, 720)
        main_object.window.setMinimumSize(QtCore.QSize(1024, 720))
        main_object.window.setMaximumSize(QtCore.QSize(1024, 720))

        # Central widget
        main_object.centralwidget = QtWidgets.QWidget(main_object.window)
        main_object.centralwidget.setEnabled(True)

        # Background
        main_object.bg = QtWidgets.QFrame(main_object.centralwidget)
        main_object.bg.setEnabled(True)
        main_object.bg.setGeometry(QtCore.QRect(0, 0, 1024, 720))
        main_object.bg.setStyleSheet("background-color: rgb(52, 52, 52)")
        main_object.bg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        main_object.bg.setFrameShadow(QtWidgets.QFrame.Raised)

        # Random item button
        main_object.random_item = QtWidgets.QPushButton(main_object.bg)
        main_object.random_item.setGeometry(QtCore.QRect(370, 670, 291, 41))
        main_object.random_item.setStyleSheet(
            "color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";background-color: rgb(27, 27, 45)")

        # Next button
        main_object.next_button = QtWidgets.QPushButton(main_object.bg)
        main_object.next_button.setGeometry(QtCore.QRect(870, 670, 141, 41))
        main_object.next_button.setStyleSheet(
            "color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";background-color: rgb(27, 27, 45)")

        # My List button
        main_object.my_list_button = QtWidgets.QPushButton(main_object.bg)
        main_object.my_list_button.setGeometry(QtCore.QRect(10, 10, 301, 51))
        main_object.my_list_button.setStyleSheet(
            "color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";background-color: rgb(27, 27, 45)")
        main_object.my_list_button.hide()

        # Prev button
        main_object.prev_button = QtWidgets.QPushButton(main_object.bg)
        main_object.prev_button.setGeometry(QtCore.QRect(10, 670, 141, 41))
        main_object.prev_button.setStyleSheet(
            "color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";background-color: rgb(27, 27, 45)")

        # Logged as
        main_object.logged_as = QtWidgets.QLabel(main_object.bg)
        main_object.logged_as.setGeometry(QtCore.QRect(700, 10, 160, 51))
        main_object.logged_as.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";")
        main_object.logged_as.hide()

        # Login button
        main_object.login_button = QtWidgets.QPushButton(main_object.bg)
        main_object.login_button.setGeometry(QtCore.QRect(900, 10, 111, 51))
        main_object.login_button.setStyleSheet(
            "color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\"; background-color: rgb(27, 27, 45);")

        # First item background
        main_object.first_item_bg = QtWidgets.QFrame(main_object.bg)
        main_object.first_item_bg.setEnabled(True)
        main_object.first_item_bg.setGeometry(QtCore.QRect(10, 70, 1001, 191))
        main_object.first_item_bg.setStyleSheet("background-color: rgb(27, 27, 45)")
        main_object.first_item_bg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        main_object.first_item_bg.setFrameShadow(QtWidgets.QFrame.Raised)

        # First item title
        main_object.first_item_title = QtWidgets.QLabel(main_object.first_item_bg)
        main_object.first_item_title.setGeometry(QtCore.QRect(200, 0, 790, 51))
        main_object.first_item_title.setStyleSheet(
            "color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";")
        main_object.first_item_title.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        # First item synopsis
        main_object.first_item_synopsis = QtWidgets.QLabel(main_object.first_item_bg)
        main_object.first_item_synopsis.setGeometry(QtCore.QRect(200, 30, 790, 151))
        main_object.first_item_synopsis.setStyleSheet(
            "color: rgb(255, 255, 255); font: 63 8pt \"Segoe UI Variable Display Semib\";")
        main_object.first_item_synopsis.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        main_object.first_item_synopsis.setWordWrap(True)

        # First item image
        main_object.first_item_img = QtWidgets.QLabel(main_object.first_item_bg)
        main_object.first_item_img.setEnabled(True)
        main_object.first_item_img.setGeometry(QtCore.QRect(0, 0, 191, 191))
        main_object.first_item_img.setPixmap(QtGui.QPixmap(""))
        main_object.first_item_img.setScaledContents(True)

        # First item button
        main_object.first_item_button = QtWidgets.QPushButton(main_object.first_item_bg)
        main_object.first_item_button.setGeometry(QtCore.QRect(0, 0, 1001, 191))
        main_object.first_item_button.setStyleSheet("background-color: 0 0 0 0; border: 0;")

        # Second item background
        main_object.second_item_bg = QtWidgets.QFrame(main_object.bg)
        main_object.second_item_bg.setEnabled(True)
        main_object.second_item_bg.setGeometry(QtCore.QRect(10, 270, 1001, 191))
        main_object.second_item_bg.setStyleSheet("background-color: rgb(27, 27, 45)")
        main_object.second_item_bg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        main_object.second_item_bg.setFrameShadow(QtWidgets.QFrame.Raised)

        # Second item title
        main_object.second_item_title = QtWidgets.QLabel(main_object.second_item_bg)
        main_object.second_item_title.setGeometry(QtCore.QRect(200, 0, 790, 51))
        main_object.second_item_title.setStyleSheet(
            "color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";")
        main_object.second_item_title.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        # Second item synopsis
        main_object.second_item_synopsis = QtWidgets.QLabel(main_object.second_item_bg)
        main_object.second_item_synopsis.setGeometry(QtCore.QRect(200, 30, 790, 151))
        main_object.second_item_synopsis.setStyleSheet(
            "color: rgb(255, 255, 255); font: 63 8pt \"Segoe UI Variable Display Semib\";")
        main_object.second_item_synopsis.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        main_object.second_item_synopsis.setWordWrap(True)

        # Second item image
        main_object.second_item_img = QtWidgets.QLabel(main_object.second_item_bg)
        main_object.second_item_img.setEnabled(True)
        main_object.second_item_img.setGeometry(QtCore.QRect(0, 0, 191, 191))
        main_object.second_item_img.setPixmap(QtGui.QPixmap(""))
        main_object.second_item_img.setScaledContents(True)

        # Second item button
        main_object.second_item_button = QtWidgets.QPushButton(main_object.second_item_bg)
        main_object.second_item_button.setGeometry(QtCore.QRect(0, 0, 1001, 191))
        main_object.second_item_button.setStyleSheet("background-color: 0 0 0 0; border: 0;")

        # Third item background
        main_object.third_item_bg = QtWidgets.QFrame(main_object.bg)
        main_object.third_item_bg.setEnabled(True)
        main_object.third_item_bg.setGeometry(QtCore.QRect(10, 470, 1001, 191))
        main_object.third_item_bg.setStyleSheet("background-color: rgb(27, 27, 45)")
        main_object.third_item_bg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        main_object.third_item_bg.setFrameShadow(QtWidgets.QFrame.Raised)

        # Third item title
        main_object.third_item_title = QtWidgets.QLabel(main_object.third_item_bg)
        main_object.third_item_title.setGeometry(QtCore.QRect(200, 0, 790, 51))
        main_object.third_item_title.setStyleSheet(
            "color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\";")
        main_object.third_item_title.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        # Third item synopsis
        main_object.third_item_synopsis = QtWidgets.QLabel(main_object.third_item_bg)
        main_object.third_item_synopsis.setGeometry(QtCore.QRect(200, 30, 790, 151))
        main_object.third_item_synopsis.setStyleSheet(
            "color: rgb(255, 255, 255); font: 63 8pt \"Segoe UI Variable Display Semib\";")
        main_object.third_item_synopsis.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        main_object.third_item_synopsis.setWordWrap(True)

        # Third item image
        main_object.third_item_img = QtWidgets.QLabel(main_object.third_item_bg)
        main_object.third_item_img.setGeometry(QtCore.QRect(0, 0, 191, 191))
        main_object.third_item_img.setPixmap(QtGui.QPixmap(""))
        main_object.third_item_img.setScaledContents(True)

        # Third item button
        main_object.third_item_button = QtWidgets.QPushButton(main_object.third_item_bg)
        main_object.third_item_button.setGeometry(QtCore.QRect(0, 0, 1001, 191))
        main_object.third_item_button.setStyleSheet("background-color: 0 0 0 0; border: 0;")

        # Switch mode button
        main_object.switch_mode = QtWidgets.QPushButton(main_object.bg)
        main_object.switch_mode.setGeometry(QtCore.QRect(380, 10, 300, 51))
        main_object.switch_mode.setStyleSheet(u"color: rgb(255, 255, 255);"
                                       "font: 63 11pt \"Segoe UI Variable Display Semib\";""background-color: rgb(27, 27, 45)")

        # Admin button
        main_object.admin_button = QtWidgets.QPushButton(main_object.bg)
        main_object.admin_button.setObjectName("admin")
        main_object.admin_button.setGeometry(QtCore.QRect(165, 670, 190, 41))
        main_object.admin_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "font: 63 11pt \"Segoe UI Variable Display Semib\";background-color: rgb(27, 27, 45)")
        main_object.admin_button.hide()

        # Button bindings
        main_object.next_button.clicked.connect(lambda: main_object.load_page(1))
        main_object.prev_button.clicked.connect(lambda: main_object.load_page(-1))
        main_object.login_button.clicked.connect(main_object.login)
        main_object.first_item_button.clicked.connect(lambda: main_object.item_info(main_object.first_item))
        main_object.second_item_button.clicked.connect(lambda: main_object.item_info(main_object.second_item))
        main_object.third_item_button.clicked.connect(lambda: main_object.item_info(main_object.third_item))
        main_object.random_item.clicked.connect(main_object.load_random)
        main_object.my_list_button.clicked.connect(main_object.open_my_list)
        main_object.switch_mode.clicked.connect(main_object.switch_modes)
        main_object.admin_button.clicked.connect(main_object.admin_window)
        main_object.window.setCentralWidget(main_object.centralwidget)

        load_ui(main_object)
        QtCore.QMetaObject.connectSlotsByName(main_object.window)
    except:
        main_object.err = ErrorWindow(exc_info())


def load_ui(main_object):
    """
    Loads UI
    """
    try:
        main_object.window.setWindowTitle("WeebApp")
        main_object.random_item.setText(f"Random {Mode.ANIME.value if main_object.mode == Mode.ANIME else Mode.MANGA.value}")
        main_object.logged_as.setText(f"Logged as {main_object.logged_user}")
        main_object.next_button.setText("Next")
        main_object.my_list_button.setText("My List")
        main_object.prev_button.setText("Prev")
        main_object.login_button.setText("Login")
        main_object.switch_mode.setText(f"Switch to {Mode.MANGA.value if main_object.mode == Mode.ANIME else Mode.ANIME.value}")
        main_object.admin_button.setText("Admin")
        main_object.load_page()
    except:
        main_object.err = ErrorWindow(exc_info())
