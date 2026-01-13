# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'connect_arm.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)
import resources_2_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(889, 819)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Left_main_cointainer = QWidget(Form)
        self.Left_main_cointainer.setObjectName(u"Left_main_cointainer")
        self.Left_main_cointainer.setMinimumSize(QSize(443, 0))
        self.Left_main_cointainer.setMaximumSize(QSize(445, 16777215))
        self.Left_main_cointainer.setStyleSheet(u"background-color: #1a1a1a;")
        self.verticalLayout_2 = QVBoxLayout(self.Left_main_cointainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.Left_main_cointainer)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(445, 0))
        self.widget_6.setMaximumSize(QSize(16777215, 16777215))
        self.widget_6.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.widget_6)
        self.pushButton.setObjectName(u"pushButton")
        icon = QIcon()
        icon.addFile(u":/WhatsApp Image 2025-04-20 at 23.48.25.jpeg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/WhatsApp Image 2025-04-21 at 00.15.47.jpeg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(30, 30))
        self.pushButton.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget_6)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon1 = QIcon()
        icon1.addFile(u":/WhatsApp Image 2025-04-20 at 23.54.22.jpeg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/WhatsApp Image 2025-04-21 at 00.15.47.jpeg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(30, 30))
        self.pushButton_2.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.widget_6)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon2 = QIcon()
        icon2.addFile(u":/3.jpeg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/WhatsApp Image 2025-04-21 at 00.15.47.jpeg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(30, 30))
        self.pushButton_3.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.pushButton_3)


        self.verticalLayout_2.addWidget(self.widget_6, 0, Qt.AlignmentFlag.AlignTop)

        self.widget_7 = QWidget(self.Left_main_cointainer)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(445, 780))
        self.widget_7.setMaximumSize(QSize(16777215, 780))
        self.verticalLayout_3 = QVBoxLayout(self.widget_7)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_3 = QStackedWidget(self.widget_7)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.stackedWidget_3.setMinimumSize(QSize(445, 780))
        self.stackedWidget_3.setMaximumSize(QSize(16777215, 780))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_4 = QWidget(self.page)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_7 = QVBoxLayout(self.widget_4)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_4)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label)


        self.verticalLayout_4.addWidget(self.widget_4, 0, Qt.AlignmentFlag.AlignTop)

        self.widget_3 = QWidget(self.page)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_5 = QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.widget_3)
        self.label_6.setObjectName(u"label_6")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_6)

        self.PC_IP = QLineEdit(self.widget_3)
        self.PC_IP.setObjectName(u"PC_IP")
        self.PC_IP.setStyleSheet(u"QLineEdit{\n"
"	padding-left:20px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 10px;\n"
"\n"
"}")

        self.verticalLayout_5.addWidget(self.PC_IP)


        self.verticalLayout_4.addWidget(self.widget_3, 0, Qt.AlignmentFlag.AlignTop)

        self.widget_2 = QWidget(self.page)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_6 = QVBoxLayout(self.widget_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_7)

        self.Robot_IP = QLineEdit(self.widget_2)
        self.Robot_IP.setObjectName(u"Robot_IP")
        self.Robot_IP.setStyleSheet(u"QLineEdit{\n"
"	padding-left:20px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 10px;\n"
"\n"
"}")

        self.verticalLayout_6.addWidget(self.Robot_IP)


        self.verticalLayout_4.addWidget(self.widget_2, 0, Qt.AlignmentFlag.AlignTop)

        self.widget = QWidget(self.page)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_8 = QVBoxLayout(self.widget)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget_8 = QWidget(self.widget)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_14 = QWidget(self.widget_8)
        self.widget_14.setObjectName(u"widget_14")
        self.Simulation = QPushButton(self.widget_14)
        self.Simulation.setObjectName(u"Simulation")
        self.Simulation.setGeometry(QRect(20, 0, 151, 61))
        self.Simulation.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"   \n"
"    background-color: #1a1a1a;\n"
"    color: white;\n"
"	padding-left:10px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: white;\n"
"    color: black;\n"
"	padding-left:10px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/gazebo_horz_neg-e0da3ed723798565c8f4016312f47f2041760d58a13991c79f01f7210fb140b2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Simulation.setIcon(icon3)
        self.Simulation.setIconSize(QSize(140, 140))
        self.Simulation.setCheckable(True)
        self.widget_13 = QWidget(self.widget_14)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setGeometry(QRect(200, 0, 198, 70))
        self.congigureBtn = QPushButton(self.widget_13)
        self.congigureBtn.setObjectName(u"congigureBtn")
        self.congigureBtn.setGeometry(QRect(40, 0, 101, 32))
        self.congigureBtn.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"   \n"
"    background-color: #1a1a1a;\n"
"    color: white;\n"
"	padding-left:10px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: white;\n"
"    color: black;\n"
"	padding-left:10px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"")
        self.congigureBtn.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.widget_14)


        self.verticalLayout_8.addWidget(self.widget_8)

        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")

        self.verticalLayout_8.addWidget(self.widget_5)


        self.verticalLayout_4.addWidget(self.widget)

        self.lineEdit_2 = QLineEdit(self.page)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_4.addWidget(self.lineEdit_2)

        self.stackedWidget_3.addWidget(self.page)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_17 = QVBoxLayout(self.page_6)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.widget_27 = QWidget(self.page_6)
        self.widget_27.setObjectName(u"widget_27")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_27)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.widget_27)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_8)


        self.verticalLayout_17.addWidget(self.widget_27, 0, Qt.AlignmentFlag.AlignTop)

        self.widget_28 = QWidget(self.page_6)
        self.widget_28.setObjectName(u"widget_28")
        self.gridLayout = QGridLayout(self.widget_28)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_7 = QPushButton(self.widget_28)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"   \n"
"    background-color: #1a1a1a;\n"
"    color: white;\n"
"	padding-left:10px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: white;\n"
"    color: black;\n"
"	padding-left:10px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"")
        self.pushButton_7.setCheckable(True)

        self.gridLayout.addWidget(self.pushButton_7, 0, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.widget_28)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"   \n"
"    background-color: #1a1a1a;\n"
"    color: white;\n"
"	padding-left:10px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: white;\n"
"    color: black;\n"
"	padding-left:10px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"")
        self.pushButton_8.setCheckable(True)

        self.gridLayout.addWidget(self.pushButton_8, 0, 1, 1, 1)

        self.pushButton_9 = QPushButton(self.widget_28)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"   \n"
"    background-color: #1a1a1a;\n"
"    color: white;\n"
"	padding-left:10px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: white;\n"
"    color: black;\n"
"	padding-left:10px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"")
        self.pushButton_9.setCheckable(True)

        self.gridLayout.addWidget(self.pushButton_9, 1, 0, 1, 1)

        self.pushButton_10 = QPushButton(self.widget_28)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"   \n"
"    background-color: #1a1a1a;\n"
"    color: white;\n"
"	padding-left:10px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 30px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: white;\n"
"    color: black;\n"
"	padding-left:10px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 30px;\n"
"}\n"
"\n"
"\n"
"")
        self.pushButton_10.setCheckable(True)

        self.gridLayout.addWidget(self.pushButton_10, 1, 1, 1, 1)


        self.verticalLayout_17.addWidget(self.widget_28)

        self.widget_29 = QWidget(self.page_6)
        self.widget_29.setObjectName(u"widget_29")
        self.gridLayout_2 = QGridLayout(self.widget_29)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_11 = QPushButton(self.widget_29)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"   \n"
"    background-color: #1a1a1a;\n"
"    color: white;\n"
"	padding-left:10px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: white;\n"
"    color: black;\n"
"	padding-left:10px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"")
        self.pushButton_11.setCheckable(True)

        self.gridLayout_2.addWidget(self.pushButton_11, 0, 0, 1, 1)

        self.pushButton_14 = QPushButton(self.widget_29)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"   \n"
"    background-color: #1a1a1a;\n"
"    color: white;\n"
"	padding-left:10px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: white;\n"
"    color: black;\n"
"	padding-left:10px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"")
        self.pushButton_14.setCheckable(True)

        self.gridLayout_2.addWidget(self.pushButton_14, 1, 1, 1, 1)

        self.pushButton_12 = QPushButton(self.widget_29)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"   \n"
"    background-color: #1a1a1a;\n"
"    color: white;\n"
"	padding-left:10px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: white;\n"
"    color: black;\n"
"	padding-left:10px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"")
        self.pushButton_12.setCheckable(True)

        self.gridLayout_2.addWidget(self.pushButton_12, 0, 1, 1, 1)

        self.pushButton_13 = QPushButton(self.widget_29)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"   \n"
"    background-color: #1a1a1a;\n"
"    color: white;\n"
"	padding-left:10px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: white;\n"
"    color: black;\n"
"	padding-left:10px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"")
        self.pushButton_13.setCheckable(True)

        self.gridLayout_2.addWidget(self.pushButton_13, 1, 0, 1, 1)


        self.verticalLayout_17.addWidget(self.widget_29)

        self.widget_30 = QWidget(self.page_6)
        self.widget_30.setObjectName(u"widget_30")

        self.verticalLayout_17.addWidget(self.widget_30)

        self.stackedWidget_3.addWidget(self.page_6)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_16 = QVBoxLayout(self.page_5)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.widget_25 = QWidget(self.page_5)
        self.widget_25.setObjectName(u"widget_25")
        self.verticalLayout_18 = QVBoxLayout(self.widget_25)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.widget_23 = QWidget(self.widget_25)
        self.widget_23.setObjectName(u"widget_23")
        self.verticalLayout_19 = QVBoxLayout(self.widget_23)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.widget_32 = QWidget(self.widget_23)
        self.widget_32.setObjectName(u"widget_32")
        self.verticalLayout_20 = QVBoxLayout(self.widget_32)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_5 = QLabel(self.widget_32)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_20.addWidget(self.label_5)


        self.verticalLayout_19.addWidget(self.widget_32)

        self.widget_33 = QWidget(self.widget_23)
        self.widget_33.setObjectName(u"widget_33")

        self.verticalLayout_19.addWidget(self.widget_33)


        self.verticalLayout_18.addWidget(self.widget_23)

        self.widget_24 = QWidget(self.widget_25)
        self.widget_24.setObjectName(u"widget_24")

        self.verticalLayout_18.addWidget(self.widget_24)

        self.widget_26 = QWidget(self.widget_25)
        self.widget_26.setObjectName(u"widget_26")

        self.verticalLayout_18.addWidget(self.widget_26)

        self.widget_31 = QWidget(self.widget_25)
        self.widget_31.setObjectName(u"widget_31")

        self.verticalLayout_18.addWidget(self.widget_31)


        self.verticalLayout_16.addWidget(self.widget_25)

        self.stackedWidget_3.addWidget(self.page_5)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_13 = QVBoxLayout(self.page_4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.widget_19 = QWidget(self.page_4)
        self.widget_19.setObjectName(u"widget_19")
        self.verticalLayout_14 = QVBoxLayout(self.widget_19)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_4 = QLabel(self.widget_19)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_4)


        self.verticalLayout_13.addWidget(self.widget_19, 0, Qt.AlignmentFlag.AlignTop)

        self.widget_20 = QWidget(self.page_4)
        self.widget_20.setObjectName(u"widget_20")
        self.verticalLayout_15 = QVBoxLayout(self.widget_20)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.launchdriverBtn = QPushButton(self.widget_20)
        self.launchdriverBtn.setObjectName(u"launchdriverBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(181)
        sizePolicy.setHeightForWidth(self.launchdriverBtn.sizePolicy().hasHeightForWidth())
        self.launchdriverBtn.setSizePolicy(sizePolicy)
        self.launchdriverBtn.setMaximumSize(QSize(16777215, 181))
        font2 = QFont()
        font2.setPointSize(25)
        self.launchdriverBtn.setFont(font2)
        self.launchdriverBtn.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"    font-size: 25pt;\n"
"    background-color: #1a1a1a;\n"
"    color: white;\n"
"	padding-left:20px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 30px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: white;\n"
"    color: black;\n"
"	padding-left:20px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 30px;\n"
"}\n"
"\n"
"\n"
"")
        self.launchdriverBtn.setIconSize(QSize(17, 16))
        self.launchdriverBtn.setCheckable(True)

        self.verticalLayout_15.addWidget(self.launchdriverBtn)


        self.verticalLayout_13.addWidget(self.widget_20)

        self.widget_21 = QWidget(self.page_4)
        self.widget_21.setObjectName(u"widget_21")

        self.verticalLayout_13.addWidget(self.widget_21)

        self.widget_22 = QWidget(self.page_4)
        self.widget_22.setObjectName(u"widget_22")

        self.verticalLayout_13.addWidget(self.widget_22)

        self.stackedWidget_3.addWidget(self.page_4)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_11 = QVBoxLayout(self.page_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.widget_16 = QWidget(self.page_3)
        self.widget_16.setObjectName(u"widget_16")
        self.verticalLayout_12 = QVBoxLayout(self.widget_16)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_3 = QLabel(self.widget_16)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_3)


        self.verticalLayout_11.addWidget(self.widget_16, 0, Qt.AlignmentFlag.AlignTop)

        self.widget_15 = QWidget(self.page_3)
        self.widget_15.setObjectName(u"widget_15")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.calibrateBtn = QPushButton(self.widget_15)
        self.calibrateBtn.setObjectName(u"calibrateBtn")
        sizePolicy.setHeightForWidth(self.calibrateBtn.sizePolicy().hasHeightForWidth())
        self.calibrateBtn.setSizePolicy(sizePolicy)
        self.calibrateBtn.setMaximumSize(QSize(16777215, 181))
        self.calibrateBtn.setFont(font2)
        self.calibrateBtn.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"    font-size: 25pt;\n"
"    background-color: #1a1a1a;\n"
"    color: white;\n"
"	padding-left:20px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 30px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: white;\n"
"    color: black;\n"
"	padding-left:20px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 30px;\n"
"}\n"
"\n"
"\n"
"")
        self.calibrateBtn.setIconSize(QSize(17, 16))
        self.calibrateBtn.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.calibrateBtn)


        self.verticalLayout_11.addWidget(self.widget_15)

        self.widget_17 = QWidget(self.page_3)
        self.widget_17.setObjectName(u"widget_17")

        self.verticalLayout_11.addWidget(self.widget_17)

        self.widget_18 = QWidget(self.page_3)
        self.widget_18.setObjectName(u"widget_18")

        self.verticalLayout_11.addWidget(self.widget_18)

        self.stackedWidget_3.addWidget(self.page_3)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_9 = QVBoxLayout(self.page_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.widget_9 = QWidget(self.page_2)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_10 = QVBoxLayout(self.widget_9)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_2 = QLabel(self.widget_9)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_2)


        self.verticalLayout_9.addWidget(self.widget_9, 0, Qt.AlignmentFlag.AlignTop)

        self.widget_10 = QWidget(self.page_2)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.roscoreBtn = QPushButton(self.widget_10)
        self.roscoreBtn.setObjectName(u"roscoreBtn")
        sizePolicy.setHeightForWidth(self.roscoreBtn.sizePolicy().hasHeightForWidth())
        self.roscoreBtn.setSizePolicy(sizePolicy)
        self.roscoreBtn.setMaximumSize(QSize(16777215, 181))
        self.roscoreBtn.setFont(font2)
        self.roscoreBtn.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"    font-size: 25pt;\n"
"    background-color: #1a1a1a;\n"
"    color: white;\n"
"	padding-left:20px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 30px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: white;\n"
"    color: black;\n"
"	padding-left:20px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 30px;\n"
"}\n"
"\n"
"\n"
"")
        self.roscoreBtn.setIconSize(QSize(17, 16))
        self.roscoreBtn.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.roscoreBtn)


        self.verticalLayout_9.addWidget(self.widget_10)

        self.widget_11 = QWidget(self.page_2)
        self.widget_11.setObjectName(u"widget_11")

        self.verticalLayout_9.addWidget(self.widget_11)

        self.widget_12 = QWidget(self.page_2)
        self.widget_12.setObjectName(u"widget_12")

        self.verticalLayout_9.addWidget(self.widget_12)

        self.stackedWidget_3.addWidget(self.page_2)

        self.verticalLayout_3.addWidget(self.stackedWidget_3)


        self.verticalLayout_2.addWidget(self.widget_7)


        self.horizontalLayout.addWidget(self.Left_main_cointainer)

        self.right_main_cointainer = QWidget(Form)
        self.right_main_cointainer.setObjectName(u"right_main_cointainer")
        self.right_main_cointainer.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.verticalLayout = QVBoxLayout(self.right_main_cointainer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.terminal_1 = QWidget(self.right_main_cointainer)
        self.terminal_1.setObjectName(u"terminal_1")

        self.verticalLayout.addWidget(self.terminal_1)

        self.terminal_2 = QWidget(self.right_main_cointainer)
        self.terminal_2.setObjectName(u"terminal_2")

        self.verticalLayout.addWidget(self.terminal_2)

        self.terminal_3 = QWidget(self.right_main_cointainer)
        self.terminal_3.setObjectName(u"terminal_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.terminal_3.sizePolicy().hasHeightForWidth())
        self.terminal_3.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.terminal_3)


        self.horizontalLayout.addWidget(self.right_main_cointainer)


        self.retranslateUi(Form)

        self.stackedWidget_3.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"Configure IP Address", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Enter PC IP Address (default: 192.168.x.x):", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Enter Robot IP Address (default: 192.168.x.x):", None))
        self.Simulation.setText("")
        self.congigureBtn.setText(QCoreApplication.translate("Form", u"Configure", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Path plan", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"Hemisphere", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"plane", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_10.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_11.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_14.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_12.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_13.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Simulation plan", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Launch Driver", None))
        self.launchdriverBtn.setText(QCoreApplication.translate("Form", u"Launch", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Calibrate Robot", None))
        self.calibrateBtn.setText(QCoreApplication.translate("Form", u"RViz", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Start  Roscore", None))
        self.roscoreBtn.setText(QCoreApplication.translate("Form", u"Roscore", None))
    # retranslateUi