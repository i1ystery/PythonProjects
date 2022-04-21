from sys import exc_info
from PyQt5 import QtCore, QtGui, QtWidgets
from Windows.ErrorWindow import ErrorWindow
from models.Status import Status


def main_ui(list_object):
    """
    Setups and loads window UI
    """
    try:
        list_object.window.resize(1024, 720)
        list_object.window.setMinimumSize(QtCore.QSize(1024, 720))
        list_object.window.setMaximumSize(QtCore.QSize(1024, 720))

        # Central widget
        list_object.centralwidget = QtWidgets.QWidget(list_object.window)
        list_object.centralwidget.setEnabled(True)
        list_object.centralwidget.setObjectName("centralwidget")

        # Background
        list_object.bg = QtWidgets.QFrame(list_object.centralwidget)
        list_object.bg.setEnabled(True)
        list_object.bg.setGeometry(QtCore.QRect(0, 0, 1024, 720))
        list_object.bg.setStyleSheet("background-color: rgb(52, 52, 52)")
        list_object.bg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        list_object.bg.setFrameShadow(QtWidgets.QFrame.Raised)

        # Logged as
        list_object.logged_as = QtWidgets.QLabel(list_object.bg)
        list_object.logged_as.setGeometry(QtCore.QRect(828, 10, 181, 51))
        list_object.logged_as.setStyleSheet("color: rgb(255, 255, 255);font: 63 11pt \"Segoe UI Variable Display Semib\";")

        # Next button
        list_object.next_button = QtWidgets.QPushButton(list_object.bg)
        list_object.next_button.setGeometry(QtCore.QRect(830, 670, 181, 41))
        list_object.next_button.setStyleSheet("color: rgb(255, 255, 255);font: 63 11pt \"Segoe UI Variable Display Semib\";background-color: rgb(27, 27, 45)")

        # Prev button
        list_object.prev_button = QtWidgets.QPushButton(list_object.bg)
        list_object.prev_button.setGeometry(QtCore.QRect(10, 670, 191, 41))
        list_object.prev_button.setStyleSheet("color: rgb(255, 255, 255);font: 63 11pt \"Segoe UI Variable Display Semib\";background-color: rgb(27, 27, 45)")

        # Switch mode button
        list_object.switch_mode = QtWidgets.QPushButton(list_object.bg)
        list_object.switch_mode.setGeometry(QtCore.QRect(10, 10, 301, 51))
        list_object.switch_mode.setStyleSheet("color: rgb(255, 255, 255);font: 63 11pt \"Segoe UI Variable Display Semib\";background-color: rgb(27, 27, 45)")

        # Filter box
        list_object.filter_box = QtWidgets.QComboBox(list_object.bg)
        list_object.filter_box.setGeometry(QtCore.QRect(320, 10, 301, 51))
        list_object.filter_box.setStyleSheet("color: rgb(255, 255, 255);font: 63 11pt \"Segoe UI Variable Display Semib\";background-color: rgb(27, 27, 45)")

        # Filter button
        list_object.filter_btn = QtWidgets.QPushButton(list_object.bg)
        list_object.filter_btn.setGeometry(QtCore.QRect(630, 10, 181, 51))
        list_object.filter_btn.setStyleSheet("color: rgb(255, 255, 255);font: 63 11pt \"Segoe UI Variable Display Semib\";background-color: rgb(27, 27, 45)")

        # Back to menu button
        list_object.back_btn = QtWidgets.QPushButton(list_object.bg)
        list_object.back_btn.setGeometry(QtCore.QRect(210, 670, 611, 41))
        list_object.back_btn.setStyleSheet("color: rgb(255, 255, 255);font: 63 11pt \"Segoe UI Variable Display Semib\";background-color: rgb(27, 27, 45)")

        # First item background
        list_object.first_item_bg = QtWidgets.QFrame(list_object.bg)
        list_object.first_item_bg.setEnabled(True)
        list_object.first_item_bg.setGeometry(QtCore.QRect(10, 70, 1000, 190))
        list_object.first_item_bg.setStyleSheet("background-color: rgb(27, 27, 45)")
        list_object.first_item_bg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        list_object.first_item_bg.setFrameShadow(QtWidgets.QFrame.Raised)

        # First item title
        list_object.first_item_title = QtWidgets.QLabel(list_object.first_item_bg)
        list_object.first_item_title.setGeometry(QtCore.QRect(195, 5, 641, 50))
        list_object.first_item_title.setStyleSheet("color: rgb(255, 255, 255);font: 63 11pt \"Segoe UI Variable Display Semib\";")
        list_object.first_item_title.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        # First item status label
        list_object.first_item_status = QtWidgets.QLabel(list_object.first_item_bg)
        list_object.first_item_status.setGeometry(QtCore.QRect(195, 50, 90, 40))
        list_object.first_item_status.setStyleSheet("color: rgb(255, 255, 255);font: 63 11pt \"Segoe UI Variable Display Semib\";")
        list_object.first_item_status.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        # First item image
        list_object.first_item_img = QtWidgets.QLabel(list_object.first_item_bg)
        list_object.first_item_img.setEnabled(True)
        list_object.first_item_img.setGeometry(QtCore.QRect(0, 0, 191, 191))
        list_object.first_item_img.setScaledContents(True)
        list_object.first_item_img.setIndent(-1)

        # First item score label
        list_object.first_item_score = QtWidgets.QLabel(list_object.first_item_bg)
        list_object.first_item_score.setGeometry(QtCore.QRect(195, 80, 90, 40))
        list_object.first_item_score.setStyleSheet("color: rgb(255, 255, 255);font: 63 11pt \"Segoe UI Variable Display Semib\";")
        list_object.first_item_score.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        # First item counter 1 label
        list_object.first_item_counter1 = QtWidgets.QLabel(list_object.first_item_bg)
        list_object.first_item_counter1.setGeometry(QtCore.QRect(195, 110, 90, 40))
        list_object.first_item_counter1.setStyleSheet("color: rgb(255, 255, 255);font: 63 11pt \"Segoe UI Variable Display Semib\";")
        list_object.first_item_counter1.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        # First item counter 2 label
        list_object.first_item_counter2 = QtWidgets.QLabel(list_object.first_item_bg)
        list_object.first_item_counter2.setGeometry(QtCore.QRect(195, 140, 90, 40))
        list_object.first_item_counter2.setStyleSheet("color: rgb(255, 255, 255);font: 63 11pt \"Segoe UI Variable Display Semib\";")
        list_object.first_item_counter2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        # First item status
        list_object.first_item_status_value = QtWidgets.QLabel(list_object.first_item_bg)
        list_object.first_item_status_value.setGeometry(QtCore.QRect(280, 50, 161, 40))
        list_object.first_item_status_value.setStyleSheet("color: rgb(255, 255, 255);font: 63 11pt \"Segoe UI Variable Display Semib\";")
        list_object.first_item_status_value.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        # First item score
        list_object.first_item_score_value = QtWidgets.QLabel(list_object.first_item_bg)
        list_object.first_item_score_value.setGeometry(QtCore.QRect(280, 80, 161, 40))
        list_object.first_item_score_value.setStyleSheet("color: rgb(255, 255, 255);font: 63 11pt \"Segoe UI Variable Display Semib\";")
        list_object.first_item_score_value.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        # First item counter 1 value
        list_object.first_item_counter1_value = QtWidgets.QLabel(list_object.first_item_bg)
        list_object.first_item_counter1_value.setGeometry(QtCore.QRect(280, 110, 161, 40))
        list_object.first_item_counter1_value.setStyleSheet("color: rgb(255, 255, 255);font: 63 11pt \"Segoe UI Variable Display Semib\";")
        list_object.first_item_counter1_value.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        # First item counter 2 value
        list_object.first_item_counter2_value = QtWidgets.QLabel(list_object.first_item_bg)
        list_object.first_item_counter2_value.setGeometry(QtCore.QRect(280, 140, 161, 40))
        list_object.first_item_counter2_value.setStyleSheet("color: rgb(255, 255, 255);font: 63 11pt \"Segoe UI Variable Display Semib\";")
        list_object.first_item_counter2_value.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        # First item button
        list_object.first_item_button = QtWidgets.QPushButton(list_object.first_item_bg)
        list_object.first_item_button.setGeometry(QtCore.QRect(0, 0, 841, 191))
        list_object.first_item_button.setStyleSheet("background-color: 0 0 0 0; border: 0;")

        # First item change button
        list_object.first_item_change_button = QtWidgets.QPushButton(list_object.first_item_bg)
        list_object.first_item_change_button.setGeometry(QtCore.QRect(840, 0, 161, 141))
        list_object.first_item_change_button.setStyleSheet("color: rgb(255, 255, 255);font: 63 11pt \"Segoe UI Variable Display Semib\";")

        # First item delete button
        list_object.first_item_delete_button = QtWidgets.QPushButton(list_object.first_item_bg)
        list_object.first_item_delete_button.setGeometry(QtCore.QRect(840, 140, 161, 51))
        list_object.first_item_delete_button.setStyleSheet("color: rgb(255, 255, 255);font: 63 11pt \"Segoe UI Variable Display Semib\";")

        # Second item background
        list_object.second_item_bg = QtWidgets.QFrame(list_object.bg)
        list_object.second_item_bg.setEnabled(True)
        list_object.second_item_bg.setGeometry(QtCore.QRect(10, 270, 1000, 190))
        list_object.second_item_bg.setStyleSheet("background-color: rgb(27, 27, 45)")
        list_object.second_item_bg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        list_object.second_item_bg.setFrameShadow(QtWidgets.QFrame.Raised)

        # Second item title
        list_object.second_item_title = QtWidgets.QLabel(list_object.second_item_bg)
        list_object.second_item_title.setGeometry(QtCore.QRect(195, 5, 641, 50))
        list_object.second_item_title.setStyleSheet("color: rgb(255, 255, 255);font: 63 11pt \"Segoe UI Variable Display Semib\";")
        list_object.second_item_title.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        # Second item status
        list_object.second_item_status = QtWidgets.QLabel(list_object.second_item_bg)
        list_object.second_item_status.setGeometry(QtCore.QRect(195, 50, 90, 40))
        list_object.second_item_status.setStyleSheet("color: rgb(255, 255, 255);font: 63 11pt \"Segoe UI Variable Display Semib\";")
        list_object.second_item_status.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        # Second item image
        list_object.second_item_img = QtWidgets.QLabel(list_object.second_item_bg)
        list_object.second_item_img.setEnabled(True)
        list_object.second_item_img.setGeometry(QtCore.QRect(0, 0, 191, 191))
        list_object.second_item_img.setScaledContents(True)
        list_object.second_item_img.setIndent(-1)

        # Second item score label
        list_object.second_item_score = QtWidgets.QLabel(list_object.second_item_bg)
        list_object.second_item_score.setGeometry(QtCore.QRect(195, 80, 90, 40))
        list_object.second_item_score.setStyleSheet("color: rgb(255, 255, 255);font: 63 11pt \"Segoe UI Variable Display Semib\";")
        list_object.second_item_score.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        # Second item counter 1 label
        list_object.second_item_counter1 = QtWidgets.QLabel(list_object.second_item_bg)
        list_object.second_item_counter1.setGeometry(QtCore.QRect(195, 110, 90, 40))
        list_object.second_item_counter1.setStyleSheet("color: rgb(255, 255, 255);font: 63 11pt \"Segoe UI Variable Display Semib\";")
        list_object.second_item_counter1.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        # Second item counter 2 label
        list_object.second_item_counter2 = QtWidgets.QLabel(list_object.second_item_bg)
        list_object.second_item_counter2.setGeometry(QtCore.QRect(195, 140, 90, 40))
        list_object.second_item_counter2.setStyleSheet("color: rgb(255, 255, 255);font: 63 11pt \"Segoe UI Variable Display Semib\";")
        list_object.second_item_counter2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        # Second item status
        list_object.second_item_status_value = QtWidgets.QLabel(list_object.second_item_bg)
        list_object.second_item_status_value.setGeometry(QtCore.QRect(280, 50, 161, 40))
        list_object.second_item_status_value.setStyleSheet("color: rgb(255, 255, 255);font: 63 11pt \"Segoe UI Variable Display Semib\";")
        list_object.second_item_status_value.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        list_object.second_item_status_value.setObjectName("second_item_status_value")

        # Second item score
        list_object.second_item_score_value = QtWidgets.QLabel(list_object.second_item_bg)
        list_object.second_item_score_value.setGeometry(QtCore.QRect(280, 80, 161, 40))
        list_object.second_item_score_value.setStyleSheet("color: rgb(255, 255, 255);font: 63 11pt \"Segoe UI Variable Display Semib\";")
        list_object.second_item_score_value.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        # Second item counter 1 value
        list_object.second_item_counter1_value = QtWidgets.QLabel(list_object.second_item_bg)
        list_object.second_item_counter1_value.setGeometry(QtCore.QRect(280, 110, 161, 40))
        list_object.second_item_counter1_value.setStyleSheet("color: rgb(255, 255, 255);font: 63 11pt \"Segoe UI Variable Display Semib\";")
        list_object.second_item_counter1_value.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        # Second item counter 2 value
        list_object.second_item_counter2_value = QtWidgets.QLabel(list_object.second_item_bg)
        list_object.second_item_counter2_value.setGeometry(QtCore.QRect(280, 140, 161, 40))
        list_object.second_item_counter2_value.setStyleSheet("color: rgb(255, 255, 255);font: 63 11pt \"Segoe UI Variable Display Semib\";")
        list_object.second_item_counter2_value.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        # Second item button
        list_object.second_item_button = QtWidgets.QPushButton(list_object.second_item_bg)
        list_object.second_item_button.setGeometry(QtCore.QRect(0, 0, 841, 191))
        list_object.second_item_button.setStyleSheet("background-color: 0 0 0 0; border: 0;")

        # Second item change button
        list_object.second_item_change_button = QtWidgets.QPushButton(list_object.second_item_bg)
        list_object.second_item_change_button.setGeometry(QtCore.QRect(840, 0, 161, 141))
        list_object.second_item_change_button.setStyleSheet("color: rgb(255, 255, 255);font: 63 11pt \"Segoe UI Variable Display Semib\";")

        # Second item delete button
        list_object.second_item_delete_button = QtWidgets.QPushButton(list_object.second_item_bg)
        list_object.second_item_delete_button.setGeometry(QtCore.QRect(840, 140, 161, 51))
        list_object.second_item_delete_button.setStyleSheet("color: rgb(255, 255, 255);font: 63 11pt \"Segoe UI Variable Display Semib\";")

        # Third item background
        list_object.third_item_bg = QtWidgets.QFrame(list_object.bg)
        list_object.third_item_bg.setEnabled(True)
        list_object.third_item_bg.setGeometry(QtCore.QRect(10, 470, 1000, 190))
        list_object.third_item_bg.setStyleSheet("background-color: rgb(27, 27, 45)")
        list_object.third_item_bg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        list_object.third_item_bg.setFrameShadow(QtWidgets.QFrame.Raised)

        # Third item title
        list_object.third_item_title = QtWidgets.QLabel(list_object.third_item_bg)
        list_object.third_item_title.setGeometry(QtCore.QRect(195, 5, 641, 50))
        list_object.third_item_title.setStyleSheet("color: rgb(255, 255, 255);font: 63 11pt \"Segoe UI Variable Display Semib\";")
        list_object.third_item_title.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        # Third item status
        list_object.third_item_status = QtWidgets.QLabel(list_object.third_item_bg)
        list_object.third_item_status.setGeometry(QtCore.QRect(195, 50, 90, 40))
        list_object.third_item_status.setStyleSheet("color: rgb(255, 255, 255);font: 63 11pt \"Segoe UI Variable Display Semib\";")
        list_object.third_item_status.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        # Third item image
        list_object.third_item_img = QtWidgets.QLabel(list_object.third_item_bg)
        list_object.third_item_img.setEnabled(True)
        list_object.third_item_img.setGeometry(QtCore.QRect(0, 0, 191, 191))
        list_object.third_item_img.setScaledContents(True)
        list_object.third_item_img.setIndent(-1)

        # Third item score
        list_object.third_item_score = QtWidgets.QLabel(list_object.third_item_bg)
        list_object.third_item_score.setGeometry(QtCore.QRect(195, 80, 90, 40))
        list_object.third_item_score.setStyleSheet("color: rgb(255, 255, 255);font: 63 11pt \"Segoe UI Variable Display Semib\";")
        list_object.third_item_score.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        # Third item counter 1 label
        list_object.third_item_counter1 = QtWidgets.QLabel(list_object.third_item_bg)
        list_object.third_item_counter1.setGeometry(QtCore.QRect(195, 110, 90, 40))
        list_object.third_item_counter1.setStyleSheet("color: rgb(255, 255, 255);font: 63 11pt \"Segoe UI Variable Display Semib\";")
        list_object.third_item_counter1.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        # Third item counter 2 label
        list_object.third_item_counter2 = QtWidgets.QLabel(list_object.third_item_bg)
        list_object.third_item_counter2.setGeometry(QtCore.QRect(195, 140, 90, 40))
        list_object.third_item_counter2.setStyleSheet("color: rgb(255, 255, 255);font: 63 11pt \"Segoe UI Variable Display Semib\";")
        list_object.third_item_counter2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        # Third item status
        list_object.third_item_status_value = QtWidgets.QLabel(list_object.third_item_bg)
        list_object.third_item_status_value.setGeometry(QtCore.QRect(280, 50, 161, 40))
        list_object.third_item_status_value.setStyleSheet("color: rgb(255, 255, 255);font: 63 11pt \"Segoe UI Variable Display Semib\";")
        list_object.third_item_status_value.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        # Third item score
        list_object.third_item_score_value = QtWidgets.QLabel(list_object.third_item_bg)
        list_object.third_item_score_value.setGeometry(QtCore.QRect(280, 80, 161, 40))
        list_object.third_item_score_value.setStyleSheet("color: rgb(255, 255, 255);font: 63 11pt \"Segoe UI Variable Display Semib\";")
        list_object.third_item_score_value.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        # Third item counter 1 value
        list_object.third_item_counter1_value = QtWidgets.QLabel(list_object.third_item_bg)
        list_object.third_item_counter1_value.setGeometry(QtCore.QRect(280, 110, 161, 40))
        list_object.third_item_counter1_value.setStyleSheet("color: rgb(255, 255, 255);font: 63 11pt \"Segoe UI Variable Display Semib\";")
        list_object.third_item_counter1_value.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        # Third item counter 2 value
        list_object.third_item_counter2_value = QtWidgets.QLabel(list_object.third_item_bg)
        list_object.third_item_counter2_value.setGeometry(QtCore.QRect(280, 140, 161, 40))
        list_object.third_item_counter2_value.setStyleSheet("color: rgb(255, 255, 255);font: 63 11pt \"Segoe UI Variable Display Semib\";")
        list_object.third_item_counter2_value.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        # Third item button
        list_object.third_item_button = QtWidgets.QPushButton(list_object.third_item_bg)
        list_object.third_item_button.setGeometry(QtCore.QRect(0, 0, 841, 191))
        list_object.third_item_button.setStyleSheet("background-color: 0 0 0 0; border: 0;")

        # Third item change button
        list_object.third_item_change_button = QtWidgets.QPushButton(list_object.third_item_bg)
        list_object.third_item_change_button.setGeometry(QtCore.QRect(840, 0, 161, 141))
        list_object.third_item_change_button.setStyleSheet("color: rgb(255, 255, 255);font: 63 11pt \"Segoe UI Variable Display Semib\";")
        list_object.third_item_change_button.setObjectName("third_item_change_button")

        # Third item delete button
        list_object.third_item_delete_button = QtWidgets.QPushButton(list_object.third_item_bg)
        list_object.third_item_delete_button.setGeometry(QtCore.QRect(840, 140, 161, 51))
        list_object.third_item_delete_button.setStyleSheet("color: rgb(255, 255, 255);font: 63 11pt \"Segoe UI Variable Display Semib\";")
        list_object.window.setCentralWidget(list_object.centralwidget)

        # Button bindings
        list_object.back_btn.clicked.connect(lambda: list_object.back_to_menu())
        list_object.prev_button.clicked.connect(lambda: list_object.load_page(Status(list_object.filter_box.currentText()), -1))
        list_object.next_button.clicked.connect(lambda: list_object.load_page(Status(list_object.filter_box.currentText()), 1))
        list_object.switch_mode.clicked.connect(list_object.switch_modes)
        list_object.first_item_button.clicked.connect(lambda: list_object.item_info(list_object.first_item))
        list_object.second_item_button.clicked.connect(lambda: list_object.item_info(list_object.second_item))
        list_object.third_item_button.clicked.connect(lambda: list_object.item_info(list_object.third_item))
        list_object.first_item_delete_button.clicked.connect(lambda: list_object.delete_item(list_object.first_item))
        list_object.second_item_delete_button.clicked.connect(lambda: list_object.delete_item(list_object.second_item))
        list_object.third_item_delete_button.clicked.connect(lambda: list_object.delete_item(list_object.third_item))
        list_object.first_item_change_button.clicked.connect(lambda: list_object.update_item(list_object.first_item))
        list_object.second_item_change_button.clicked.connect(lambda: list_object.update_item(list_object.second_item))
        list_object.third_item_change_button.clicked.connect(lambda: list_object.update_item(list_object.third_item))
        list_object.filter_btn.clicked.connect(list_object.filter_items)

        load_ui(list_object)
        QtCore.QMetaObject.connectSlotsByName(list_object.window)
    except:
        list_object.err = ErrorWindow(exc_info())


def load_ui(list_object):
    """
    Loads window UI
    """
    try:
        list_object.window.setWindowTitle(f'{list_object.parent.logged_user.username}\'s list')
        list_object.logged_as.setText(f"Logged as {list_object.parent.logged_user.username}")
        list_object.next_button.setText("Next")
        list_object.prev_button.setText("Prev")
        list_object.filter_box.addItem(Status.ALL.value)
        list_object.filter_box.addItem(Status.COMPLETED.value)
        list_object.filter_box.addItem(Status.DROPPED.value)
        list_object.filter_box.addItem("")
        list_object.filter_box.addItem("")
        list_object.filter_btn.setText("Filter")
        list_object.first_item_status.setText("Status")
        list_object.first_item_score.setText("Score")
        list_object.first_item_counter2.setText('Volumes')
        list_object.first_item_delete_button.setText("Delete from list")
        list_object.first_item_change_button.setText("Change details")
        list_object.second_item_status.setText("Status")
        list_object.second_item_score.setText("Score")
        list_object.second_item_counter2.setText("Volumes")
        list_object.second_item_change_button.setText("Change details")
        list_object.second_item_delete_button.setText("Delete from list")
        list_object.third_item_status.setText("Status")
        list_object.third_item_score.setText("Score")
        list_object.third_item_counter2.setText("Volumes")
        list_object.third_item_delete_button.setText("Delete from list")
        list_object.third_item_change_button.setText("Change details")
        list_object.back_btn.setText("Back to main menu")
        list_object.load_page()
    except:
        list_object.err = ErrorWindow(exc_info())
