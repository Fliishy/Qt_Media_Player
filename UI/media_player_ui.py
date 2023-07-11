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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QSizePolicy, QWidget)

class Ui_Media_Player(object):
    def setupUi(self, Media_Player):
        if not Media_Player.objectName():
            Media_Player.setObjectName(u"Media_Player")
        Media_Player.resize(442, 395)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Media_Player.sizePolicy().hasHeightForWidth())
        Media_Player.setSizePolicy(sizePolicy)
        Media_Player.setToolTipDuration(0)
        self.gridLayout = QGridLayout(Media_Player)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lb_song_title = QLabel(Media_Player)
        self.lb_song_title.setObjectName(u"lb_song_title")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lb_song_title.sizePolicy().hasHeightForWidth())
        self.lb_song_title.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.lb_song_title.setFont(font)
        self.lb_song_title.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_song_title, 1, 0, 1, 1)

        self.frame = QFrame(Media_Player)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.lb_song_time = QLabel(Media_Player)
        self.lb_song_time.setObjectName(u"lb_song_time")
        sizePolicy1.setHeightForWidth(self.lb_song_time.sizePolicy().hasHeightForWidth())
        self.lb_song_time.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(12)
        self.lb_song_time.setFont(font1)
        self.lb_song_time.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_song_time, 2, 0, 1, 1)


        self.retranslateUi(Media_Player)

        QMetaObject.connectSlotsByName(Media_Player)
    # setupUi

    def retranslateUi(self, Media_Player):
        Media_Player.setWindowTitle(QCoreApplication.translate("Media_Player", u"Media Player", None))
        self.lb_song_title.setText("")
        self.lb_song_time.setText("")
    # retranslateUi

