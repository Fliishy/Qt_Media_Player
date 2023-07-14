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
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSlider,
    QWidget)
import icons_rc

class Ui_Media_Player(object):
    def setupUi(self, Media_Player):
        if not Media_Player.objectName():
            Media_Player.setObjectName(u"Media_Player")
        Media_Player.resize(442, 428)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Media_Player.sizePolicy().hasHeightForWidth())
        Media_Player.setSizePolicy(sizePolicy)
        Media_Player.setToolTipDuration(0)
        self.gridLayout = QGridLayout(Media_Player)
        self.gridLayout.setObjectName(u"gridLayout")
        self.button_frame = QFrame(Media_Player)
        self.button_frame.setObjectName(u"button_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.button_frame.sizePolicy().hasHeightForWidth())
        self.button_frame.setSizePolicy(sizePolicy1)
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


        self.gridLayout.addWidget(self.button_frame, 3, 0, 1, 1)

        self.album_frame = QFrame(Media_Player)
        self.album_frame.setObjectName(u"album_frame")
        self.album_frame.setStyleSheet(u"QFrame {\n"
"	background-color: pink;\n"
"}")
        self.album_frame.setFrameShape(QFrame.StyledPanel)
        self.album_frame.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.album_frame, 0, 0, 1, 1)

        self.volume_slider = QSlider(Media_Player)
        self.volume_slider.setObjectName(u"volume_slider")
        self.volume_slider.setMaximum(100)
        self.volume_slider.setPageStep(20)
        self.volume_slider.setValue(0)
        self.volume_slider.setOrientation(Qt.Horizontal)
        self.volume_slider.setInvertedAppearance(False)
        self.volume_slider.setInvertedControls(False)
        self.volume_slider.setTickPosition(QSlider.NoTicks)
        self.volume_slider.setTickInterval(0)

        self.gridLayout.addWidget(self.volume_slider, 4, 0, 1, 1)

        self.lb_song_time = QLabel(Media_Player)
        self.lb_song_time.setObjectName(u"lb_song_time")
        sizePolicy1.setHeightForWidth(self.lb_song_time.sizePolicy().hasHeightForWidth())
        self.lb_song_time.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(12)
        self.lb_song_time.setFont(font)
        self.lb_song_time.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_song_time, 2, 0, 1, 1)

        self.lb_song_title = QLabel(Media_Player)
        self.lb_song_title.setObjectName(u"lb_song_title")
        sizePolicy1.setHeightForWidth(self.lb_song_title.sizePolicy().hasHeightForWidth())
        self.lb_song_title.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.lb_song_title.setFont(font1)
        self.lb_song_title.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_song_title, 1, 0, 1, 1)

        QWidget.setTabOrder(self.pb_back, self.pb_stop)
        QWidget.setTabOrder(self.pb_stop, self.pb_play_pause)
        QWidget.setTabOrder(self.pb_play_pause, self.pb_forward)

        self.retranslateUi(Media_Player)

        QMetaObject.connectSlotsByName(Media_Player)
    # setupUi

    def retranslateUi(self, Media_Player):
        Media_Player.setWindowTitle(QCoreApplication.translate("Media_Player", u"Media Player", None))
        self.pb_back.setText("")
        self.pb_stop.setText("")
        self.pb_play_pause.setText("")
        self.pb_forward.setText("")
        self.lb_song_time.setText(QCoreApplication.translate("Media_Player", u"-", None))
        self.lb_song_title.setText(QCoreApplication.translate("Media_Player", u"-", None))
    # retranslateUi

