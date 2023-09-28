# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(496, 372)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_6 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.my_grid = QGridLayout()
        self.my_grid.setObjectName(u"my_grid")

        self.verticalLayout_5.addLayout(self.my_grid)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_5.addItem(self.horizontalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.b_NG = QPushButton(self.centralwidget)
        self.b_NG.setObjectName(u"b_NG")
        font = QFont()
        font.setBold(True)
        font.setItalic(True)
        self.b_NG.setFont(font)

        self.horizontalLayout_4.addWidget(self.b_NG)

        self.b_check = QPushButton(self.centralwidget)
        self.b_check.setObjectName(u"b_check")
        self.b_check.setFont(font)

        self.horizontalLayout_4.addWidget(self.b_check)

        self.b_reset = QPushButton(self.centralwidget)
        self.b_reset.setObjectName(u"b_reset")
        self.b_reset.setFont(font)

        self.horizontalLayout_4.addWidget(self.b_reset)

        self.b_mode = QPushButton(self.centralwidget)
        self.b_mode.setObjectName(u"b_mode")
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setItalic(True)
        self.b_mode.setFont(font1)

        self.horizontalLayout_4.addWidget(self.b_mode)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 496, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.b_NG.setText(QCoreApplication.translate("MainWindow", u"New Game", None))
        self.b_check.setText(QCoreApplication.translate("MainWindow", u"Check Game", None))
        self.b_reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.b_mode.setText(QCoreApplication.translate("MainWindow", u"light mode    /    dark mode", None))
    # retranslateUi

