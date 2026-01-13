# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calibration_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class calibrate_form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(730, 673)
        Form.setStyleSheet(u"background-color: #1a1a1a;\n"
"border: none;\n"
"")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")

        self.horizontalLayout_2.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout = QVBoxLayout(self.widget_3)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_2 = QVBoxLayout(self.widget_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_8 = QWidget(self.widget_5)
        self.widget_8.setObjectName(u"widget_8")

        self.verticalLayout_2.addWidget(self.widget_8)

        self.widget_6 = QWidget(self.widget_5)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_3 = QVBoxLayout(self.widget_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_111 = QPushButton(self.widget_6)
        self.pushButton_111.setObjectName(u"pushButton_111")
        self.pushButton_111.setStyleSheet(u"QPushButton {\n"
"    background-color: #121212;   /* Matte black background */\n"
"    color: white;                /* Text color */\n"
"    border: 1px solid white;     /* White border */\n"
"    border-radius: 10px;         /* Rounded corners */\n"
"    padding: 15px 30px;           /* Optional: nice spacing */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1f1f1f;   /* Slightly lighter on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0d0d0d;   /* Slightly darker when pressed */\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.pushButton_111)

        self.pushButton_222 = QPushButton(self.widget_6)
        self.pushButton_222.setObjectName(u"pushButton_222")
        self.pushButton_222.setStyleSheet(u"QPushButton {\n"
"    background-color: #121212;   /* Matte black background */\n"
"    color: white;                /* Text color */\n"
"    border: 1px solid white;     /* White border */\n"
"    border-radius: 10px;         /* Rounded corners */\n"
"    padding: 15px 30px;           /* Optional: nice spacing */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1f1f1f;   /* Slightly lighter on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0d0d0d;   /* Slightly darker when pressed */\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.pushButton_222)


        self.verticalLayout_2.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.widget_5)
        self.widget_7.setObjectName(u"widget_7")

        self.verticalLayout_2.addWidget(self.widget_7)


        self.verticalLayout.addWidget(self.widget_5)


        self.horizontalLayout_2.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")

        self.horizontalLayout_2.addWidget(self.widget_4)


        self.horizontalLayout.addWidget(self.widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_111.setText(QCoreApplication.translate("Form", u"Calibrate", None))
        self.pushButton_222.setText(QCoreApplication.translate("Form", u"Save Result", None))
    # retranslateUi