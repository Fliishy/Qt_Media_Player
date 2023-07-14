# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'media_player.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QListView, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSlider, QStatusBar, QWidget)
import icons_rc

class Ui_media_player(object):
    def setupUi(self, media_player):
        if not media_player.objectName():
            media_player.setObjectName(u"media_player")
        media_player.resize(594, 537)
        self.actionBrowse = QAction(media_player)
        self.actionBrowse.setObjectName(u"actionBrowse")
        font = QFont()
        self.actionBrowse.setFont(font)
        self.actionQuit = QAction(media_player)
        self.actionQuit.setObjectName(u"actionQuit")
        self.centralwidget = QWidget(media_player)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lb_song_time = QLabel(self.centralwidget)
        self.lb_song_time.setObjectName(u"lb_song_time")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_song_time.sizePolicy().hasHeightForWidth())
        self.lb_song_time.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(12)
        self.lb_song_time.setFont(font1)
        self.lb_song_time.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_song_time, 3, 0, 1, 1)

        self.volume_slider = QSlider(self.centralwidget)
        self.volume_slider.setObjectName(u"volume_slider")
        self.volume_slider.setMaximum(100)
        self.volume_slider.setPageStep(20)
        self.volume_slider.setValue(0)
        self.volume_slider.setOrientation(Qt.Horizontal)
        self.volume_slider.setInvertedAppearance(False)
        self.volume_slider.setInvertedControls(False)
        self.volume_slider.setTickPosition(QSlider.NoTicks)
        self.volume_slider.setTickInterval(0)

        self.gridLayout.addWidget(self.volume_slider, 5, 0, 1, 1)

        self.button_frame = QFrame(self.centralwidget)
        self.button_frame.setObjectName(u"button_frame")
        sizePolicy.setHeightForWidth(self.button_frame.sizePolicy().hasHeightForWidth())
        self.button_frame.setSizePolicy(sizePolicy)
        self.button_frame.setMinimumSize(QSize(0, 1))
        self.button_frame.setFrameShape(QFrame.NoFrame)
        self.button_frame.setFrameShadow(QFrame.Plain)
        self.button_frame.setLineWidth(1)
        self.horizontalLayout = QHBoxLayout(self.button_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pb_back = QPushButton(self.button_frame)
        self.pb_back.setObjectName(u"pb_back")
        icon = QIcon()
        icon.addFile(u":/buttons/previous-track.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_back.setIcon(icon)

        self.horizontalLayout.addWidget(self.pb_back)

        self.pb_stop = QPushButton(self.button_frame)
        self.pb_stop.setObjectName(u"pb_stop")
        icon1 = QIcon()
        icon1.addFile(u":/buttons/stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_stop.setIcon(icon1)

        self.horizontalLayout.addWidget(self.pb_stop)

        self.pb_play_pause = QPushButton(self.button_frame)
        self.pb_play_pause.setObjectName(u"pb_play_pause")
        icon2 = QIcon()
        icon2.addFile(u":/buttons/pause-play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_play_pause.setIcon(icon2)

        self.horizontalLayout.addWidget(self.pb_play_pause)

        self.pb_forward = QPushButton(self.button_frame)
        self.pb_forward.setObjectName(u"pb_forward")
        icon3 = QIcon()
        icon3.addFile(u":/buttons/next-track.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_forward.setIcon(icon3)

        self.horizontalLayout.addWidget(self.pb_forward)


        self.gridLayout.addWidget(self.button_frame, 4, 0, 1, 1)

        self.lb_song_title = QLabel(self.centralwidget)
        self.lb_song_title.setObjectName(u"lb_song_title")
        sizePolicy.setHeightForWidth(self.lb_song_title.sizePolicy().hasHeightForWidth())
        self.lb_song_title.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        self.lb_song_title.setFont(font2)
        self.lb_song_title.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_song_title, 2, 0, 1, 1)

        self.album_frame = QFrame(self.centralwidget)
        self.album_frame.setObjectName(u"album_frame")
        self.album_frame.setFrameShape(QFrame.NoFrame)
        self.album_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.album_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.folder_view = QListView(self.album_frame)
        self.folder_view.setObjectName(u"folder_view")
        self.folder_view.setFrameShape(QFrame.NoFrame)
        self.folder_view.setSelectionMode(QAbstractItemView.SingleSelection)

        self.gridLayout_2.addWidget(self.folder_view, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.album_frame, 1, 0, 1, 1)

        media_player.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(media_player)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 594, 20))
        font3 = QFont()
        font3.setPointSize(10)
        self.menubar.setFont(font3)
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        media_player.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(media_player)
        self.statusbar.setObjectName(u"statusbar")
        media_player.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionBrowse)
        self.menuFile.addAction(self.actionQuit)

        self.retranslateUi(media_player)

        QMetaObject.connectSlotsByName(media_player)
    # setupUi

    def retranslateUi(self, media_player):
        media_player.setWindowTitle(QCoreApplication.translate("media_player", u"Media Player", None))
        self.actionBrowse.setText(QCoreApplication.translate("media_player", u"Browse", None))
        self.actionQuit.setText(QCoreApplication.translate("media_player", u"Quit", None))
        self.lb_song_time.setText(QCoreApplication.translate("media_player", u"-", None))
        self.pb_back.setText("")
        self.pb_stop.setText("")
        self.pb_play_pause.setText("")
        self.pb_forward.setText("")
        self.lb_song_title.setText(QCoreApplication.translate("media_player", u"-", None))
        self.menuFile.setTitle(QCoreApplication.translate("media_player", u"File", None))
    # retranslateUi

