# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'esteganografiaodwgaS.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *

from PyQt5 import QtGui

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(350, 760)
        Frame.setLayoutDirection(Qt.LeftToRight)
        Frame.setStyleSheet(u"")
        self.label = QLabel(Frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 181, 31))
        self.plainTextEdit = QPlainTextEdit(Frame)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(40, 70, 281, 131))
        self.plainTextEdit.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.pushButton = QPushButton(Frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(110, 220, 151, 31))
        self.pushButton.setStyleSheet(u"background-color: rgb(82, 82, 82);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2 = QPushButton(Frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(110, 350, 151, 31))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(82, 82, 82);\n"
"color: rgb(255, 255, 255);")
        self.label_2 = QLabel(Frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 320, 201, 31))

        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.label.setText(QCoreApplication.translate("Frame", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; color:#ffffff;\">Esteganography</span></p></body></html>", None))
        self.plainTextEdit.setPlainText("")
        self.pushButton.setText(QCoreApplication.translate("Frame", u"Encode", None))
        self.pushButton_2.setText(QCoreApplication.translate("Frame", u"Decode", None))
        self.label_2.setText(QCoreApplication.translate("Frame", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Already have an encoded image?</span></p></body></html>", None))
    # retranslateUi

