# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1214, 819)
        MainWindow.setStyleSheet(u"*{\n"
"	border:none;\n"
"	background-color:transparent;\n"
"	background:transparent;\n"
"	padding:0;\n"
"	margin:0;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"#centralwidget{\n"
"	background-color: #242424;\n"
"\n"
"}\n"
"\n"
"#leftMenuSubContainer{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"\n"
"#leftMenuSubContainer QPushButton{\n"
"	text-align: left;\n"
"	padding: 5px 10px;\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"\n"
"}\n"
"\n"
"#centerMenuSubContainer{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"#frame_4{\n"
"	\n"
"	background-color: #16191d;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"#headerContainer{\n"
"	background-color: rgb(0, 0, 0);\n"
"	\n"
"\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QWidget(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftMenuContainer.sizePolicy().hasHeightForWidth())
        self.leftMenuContainer.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.frame = QFrame(self.leftMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menuBtn = QPushButton(self.frame)
        self.menuBtn.setObjectName(u"menuBtn")
        icon = QIcon()
        icon.addFile(u":/icons/icons_1/WhatsApp Image 2025-04-11 at 10.21.21.jpeg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(30, 30))
        self.menuBtn.setCheckable(True)
        self.menuBtn.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.menuBtn)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignTop)

        self.frame_2 = QFrame(self.leftMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.connect_camera_sensorBtn = QPushButton(self.frame_2)
        self.connect_camera_sensorBtn.setObjectName(u"connect_camera_sensorBtn")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons_1/WhatsApp Image 2025-04-10 at 16.56.59.jpeg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.connect_camera_sensorBtn.setIcon(icon1)
        self.connect_camera_sensorBtn.setIconSize(QSize(30, 30))
        self.connect_camera_sensorBtn.setCheckable(True)
        self.connect_camera_sensorBtn.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.connect_camera_sensorBtn)

        self.conntct_armBtn = QPushButton(self.frame_2)
        self.conntct_armBtn.setObjectName(u"conntct_armBtn")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons_1/WhatsApp Image 2025-04-10 at 17.10.04.jpeg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.conntct_armBtn.setIcon(icon2)
        self.conntct_armBtn.setIconSize(QSize(30, 30))
        self.conntct_armBtn.setCheckable(True)
        self.conntct_armBtn.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.conntct_armBtn)

        self.calibrate_Btn = QPushButton(self.frame_2)
        self.calibrate_Btn.setObjectName(u"calibrate_Btn")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons_1/WhatsApp Image 2025-04-10 at 17.17.54.jpeg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.calibrate_Btn.setIcon(icon3)
        self.calibrate_Btn.setIconSize(QSize(30, 30))
        self.calibrate_Btn.setCheckable(True)
        self.calibrate_Btn.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.calibrate_Btn)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignmentFlag.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.leftMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 10, 0, 10)
        self.helpBtn = QPushButton(self.frame_3)
        self.helpBtn.setObjectName(u"helpBtn")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons_1/WhatsApp Image 2025-04-12 at 22.54.42.jpeg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.helpBtn.setIcon(icon4)
        self.helpBtn.setIconSize(QSize(30, 30))
        self.helpBtn.setCheckable(True)
        self.helpBtn.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.helpBtn)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout.addWidget(self.leftMenuSubContainer, 0, Qt.AlignmentFlag.AlignLeft)


        self.horizontalLayout.addWidget(self.leftMenuContainer, 0, Qt.AlignmentFlag.AlignLeft)

        self.centerMenuContainer = QWidget(self.centralwidget)
        self.centerMenuContainer.setObjectName(u"centerMenuContainer")
        sizePolicy.setHeightForWidth(self.centerMenuContainer.sizePolicy().hasHeightForWidth())
        self.centerMenuContainer.setSizePolicy(sizePolicy)
        self.centerMenuContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_6 = QVBoxLayout(self.centerMenuContainer)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.centerMenuSubContainer = QWidget(self.centerMenuContainer)
        self.centerMenuSubContainer.setObjectName(u"centerMenuSubContainer")
        self.centerMenuSubContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_7 = QVBoxLayout(self.centerMenuSubContainer)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.centerMenuSubContainer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons_1/WhatsApp Image 2025-04-12 at 22.57.37.jpeg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon5)
        self.pushButton.setIconSize(QSize(20, 20))
        self.pushButton.setCheckable(True)
        self.pushButton.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.pushButton, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_7.addWidget(self.frame_4, 0, Qt.AlignmentFlag.AlignTop)

        self.stackedWidget = QStackedWidget(self.centerMenuSubContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.verticalLayout_8 = QVBoxLayout(self.page_7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_2 = QLabel(self.page_7)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_2)

        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.stackedWidget.addWidget(self.page_8)

        self.verticalLayout_7.addWidget(self.stackedWidget)


        self.verticalLayout_6.addWidget(self.centerMenuSubContainer, 0, Qt.AlignmentFlag.AlignLeft)


        self.horizontalLayout.addWidget(self.centerMenuContainer, 0, Qt.AlignmentFlag.AlignLeft)

        self.MainBodyCointainer = QWidget(self.centralwidget)
        self.MainBodyCointainer.setObjectName(u"MainBodyCointainer")
        sizePolicy.setHeightForWidth(self.MainBodyCointainer.sizePolicy().hasHeightForWidth())
        self.MainBodyCointainer.setSizePolicy(sizePolicy)
        self.MainBodyCointainer.setMinimumSize(QSize(800, 0))
        self.MainBodyCointainer.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.MainBodyCointainer)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.MainBodyCointainer)
        self.headerContainer.setObjectName(u"headerContainer")
        self.headerContainer.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.horizontalLayout_3 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.headerContainer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_3.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.headerContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")

        self.horizontalLayout_3.addWidget(self.frame_7)

        self.frame_5 = QFrame(self.headerContainer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 6, 0)
        self.minimizeBtn = QPushButton(self.frame_5)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons_1/WhatsApp Image 2025-04-13 at 15.35.49.jpeg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeBtn.setIcon(icon6)
        self.minimizeBtn.setCheckable(True)
        self.minimizeBtn.setAutoExclusive(True)

        self.horizontalLayout_6.addWidget(self.minimizeBtn)

        self.restoreBtn = QPushButton(self.frame_5)
        self.restoreBtn.setObjectName(u"restoreBtn")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons_1/WhatsApp Image 2025-04-13 at 15.34.58.jpeg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.restoreBtn.setIcon(icon7)
        self.restoreBtn.setCheckable(True)
        self.restoreBtn.setAutoExclusive(True)

        self.horizontalLayout_6.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.frame_5)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setIcon(icon5)
        self.closeBtn.setCheckable(True)
        self.closeBtn.setAutoExclusive(True)

        self.horizontalLayout_6.addWidget(self.closeBtn)


        self.horizontalLayout_3.addWidget(self.frame_5, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_9.addWidget(self.headerContainer, 0, Qt.AlignmentFlag.AlignTop)

        self.mainBodycontent = QWidget(self.MainBodyCointainer)
        self.mainBodycontent.setObjectName(u"mainBodycontent")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainBodycontent.sizePolicy().hasHeightForWidth())
        self.mainBodycontent.setSizePolicy(sizePolicy1)

        
        self.horizontalLayout_4 = QHBoxLayout(self.mainBodycontent)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.mainContentsContainer = QWidget(self.mainBodycontent)
        self.mainContentsContainer.setObjectName(u"mainContentsContainer")
        self.verticalLayout_10 = QVBoxLayout(self.mainContentsContainer)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_2 = QStackedWidget(self.mainContentsContainer)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_13 = QVBoxLayout(self.page_3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_5 = QLabel(self.page_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_5)

        self.stackedWidget_2.addWidget(self.page_3)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_11 = QVBoxLayout(self.page)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_3)

        self.stackedWidget_2.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_12 = QVBoxLayout(self.page_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_4)

        self.stackedWidget_2.addWidget(self.page_2)

        self.verticalLayout_10.addWidget(self.stackedWidget_2)


        self.horizontalLayout_4.addWidget(self.mainContentsContainer)


        self.verticalLayout_9.addWidget(self.mainBodycontent)

        self.footerContainer = QWidget(self.MainBodyCointainer)
        self.footerContainer.setObjectName(u"footerContainer")
        self.footerContainer.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.horizontalLayout_7 = QHBoxLayout(self.footerContainer)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.footerContainer)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_7.addWidget(self.frame_9)

        self.sizeGrip = QFrame(self.footerContainer)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(10, 10))
        self.sizeGrip.setMaximumSize(QSize(40, 40))
        self.sizeGrip.setFrameShape(QFrame.Shape.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_7.addWidget(self.sizeGrip)


        self.verticalLayout_9.addWidget(self.footerContainer, 0, Qt.AlignmentFlag.AlignBottom)


        self.horizontalLayout.addWidget(self.MainBodyCointainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.connect_camera_sensorBtn.setToolTip(QCoreApplication.translate("MainWindow", u"connect Camera / Sensor", None))
#endif // QT_CONFIG(tooltip)
        self.connect_camera_sensorBtn.setText(QCoreApplication.translate("MainWindow", u"Connect Camera / Sensor", None))
#if QT_CONFIG(tooltip)
        self.conntct_armBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Connect Arm", None))
#endif // QT_CONFIG(tooltip)
        self.conntct_armBtn.setText(QCoreApplication.translate("MainWindow", u"Connect Arm ", None))
#if QT_CONFIG(tooltip)
        self.calibrate_Btn.setToolTip(QCoreApplication.translate("MainWindow", u"Calibrate", None))
#endif // QT_CONFIG(tooltip)
        self.calibrate_Btn.setText(QCoreApplication.translate("MainWindow", u"Calibrate", None))
#if QT_CONFIG(tooltip)
        self.helpBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Help", None))
#endif // QT_CONFIG(tooltip)
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"Result", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"More Menu", None))
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"Close Menu", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"result", None))
#if QT_CONFIG(tooltip)
        self.minimizeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize Window", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.restoreBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Restore Window", None))
#endif // QT_CONFIG(tooltip)
        self.restoreBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Window", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Calibration", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Connect camers/ sensor", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Connect Arm", None))
    # retranslateUi

