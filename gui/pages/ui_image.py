# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagesqutfHo.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

# IMPORT QT CORE
from qt_core import *

from PyQt5 import QtGui

class Ui_application_image(object):
    def setupUi(self, application_image):
        if not application_image.objectName():
            application_image.setObjectName(u"application_image")
        application_image.resize(594, 604)
        application_image.setStyleSheet(u"background-color: rgb(31, 31, 31);")
        self.image = QWidget()
        self.image.setObjectName(u"image")
        self.verticalLayout = QVBoxLayout(self.image)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.image_label = QLabel(self.image)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.image_label)

        application_image.addWidget(self.image)

        self.retranslateUi(application_image)

        QMetaObject.connectSlotsByName(application_image)
    # setupUi

    def retranslateUi(self, application_image):
        application_image.setWindowTitle(QCoreApplication.translate("application_image", u"StackedWidget", None))
        # self.image_label.setText(QCoreApplication.translate("application_image", u"Display Image", None))
        # self.image_label.setPixmap(QtGui.QPixmap('reitoria.png'))
    # retranslateUi

