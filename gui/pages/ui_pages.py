# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagesCerITO.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_application_image(object):
    def setupUi(self, application_image):
        if not application_image.objectName():
            application_image.setObjectName(u"application_image")
        application_image.resize(594, 604)
        self.image = QWidget()
        self.image.setObjectName(u"image")
        self.verticalLayout = QVBoxLayout(self.image)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_image = QLabel(self.image)
        self.label_image.setObjectName(u"label_image")
        self.label_image.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_image)

        application_image.addWidget(self.image)

        self.retranslateUi(application_image)

        QMetaObject.connectSlotsByName(application_image)
    # setupUi

    def retranslateUi(self, application_image):
        application_image.setWindowTitle(QCoreApplication.translate("application_image", u"StackedWidget", None))
        self.label_image.setText(QCoreApplication.translate("application_image", u"Display Imagem", None))
    # retranslateUi

