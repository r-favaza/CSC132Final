# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiPracticeTpMRuu.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(800, 600)
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 801, 601))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 190, 451, 81))
        font = QFont()
        font.setPointSize(32)
        font.setBold(True)
        self.label.setFont(font)
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(160, 380, 461, 31))
        font1 = QFont()
        font1.setPointSize(14)
        self.label_2.setFont(font1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.listWidget = QListWidget(self.tab_2)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(0, 0, 256, 571))
        self.listWidget_2 = QListWidget(self.tab_2)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setGeometry(QRect(270, 0, 256, 571))
        self.listWidget_3 = QListWidget(self.tab_2)
        self.listWidget_3.setObjectName(u"listWidget_3")
        self.listWidget_3.setGeometry(QRect(540, 0, 256, 571))
        self.verticalLayoutWidget = QWidget(self.tab_2)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 251, 571))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout.addWidget(self.pushButton_6)

        self.pushButton_3 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_7 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.verticalLayout.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.verticalLayout.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.verticalLayout.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.verticalLayout.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.verticalLayout.addWidget(self.pushButton_12)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Welcome to the Expo!", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Use the Tabs in the upper right hand corner to explore!", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Dialog", u"Home", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"Project 1", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"Project 2", None))
        self.pushButton_6.setText(QCoreApplication.translate("Dialog", u"Project 3", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Project 4", None))
        self.pushButton_7.setText(QCoreApplication.translate("Dialog", u"Project 5", None))
        self.pushButton_8.setText(QCoreApplication.translate("Dialog", u"Project 6", None))
        self.pushButton_9.setText(QCoreApplication.translate("Dialog", u"Project 7", None))
        self.pushButton_10.setText(QCoreApplication.translate("Dialog", u"Project 8", None))
        self.pushButton_11.setText(QCoreApplication.translate("Dialog", u"Project 9", None))
        self.pushButton_12.setText(QCoreApplication.translate("Dialog", u"Project 10", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Dialog", u"List", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Dialog", u"Map", None))
    # retranslateUi

