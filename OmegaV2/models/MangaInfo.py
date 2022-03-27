from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 572)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bg = QtWidgets.QFrame(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 800, 581))
        self.bg.setStyleSheet("background-color: rgb(52, 52, 52)")
        self.bg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bg.setObjectName("bg")
        self.image = QtWidgets.QLabel(self.bg)
        self.image.setGeometry(QtCore.QRect(20, 20, 150, 210))
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap(".\\../1.jpg"))
        self.image.setScaledContents(True)
        self.image.setObjectName("image")
        self.manga_name = QtWidgets.QLabel(self.bg)
        self.manga_name.setGeometry(QtCore.QRect(175, 20, 601, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display Semib")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.manga_name.setFont(font)
        self.manga_name.setStyleSheet("color: rgb(255, 255, 255); font: 63 14pt Segoe UI Variable Display Semib;")
        self.manga_name.setObjectName("manga_name")
        self.en_title = QtWidgets.QLabel(self.bg)
        self.en_title.setGeometry(QtCore.QRect(175, 60, 101, 21))
        self.en_title.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
        self.en_title.setObjectName("en_title")
        self.en_name = QtWidgets.QLabel(self.bg)
        self.en_name.setGeometry(QtCore.QRect(300, 60, 371, 21))
        self.en_name.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
        self.en_name.setObjectName("en_name")
        self.jp_title = QtWidgets.QLabel(self.bg)
        self.jp_title.setGeometry(QtCore.QRect(175, 90, 111, 21))
        self.jp_title.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
        self.jp_title.setObjectName("jp_title")
        self.jp_name = QtWidgets.QLabel(self.bg)
        self.jp_name.setGeometry(QtCore.QRect(300, 90, 371, 21))
        self.jp_name.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
        self.jp_name.setObjectName("jp_name")
        self.score = QtWidgets.QLabel(self.bg)
        self.score.setGeometry(QtCore.QRect(710, 60, 81, 21))
        self.score.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
        self.score.setObjectName("score")
        self.score_number = QtWidgets.QLabel(self.bg)
        self.score_number.setGeometry(QtCore.QRect(710, 80, 51, 21))
        self.score_number.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
        self.score_number.setAlignment(QtCore.Qt.AlignCenter)
        self.score_number.setObjectName("score_number")
        self.status_name = QtWidgets.QLabel(self.bg)
        self.status_name.setGeometry(QtCore.QRect(145, 240, 151, 21))
        self.status_name.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
        self.status_name.setObjectName("status_name")
        self.current_status = QtWidgets.QLabel(self.bg)
        self.current_status.setGeometry(QtCore.QRect(20, 240, 111, 21))
        self.current_status.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
        self.current_status.setObjectName("current_status")
        self.published_from_date = QtWidgets.QLabel(self.bg)
        self.published_from_date.setGeometry(QtCore.QRect(145, 270, 151, 21))
        self.published_from_date.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
        self.published_from_date.setObjectName("published_from_date")
        self.published_from = QtWidgets.QLabel(self.bg)
        self.published_from.setGeometry(QtCore.QRect(20, 270, 111, 21))
        self.published_from.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
        self.published_from.setObjectName("published_from")
        self.published_to_date = QtWidgets.QLabel(self.bg)
        self.published_to_date.setGeometry(QtCore.QRect(145, 300, 151, 21))
        self.published_to_date.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
        self.published_to_date.setObjectName("published_to_date")
        self.published_to = QtWidgets.QLabel(self.bg)
        self.published_to.setGeometry(QtCore.QRect(20, 300, 111, 21))
        self.published_to.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
        self.published_to.setObjectName("published_to")
        self.chapters = QtWidgets.QLabel(self.bg)
        self.chapters.setGeometry(QtCore.QRect(20, 330, 111, 21))
        self.chapters.setAcceptDrops(False)
        self.chapters.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
        self.chapters.setScaledContents(False)
        self.chapters.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.chapters.setWordWrap(True)
        self.chapters.setObjectName("chapters")
        self.episodes_cnt = QtWidgets.QLabel(self.bg)
        self.episodes_cnt.setGeometry(QtCore.QRect(145, 330, 111, 21))
        self.episodes_cnt.setAcceptDrops(False)
        self.episodes_cnt.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
        self.episodes_cnt.setScaledContents(False)
        self.episodes_cnt.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.episodes_cnt.setWordWrap(True)
        self.episodes_cnt.setObjectName("episodes_cnt")
        self.volumes = QtWidgets.QLabel(self.bg)
        self.volumes.setGeometry(QtCore.QRect(20, 360, 111, 21))
        self.volumes.setAcceptDrops(False)
        self.volumes.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
        self.volumes.setScaledContents(False)
        self.volumes.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.volumes.setWordWrap(True)
        self.volumes.setObjectName("volumes")
        self.volumes_cnt = QtWidgets.QLabel(self.bg)
        self.volumes_cnt.setGeometry(QtCore.QRect(145, 360, 111, 21))
        self.volumes_cnt.setAcceptDrops(False)
        self.volumes_cnt.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
        self.volumes_cnt.setScaledContents(False)
        self.volumes_cnt.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.volumes_cnt.setWordWrap(True)
        self.volumes_cnt.setObjectName("volumes_cnt")
        self.genres = QtWidgets.QLabel(self.bg)
        self.genres.setGeometry(QtCore.QRect(300, 240, 111, 31))
        self.genres.setAcceptDrops(False)
        self.genres.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
        self.genres.setScaledContents(False)
        self.genres.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.genres.setWordWrap(True)
        self.genres.setObjectName("genres")
        self.genres_names = QtWidgets.QLabel(self.bg)
        self.genres_names.setGeometry(QtCore.QRect(300, 280, 161, 91))
        self.genres_names.setAcceptDrops(False)
        self.genres_names.setStyleSheet("color: rgb(255, 255, 255); font: 63 10pt Segoe UI Variable Display Semib;")
        self.genres_names.setScaledContents(False)
        self.genres_names.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.genres_names.setWordWrap(True)
        self.genres_names.setObjectName("genres_names")
        self.themes = QtWidgets.QLabel(self.bg)
        self.themes.setGeometry(QtCore.QRect(480, 240, 111, 31))
        self.themes.setAcceptDrops(False)
        self.themes.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
        self.themes.setScaledContents(False)
        self.themes.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.themes.setWordWrap(True)
        self.themes.setObjectName("themes")
        self.theme_names = QtWidgets.QLabel(self.bg)
        self.theme_names.setGeometry(QtCore.QRect(480, 280, 171, 91))
        self.theme_names.setAcceptDrops(False)
        self.theme_names.setStyleSheet("color: rgb(255, 255, 255); font: 63 10pt Segoe UI Variable Display Semib;")
        self.theme_names.setScaledContents(False)
        self.theme_names.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.theme_names.setWordWrap(True)
        self.theme_names.setObjectName("theme_names")
        self.synopsis = QtWidgets.QLabel(self.bg)
        self.synopsis.setGeometry(QtCore.QRect(175, 120, 71, 21))
        self.synopsis.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
        self.synopsis.setObjectName("synopsis")
        self.synopsis_text = QtWidgets.QLabel(self.bg)
        self.synopsis_text.setGeometry(QtCore.QRect(175, 140, 521, 91))
        self.synopsis_text.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt Segoe UI Variable Display Semib;")
        self.synopsis_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.synopsis_text.setWordWrap(True)
        self.synopsis_text.setObjectName("synopsis_text")
        self.add_to_list = QtWidgets.QPushButton(self.bg)
        self.add_to_list.setGeometry(QtCore.QRect(20, 510, 441, 51))
        self.add_to_list.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\"; background-color: rgb(27, 27, 45);")
        self.add_to_list.setObjectName("add_to_list")
        self.back_btn = QtWidgets.QPushButton(self.bg)
        self.back_btn.setGeometry(QtCore.QRect(640, 510, 141, 51))
        self.back_btn.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\"; background-color: rgb(27, 27, 45);")
        self.back_btn.setObjectName("back_btn")
        self.characters = QtWidgets.QPushButton(self.bg)
        self.characters.setGeometry(QtCore.QRect(20, 390, 161, 51))
        self.characters.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\"; background-color: rgb(27, 27, 45);")
        self.characters.setObjectName("characters")
        self.episodes = QtWidgets.QPushButton(self.bg)
        self.episodes.setGeometry(QtCore.QRect(20, 450, 161, 51))
        self.episodes.setStyleSheet("color: rgb(255, 255, 255); font: 63 11pt \"Segoe UI Variable Display Semib\"; background-color: rgb(27, 27, 45);")
        self.episodes.setObjectName("episodes")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.manga_name.setText(_translate("MainWindow", "Manga name"))
        self.en_title.setText(_translate("MainWindow", "English Name:"))
        self.en_name.setText(_translate("MainWindow", "en_name"))
        self.jp_title.setText(_translate("MainWindow", "Japanese Name:"))
        self.jp_name.setText(_translate("MainWindow", "jp_name"))
        self.score.setText(_translate("MainWindow", "SCORE"))
        self.score_number.setText(_translate("MainWindow", "7"))
        self.status_name.setText(_translate("MainWindow", "status_name"))
        self.current_status.setText(_translate("MainWindow", "Current status"))
        self.published_from_date.setText(_translate("MainWindow", "aired_from"))
        self.published_from.setText(_translate("MainWindow", "Published from"))
        self.published_to_date.setText(_translate("MainWindow", "aired_to"))
        self.published_to.setText(_translate("MainWindow", "Published to"))
        self.chapters.setText(_translate("MainWindow", "Chapters"))
        self.episodes_cnt.setText(_translate("MainWindow", "number"))
        self.volumes.setText(_translate("MainWindow", "Volumes"))
        self.volumes_cnt.setText(_translate("MainWindow", "duration"))
        self.genres.setText(_translate("MainWindow", "Genres"))
        self.genres_names.setText(_translate("MainWindow", "genres_names"))
        self.themes.setText(_translate("MainWindow", "Themes"))
        self.theme_names.setText(_translate("MainWindow", "theme_names"))
        self.synopsis.setText(_translate("MainWindow", "Synopsis"))
        self.synopsis_text.setText(_translate("MainWindow", "synopsis_text"))
        self.add_to_list.setText(_translate("MainWindow", "Add to my list"))
        self.back_btn.setText(_translate("MainWindow", "Back"))
        self.characters.setText(_translate("MainWindow", "Characters"))
        self.episodes.setText(_translate("MainWindow", "Authors"))
