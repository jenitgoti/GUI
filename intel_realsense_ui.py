# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'intel_realsense.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QTabWidget, QVBoxLayout, QWidget)

class Ui_Form_2(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(889, 819)
        self.verticalLayout_4 = QVBoxLayout(Form)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_7 = QWidget(self.widget_2)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget_10 = QWidget(self.widget_7)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.widget_10)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #666666;  /* Matte gray */\n"
"    color: white;               /* Text color */\n"
"    border: none;\n"
"    padding: 8px 16px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #777777;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #555555;\n"
"}\n"
"")
        self.pushButton.setCheckable(True)
        self.pushButton.setAutoRepeat(True)

        self.horizontalLayout_4.addWidget(self.pushButton)


        self.horizontalLayout_3.addWidget(self.widget_10)

        self.widget_9 = QWidget(self.widget_7)
        self.widget_9.setObjectName(u"widget_9")

        self.horizontalLayout_3.addWidget(self.widget_9)

        self.widget_8 = QWidget(self.widget_7)
        self.widget_8.setObjectName(u"widget_8")

        self.horizontalLayout_3.addWidget(self.widget_8)


        self.horizontalLayout_2.addWidget(self.widget_7)


        self.verticalLayout.addWidget(self.widget_2, 0, Qt.AlignmentFlag.AlignTop)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.widget_3)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_5 = QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.tab_3)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_2)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_3 = QVBoxLayout(self.tab_4)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.tab_4)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.tabWidget.addTab(self.tab_4, "")

        self.verticalLayout_2.addWidget(self.tabWidget)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout = QHBoxLayout(self.widget_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.widget_4)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setSpacing(12)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(12, 12, 12, 12)
        self.widget_11 = QWidget(self.widget_5)
        self.widget_11.setObjectName(u"widget_11")

        self.horizontalLayout_5.addWidget(self.widget_11)

        self.widget_6 = QWidget(self.widget_5)
        self.widget_6.setObjectName(u"widget_6")

        self.horizontalLayout_5.addWidget(self.widget_6)

        self.widget_12 = QWidget(self.widget_5)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.widget_12)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #666666;  /* Matte gray */\n"
"    color: white;               /* Text color */\n"
"    border: none;\n"
"    padding: 8px 16px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #777777;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #555555;\n"
"}\n"
"")
        self.pushButton_2.setIconSize(QSize(20, 20))
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setAutoRepeat(True)

        self.horizontalLayout_6.addWidget(self.pushButton_2)


        self.horizontalLayout_5.addWidget(self.widget_12)


        self.horizontalLayout.addWidget(self.widget_5)


        self.verticalLayout.addWidget(self.widget_4, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_4.addWidget(self.widget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Select", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"selected_1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"Tab 1", None))
        self.label.setText(QCoreApplication.translate("Form", u"selected_2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Form", u"Tab 2", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"cancel", None))
    # retranslateUi

