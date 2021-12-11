# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'linear_partszPyext.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *

from PyQt5 import QtGui

class Ui_LinearParts(object):
    def setupUi(self, LinearParts):
        if not LinearParts.objectName():
            LinearParts.setObjectName(u"LinearParts")
        LinearParts.resize(350, 760)
        LinearParts.setStyleSheet(u"background-color: rgb(82, 82, 82);")
        self.title = QLabel(LinearParts)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(20, 10, 171, 31))
        self.title.setLayoutDirection(Qt.LeftToRight)
        self.title.setAlignment(Qt.AlignCenter)
        self.points_x_values = QPlainTextEdit(LinearParts)
        self.points_x_values.setObjectName(u"points_x_values")
        self.points_x_values.setGeometry(QRect(40, 110, 271, 31))
        self.points_x_values.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.points_y_values = QPlainTextEdit(LinearParts)
        self.points_y_values.setObjectName(u"points_y_values")
        self.points_y_values.setGeometry(QRect(40, 180, 271, 31))
        self.points_y_values.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.points_x_label = QLabel(LinearParts)
        self.points_x_label.setObjectName(u"points_x_label")
        self.points_x_label.setGeometry(QRect(150, 80, 51, 31))
        self.points_y_label = QLabel(LinearParts)
        self.points_y_label.setObjectName(u"points_y_label")
        self.points_y_label.setGeometry(QRect(150, 150, 51, 31))
        self.see_plot_button = QPushButton(LinearParts)
        self.see_plot_button.setObjectName(u"see_plot_button")
        self.see_plot_button.setGeometry(QRect(110, 240, 131, 31))
        self.see_plot_button.setStyleSheet(u"background-color: rgb(65, 65, 65);\n"
"color: rgb(255, 255, 255);")
        self.apply_checked = QCheckBox(LinearParts)
        self.apply_checked.setObjectName(u"apply_checked")
        self.apply_checked.setGeometry(QRect(100, 310, 151, 20))
        self.apply_checked.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Segoe UI\";")

        self.retranslateUi(LinearParts)

        QMetaObject.connectSlotsByName(LinearParts)
    # setupUi

    def retranslateUi(self, LinearParts):
        LinearParts.setWindowTitle(QCoreApplication.translate("LinearParts", u"Frame", None))
        self.title.setText(QCoreApplication.translate("LinearParts", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; color:#ffffff;\">Linear Parts Points</span></p></body></html>", None))
        self.points_x_values.setPlainText("")
        self.points_y_values.setPlainText("")
        self.points_x_label.setText(QCoreApplication.translate("LinearParts", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Points x</span></p></body></html>", None))
        self.points_y_label.setText(QCoreApplication.translate("LinearParts", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Points y</span></p></body></html>", None))
        self.see_plot_button.setText(QCoreApplication.translate("LinearParts", u"See Plot", None))
        self.apply_checked.setText(QCoreApplication.translate("LinearParts", u"Linear Parts Apply", None))
    # retranslateUi

