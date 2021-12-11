# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'left_menuYgiGfM.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *

from PyQt5 import QtGui

class Ui_LeftMenu(object):
    def setupUi(self, LeftMenu):
        if not LeftMenu.objectName():
            LeftMenu.setObjectName(u"LeftMenu")
        LeftMenu.resize(200, 760)
        LeftMenu.setStyleSheet(u"background-color: rgb(12, 12, 12);")
        self.esteg_button = QPushButton(LeftMenu)
        self.esteg_button.setObjectName(u"esteg_button")
        self.esteg_button.setGeometry(QRect(10, 370, 181, 41))
        self.esteg_button.setStyleSheet(u"background-color: rgb(65, 65, 65);\n"
"color: rgb(255, 255, 255);")
        self.linear_parts_button = QPushButton(LeftMenu)
        self.linear_parts_button.setObjectName(u"linear_parts_button")
        self.linear_parts_button.setGeometry(QRect(10, 420, 181, 41))
        self.linear_parts_button.setStyleSheet(u"background-color: rgb(65, 65, 65);\n"
"color: rgb(255, 255, 255);")
        self.general_button = QPushButton(LeftMenu)
        self.general_button.setObjectName(u"general_button")
        self.general_button.setGeometry(QRect(10, 320, 181, 41))
        self.general_button.setStyleSheet(u"background-color: rgb(65, 65, 65);\n"
"color: rgb(255, 255, 255);")
        self.filters_button = QPushButton(LeftMenu)
        self.filters_button.setObjectName(u"filters_button")
        self.filters_button.setGeometry(QRect(10, 470, 181, 41))
        self.filters_button.setStyleSheet(u"background-color: rgb(65, 65, 65);\n"
"color: rgb(255, 255, 255);")
        self.choose_label = QLabel(LeftMenu)
        self.choose_label.setObjectName(u"choose_label")
        self.choose_label.setGeometry(QRect(50, 180, 101, 21))
        self.choose_label.setStyleSheet(u"color: rgb(214, 214, 214);")
        self.import_button = QPushButton(LeftMenu)
        self.import_button.setObjectName(u"import_button")
        self.import_button.setGeometry(QRect(40, 210, 131, 31))
        self.import_button.setStyleSheet(u"background-color: rgb(65, 65, 65);\n"
"color: rgb(255, 255, 255);")
        self.title_label = QLabel(LeftMenu)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(10, 20, 181, 101))
        self.title_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line = QFrame(LeftMenu)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 140, 181, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(LeftMenu)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(10, 270, 181, 20))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.retranslateUi(LeftMenu)

        QMetaObject.connectSlotsByName(LeftMenu)
    # setupUi

    def retranslateUi(self, LeftMenu):
        LeftMenu.setWindowTitle(QCoreApplication.translate("LeftMenu", u"Frame", None))
        self.esteg_button.setText(QCoreApplication.translate("LeftMenu", u"Esteganography", None))
        self.linear_parts_button.setText(QCoreApplication.translate("LeftMenu", u"Linear Part Points", None))
        self.general_button.setText(QCoreApplication.translate("LeftMenu", u"General", None))
        self.filters_button.setText(QCoreApplication.translate("LeftMenu", u"Filters", None))
        self.choose_label.setText(QCoreApplication.translate("LeftMenu", u"Choose an image...", None))
        self.import_button.setText(QCoreApplication.translate("LeftMenu", u"Import", None))
        self.title_label.setText(QCoreApplication.translate("LeftMenu", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:700;\">Homebrew</span></p><p align=\"center\"><span style=\" font-size:24pt; font-weight:700;\">GIMP</span></p></body></html>", None))
    # retranslateUi

