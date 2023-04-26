# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiPractice2yYFZFl.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys


from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QSizePolicy,
    QTabWidget, QWidget)

from project import Project

class Ui_Dialog(object):
    def setupUi(self, Dialog, manager):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")

        self.projectWidgets = []

        self.manager = manager

        Dialog.resize(800, 600)
        self.listTabWidget = QTabWidget(Dialog)
        self.listTabWidget.setObjectName(u"listTabWidget")
        self.listTabWidget.setGeometry(QRect(0, 0, 801, 601))
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
        self.listTabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.projPageWidget = QTabWidget(self.tab_2)
        self.projPageWidget.setObjectName(u"projPageWidget")
        self.projPageWidget.setGeometry(QRect(6, 9, 781, 561))
        self.projPageWidget.setTabPosition(QTabWidget.North)
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")



        self.projInfoWidget = QTabWidget(self.tab_4)
        self.projInfoWidget.setObjectName(u"projInfoWidget")
        self.projInfoWidget.setGeometry(QRect(6, 9, 761, 511))
        self.projInfoWidget.setTabPosition(QTabWidget.West)

        self.projInfoWidget.tabBarClicked.connect(self.projectSelected)

        '''self.projInfoTab = QWidget()
        self.projInfoTab.setObjectName(u"projInfoTab")
        self.nameLabel = QLabel(self.projInfoTab)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setGeometry(QRect(18, 15, 691, 61))
        font2 = QFont()
        font2.setPointSize(20)
        self.nameLabel.setFont(font2)
        self.nameLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.nameLabel.setWordWrap(True)
        self.membersLabel = QLabel(self.projInfoTab)
        self.membersLabel.setObjectName(u"membersLabel")
        self.membersLabel.setGeometry(QRect(20, 80, 691, 71))
        font3 = QFont()
        font3.setPointSize(16)
        self.membersLabel.setFont(font3)
        self.membersLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.membersLabel.setWordWrap(True)
        self.categoriesLabel = QLabel(self.projInfoTab)
        self.categoriesLabel.setObjectName(u"categoriesLabel")
        self.categoriesLabel.setGeometry(QRect(20, 140, 691, 51))
        self.categoriesLabel.setFont(font3)
        self.categoriesLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.categoriesLabel.setWordWrap(True)
        self.descriptionLabel = QLabel(self.projInfoTab)
        self.descriptionLabel.setObjectName(u"descriptionLabel")
        self.descriptionLabel.setGeometry(QRect(28, 195, 681, 291))
        self.descriptionLabel.setFont(font3)
        self.descriptionLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.descriptionLabel.setWordWrap(True)'''
        #self.projInfoWidget.addTab(self.projInfoTab, "")
        self.projPageWidget.addTab(self.tab_4, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.listTabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget_5 = QTabWidget(self.tab_3)
        self.tabWidget_5.setObjectName(u"tabWidget_5")
        self.tabWidget_5.setGeometry(QRect(6, 9, 781, 561))
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.tabWidget_6 = QTabWidget(self.tab_12)
        self.tabWidget_6.setObjectName(u"tabWidget_6")
        self.tabWidget_6.setGeometry(QRect(6, 9, 761, 511))
        self.tabWidget_6.setTabPosition(QTabWidget.West)
        self.tab_15 = QWidget()
        self.tab_15.setObjectName(u"tab_15")
        self.tabWidget_6.addTab(self.tab_15, "")
        self.tab_16 = QWidget()
        self.tab_16.setObjectName(u"tab_16")
        self.tabWidget_6.addTab(self.tab_16, "")
        self.tabWidget_5.addTab(self.tab_12, "")
        self.tab_13 = QWidget()
        self.tab_13.setObjectName(u"tab_13")
        self.tabWidget_7 = QTabWidget(self.tab_13)
        self.tabWidget_7.setObjectName(u"tabWidget_7")
        self.tabWidget_7.setGeometry(QRect(6, 9, 761, 511))
        self.tabWidget_7.setTabPosition(QTabWidget.West)
        self.tab_17 = QWidget()
        self.tab_17.setObjectName(u"tab_17")
        self.tabWidget_7.addTab(self.tab_17, "")
        self.tab_18 = QWidget()
        self.tab_18.setObjectName(u"tab_18")
        self.tabWidget_7.addTab(self.tab_18, "")
        self.tabWidget_5.addTab(self.tab_13, "")
        self.tab_14 = QWidget()
        self.tab_14.setObjectName(u"tab_14")
        self.tabWidget_8 = QTabWidget(self.tab_14)
        self.tabWidget_8.setObjectName(u"tabWidget_8")
        self.tabWidget_8.setGeometry(QRect(6, 9, 761, 511))
        self.tabWidget_8.setTabPosition(QTabWidget.West)
        self.tab_19 = QWidget()
        self.tab_19.setObjectName(u"tab_19")
        self.tabWidget_8.addTab(self.tab_19, "")
        self.tab_20 = QWidget()
        self.tab_20.setObjectName(u"tab_20")
        self.tabWidget_8.addTab(self.tab_20, "")
        self.tabWidget_5.addTab(self.tab_14, "")
        self.listTabWidget.addTab(self.tab_3, "")

        self.retranslateUi(Dialog)

        self.listTabWidget.setCurrentIndex(0)
        self.projPageWidget.setCurrentIndex(0)
        self.projInfoWidget.setCurrentIndex(0)
        self.tabWidget_5.setCurrentIndex(0)
        self.tabWidget_6.setCurrentIndex(0)
        self.tabWidget_7.setCurrentIndex(0)
        self.tabWidget_8.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def projectSelected(self, index):
        print("SELECTED", index)
        self.manager.onProjectSelected(index)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Welcome to the Expo!", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Use the Tabs in the upper right hand corner to explore!", None))
        self.listTabWidget.setTabText(self.listTabWidget.indexOf(self.tab), QCoreApplication.translate("Dialog", u"Home", None))
        self.projPageWidget.setTabText(self.projPageWidget.indexOf(self.tab_4), QCoreApplication.translate("Dialog", u"Projects Page", None))
        self.listTabWidget.setTabText(self.listTabWidget.indexOf(self.tab_2), QCoreApplication.translate("Dialog", u"List", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_15), QCoreApplication.translate("Dialog", u"Section 1", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_16), QCoreApplication.translate("Dialog", u"Section 2", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_12), QCoreApplication.translate("Dialog", u"Floor 1", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_17), QCoreApplication.translate("Dialog", u"Section 1", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_18), QCoreApplication.translate("Dialog", u"Section 2", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_13), QCoreApplication.translate("Dialog", u"Floor 2", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_19), QCoreApplication.translate("Dialog", u"Section 1", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_20), QCoreApplication.translate("Dialog", u"Section 2", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_14), QCoreApplication.translate("Dialog", u"Floor 3", None))
        self.listTabWidget.setTabText(self.listTabWidget.indexOf(self.tab_3), QCoreApplication.translate("Dialog", u"Map", None))
    # retranslateUi







# UI setup
app = QApplication(sys.argv)
d = QDialog()
ui = Ui_Dialog()
#ui.setupUi(d)

def makeProjectWidget(project:Project, widget:QWidget):
    ui.projInfoWidget.addTab(widget, "")
    ui.projInfoWidget.setTabText(ui.projInfoWidget.indexOf(widget), QCoreApplication.translate("Dialog", f"Project {ui.projInfoWidget.indexOf(widget)}", None))

def makeProjectInfoTab(project:Project, manager):
    projInfoTab = QWidget()

    projInfoTab.project = project
    projInfoTab.manager = manager

    print(projInfoTab.project, projInfoTab.manager, projInfoTab.mousePressEvent)

    projInfoTab.setObjectName(u"projInfoTab")
    nameLabel = QLabel(projInfoTab)
    nameLabel.setObjectName(u"nameLabel")
    nameLabel.setGeometry(QRect(18, 15, 691, 61))
    font2 = QFont()
    font2.setPointSize(20)
    nameLabel.setFont(font2)
    nameLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
    nameLabel.setWordWrap(True)
    membersLabel = QLabel(projInfoTab)
    membersLabel.setObjectName(u"membersLabel")
    membersLabel.setGeometry(QRect(20, 80, 691, 71))
    font3 = QFont()
    font3.setPointSize(16)
    membersLabel.setFont(font3)
    membersLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
    membersLabel.setWordWrap(True)
    categoriesLabel = QLabel(projInfoTab)
    categoriesLabel.setObjectName(u"categoriesLabel")
    categoriesLabel.setGeometry(QRect(20, 140, 691, 51))
    categoriesLabel.setFont(font3)
    categoriesLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
    categoriesLabel.setWordWrap(True)
    descriptionLabel = QLabel(projInfoTab)
    descriptionLabel.setObjectName(u"descriptionLabel")
    descriptionLabel.setGeometry(QRect(28, 195, 681, 291))
    descriptionLabel.setFont(font3)
    descriptionLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
    descriptionLabel.setWordWrap(True)

    nameLabel.setText(QCoreApplication.translate("Dialog", f"Name: {project.name}", None))
    membersLabel.setText(QCoreApplication.translate("Dialog", f"Group Members: {project.members}", None))
    categoriesLabel.setText(QCoreApplication.translate("Dialog", f"Categories: {project.categories}", None))
    descriptionLabel.setText(QCoreApplication.translate("Dialog", f"Description: {project.desc}", None))

    return projInfoTab

def generateFromProjects(projects:list[Project], manager):
    
    ui.setupUi(d, manager)

    for project in projects:
        widget = makeProjectInfoTab(project, manager)
        makeProjectWidget(project, widget)

def startUI():
    d.exec_()