# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(780, 640)
        MainWindow.setMinimumSize(QSize(780, 640))
        self.actionLight = QAction(MainWindow)
        self.actionLight.setObjectName(u"actionLight")
        self.actionDark = QAction(MainWindow)
        self.actionDark.setObjectName(u"actionDark")
        self.actionWhats_New = QAction(MainWindow)
        self.actionWhats_New.setObjectName(u"actionWhats_New")
        self.actionKnown_Issues = QAction(MainWindow)
        self.actionKnown_Issues.setObjectName(u"actionKnown_Issues")
        self.actionUseful_Info = QAction(MainWindow)
        self.actionUseful_Info.setObjectName(u"actionUseful_Info")
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.verticalLayout_5 = QVBoxLayout(self.tab_1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.tab_1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(75, 0))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.romLineEdit = QLineEdit(self.tab_1)
        self.romLineEdit.setObjectName(u"romLineEdit")

        self.horizontalLayout_2.addWidget(self.romLineEdit)

        self.romButton = QPushButton(self.tab_1)
        self.romButton.setObjectName(u"romButton")

        self.horizontalLayout_2.addWidget(self.romButton)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.tab_1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(75, 0))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.outLineEdit = QLineEdit(self.tab_1)
        self.outLineEdit.setObjectName(u"outLineEdit")

        self.horizontalLayout_3.addWidget(self.outLineEdit)

        self.outButton = QPushButton(self.tab_1)
        self.outButton.setObjectName(u"outButton")

        self.horizontalLayout_3.addWidget(self.outButton)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.tab_1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(75, 0))

        self.horizontalLayout_4.addWidget(self.label_4)

        self.seedLineEdit = QLineEdit(self.tab_1)
        self.seedLineEdit.setObjectName(u"seedLineEdit")

        self.horizontalLayout_4.addWidget(self.seedLineEdit)

        self.seedButton = QPushButton(self.tab_1)
        self.seedButton.setObjectName(u"seedButton")

        self.horizontalLayout_4.addWidget(self.seedButton)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.tabWidget_2 = QTabWidget(self.tab_1)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_7 = QVBoxLayout(self.tab_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.tab_5)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.verticalLayout_9 = QVBoxLayout(self.groupBox)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.chestsCheck = QCheckBox(self.groupBox)
        self.chestsCheck.setObjectName(u"chestsCheck")
        self.chestsCheck.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_5.addWidget(self.chestsCheck)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.giftsCheck = QCheckBox(self.groupBox)
        self.giftsCheck.setObjectName(u"giftsCheck")
        self.giftsCheck.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_5.addWidget(self.giftsCheck)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.tradeCheck = QCheckBox(self.groupBox)
        self.tradeCheck.setObjectName(u"tradeCheck")
        self.tradeCheck.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_5.addWidget(self.tradeCheck)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_12)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.leavesCheck = QCheckBox(self.groupBox)
        self.leavesCheck.setObjectName(u"leavesCheck")
        self.leavesCheck.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_6.addWidget(self.leavesCheck)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.heartsCheck = QCheckBox(self.groupBox)
        self.heartsCheck.setObjectName(u"heartsCheck")
        self.heartsCheck.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_6.addWidget(self.heartsCheck)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.shellsCheck = QCheckBox(self.groupBox)
        self.shellsCheck.setObjectName(u"shellsCheck")
        self.shellsCheck.setMinimumSize(QSize(150, 0))
        font = QFont()
        font.setStrikeOut(True)
        self.shellsCheck.setFont(font)
        self.shellsCheck.setStyleSheet(u"color: rgb(80, 80, 80);")
        self.shellsCheck.setCheckable(False)

        self.horizontalLayout_6.addWidget(self.shellsCheck)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_13)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.miscCheck = QCheckBox(self.groupBox)
        self.miscCheck.setObjectName(u"miscCheck")
        self.miscCheck.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_7.addWidget(self.miscCheck)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)

        self.mansionComboBox = QComboBox(self.groupBox)
        self.mansionComboBox.addItem("")
        self.mansionComboBox.addItem("")
        self.mansionComboBox.addItem("")
        self.mansionComboBox.addItem("")
        self.mansionComboBox.addItem("")
        self.mansionComboBox.addItem("")
        self.mansionComboBox.setObjectName(u"mansionComboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mansionComboBox.sizePolicy().hasHeightForWidth())
        self.mansionComboBox.setSizePolicy(sizePolicy)
        self.mansionComboBox.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_7.addWidget(self.mansionComboBox)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)

        self.shopCheck = QCheckBox(self.groupBox)
        self.shopCheck.setObjectName(u"shopCheck")
        self.shopCheck.setMinimumSize(QSize(150, 0))
        self.shopCheck.setFont(font)
        self.shopCheck.setStyleSheet(u"color: rgb(80, 80, 80);")
        self.shopCheck.setCheckable(False)

        self.horizontalLayout_7.addWidget(self.shopCheck)


        self.verticalLayout_8.addLayout(self.horizontalLayout_7)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tab_5)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.rupCheck = QCheckBox(self.groupBox_2)
        self.rupCheck.setObjectName(u"rupCheck")
        self.rupCheck.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_10.addWidget(self.rupCheck)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_8)

        self.bossCheck = QCheckBox(self.groupBox_2)
        self.bossCheck.setObjectName(u"bossCheck")
        self.bossCheck.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_10.addWidget(self.bossCheck)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_9)

        self.instrumentCheck = QCheckBox(self.groupBox_2)
        self.instrumentCheck.setObjectName(u"instrumentCheck")
        self.instrumentCheck.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_10.addWidget(self.instrumentCheck)


        self.verticalLayout_10.addLayout(self.horizontalLayout_10)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_9)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.itemsComboBox = QComboBox(self.groupBox_2)
        self.itemsComboBox.addItem("")
        self.itemsComboBox.addItem("")
        self.itemsComboBox.addItem("")
        self.itemsComboBox.setObjectName(u"itemsComboBox")
        self.itemsComboBox.setEnabled(False)
        sizePolicy.setHeightForWidth(self.itemsComboBox.sizePolicy().hasHeightForWidth())
        self.itemsComboBox.setSizePolicy(sizePolicy)
        self.itemsComboBox.setMinimumSize(QSize(150, 0))
        self.itemsComboBox.setFont(font)

        self.horizontalLayout_11.addWidget(self.itemsComboBox)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_10)

        self.owlsComboBox = QComboBox(self.groupBox_2)
        self.owlsComboBox.addItem("")
        self.owlsComboBox.addItem("")
        self.owlsComboBox.addItem("")
        self.owlsComboBox.addItem("")
        self.owlsComboBox.setObjectName(u"owlsComboBox")
        sizePolicy.setHeightForWidth(self.owlsComboBox.sizePolicy().hasHeightForWidth())
        self.owlsComboBox.setSizePolicy(sizePolicy)
        self.owlsComboBox.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_11.addWidget(self.owlsComboBox)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_11)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_11.addWidget(self.label_5)


        self.verticalLayout_10.addLayout(self.horizontalLayout_11)

        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_23)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")

        self.verticalLayout_10.addLayout(self.horizontalLayout_30)


        self.verticalLayout_11.addLayout(self.verticalLayout_10)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.groupBox_3 = QGroupBox(self.tab_5)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy1)
        self.groupBox_3.setMinimumSize(QSize(300, 0))
        self.groupBox_3.setAlignment(Qt.AlignCenter)
        self.verticalLayout_34 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.dampeCheck = QCheckBox(self.groupBox_3)
        self.dampeCheck.setObjectName(u"dampeCheck")

        self.horizontalLayout_9.addWidget(self.dampeCheck)

        self.rapidsCheck = QCheckBox(self.groupBox_3)
        self.rapidsCheck.setObjectName(u"rapidsCheck")

        self.horizontalLayout_9.addWidget(self.rapidsCheck)


        self.verticalLayout_33.addLayout(self.horizontalLayout_9)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_33.addItem(self.verticalSpacer_10)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.fishingCheck = QCheckBox(self.groupBox_3)
        self.fishingCheck.setObjectName(u"fishingCheck")

        self.horizontalLayout_23.addWidget(self.fishingCheck)

        self.trendyCheck = QCheckBox(self.groupBox_3)
        self.trendyCheck.setObjectName(u"trendyCheck")
        self.trendyCheck.setFont(font)
        self.trendyCheck.setStyleSheet(u"color: rgb(80, 80, 80);")

        self.horizontalLayout_23.addWidget(self.trendyCheck)


        self.verticalLayout_33.addLayout(self.horizontalLayout_23)

        self.verticalSpacer_24 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_33.addItem(self.verticalSpacer_24)


        self.verticalLayout_34.addLayout(self.verticalLayout_33)


        self.horizontalLayout_8.addWidget(self.groupBox_3)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_12)

        self.groupBox_12 = QGroupBox(self.tab_5)
        self.groupBox_12.setObjectName(u"groupBox_12")
        sizePolicy1.setHeightForWidth(self.groupBox_12.sizePolicy().hasHeightForWidth())
        self.groupBox_12.setSizePolicy(sizePolicy1)
        self.groupBox_12.setMinimumSize(QSize(300, 0))
        self.groupBox_12.setAlignment(Qt.AlignCenter)
        self.verticalLayout_36 = QVBoxLayout(self.groupBox_12)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.spoilerCheck = QCheckBox(self.groupBox_12)
        self.spoilerCheck.setObjectName(u"spoilerCheck")

        self.verticalLayout_35.addWidget(self.spoilerCheck)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_35.addItem(self.verticalSpacer_11)

        self.platformComboBox = QComboBox(self.groupBox_12)
        self.platformComboBox.addItem("")
        self.platformComboBox.addItem("")
        self.platformComboBox.setObjectName(u"platformComboBox")

        self.verticalLayout_35.addWidget(self.platformComboBox)

        self.verticalSpacer_25 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_35.addItem(self.verticalSpacer_25)


        self.verticalLayout_36.addLayout(self.verticalLayout_35)


        self.horizontalLayout_8.addWidget(self.groupBox_12)

        self.horizontalLayout_8.setStretch(0, 3)
        self.horizontalLayout_8.setStretch(1, 1)
        self.horizontalLayout_8.setStretch(2, 3)

        self.verticalLayout.addLayout(self.horizontalLayout_8)


        self.verticalLayout_7.addLayout(self.verticalLayout)

        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.verticalLayout_13 = QVBoxLayout(self.tab_6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.groupBox_4 = QGroupBox(self.tab_6)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setAlignment(Qt.AlignCenter)
        self.verticalLayout_38 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_37 = QVBoxLayout()
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.enemyCheck = QCheckBox(self.groupBox_4)
        self.enemyCheck.setObjectName(u"enemyCheck")
        self.enemyCheck.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_12.addWidget(self.enemyCheck)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_13)

        self.enemySizesCheck = QCheckBox(self.groupBox_4)
        self.enemySizesCheck.setObjectName(u"enemySizesCheck")
        self.enemySizesCheck.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_12.addWidget(self.enemySizesCheck)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_14)

        self.chestsComboBox = QComboBox(self.groupBox_4)
        self.chestsComboBox.addItem("")
        self.chestsComboBox.addItem("")
        self.chestsComboBox.addItem("")
        self.chestsComboBox.setObjectName(u"chestsComboBox")
        self.chestsComboBox.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_12.addWidget(self.chestsComboBox)


        self.verticalLayout_37.addLayout(self.horizontalLayout_12)


        self.verticalLayout_38.addLayout(self.verticalLayout_37)


        self.verticalLayout_12.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.tab_6)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setAlignment(Qt.AlignCenter)
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.kanaletCheck = QCheckBox(self.groupBox_5)
        self.kanaletCheck.setObjectName(u"kanaletCheck")
        self.kanaletCheck.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_14.addWidget(self.kanaletCheck)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_15)

        self.mabeCheck = QCheckBox(self.groupBox_5)
        self.mabeCheck.setObjectName(u"mabeCheck")
        self.mabeCheck.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_14.addWidget(self.mabeCheck)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_16)

        self.mazeCheck = QCheckBox(self.groupBox_5)
        self.mazeCheck.setObjectName(u"mazeCheck")
        self.mazeCheck.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_14.addWidget(self.mazeCheck)


        self.verticalLayout_14.addLayout(self.horizontalLayout_14)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.bridgeCheck = QCheckBox(self.groupBox_5)
        self.bridgeCheck.setObjectName(u"bridgeCheck")
        self.bridgeCheck.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_15.addWidget(self.bridgeCheck)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_17)

        self.classicD2Check = QCheckBox(self.groupBox_5)
        self.classicD2Check.setObjectName(u"classicD2Check")
        self.classicD2Check.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_15.addWidget(self.classicD2Check)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_18)

        self.dungeonsCheck = QCheckBox(self.groupBox_5)
        self.dungeonsCheck.setObjectName(u"dungeonsCheck")
        self.dungeonsCheck.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_15.addWidget(self.dungeonsCheck)


        self.verticalLayout_14.addLayout(self.horizontalLayout_15)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.consumableCheck = QCheckBox(self.groupBox_5)
        self.consumableCheck.setObjectName(u"consumableCheck")
        self.consumableCheck.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_16.addWidget(self.consumableCheck)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_19)


        self.verticalLayout_14.addLayout(self.horizontalLayout_16)


        self.verticalLayout_15.addLayout(self.verticalLayout_14)


        self.verticalLayout_12.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.tab_6)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setAlignment(Qt.AlignCenter)
        self.verticalLayout_17 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.petsCheck = QCheckBox(self.groupBox_6)
        self.petsCheck.setObjectName(u"petsCheck")
        self.petsCheck.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_17.addWidget(self.petsCheck)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_20)

        self.fastFishingCheck = QCheckBox(self.groupBox_6)
        self.fastFishingCheck.setObjectName(u"fastFishingCheck")
        self.fastFishingCheck.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_17.addWidget(self.fastFishingCheck)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_21)

        self.shuffledBombsCheck = QCheckBox(self.groupBox_6)
        self.shuffledBombsCheck.setObjectName(u"shuffledBombsCheck")
        self.shuffledBombsCheck.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_17.addWidget(self.shuffledBombsCheck)


        self.verticalLayout_16.addLayout(self.horizontalLayout_17)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_16)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.bookCheck = QCheckBox(self.groupBox_6)
        self.bookCheck.setObjectName(u"bookCheck")
        self.bookCheck.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_18.addWidget(self.bookCheck)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_22)

        self.stalfosCheck = QCheckBox(self.groupBox_6)
        self.stalfosCheck.setObjectName(u"stalfosCheck")
        self.stalfosCheck.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_18.addWidget(self.stalfosCheck)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_23)

        self.shuffledPowderCheck = QCheckBox(self.groupBox_6)
        self.shuffledPowderCheck.setObjectName(u"shuffledPowderCheck")
        self.shuffledPowderCheck.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_18.addWidget(self.shuffledPowderCheck)


        self.verticalLayout_16.addLayout(self.horizontalLayout_18)

        self.verticalSpacer_30 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_30)


        self.verticalLayout_17.addLayout(self.verticalLayout_16)


        self.verticalLayout_12.addWidget(self.groupBox_6)

        self.verticalLayout_12.setStretch(0, 1)
        self.verticalLayout_12.setStretch(1, 3)
        self.verticalLayout_12.setStretch(2, 2)

        self.verticalLayout_13.addLayout(self.verticalLayout_12)

        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.verticalLayout_19 = QVBoxLayout(self.tab_7)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.groupBox_7 = QGroupBox(self.tab_7)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setAlignment(Qt.AlignCenter)
        self.verticalLayout_21 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.niceBombsCheck = QCheckBox(self.groupBox_7)
        self.niceBombsCheck.setObjectName(u"niceBombsCheck")
        self.niceBombsCheck.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_19.addWidget(self.niceBombsCheck)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_24)

        self.niceRodCheck = QCheckBox(self.groupBox_7)
        self.niceRodCheck.setObjectName(u"niceRodCheck")
        self.niceRodCheck.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_19.addWidget(self.niceRodCheck)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_25)

        self.niceSwordCheck = QCheckBox(self.groupBox_7)
        self.niceSwordCheck.setObjectName(u"niceSwordCheck")
        self.niceSwordCheck.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_19.addWidget(self.niceSwordCheck)


        self.verticalLayout_20.addLayout(self.horizontalLayout_19)


        self.verticalLayout_21.addLayout(self.verticalLayout_20)


        self.verticalLayout_18.addWidget(self.groupBox_7)

        self.groupBox_8 = QGroupBox(self.tab_7)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setAlignment(Qt.AlignCenter)
        self.verticalLayout_23 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.bossAnimCheck = QCheckBox(self.groupBox_8)
        self.bossAnimCheck.setObjectName(u"bossAnimCheck")
        self.bossAnimCheck.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_20.addWidget(self.bossAnimCheck)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_26)

        self.chestAnimCheck = QCheckBox(self.groupBox_8)
        self.chestAnimCheck.setObjectName(u"chestAnimCheck")
        self.chestAnimCheck.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_20.addWidget(self.chestAnimCheck)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_27)

        self.keyAnimCheck = QCheckBox(self.groupBox_8)
        self.keyAnimCheck.setObjectName(u"keyAnimCheck")
        self.keyAnimCheck.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_20.addWidget(self.keyAnimCheck)


        self.verticalLayout_22.addLayout(self.horizontalLayout_20)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_2)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.songAnimCheck = QCheckBox(self.groupBox_8)
        self.songAnimCheck.setObjectName(u"songAnimCheck")
        self.songAnimCheck.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_21.addWidget(self.songAnimCheck)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_28)

        self.pickupAnimCheck = QCheckBox(self.groupBox_8)
        self.pickupAnimCheck.setObjectName(u"pickupAnimCheck")
        self.pickupAnimCheck.setMinimumSize(QSize(150, 0))
        self.pickupAnimCheck.setFont(font)
        self.pickupAnimCheck.setStyleSheet(u"color: rgb(80, 80, 80);")
        self.pickupAnimCheck.setCheckable(False)

        self.horizontalLayout_21.addWidget(self.pickupAnimCheck)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_29)

        self.creditsAnimCheck = QCheckBox(self.groupBox_8)
        self.creditsAnimCheck.setObjectName(u"creditsAnimCheck")
        self.creditsAnimCheck.setMinimumSize(QSize(150, 0))
        self.creditsAnimCheck.setFont(font)
        self.creditsAnimCheck.setStyleSheet(u"color: rgb(80, 80, 80);")
        self.creditsAnimCheck.setCheckable(False)

        self.horizontalLayout_21.addWidget(self.creditsAnimCheck)


        self.verticalLayout_22.addLayout(self.horizontalLayout_21)

        self.verticalSpacer_26 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_26)


        self.verticalLayout_23.addLayout(self.verticalLayout_22)


        self.verticalLayout_18.addWidget(self.groupBox_8)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.groupBox_9 = QGroupBox(self.tab_7)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setAlignment(Qt.AlignCenter)
        self.verticalLayout_28 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.poolComboBox = QComboBox(self.groupBox_9)
        self.poolComboBox.addItem("")
        self.poolComboBox.addItem("")
        self.poolComboBox.addItem("")
        self.poolComboBox.setObjectName(u"poolComboBox")
        self.poolComboBox.setEnabled(False)
        self.poolComboBox.setFont(font)
        self.poolComboBox.setStyleSheet(u"color: rgb(80, 80, 80);")

        self.verticalLayout_27.addWidget(self.poolComboBox)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_17)

        self.trapsComboBox = QComboBox(self.groupBox_9)
        self.trapsComboBox.addItem("")
        self.trapsComboBox.addItem("")
        self.trapsComboBox.addItem("")
        self.trapsComboBox.addItem("")
        self.trapsComboBox.setObjectName(u"trapsComboBox")

        self.verticalLayout_27.addWidget(self.trapsComboBox)

        self.verticalSpacer_27 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_27)


        self.verticalLayout_28.addLayout(self.verticalLayout_27)


        self.verticalLayout_24.addWidget(self.groupBox_9)


        self.horizontalLayout_22.addLayout(self.verticalLayout_24)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.groupBox_10 = QGroupBox(self.tab_7)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setAlignment(Qt.AlignCenter)
        self.verticalLayout_30 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.fastStealingCheck = QCheckBox(self.groupBox_10)
        self.fastStealingCheck.setObjectName(u"fastStealingCheck")

        self.verticalLayout_29.addWidget(self.fastStealingCheck)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_29.addItem(self.verticalSpacer_18)

        self.stealingComboBox = QComboBox(self.groupBox_10)
        self.stealingComboBox.addItem("")
        self.stealingComboBox.addItem("")
        self.stealingComboBox.addItem("")
        self.stealingComboBox.setObjectName(u"stealingComboBox")

        self.verticalLayout_29.addWidget(self.stealingComboBox)

        self.verticalSpacer_28 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_29.addItem(self.verticalSpacer_28)


        self.verticalLayout_30.addLayout(self.verticalLayout_29)


        self.verticalLayout_25.addWidget(self.groupBox_10)


        self.horizontalLayout_22.addLayout(self.verticalLayout_25)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.groupBox_11 = QGroupBox(self.tab_7)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setAlignment(Qt.AlignCenter)
        self.verticalLayout_32 = QVBoxLayout(self.groupBox_11)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.ohkoCheck = QCheckBox(self.groupBox_11)
        self.ohkoCheck.setObjectName(u"ohkoCheck")

        self.verticalLayout_31.addWidget(self.ohkoCheck)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_31.addItem(self.verticalSpacer_19)

        self.endingCheck = QCheckBox(self.groupBox_11)
        self.endingCheck.setObjectName(u"endingCheck")

        self.verticalLayout_31.addWidget(self.endingCheck)

        self.verticalSpacer_29 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_31.addItem(self.verticalSpacer_29)


        self.verticalLayout_32.addLayout(self.verticalLayout_31)


        self.verticalLayout_26.addWidget(self.groupBox_11)


        self.horizontalLayout_22.addLayout(self.verticalLayout_26)


        self.verticalLayout_18.addLayout(self.horizontalLayout_22)

        self.verticalLayout_18.setStretch(0, 1)
        self.verticalLayout_18.setStretch(1, 2)
        self.verticalLayout_18.setStretch(2, 2)

        self.verticalLayout_19.addLayout(self.verticalLayout_18)

        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_49 = QVBoxLayout(self.tab)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_48 = QVBoxLayout()
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.groupBox_13 = QGroupBox(self.tab)
        self.groupBox_13.setObjectName(u"groupBox_13")
        sizePolicy1.setHeightForWidth(self.groupBox_13.sizePolicy().hasHeightForWidth())
        self.groupBox_13.setSizePolicy(sizePolicy1)
        self.groupBox_13.setMinimumSize(QSize(300, 0))
        self.groupBox_13.setAlignment(Qt.AlignCenter)
        self.verticalLayout_51 = QVBoxLayout(self.groupBox_13)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_50 = QVBoxLayout()
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.blurCheck = QCheckBox(self.groupBox_13)
        self.blurCheck.setObjectName(u"blurCheck")

        self.verticalLayout_50.addWidget(self.blurCheck)

        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_50.addItem(self.verticalSpacer_20)


        self.verticalLayout_51.addLayout(self.verticalLayout_50)


        self.horizontalLayout_29.addWidget(self.groupBox_13)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_30)

        self.groupBox_14 = QGroupBox(self.tab)
        self.groupBox_14.setObjectName(u"groupBox_14")
        sizePolicy1.setHeightForWidth(self.groupBox_14.sizePolicy().hasHeightForWidth())
        self.groupBox_14.setSizePolicy(sizePolicy1)
        self.groupBox_14.setMinimumSize(QSize(300, 0))
        self.groupBox_14.setAlignment(Qt.AlignCenter)
        self.verticalLayout_53 = QVBoxLayout(self.groupBox_14)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_52 = QVBoxLayout()
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.beepCheck = QCheckBox(self.groupBox_14)
        self.beepCheck.setObjectName(u"beepCheck")
        font1 = QFont()
        font1.setStrikeOut(False)
        self.beepCheck.setFont(font1)

        self.verticalLayout_52.addWidget(self.beepCheck)

        self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_52.addItem(self.verticalSpacer_21)

        self.musicCheck = QCheckBox(self.groupBox_14)
        self.musicCheck.setObjectName(u"musicCheck")

        self.verticalLayout_52.addWidget(self.musicCheck)

        self.verticalSpacer_22 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_52.addItem(self.verticalSpacer_22)

        self.soundCheck = QCheckBox(self.groupBox_14)
        self.soundCheck.setObjectName(u"soundCheck")
        self.soundCheck.setFont(font)
        self.soundCheck.setStyleSheet(u"color: rgb(80, 80, 80);")
        self.soundCheck.setCheckable(False)

        self.verticalLayout_52.addWidget(self.soundCheck)


        self.verticalLayout_53.addLayout(self.verticalLayout_52)


        self.horizontalLayout_29.addWidget(self.groupBox_14)

        self.horizontalLayout_29.setStretch(0, 3)
        self.horizontalLayout_29.setStretch(1, 1)
        self.horizontalLayout_29.setStretch(2, 3)

        self.verticalLayout_48.addLayout(self.horizontalLayout_29)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_48.addItem(self.verticalSpacer_8)

        self.verticalLayout_48.setStretch(0, 1)
        self.verticalLayout_48.setStretch(1, 2)

        self.verticalLayout_49.addLayout(self.verticalLayout_48)

        self.tabWidget_2.addTab(self.tab, "")

        self.verticalLayout_6.addWidget(self.tabWidget_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_6)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_24 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(12)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout_39 = QVBoxLayout()
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 31))
        font2 = QFont()
        font2.setPointSize(12)
        self.label_6.setFont(font2)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_39.addWidget(self.label_6)

        self.randomItemsList = QListWidget(self.tab_2)
        self.randomItemsList.setObjectName(u"randomItemsList")
        self.randomItemsList.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout_39.addWidget(self.randomItemsList)


        self.horizontalLayout_13.addLayout(self.verticalLayout_39)

        self.verticalLayout_40 = QVBoxLayout()
        self.verticalLayout_40.setSpacing(12)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 48, -1, 21)
        self.instrumentsComboBox = QComboBox(self.tab_2)
        self.instrumentsComboBox.addItem("")
        self.instrumentsComboBox.addItem("")
        self.instrumentsComboBox.addItem("")
        self.instrumentsComboBox.addItem("")
        self.instrumentsComboBox.addItem("")
        self.instrumentsComboBox.addItem("")
        self.instrumentsComboBox.addItem("")
        self.instrumentsComboBox.addItem("")
        self.instrumentsComboBox.addItem("")
        self.instrumentsComboBox.setObjectName(u"instrumentsComboBox")

        self.verticalLayout_40.addWidget(self.instrumentsComboBox)

        self.dungeonItemsComboBox = QComboBox(self.tab_2)
        self.dungeonItemsComboBox.addItem("")
        self.dungeonItemsComboBox.addItem("")
        self.dungeonItemsComboBox.addItem("")
        self.dungeonItemsComboBox.addItem("")
        self.dungeonItemsComboBox.setObjectName(u"dungeonItemsComboBox")

        self.verticalLayout_40.addWidget(self.dungeonItemsComboBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_40.addItem(self.verticalSpacer)

        self.itemsExcludeButton = QPushButton(self.tab_2)
        self.itemsExcludeButton.setObjectName(u"itemsExcludeButton")
        self.itemsExcludeButton.setMinimumSize(QSize(0, 81))
        font3 = QFont()
        font3.setPointSize(11)
        self.itemsExcludeButton.setFont(font3)

        self.verticalLayout_40.addWidget(self.itemsExcludeButton)

        self.itemsIncludeButton = QPushButton(self.tab_2)
        self.itemsIncludeButton.setObjectName(u"itemsIncludeButton")
        self.itemsIncludeButton.setMinimumSize(QSize(0, 81))
        self.itemsIncludeButton.setFont(font3)

        self.verticalLayout_40.addWidget(self.itemsIncludeButton)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_40.addItem(self.verticalSpacer_3)

        self.rupeesSpinBox = QSpinBox(self.tab_2)
        self.rupeesSpinBox.setObjectName(u"rupeesSpinBox")
        self.rupeesSpinBox.setMinimumSize(QSize(0, 41))
        font4 = QFont()
        font4.setPointSize(10)
        self.rupeesSpinBox.setFont(font4)
        self.rupeesSpinBox.setMaximum(9999)

        self.verticalLayout_40.addWidget(self.rupeesSpinBox)


        self.horizontalLayout_13.addLayout(self.verticalLayout_40)

        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, -1, -1, -1)
        self.label_7 = QLabel(self.tab_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 31))
        self.label_7.setFont(font2)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_41.addWidget(self.label_7)

        self.startingItemsList = QListWidget(self.tab_2)
        self.startingItemsList.setObjectName(u"startingItemsList")
        self.startingItemsList.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout_41.addWidget(self.startingItemsList)


        self.horizontalLayout_13.addLayout(self.verticalLayout_41)

        self.horizontalLayout_13.setStretch(0, 3)
        self.horizontalLayout_13.setStretch(1, 2)
        self.horizontalLayout_13.setStretch(2, 3)

        self.horizontalLayout_24.addLayout(self.horizontalLayout_13)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.horizontalLayout_26 = QHBoxLayout(self.tab_3)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setSpacing(12)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.verticalLayout_42 = QVBoxLayout()
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.label_8 = QLabel(self.tab_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 31))
        self.label_8.setFont(font2)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_42.addWidget(self.label_8)

        self.includedLocationsList = QListWidget(self.tab_3)
        self.includedLocationsList.setObjectName(u"includedLocationsList")
        self.includedLocationsList.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout_42.addWidget(self.includedLocationsList)


        self.horizontalLayout_25.addLayout(self.verticalLayout_42)

        self.verticalLayout_43 = QVBoxLayout()
        self.verticalLayout_43.setSpacing(12)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(-1, 48, -1, 6)
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_43.addItem(self.verticalSpacer_4)

        self.locationsExcludeButton = QPushButton(self.tab_3)
        self.locationsExcludeButton.setObjectName(u"locationsExcludeButton")
        self.locationsExcludeButton.setMinimumSize(QSize(0, 81))
        self.locationsExcludeButton.setFont(font3)

        self.verticalLayout_43.addWidget(self.locationsExcludeButton)

        self.locationsIncludeButton = QPushButton(self.tab_3)
        self.locationsIncludeButton.setObjectName(u"locationsIncludeButton")
        self.locationsIncludeButton.setMinimumSize(QSize(0, 81))
        self.locationsIncludeButton.setFont(font3)

        self.verticalLayout_43.addWidget(self.locationsIncludeButton)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_43.addItem(self.verticalSpacer_5)

        self.verticalLayout_43.setStretch(1, 1)
        self.verticalLayout_43.setStretch(2, 1)

        self.horizontalLayout_25.addLayout(self.verticalLayout_43)

        self.verticalLayout_44 = QVBoxLayout()
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.label_9 = QLabel(self.tab_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 31))
        self.label_9.setFont(font2)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_44.addWidget(self.label_9)

        self.excludedLocationsList = QListWidget(self.tab_3)
        self.excludedLocationsList.setObjectName(u"excludedLocationsList")
        self.excludedLocationsList.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout_44.addWidget(self.excludedLocationsList)


        self.horizontalLayout_25.addLayout(self.verticalLayout_44)

        self.horizontalLayout_25.setStretch(0, 3)
        self.horizontalLayout_25.setStretch(1, 2)
        self.horizontalLayout_25.setStretch(2, 3)

        self.horizontalLayout_26.addLayout(self.horizontalLayout_25)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.horizontalLayout_28 = QHBoxLayout(self.tab_4)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setSpacing(12)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.verticalLayout_45 = QVBoxLayout()
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.label_10 = QLabel(self.tab_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 31))
        self.label_10.setFont(font2)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_45.addWidget(self.label_10)

        self.includedLogicList = QListWidget(self.tab_4)
        self.includedLogicList.setObjectName(u"includedLogicList")
        self.includedLogicList.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout_45.addWidget(self.includedLogicList)


        self.horizontalLayout_27.addLayout(self.verticalLayout_45)

        self.verticalLayout_46 = QVBoxLayout()
        self.verticalLayout_46.setSpacing(12)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(-1, 48, -1, 40)
        self.logicComboBox = QComboBox(self.tab_4)
        self.logicComboBox.addItem("")
        self.logicComboBox.addItem("")
        self.logicComboBox.addItem("")
        self.logicComboBox.addItem("")
        self.logicComboBox.addItem("")
        self.logicComboBox.setObjectName(u"logicComboBox")

        self.verticalLayout_46.addWidget(self.logicComboBox)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_46.addItem(self.verticalSpacer_6)

        self.logicExcludeButton = QPushButton(self.tab_4)
        self.logicExcludeButton.setObjectName(u"logicExcludeButton")
        self.logicExcludeButton.setMinimumSize(QSize(0, 81))
        self.logicExcludeButton.setFont(font3)

        self.verticalLayout_46.addWidget(self.logicExcludeButton)

        self.logicIncludeButton = QPushButton(self.tab_4)
        self.logicIncludeButton.setObjectName(u"logicIncludeButton")
        self.logicIncludeButton.setMinimumSize(QSize(0, 81))
        self.logicIncludeButton.setFont(font3)

        self.verticalLayout_46.addWidget(self.logicIncludeButton)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_46.addItem(self.verticalSpacer_7)


        self.horizontalLayout_27.addLayout(self.verticalLayout_46)

        self.verticalLayout_47 = QVBoxLayout()
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.label_11 = QLabel(self.tab_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 31))
        self.label_11.setFont(font2)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_47.addWidget(self.label_11)

        self.excludedLogicList = QListWidget(self.tab_4)
        self.excludedLogicList.setObjectName(u"excludedLogicList")
        self.excludedLogicList.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout_47.addWidget(self.excludedLogicList)


        self.horizontalLayout_27.addLayout(self.verticalLayout_47)

        self.horizontalLayout_27.setStretch(0, 3)
        self.horizontalLayout_27.setStretch(1, 2)
        self.horizontalLayout_27.setStretch(2, 3)

        self.horizontalLayout_28.addLayout(self.horizontalLayout_27)

        self.tabWidget.addTab(self.tab_4, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(4, 0, 4, 0)
        self.explanationLabel = QLabel(self.centralwidget)
        self.explanationLabel.setObjectName(u"explanationLabel")
        self.explanationLabel.setMinimumSize(QSize(0, 31))
        self.explanationLabel.setStyleSheet(u"color: rgb(80, 80, 80);")
        self.explanationLabel.setTextFormat(Qt.RichText)
        self.explanationLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_4.addWidget(self.explanationLabel)

        self.settingsLineEdit = QLineEdit(self.centralwidget)
        self.settingsLineEdit.setObjectName(u"settingsLineEdit")

        self.verticalLayout_4.addWidget(self.settingsLineEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.copyButton = QPushButton(self.centralwidget)
        self.copyButton.setObjectName(u"copyButton")

        self.horizontalLayout.addWidget(self.copyButton)

        self.pasteButton = QPushButton(self.centralwidget)
        self.pasteButton.setObjectName(u"pasteButton")

        self.horizontalLayout.addWidget(self.pasteButton)

        self.resetButton = QPushButton(self.centralwidget)
        self.resetButton.setObjectName(u"resetButton")

        self.horizontalLayout.addWidget(self.resetButton)

        self.randomizeSettingsButton = QPushButton(self.centralwidget)
        self.randomizeSettingsButton.setObjectName(u"randomizeSettingsButton")

        self.horizontalLayout.addWidget(self.randomizeSettingsButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.randomizeButton = QPushButton(self.centralwidget)
        self.randomizeButton.setObjectName(u"randomizeButton")

        self.horizontalLayout.addWidget(self.randomizeButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout_4)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 780, 22))
        self.menuTheme = QMenu(self.menuBar)
        self.menuTheme.setObjectName(u"menuTheme")
        self.menuAbout = QMenu(self.menuBar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuTheme.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())
        self.menuTheme.addAction(self.actionLight)
        self.menuTheme.addSeparator()
        self.menuTheme.addAction(self.actionDark)
        self.menuAbout.addAction(self.actionWhats_New)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionKnown_Issues)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionUseful_Info)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionHelp)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.itemsComboBox.setCurrentIndex(0)
        self.owlsComboBox.setCurrentIndex(0)
        self.platformComboBox.setCurrentIndex(0)
        self.chestsComboBox.setCurrentIndex(0)
        self.poolComboBox.setCurrentIndex(1)
        self.stealingComboBox.setCurrentIndex(2)
        self.instrumentsComboBox.setCurrentIndex(0)
        self.dungeonItemsComboBox.setCurrentIndex(0)
        self.logicComboBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionLight.setText(QCoreApplication.translate("MainWindow", u"Light", None))
        self.actionDark.setText(QCoreApplication.translate("MainWindow", u"Dark", None))
        self.actionWhats_New.setText(QCoreApplication.translate("MainWindow", u"What's New", None))
        self.actionKnown_Issues.setText(QCoreApplication.translate("MainWindow", u"Known Issues", None))
        self.actionUseful_Info.setText(QCoreApplication.translate("MainWindow", u"Useful Info", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"RomFS Path", None))
        self.romButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Output Path", None))
        self.outButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Optional Seed", None))
        self.seedButton.setText(QCoreApplication.translate("MainWindow", u"New Seed", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Main Checks", None))
        self.chestsCheck.setText(QCoreApplication.translate("MainWindow", u"Chests", None))
        self.giftsCheck.setText(QCoreApplication.translate("MainWindow", u"Free Gifts", None))
        self.tradeCheck.setText(QCoreApplication.translate("MainWindow", u"Trade Quest", None))
        self.leavesCheck.setText(QCoreApplication.translate("MainWindow", u"Golden Leaves", None))
        self.heartsCheck.setText(QCoreApplication.translate("MainWindow", u"Heart Pieces", None))
        self.shellsCheck.setText(QCoreApplication.translate("MainWindow", u"Seashells", None))
        self.miscCheck.setText(QCoreApplication.translate("MainWindow", u"Miscellaneous", None))
        self.mansionComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Seashell Mansion:  0", None))
        self.mansionComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Seashell Mansion:  5", None))
        self.mansionComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Seashell Mansion:  15", None))
        self.mansionComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Seashell Mansion:  30", None))
        self.mansionComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Seashell Mansion:  40", None))
        self.mansionComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Seashell Mansion:  50", None))

        self.shopCheck.setText(QCoreApplication.translate("MainWindow", u"Shop", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Dungeons", None))
        self.rupCheck.setText(QCoreApplication.translate("MainWindow", u"Blupsanity", None))
        self.bossCheck.setText(QCoreApplication.translate("MainWindow", u"Boss Drops", None))
        self.instrumentCheck.setText(QCoreApplication.translate("MainWindow", u"Instruments", None))
        self.itemsComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Items:  Standard", None))
        self.itemsComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Items:  Keysanity", None))
        self.itemsComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Items:  Keysanity + MCB", None))

        self.owlsComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Owl Gifts:  None", None))
        self.owlsComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Owl Gifts:  Overworld", None))
        self.owlsComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Owl Gifts:  Dungeons", None))
        self.owlsComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Owl Gifts:  All", None))

        self.label_5.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Minigames", None))
        self.dampeCheck.setText(QCoreApplication.translate("MainWindow", u"Damp\u00e9", None))
        self.rapidsCheck.setText(QCoreApplication.translate("MainWindow", u"Rapids", None))
        self.fishingCheck.setText(QCoreApplication.translate("MainWindow", u"Fishing", None))
        self.trendyCheck.setText(QCoreApplication.translate("MainWindow", u"Trendy Game", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"Output Settings", None))
        self.spoilerCheck.setText(QCoreApplication.translate("MainWindow", u"Create Spoiler Log", None))
        self.platformComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Platform:  Console", None))
        self.platformComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Platform:  Emulator", None))

        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Main Settings", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Global", None))
        self.enemyCheck.setText(QCoreApplication.translate("MainWindow", u"Randomize Enemies", None))
        self.enemySizesCheck.setText(QCoreApplication.translate("MainWindow", u"Randomize Enemy Sizes", None))
        self.chestsComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Chests:  Default", None))
        self.chestsComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Chests:  Size", None))
        self.chestsComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Chests:  Textures + Size", None))

        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Overworld", None))
        self.kanaletCheck.setText(QCoreApplication.translate("MainWindow", u"Open Kanalet", None))
        self.mabeCheck.setText(QCoreApplication.translate("MainWindow", u"Open Mabe", None))
        self.mazeCheck.setText(QCoreApplication.translate("MainWindow", u"Open Mamu", None))
        self.bridgeCheck.setText(QCoreApplication.translate("MainWindow", u"Completed Bridge", None))
        self.classicD2Check.setText(QCoreApplication.translate("MainWindow", u"Classic D2", None))
        self.dungeonsCheck.setText(QCoreApplication.translate("MainWindow", u"Shuffled Dungeons", None))
        self.consumableCheck.setText(QCoreApplication.translate("MainWindow", u"Consumable Drops", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Logic", None))
        self.petsCheck.setText(QCoreApplication.translate("MainWindow", u"Bad Pets", None))
        self.fastFishingCheck.setText(QCoreApplication.translate("MainWindow", u"Fast Fishing", None))
        self.shuffledBombsCheck.setText(QCoreApplication.translate("MainWindow", u"Shuffled Bombs", None))
        self.bookCheck.setText(QCoreApplication.translate("MainWindow", u"Free Book", None))
        self.stalfosCheck.setText(QCoreApplication.translate("MainWindow", u"Fast Stalfos", None))
        self.shuffledPowderCheck.setText(QCoreApplication.translate("MainWindow", u"Shuffled Powder", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"World Settings", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Nice Items", None))
        self.niceBombsCheck.setText(QCoreApplication.translate("MainWindow", u"Nice Bombs", None))
        self.niceRodCheck.setText(QCoreApplication.translate("MainWindow", u"Nice Magic Rod", None))
        self.niceSwordCheck.setText(QCoreApplication.translate("MainWindow", u"Nice Sword", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Speed Options", None))
        self.bossAnimCheck.setText(QCoreApplication.translate("MainWindow", u"Boss Cutscenes", None))
        self.chestAnimCheck.setText(QCoreApplication.translate("MainWindow", u"Chest Animations", None))
        self.keyAnimCheck.setText(QCoreApplication.translate("MainWindow", u"Key Animations", None))
        self.songAnimCheck.setText(QCoreApplication.translate("MainWindow", u"Song Cutscenes", None))
        self.pickupAnimCheck.setText(QCoreApplication.translate("MainWindow", u"Pickup Animations", None))
        self.creditsAnimCheck.setText(QCoreApplication.translate("MainWindow", u"Skip Credits", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Item Pool", None))
        self.poolComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Item Pool:  Plentiful", None))
        self.poolComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Item Pool:  Standard", None))
        self.poolComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Item Pool:  Reduced", None))

        self.trapsComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Traps:  None", None))
        self.trapsComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Traps:  Few", None))
        self.trapsComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Traps:  Many", None))
        self.trapsComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Traps:  Trapsanity", None))

        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Shop", None))
        self.fastStealingCheck.setText(QCoreApplication.translate("MainWindow", u"Fast Stealing", None))
        self.stealingComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Stealing:  Always", None))
        self.stealingComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Stealing:  Never", None))
        self.stealingComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Stealing:  Normal", None))

        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Other", None))
        self.ohkoCheck.setText(QCoreApplication.translate("MainWindow", u"One Hit KO Mode", None))
        self.endingCheck.setText(QCoreApplication.translate("MainWindow", u"Perfect Ending", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Gameplay Settings", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"Visuals", None))
        self.blurCheck.setText(QCoreApplication.translate("MainWindow", u"Blur Removal", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", u"Audio", None))
        self.beepCheck.setText(QCoreApplication.translate("MainWindow", u"Disable Low HP Beeps", None))
        self.musicCheck.setText(QCoreApplication.translate("MainWindow", u"Randomize Music", None))
        self.soundCheck.setText(QCoreApplication.translate("MainWindow", u"Randomize Sound Effects", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Cosmetic Settings", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"Randomizer Settings", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Randomized Items", None))
        self.instrumentsComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Starting Instruments:  0", None))
        self.instrumentsComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Starting Instruments:  1", None))
        self.instrumentsComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Starting Instruments:  2", None))
        self.instrumentsComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Starting Instruments:  3", None))
        self.instrumentsComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Starting Instruments:  4", None))
        self.instrumentsComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Starting Instruments:  5", None))
        self.instrumentsComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Starting Instruments:  6", None))
        self.instrumentsComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Starting Instruments:  7", None))
        self.instrumentsComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Starting Instruments:  8", None))

        self.dungeonItemsComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Dungeon Items:  None", None))
        self.dungeonItemsComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Dungeon Items:  Beaks", None))
        self.dungeonItemsComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Dungeon Items:  MC", None))
        self.dungeonItemsComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Dungeon Items:  MCB", None))

        self.itemsExcludeButton.setText(QCoreApplication.translate("MainWindow", u"->", None))
        self.itemsIncludeButton.setText(QCoreApplication.translate("MainWindow", u"<-", None))
        self.rupeesSpinBox.setPrefix(QCoreApplication.translate("MainWindow", u"Rupees:  ", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Starting Items", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Starting Items", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Included Checks", None))
        self.locationsExcludeButton.setText(QCoreApplication.translate("MainWindow", u"->", None))
        self.locationsIncludeButton.setText(QCoreApplication.translate("MainWindow", u"<-", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Excluded Checks", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Locations", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Included Tricks", None))
        self.logicComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Logic Preset:  Basic", None))
        self.logicComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Logic Preset:  Advanced", None))
        self.logicComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Logic Preset:  Glitched", None))
        self.logicComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Logic Preset:  Hell", None))
        self.logicComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Logic Preset:  None", None))

        self.logicExcludeButton.setText(QCoreApplication.translate("MainWindow", u"->", None))
        self.logicIncludeButton.setText(QCoreApplication.translate("MainWindow", u"<-", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Excluded Tricks", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Logic", None))
        self.explanationLabel.setText(QCoreApplication.translate("MainWindow", u"Hover over an option to see what it does", None))
        self.copyButton.setText(QCoreApplication.translate("MainWindow", u"Copy Settings", None))
        self.pasteButton.setText(QCoreApplication.translate("MainWindow", u"Paste Settings", None))
        self.resetButton.setText(QCoreApplication.translate("MainWindow", u"Reset Settings", None))
        self.randomizeSettingsButton.setText(QCoreApplication.translate("MainWindow", u"Random Settings", None))
        self.randomizeButton.setText(QCoreApplication.translate("MainWindow", u"Randomize", None))
        self.menuTheme.setTitle(QCoreApplication.translate("MainWindow", u"Theme", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

