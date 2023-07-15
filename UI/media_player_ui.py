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
        media_player.resize(713, 598)
        font = QFont()
        font.setPointSize(11)
        media_player.setFont(font)
        self.actionBrowse = QAction(media_player)
        self.actionBrowse.setObjectName(u"actionBrowse")
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

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.volume_percent = QLabel(self.frame)
        self.volume_percent.setObjectName(u"volume_percent")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.volume_percent.sizePolicy().hasHeightForWidth())
        self.volume_percent.setSizePolicy(sizePolicy1)
        self.volume_percent.setMinimumSize(QSize(34, 0))
        self.volume_percent.setMaximumSize(QSize(34, 16777215))
        self.volume_percent.setStyleSheet(u"QLabel {\n"
"	color:black;\n"
"}")

        self.gridLayout_3.addWidget(self.volume_percent, 0, 2, 1, 1)

        self.volume_slider = QSlider(self.frame)
        self.volume_slider.setObjectName(u"volume_slider")
        sizePolicy.setHeightForWidth(self.volume_slider.sizePolicy().hasHeightForWidth())
        self.volume_slider.setSizePolicy(sizePolicy)
        self.volume_slider.setMaximum(100)
        self.volume_slider.setPageStep(10)
        self.volume_slider.setValue(0)
        self.volume_slider.setTracking(True)
        self.volume_slider.setOrientation(Qt.Horizontal)
        self.volume_slider.setInvertedAppearance(False)
        self.volume_slider.setInvertedControls(False)
        self.volume_slider.setTickPosition(QSlider.NoTicks)
        self.volume_slider.setTickInterval(0)

        self.gridLayout_3.addWidget(self.volume_slider, 0, 1, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMaximumSize(QSize(20, 20))
        self.label.setPixmap(QPixmap(u":/buttons/sound-on.png"))
        self.label.setScaledContents(True)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 5, 0, 1, 1)

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
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pb_back.sizePolicy().hasHeightForWidth())
        self.pb_back.setSizePolicy(sizePolicy2)
        icon = QIcon()
        icon.addFile(u":/buttons/previous-track.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_back.setIcon(icon)
        self.pb_back.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.pb_back)

        self.pb_stop = QPushButton(self.button_frame)
        self.pb_stop.setObjectName(u"pb_stop")
        sizePolicy2.setHeightForWidth(self.pb_stop.sizePolicy().hasHeightForWidth())
        self.pb_stop.setSizePolicy(sizePolicy2)
        icon1 = QIcon()
        icon1.addFile(u":/buttons/stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_stop.setIcon(icon1)
        self.pb_stop.setIconSize(QSize(13, 13))

        self.horizontalLayout.addWidget(self.pb_stop)

        self.pb_play_pause = QPushButton(self.button_frame)
        self.pb_play_pause.setObjectName(u"pb_play_pause")
        sizePolicy2.setHeightForWidth(self.pb_play_pause.sizePolicy().hasHeightForWidth())
        self.pb_play_pause.setSizePolicy(sizePolicy2)
        icon2 = QIcon()
        icon2.addFile(u":/buttons/pause-play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_play_pause.setIcon(icon2)
        self.pb_play_pause.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.pb_play_pause)

        self.pb_forward = QPushButton(self.button_frame)
        self.pb_forward.setObjectName(u"pb_forward")
        sizePolicy2.setHeightForWidth(self.pb_forward.sizePolicy().hasHeightForWidth())
        self.pb_forward.setSizePolicy(sizePolicy2)
        icon3 = QIcon()
        icon3.addFile(u":/buttons/next-track.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_forward.setIcon(icon3)
        self.pb_forward.setIconSize(QSize(20, 20))

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
        self.folder_view.setStyleSheet(u"")
        self.folder_view.setFrameShape(QFrame.NoFrame)
        self.folder_view.setSelectionMode(QAbstractItemView.SingleSelection)
        self.folder_view.setViewMode(QListView.ListMode)

        self.gridLayout_2.addWidget(self.folder_view, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.album_frame, 1, 0, 1, 1)

        media_player.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(media_player)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 713, 22))
        self.menubar.setFont(font)
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
        self.lb_song_time.setText("")
        self.volume_percent.setText(QCoreApplication.translate("media_player", u"0%", None))
        self.label.setText("")
        self.pb_back.setText("")
        self.pb_stop.setText("")
        self.pb_play_pause.setText("")
        self.pb_forward.setText("")
        self.lb_song_title.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("media_player", u"File", None))
    # retranslateUi

