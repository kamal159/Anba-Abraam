# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'index.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1219, 788)
        MainWindow.setMinimumSize(QtCore.QSize(1219, 788))
        MainWindow.setSizeIncrement(QtCore.QSize(1219, 788))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-1, 0, 1010, 840))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("QTabWidget{\n"
"\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton\n"
"{\n"
"    color: #fff;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 40px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: rgb(139, 139, 139)\n"
"}\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    border: 1px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #00aaff, stop: 1 #00aaff);\n"
"}\n"
"\n"
"QLineEdit {\n"
"\n"
"    color: rgb(59, 59, 89);\n"
"\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"\n"
"}\n"
"QLineEdit::hover\n"
"{\n"
"    border: 1px solid rgb(0, 170, 255);\n"
"    border-radius: 2px;\n"
"    color: rgb(0, 115, 255);\n"
"    border-radius: 6;\n"
"\n"
"\n"
"}\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_14 = QtWidgets.QWidget()
        self.tab_14.setObjectName("tab_14")
        self.lineEdit_39 = QtWidgets.QLineEdit(self.tab_14)
        self.lineEdit_39.setGeometry(QtCore.QRect(430, 410, 260, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_39.setFont(font)
        self.lineEdit_39.setStyleSheet("QLineEdit {\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"\n"
"}\n"
"QLineEdit::hover\n"
"{\n"
"    border: 1px solid rgb(0, 170, 255);\n"
"    border-radius: 2px;\n"
"    color: rgb(0, 115, 255);\n"
"    border-radius: 6;\n"
"\n"
"\n"
"}\n"
"")
        self.lineEdit_39.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_39.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_39.setObjectName("lineEdit_39")
        self.pushButton_44 = QtWidgets.QPushButton(self.tab_14)
        self.pushButton_44.setGeometry(QtCore.QRect(480, 590, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_44.setFont(font)
        self.pushButton_44.setStyleSheet("QPushButton\n"
"{\n"
"    color: #fff;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 40px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: rgb(139, 139, 139)\n"
"}\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    border: 1px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #00aaff, stop: 1 #00aaff);\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/adduser.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_44.setIcon(icon)
        self.pushButton_44.setIconSize(QtCore.QSize(24, 26))
        self.pushButton_44.setObjectName("pushButton_44")
        self.lineEdit_40 = QtWidgets.QLineEdit(self.tab_14)
        self.lineEdit_40.setGeometry(QtCore.QRect(430, 350, 260, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_40.setFont(font)
        self.lineEdit_40.setStyleSheet("")
        self.lineEdit_40.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_40.setObjectName("lineEdit_40")
        self.label_54 = QtWidgets.QLabel(self.tab_14)
        self.label_54.setGeometry(QtCore.QRect(700, 350, 160, 40))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_54.setFont(font)
        self.label_54.setStyleSheet("QLabel\n"
"{\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 14pt \"Hacen Maghreb Bd\";\n"
"\n"
"}")
        self.label_54.setAlignment(QtCore.Qt.AlignCenter)
        self.label_54.setObjectName("label_54")
        self.label_55 = QtWidgets.QLabel(self.tab_14)
        self.label_55.setGeometry(QtCore.QRect(700, 410, 160, 40))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_55.setFont(font)
        self.label_55.setStyleSheet("QLabel\n"
"{\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 14pt \"Hacen Maghreb Bd\";\n"
"\n"
"}")
        self.label_55.setAlignment(QtCore.Qt.AlignCenter)
        self.label_55.setObjectName("label_55")
        self.lineEdit_41 = QtWidgets.QLineEdit(self.tab_14)
        self.lineEdit_41.setGeometry(QtCore.QRect(430, 530, 260, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_41.setFont(font)
        self.lineEdit_41.setStyleSheet("QLineEdit {\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"\n"
"}\n"
"QLineEdit::hover\n"
"{\n"
"    border: 1px solid rgb(0, 170, 255);\n"
"    border-radius: 2px;\n"
"    color: rgb(0, 115, 255);\n"
"    border-radius: 6;\n"
"\n"
"\n"
"}\n"
"")
        self.lineEdit_41.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_41.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_41.setObjectName("lineEdit_41")
        self.label_56 = QtWidgets.QLabel(self.tab_14)
        self.label_56.setGeometry(QtCore.QRect(700, 530, 160, 40))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_56.setFont(font)
        self.label_56.setStyleSheet("QLabel\n"
"{\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 14pt \"Hacen Maghreb Bd\";\n"
"\n"
"}")
        self.label_56.setAlignment(QtCore.Qt.AlignCenter)
        self.label_56.setObjectName("label_56")
        self.label_57 = QtWidgets.QLabel(self.tab_14)
        self.label_57.setGeometry(QtCore.QRect(770, 590, 150, 35))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_57.setFont(font)
        self.label_57.setStyleSheet("QLabel\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 14pt \"Hacen Maghreb Bd\";\n"
"\n"
"}")
        self.label_57.setObjectName("label_57")
        self.pushButton_83 = QtWidgets.QPushButton(self.tab_14)
        self.pushButton_83.setGeometry(QtCore.QRect(720, 640, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_83.setFont(font)
        self.pushButton_83.setStyleSheet("QPushButton\n"
"{\n"
"    color: #fff;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 40px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: rgb(139, 139, 139)\n"
"}\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    border: 1px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #00aaff, stop: 1 #00aaff);\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ico/start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_83.setIcon(icon1)
        self.pushButton_83.setIconSize(QtCore.QSize(41, 31))
        self.pushButton_83.setObjectName("pushButton_83")
        self.label_29 = QtWidgets.QLabel(self.tab_14)
        self.label_29.setGeometry(QtCore.QRect(330, 80, 540, 150))
        font = QtGui.QFont()
        font.setFamily("Mikhak Bold")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_29.setFont(font)
        self.label_29.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_29.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_29.setStyleSheet("font: 75 25pt \"Mikhak Bold\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"image: url(:/ico/text1.png);\n"
"")
        self.label_29.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Egypt))
        self.label_29.setObjectName("label_29")
        self.label_69 = QtWidgets.QLabel(self.tab_14)
        self.label_69.setGeometry(QtCore.QRect(700, 470, 160, 40))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_69.setFont(font)
        self.label_69.setStyleSheet("QLabel\n"
"{\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 14pt \"Hacen Maghreb Bd\";\n"
"\n"
"}")
        self.label_69.setAlignment(QtCore.Qt.AlignCenter)
        self.label_69.setObjectName("label_69")
        self.lineEdit_112 = QtWidgets.QLineEdit(self.tab_14)
        self.lineEdit_112.setGeometry(QtCore.QRect(430, 470, 260, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_112.setFont(font)
        self.lineEdit_112.setStyleSheet("QLineEdit {\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"\n"
"}\n"
"QLineEdit::hover\n"
"{\n"
"    border: 1px solid rgb(0, 170, 255);\n"
"    border-radius: 2px;\n"
"    color: rgb(0, 115, 255);\n"
"    border-radius: 6;\n"
"\n"
"\n"
"}\n"
"")
        self.lineEdit_112.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_112.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_112.setObjectName("lineEdit_112")
        self.label_28 = QtWidgets.QLabel(self.tab_14)
        self.label_28.setGeometry(QtCore.QRect(10, 630, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Museo Sans 700")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.label_5 = QtWidgets.QLabel(self.tab_14)
        self.label_5.setGeometry(QtCore.QRect(30, 230, 210, 280))
        self.label_5.setStyleSheet("image: url(:/ico/pic.png);\n"
"")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.lcdNumber = QtWidgets.QLCDNumber(self.tab_14)
        self.lcdNumber.setGeometry(QtCore.QRect(720, 590, 60, 35))
        self.lcdNumber.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 14pt \"Hacen Maghreb Bd\";\n"
"\n"
"    border-radius: 6;\n"
"")
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lcdNumber.setLineWidth(1)
        self.lcdNumber.setMidLineWidth(0)
        self.lcdNumber.setDigitCount(1)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_6 = QtWidgets.QLabel(self.tab_14)
        self.label_6.setGeometry(QtCore.QRect(-1450, -470, 2800, 1460))
        self.label_6.setStyleSheet("image: url(:/ico/bg.png);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_6.raise_()
        self.label_54.raise_()
        self.lineEdit_39.raise_()
        self.pushButton_44.raise_()
        self.lineEdit_40.raise_()
        self.label_55.raise_()
        self.lineEdit_41.raise_()
        self.label_56.raise_()
        self.pushButton_83.raise_()
        self.label_29.raise_()
        self.label_69.raise_()
        self.lineEdit_112.raise_()
        self.label_28.raise_()
        self.label_5.raise_()
        self.label_57.raise_()
        self.lcdNumber.raise_()
        self.tabWidget.addTab(self.tab_14, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_19 = QtWidgets.QLabel(self.tab)
        self.label_19.setGeometry(QtCore.QRect(700, 350, 160, 40))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("QLabel\n"
"{\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 14pt \"Hacen Maghreb Bd\";\n"
"\n"
"}")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(430, 350, 260, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"\n"
"}\n"
"QLineEdit::hover\n"
"{\n"
"    border: 1px solid rgb(0, 170, 255);\n"
"    border-radius: 2px;\n"
"    color: rgb(0, 115, 255);\n"
"    border-radius: 6;\n"
"\n"
"\n"
"}\n"
"")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.label_20 = QtWidgets.QLabel(self.tab)
        self.label_20.setGeometry(QtCore.QRect(700, 410, 160, 40))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("QLabel\n"
"{\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 14pt \"Hacen Maghreb Bd\";\n"
"\n"
"}")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.pushButton_42 = QtWidgets.QPushButton(self.tab)
        self.pushButton_42.setGeometry(QtCore.QRect(430, 470, 260, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_42.sizePolicy().hasHeightForWidth())
        self.pushButton_42.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_42.setFont(font)
        self.pushButton_42.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_42.setStyleSheet("QPushButton\n"
"{\n"
"    color: #fff;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 40px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: rgb(139, 139, 139)\n"
"}\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    border: 1px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #00aaff, stop: 1 #00aaff);\n"
"}\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/ico/login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_42.setIcon(icon2)
        self.pushButton_42.setIconSize(QtCore.QSize(44, 48))
        self.pushButton_42.setObjectName("pushButton_42")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_1.setGeometry(QtCore.QRect(430, 410, 260, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_1.setFont(font)
        self.lineEdit_1.setStyleSheet("QLineEdit {\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"\n"
"}\n"
"QLineEdit::hover\n"
"{\n"
"    border: 1px solid rgb(0, 170, 255);\n"
"    border-radius: 2px;\n"
"    color: rgb(0, 115, 255);\n"
"    border-radius: 6;\n"
"\n"
"\n"
"}\n"
"")
        self.lineEdit_1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.pushButton_43 = QtWidgets.QPushButton(self.tab)
        self.pushButton_43.setGeometry(QtCore.QRect(700, 580, 140, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_43.setFont(font)
        self.pushButton_43.setStyleSheet("QPushButton\n"
"{\n"
"    color: #fff;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 40px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: rgb(139, 139, 139)\n"
"}\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    border: 1px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #00aaff, stop: 1 #00aaff);\n"
"}\n"
"")
        self.pushButton_43.setObjectName("pushButton_43")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(30, 230, 210, 280))
        self.label.setStyleSheet("image: url(:/ico/pic.png);\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_26 = QtWidgets.QLabel(self.tab)
        self.label_26.setGeometry(QtCore.QRect(330, 80, 540, 150))
        font = QtGui.QFont()
        font.setFamily("Mikhak Bold")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_26.setFont(font)
        self.label_26.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_26.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_26.setStyleSheet("font: 75 25pt \"Mikhak Bold\";\n"
"color: rgb(255, 255, 255);\n"
"image: url(:/ico/text1.png);\n"
"")
        self.label_26.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Egypt))
        self.label_26.setText("")
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.tab)
        self.label_27.setGeometry(QtCore.QRect(10, 630, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Museo Sans 700")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(-10, -80, 1690, 970))
        self.label_7.setStyleSheet("image: url(:/ico/bg2.png);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_7.raise_()
        self.label_19.raise_()
        self.lineEdit.raise_()
        self.label_20.raise_()
        self.pushButton_42.raise_()
        self.lineEdit_1.raise_()
        self.pushButton_43.raise_()
        self.label.raise_()
        self.label_26.raise_()
        self.label_27.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_8.setGeometry(QtCore.QRect(390, 470, 440, 50))
        self.groupBox_8.setTitle("")
        self.groupBox_8.setObjectName("groupBox_8")
        self.pushButton_45 = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_45.setGeometry(QtCore.QRect(30, 10, 140, 30))
        self.pushButton_45.setStyleSheet("QPushButton\n"
"{\n"
"    color: #fff;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 40px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: rgb(139, 139, 139)\n"
"}\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    border: 1px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #00aaff, stop: 1 #00aaff);\n"
"}\n"
"")
        self.pushButton_45.setObjectName("pushButton_45")
        self.pushButton_46 = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_46.setGeometry(QtCore.QRect(290, 10, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_46.setFont(font)
        self.pushButton_46.setStyleSheet("QPushButton\n"
"{\n"
"    color: #fff;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 40px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: rgb(139, 139, 139)\n"
"}\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    border: 1px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #00aaff, stop: 1 #00aaff);\n"
"}\n"
"")
        self.pushButton_46.setObjectName("pushButton_46")
        self.label_24 = QtWidgets.QLabel(self.tab_2)
        self.label_24.setGeometry(QtCore.QRect(790, 340, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("QLabel\n"
"{\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 14pt \"Hacen Maghreb Bd\";\n"
"\n"
"}")
        self.label_24.setObjectName("label_24")
        self.pushButton_47 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_47.setGeometry(QtCore.QRect(530, 400, 180, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_47.setFont(font)
        self.pushButton_47.setStyleSheet("QPushButton\n"
"{\n"
"    color: #fff;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 40px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: rgb(139, 139, 139)\n"
"}\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    border: 1px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #00aaff, stop: 1 #00aaff);\n"
"}\n"
"")
        self.pushButton_47.setObjectName("pushButton_47")
        self.lineEdit_55 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_55.setGeometry(QtCore.QRect(410, 340, 400, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_55.setFont(font)
        self.lineEdit_55.setStyleSheet("QLineEdit {\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"\n"
"}\n"
"QLineEdit::hover\n"
"{\n"
"    border: 1px solid rgb(0, 170, 255);\n"
"    border-radius: 2px;\n"
"    color: rgb(0, 115, 255);\n"
"    border-radius: 6;\n"
"\n"
"\n"
"}\n"
"")
        self.lineEdit_55.setObjectName("lineEdit_55")
        self.label_59 = QtWidgets.QLabel(self.tab_2)
        self.label_59.setGeometry(QtCore.QRect(30, 230, 210, 280))
        self.label_59.setStyleSheet("image: url(:/ico/pic.png);\n"
"")
        self.label_59.setText("")
        self.label_59.setObjectName("label_59")
        self.label_31 = QtWidgets.QLabel(self.tab_2)
        self.label_31.setGeometry(QtCore.QRect(330, 80, 540, 150))
        font = QtGui.QFont()
        font.setFamily("Mikhak Bold")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_31.setFont(font)
        self.label_31.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_31.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_31.setStyleSheet("font: 75 25pt \"Mikhak Bold\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"image: url(:/ico/text1.png);\n"
"")
        self.label_31.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Egypt))
        self.label_31.setObjectName("label_31")
        self.label_93 = QtWidgets.QLabel(self.tab_2)
        self.label_93.setGeometry(QtCore.QRect(10, 630, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Museo Sans 700")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_93.setFont(font)
        self.label_93.setObjectName("label_93")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_13 = QtWidgets.QWidget()
        self.tab_13.setObjectName("tab_13")
        self.lineEdit_38 = QtWidgets.QLineEdit(self.tab_13)
        self.lineEdit_38.setGeometry(QtCore.QRect(400, 340, 400, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_38.setFont(font)
        self.lineEdit_38.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_38.setStyleSheet("QLineEdit {\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"\n"
"}\n"
"QLineEdit::hover\n"
"{\n"
"    border: 1px solid rgb(0, 170, 255);\n"
"    border-radius: 2px;\n"
"    color: rgb(0, 115, 255);\n"
"    border-radius: 6;\n"
"\n"
"\n"
"}\n"
"")
        self.lineEdit_38.setText("")
        self.lineEdit_38.setFrame(True)
        self.lineEdit_38.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_38.setPlaceholderText("")
        self.lineEdit_38.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_38.setObjectName("lineEdit_38")
        self.comboBox_21 = QtWidgets.QComboBox(self.tab_13)
        self.comboBox_21.setGeometry(QtCore.QRect(810, 340, 130, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_21.setFont(font)
        self.comboBox_21.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.comboBox_21.setAccessibleDescription("")
        self.comboBox_21.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.comboBox_21.setAutoFillBackground(False)
        self.comboBox_21.setStyleSheet("QComboBox\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: rgb(85, 190, 255);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"")
        self.comboBox_21.setEditable(False)
        self.comboBox_21.setDuplicatesEnabled(False)
        self.comboBox_21.setFrame(True)
        self.comboBox_21.setObjectName("comboBox_21")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.pushButton_24 = QtWidgets.QPushButton(self.tab_13)
        self.pushButton_24.setGeometry(QtCore.QRect(590, 410, 210, 60))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_24.setFont(font)
        self.pushButton_24.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/ico/open1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_24.setIcon(icon3)
        self.pushButton_24.setIconSize(QtCore.QSize(47, 56))
        self.pushButton_24.setObjectName("pushButton_24")
        self.label_52 = QtWidgets.QLabel(self.tab_13)
        self.label_52.setGeometry(QtCore.QRect(30, 230, 210, 280))
        self.label_52.setStyleSheet("image: url(:/ico/pic.png);\n"
"")
        self.label_52.setText("")
        self.label_52.setObjectName("label_52")
        self.pushButton_26 = QtWidgets.QPushButton(self.tab_13)
        self.pushButton_26.setGeometry(QtCore.QRect(400, 420, 110, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_26.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/ico/print.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_26.setIcon(icon4)
        self.pushButton_26.setIconSize(QtCore.QSize(35, 30))
        self.pushButton_26.setObjectName("pushButton_26")
        self.label_30 = QtWidgets.QLabel(self.tab_13)
        self.label_30.setGeometry(QtCore.QRect(330, 80, 540, 150))
        font = QtGui.QFont()
        font.setFamily("Mikhak Bold")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_30.setFont(font)
        self.label_30.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_30.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_30.setStyleSheet("font: 75 25pt \"Mikhak Bold\";\n"
"color: rgb(255, 255, 255);\n"
"image: url(:/ico/text1.png);\n"
"")
        self.label_30.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Egypt))
        self.label_30.setObjectName("label_30")
        self.label_94 = QtWidgets.QLabel(self.tab_13)
        self.label_94.setGeometry(QtCore.QRect(10, 630, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Museo Sans 700")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_94.setFont(font)
        self.label_94.setObjectName("label_94")
        self.label_8 = QtWidgets.QLabel(self.tab_13)
        self.label_8.setGeometry(QtCore.QRect(-10, -80, 1690, 970))
        self.label_8.setStyleSheet("image: url(:/ico/bg2.png);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_8.raise_()
        self.lineEdit_38.raise_()
        self.comboBox_21.raise_()
        self.pushButton_24.raise_()
        self.label_52.raise_()
        self.pushButton_26.raise_()
        self.label_30.raise_()
        self.label_94.raise_()
        self.tabWidget.addTab(self.tab_13, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_3)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, -10, 1020, 840))
        self.tabWidget_2.setStyleSheet("QPushButton\n"
"{\n"
"    color: #fff;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 40px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: rgb(139, 139, 139)\n"
"}\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    border: 1px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #00aaff, stop: 1 #00aaff);\n"
"}\n"
"\n"
"\n"
"QLineEdit {\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"\n"
"}\n"
"QLineEdit::hover\n"
"{\n"
"    border: 1px solid rgb(0, 170, 255);\n"
"    border-radius: 2px;\n"
"    color: rgb(0, 115, 255);\n"
"    border-radius: 6;\n"
"\n"
"\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: rgb(85, 190, 255);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"\n"
"")
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_2 = QtWidgets.QLabel(self.tab_4)
        self.label_2.setGeometry(QtCore.QRect(530, 170, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_4.setGeometry(QtCore.QRect(530, 340, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_15.setGeometry(QtCore.QRect(130, 460, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_15.setFont(font)
        self.lineEdit_15.setText("")
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_9.setGeometry(QtCore.QRect(130, 340, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setText("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_7.setGeometry(QtCore.QRect(530, 520, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_14.setGeometry(QtCore.QRect(130, 400, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_14.setFont(font)
        self.lineEdit_14.setText("")
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_13.setGeometry(QtCore.QRect(130, 280, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setText("")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_2.setGeometry(QtCore.QRect(530, 220, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_3.setGeometry(QtCore.QRect(530, 280, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.tab_4)
        self.label_3.setGeometry(QtCore.QRect(130, 170, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";\n"
"\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_12.setGeometry(QtCore.QRect(130, 220, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setText("")
        self.lineEdit_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_5.setGeometry(QtCore.QRect(530, 400, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_6.setGeometry(QtCore.QRect(530, 460, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_11.setGeometry(QtCore.QRect(130, 520, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setText("")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_5.setGeometry(QtCore.QRect(732, 682, 190, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/ico/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon5)
        self.pushButton_5.setIconSize(QtCore.QSize(62, 46))
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_16.setGeometry(QtCore.QRect(340, 110, 220, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_16.setFont(font)
        self.lineEdit_16.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setGeometry(QtCore.QRect(380, 70, 140, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_4.setFont(font)
        self.label_4.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.comboBox_20 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_20.setGeometry(QtCore.QRect(530, 580, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_20.setFont(font)
        self.comboBox_20.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_20.setStyleSheet("")
        self.comboBox_20.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Egypt))
        self.comboBox_20.setObjectName("comboBox_20")
        self.label_109 = QtWidgets.QLabel(self.tab_4)
        self.label_109.setGeometry(QtCore.QRect(780, 580, 110, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_109.setFont(font)
        self.label_109.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_109.setObjectName("label_109")
        self.pushButton_66 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_66.setGeometry(QtCore.QRect(457, 616, 60, 31))
        font = QtGui.QFont()
        self.pushButton_66.setFont(font)
        self.pushButton_66.setStyleSheet("image: url(:/ico/addf.png);\n"
"QPushButton\n"
"{\n"
"    color: #fff;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 40px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: rgb(139, 139, 139)\n"
"}\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    border: 1px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #00aaff, stop: 1 #00aaff);\n"
"}\n"
"")
        self.pushButton_66.setText("")
        self.pushButton_66.setObjectName("pushButton_66")
        self.comboBox_19 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_19.setGeometry(QtCore.QRect(130, 580, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_19.setFont(font)
        self.comboBox_19.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_19.setObjectName("comboBox_19")
        self.pushButton_65 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_65.setGeometry(QtCore.QRect(393, 616, 60, 31))
        font = QtGui.QFont()
        self.pushButton_65.setFont(font)
        self.pushButton_65.setStyleSheet("image: url(:/ico/removef.png);\n"
"\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #fff;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 40px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: rgb(139, 139, 139)\n"
"}\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    border: 1px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #00aaff, stop: 1 #00aaff);\n"
"}\n"
"")
        self.pushButton_65.setText("")
        self.pushButton_65.setObjectName("pushButton_65")
        self.lineEdit_80 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_80.setGeometry(QtCore.QRect(390, 580, 130, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_80.setFont(font)
        self.lineEdit_80.setText("")
        self.lineEdit_80.setObjectName("lineEdit_80")
        self.label_4.raise_()
        self.label_2.raise_()
        self.lineEdit_4.raise_()
        self.lineEdit_15.raise_()
        self.lineEdit_9.raise_()
        self.lineEdit_7.raise_()
        self.lineEdit_14.raise_()
        self.lineEdit_13.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.label_3.raise_()
        self.lineEdit_12.raise_()
        self.lineEdit_5.raise_()
        self.lineEdit_6.raise_()
        self.lineEdit_11.raise_()
        self.pushButton_5.raise_()
        self.lineEdit_16.raise_()
        self.comboBox_20.raise_()
        self.label_109.raise_()
        self.pushButton_66.raise_()
        self.comboBox_19.raise_()
        self.pushButton_65.raise_()
        self.lineEdit_80.raise_()
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.textEdit = QtWidgets.QTextEdit(self.tab_5)
        self.textEdit.setGeometry(QtCore.QRect(140, 60, 630, 80))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.comboBox = QtWidgets.QComboBox(self.tab_5)
        self.comboBox.setGeometry(QtCore.QRect(530, 160, 240, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_5)
        self.comboBox_2.setGeometry(QtCore.QRect(530, 210, 240, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_17.setGeometry(QtCore.QRect(220, 160, 290, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_17.setFont(font)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_18.setGeometry(QtCore.QRect(220, 210, 290, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_18.setFont(font)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_19.setGeometry(QtCore.QRect(530, 260, 240, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_19.setFont(font)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_20.setGeometry(QtCore.QRect(530, 310, 240, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_20.setFont(font)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.groupBox = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox.setGeometry(QtCore.QRect(330, 370, 440, 50))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(250, 10, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(360, 10, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_4.setGeometry(QtCore.QRect(140, 10, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(30, 10, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_6.setGeometry(QtCore.QRect(32, 692, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_7.setGeometry(QtCore.QRect(732, 682, 190, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_7.setIcon(icon5)
        self.pushButton_7.setIconSize(QtCore.QSize(62, 46))
        self.pushButton_7.setObjectName("pushButton_7")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_5)
        self.comboBox_3.setGeometry(QtCore.QRect(550, 580, 220, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_22.setGeometry(QtCore.QRect(290, 580, 240, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_22.setFont(font)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.label_13 = QtWidgets.QLabel(self.tab_5)
        self.label_13.setGeometry(QtCore.QRect(430, 630, 60, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_13.setObjectName("label_13")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_23.setGeometry(QtCore.QRect(200, 630, 220, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_23.setFont(font)
        self.lineEdit_23.setPlaceholderText("")
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_24.setGeometry(QtCore.QRect(550, 630, 220, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_24.setFont(font)
        self.lineEdit_24.setPlaceholderText("")
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.pushButton_20 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_20.setGeometry(QtCore.QRect(130, 160, 75, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setStyleSheet("image: url(:/ico/addf.png);")
        self.pushButton_20.setText("")
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_21.setGeometry(QtCore.QRect(130, 210, 75, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setStyleSheet("image: url(:/ico/addf.png);")
        self.pushButton_21.setText("")
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_22.setGeometry(QtCore.QRect(70, 160, 52, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setStyleSheet("image: url(:/ico/removef.png);")
        self.pushButton_22.setText("")
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_23.setGeometry(QtCore.QRect(70, 210, 52, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setStyleSheet("image: url(:/ico/removef.png);")
        self.pushButton_23.setText("")
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_75 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_75.setGeometry(QtCore.QRect(140, 580, 52, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_75.setFont(font)
        self.pushButton_75.setStyleSheet("image: url(:/ico/removef.png);")
        self.pushButton_75.setText("")
        self.pushButton_75.setObjectName("pushButton_75")
        self.pushButton_76 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_76.setGeometry(QtCore.QRect(200, 580, 75, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_76.setFont(font)
        self.pushButton_76.setStyleSheet("image: url(:/ico/addf.png);\n"
"")
        self.pushButton_76.setText("")
        self.pushButton_76.setObjectName("pushButton_76")
        self.label_70 = QtWidgets.QLabel(self.tab_5)
        self.label_70.setGeometry(QtCore.QRect(790, 210, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_70.setFont(font)
        self.label_70.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_70.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_70.setObjectName("label_70")
        self.label_71 = QtWidgets.QLabel(self.tab_5)
        self.label_71.setGeometry(QtCore.QRect(790, 450, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_71.setFont(font)
        self.label_71.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_71.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_71.setObjectName("label_71")
        self.label_72 = QtWidgets.QLabel(self.tab_5)
        self.label_72.setGeometry(QtCore.QRect(780, 160, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_72.setFont(font)
        self.label_72.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_72.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_72.setObjectName("label_72")
        self.label_76 = QtWidgets.QLabel(self.tab_5)
        self.label_76.setGeometry(QtCore.QRect(780, 310, 210, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_76.setFont(font)
        self.label_76.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_76.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_76.setObjectName("label_76")
        self.label_79 = QtWidgets.QLabel(self.tab_5)
        self.label_79.setGeometry(QtCore.QRect(780, 370, 160, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_79.setFont(font)
        self.label_79.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_79.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_79.setObjectName("label_79")
        self.label_89 = QtWidgets.QLabel(self.tab_5)
        self.label_89.setGeometry(QtCore.QRect(780, 60, 160, 80))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_89.setFont(font)
        self.label_89.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_89.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_89.setObjectName("label_89")
        self.label_90 = QtWidgets.QLabel(self.tab_5)
        self.label_90.setGeometry(QtCore.QRect(790, 580, 170, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_90.setFont(font)
        self.label_90.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_90.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_90.setObjectName("label_90")
        self.label_91 = QtWidgets.QLabel(self.tab_5)
        self.label_91.setGeometry(QtCore.QRect(780, 630, 170, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_91.setFont(font)
        self.label_91.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_91.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_91.setObjectName("label_91")
        self.label_92 = QtWidgets.QLabel(self.tab_5)
        self.label_92.setGeometry(QtCore.QRect(780, 260, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_92.setFont(font)
        self.label_92.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_92.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_92.setObjectName("label_92")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_3.setGeometry(QtCore.QRect(290, 440, 480, 120))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_6.setGeometry(QtCore.QRect(20, 60, 400, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_6.setFont(font)
        self.radioButton_6.setText("")
        self.radioButton_6.setObjectName("radioButton_6")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_21.setEnabled(False)
        self.lineEdit_21.setGeometry(QtCore.QRect(40, 60, 430, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_21.setFont(font)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_5.setGeometry(QtCore.QRect(20, 10, 450, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setObjectName("radioButton_5")
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.tab_6)
        self.tabWidget_3.setGeometry(QtCore.QRect(0, -10, 1150, 970))
        self.tabWidget_3.setStyleSheet("QLabel\n"
"{\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 14pt \"Hacen Maghreb Bd\";\n"
"\n"
"}")
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.lineEdit_29 = QtWidgets.QLineEdit(self.tab_9)
        self.lineEdit_29.setGeometry(QtCore.QRect(280, 360, 330, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_29.setFont(font)
        self.lineEdit_29.setText("")
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.lineEdit_28 = QtWidgets.QLineEdit(self.tab_9)
        self.lineEdit_28.setGeometry(QtCore.QRect(280, 420, 330, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_28.setFont(font)
        self.lineEdit_28.setText("")
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.lineEdit_26 = QtWidgets.QLineEdit(self.tab_9)
        self.lineEdit_26.setGeometry(QtCore.QRect(280, 180, 330, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_26.setFont(font)
        self.lineEdit_26.setText("")
        self.lineEdit_26.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.checkBox = QtWidgets.QCheckBox(self.tab_9)
        self.checkBox.setGeometry(QtCore.QRect(310, 690, 290, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/ico/line.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.checkBox.setIcon(icon6)
        self.checkBox.setIconSize(QtCore.QSize(12, 171))
        self.checkBox.setObjectName("checkBox")
        self.comboBox_4 = QtWidgets.QComboBox(self.tab_9)
        self.comboBox_4.setGeometry(QtCore.QRect(280, 300, 180, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.lineEdit_27 = QtWidgets.QLineEdit(self.tab_9)
        self.lineEdit_27.setGeometry(QtCore.QRect(65, 480, 180, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_27.setFont(font)
        self.lineEdit_27.setText("")
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.label_18 = QtWidgets.QLabel(self.tab_9)
        self.label_18.setGeometry(QtCore.QRect(450, 300, 160, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_18.setObjectName("label_18")
        self.label_15 = QtWidgets.QLabel(self.tab_9)
        self.label_15.setGeometry(QtCore.QRect(780, 640, 140, 35))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 14pt \"Hacen Maghreb Bd\";\n"
"\n"
"    border-radius: 6;\n"
"")
        self.label_15.setObjectName("label_15")
        self.label_17 = QtWidgets.QLabel(self.tab_9)
        self.label_17.setGeometry(QtCore.QRect(280, 120, 330, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.lineEdit_25 = QtWidgets.QLineEdit(self.tab_9)
        self.lineEdit_25.setGeometry(QtCore.QRect(280, 240, 330, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_25.setFont(font)
        self.lineEdit_25.setText("")
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_9)
        self.pushButton_10.setGeometry(QtCore.QRect(360, 630, 170, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/ico/addperson.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_10.setIcon(icon7)
        self.pushButton_10.setIconSize(QtCore.QSize(39, 31))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_9)
        self.pushButton_8.setGeometry(QtCore.QRect(30, 700, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_9)
        self.pushButton_9.setGeometry(QtCore.QRect(730, 690, 190, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_9.setIcon(icon5)
        self.pushButton_9.setIconSize(QtCore.QSize(100, 46))
        self.pushButton_9.setObjectName("pushButton_9")
        self.comboBox_15 = QtWidgets.QComboBox(self.tab_9)
        self.comboBox_15.setGeometry(QtCore.QRect(280, 480, 220, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_15.setFont(font)
        self.comboBox_15.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_15.setObjectName("comboBox_15")
        self.label_62 = QtWidgets.QLabel(self.tab_9)
        self.label_62.setGeometry(QtCore.QRect(490, 480, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_62.setFont(font)
        self.label_62.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_62.setObjectName("label_62")
        self.pushButton_19 = QtWidgets.QPushButton(self.tab_9)
        self.pushButton_19.setGeometry(QtCore.QRect(160, 517, 80, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setStyleSheet("image: url(:/ico/addf.png);")
        self.pushButton_19.setText("")
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_60 = QtWidgets.QPushButton(self.tab_9)
        self.pushButton_60.setGeometry(QtCore.QRect(70, 517, 80, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_60.setFont(font)
        self.pushButton_60.setStyleSheet("image: url(:/ico/removef.png);")
        self.pushButton_60.setText("")
        self.pushButton_60.setObjectName("pushButton_60")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.tab_9)
        self.lcdNumber_2.setGeometry(QtCore.QRect(730, 640, 60, 35))
        self.lcdNumber_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 14pt \"Hacen Maghreb Bd\";\n"
"\n"
"    border-radius: 6;\n"
"")
        self.lcdNumber_2.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdNumber_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lcdNumber_2.setLineWidth(1)
        self.lcdNumber_2.setMidLineWidth(0)
        self.lcdNumber_2.setDigitCount(1)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.pushButton_60.raise_()
        self.pushButton_19.raise_()
        self.lineEdit_29.raise_()
        self.lineEdit_28.raise_()
        self.lineEdit_26.raise_()
        self.checkBox.raise_()
        self.lineEdit_27.raise_()
        self.label_15.raise_()
        self.label_17.raise_()
        self.lineEdit_25.raise_()
        self.pushButton_10.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.label_62.raise_()
        self.lcdNumber_2.raise_()
        self.comboBox_15.raise_()
        self.label_18.raise_()
        self.comboBox_4.raise_()
        self.tabWidget_3.addTab(self.tab_9, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.lineEdit_30 = QtWidgets.QLineEdit(self.tab_10)
        self.lineEdit_30.setGeometry(QtCore.QRect(280, 480, 330, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_30.setFont(font)
        self.lineEdit_30.setText("")
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_10)
        self.pushButton_11.setGeometry(QtCore.QRect(360, 630, 170, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setIcon(icon7)
        self.pushButton_11.setIconSize(QtCore.QSize(39, 31))
        self.pushButton_11.setObjectName("pushButton_11")
        self.label_21 = QtWidgets.QLabel(self.tab_10)
        self.label_21.setGeometry(QtCore.QRect(440, 360, 170, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_21.setObjectName("label_21")
        self.lineEdit_31 = QtWidgets.QLineEdit(self.tab_10)
        self.lineEdit_31.setGeometry(QtCore.QRect(280, 240, 330, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_31.setFont(font)
        self.lineEdit_31.setText("")
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.comboBox_5 = QtWidgets.QComboBox(self.tab_10)
        self.comboBox_5.setGeometry(QtCore.QRect(280, 360, 170, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_5.setFont(font)
        self.comboBox_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.lineEdit_32 = QtWidgets.QLineEdit(self.tab_10)
        self.lineEdit_32.setGeometry(QtCore.QRect(280, 180, 330, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_32.setFont(font)
        self.lineEdit_32.setText("")
        self.lineEdit_32.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.label_23 = QtWidgets.QLabel(self.tab_10)
        self.label_23.setGeometry(QtCore.QRect(280, 120, 330, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.lineEdit_34 = QtWidgets.QLineEdit(self.tab_10)
        self.lineEdit_34.setGeometry(QtCore.QRect(280, 420, 330, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_34.setFont(font)
        self.lineEdit_34.setText("")
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.lineEdit_35 = QtWidgets.QLineEdit(self.tab_10)
        self.lineEdit_35.setGeometry(QtCore.QRect(280, 300, 330, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_35.setFont(font)
        self.lineEdit_35.setText("")
        self.lineEdit_35.setObjectName("lineEdit_35")
        self.pushButton_13 = QtWidgets.QPushButton(self.tab_10)
        self.pushButton_13.setGeometry(QtCore.QRect(730, 690, 190, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_13.setIcon(icon5)
        self.pushButton_13.setIconSize(QtCore.QSize(62, 46))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_12 = QtWidgets.QPushButton(self.tab_10)
        self.pushButton_12.setGeometry(QtCore.QRect(30, 700, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.label_112 = QtWidgets.QLabel(self.tab_10)
        self.label_112.setGeometry(QtCore.QRect(490, 540, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_112.setFont(font)
        self.label_112.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_112.setObjectName("label_112")
        self.comboBox_22 = QtWidgets.QComboBox(self.tab_10)
        self.comboBox_22.setGeometry(QtCore.QRect(280, 540, 220, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_22.setFont(font)
        self.comboBox_22.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_22.setObjectName("comboBox_22")
        self.pushButton_67 = QtWidgets.QPushButton(self.tab_10)
        self.pushButton_67.setGeometry(QtCore.QRect(70, 575, 80, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_67.setFont(font)
        self.pushButton_67.setStyleSheet("image: url(:/ico/removef.png);")
        self.pushButton_67.setText("")
        self.pushButton_67.setObjectName("pushButton_67")
        self.lineEdit_33 = QtWidgets.QLineEdit(self.tab_10)
        self.lineEdit_33.setGeometry(QtCore.QRect(65, 538, 180, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_33.setFont(font)
        self.lineEdit_33.setText("")
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.pushButton_68 = QtWidgets.QPushButton(self.tab_10)
        self.pushButton_68.setGeometry(QtCore.QRect(160, 575, 80, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_68.setFont(font)
        self.pushButton_68.setStyleSheet("image: url(:/ico/addf.png);")
        self.pushButton_68.setText("")
        self.pushButton_68.setObjectName("pushButton_68")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.tab_10)
        self.lcdNumber_3.setGeometry(QtCore.QRect(730, 640, 60, 35))
        self.lcdNumber_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 14pt \"Hacen Maghreb Bd\";\n"
"\n"
"    border-radius: 6;\n"
"")
        self.lcdNumber_3.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdNumber_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lcdNumber_3.setLineWidth(1)
        self.lcdNumber_3.setMidLineWidth(0)
        self.lcdNumber_3.setDigitCount(1)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.label_63 = QtWidgets.QLabel(self.tab_10)
        self.label_63.setGeometry(QtCore.QRect(780, 640, 140, 35))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_63.setFont(font)
        self.label_63.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 14pt \"Hacen Maghreb Bd\";\n"
"\n"
"    border-radius: 6;\n"
"")
        self.label_63.setObjectName("label_63")
        self.pushButton_67.raise_()
        self.pushButton_68.raise_()
        self.lineEdit_30.raise_()
        self.pushButton_11.raise_()
        self.label_21.raise_()
        self.lineEdit_31.raise_()
        self.comboBox_5.raise_()
        self.lineEdit_32.raise_()
        self.label_23.raise_()
        self.lineEdit_34.raise_()
        self.lineEdit_35.raise_()
        self.pushButton_13.raise_()
        self.pushButton_12.raise_()
        self.label_112.raise_()
        self.comboBox_22.raise_()
        self.lineEdit_33.raise_()
        self.label_63.raise_()
        self.lcdNumber_3.raise_()
        self.tabWidget_3.addTab(self.tab_10, "")
        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tabWidget_4 = QtWidgets.QTabWidget(self.tab_7)
        self.tabWidget_4.setGeometry(QtCore.QRect(0, -10, 1350, 990))
        self.tabWidget_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget_4.setStyleSheet("QTextEdit {\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"\n"
"}\n"
"QTextEdit::hover\n"
"{\n"
"    border: 1px solid rgb(0, 170, 255);\n"
"    border-radius: 2px;\n"
"    color: rgb(0, 115, 255);\n"
"    border-radius: 6;\n"
"\n"
"\n"
"}\n"
"")
        self.tabWidget_4.setObjectName("tabWidget_4")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.checkBox_2 = QtWidgets.QCheckBox(self.tab_8)
        self.checkBox_2.setGeometry(QtCore.QRect(310, 690, 310, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setAccessibleDescription("")
        self.checkBox_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_2.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.checkBox_2.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Egypt))
        self.checkBox_2.setIcon(icon6)
        self.checkBox_2.setIconSize(QtCore.QSize(12, 171))
        self.checkBox_2.setObjectName("checkBox_2")
        self.pushButton_14 = QtWidgets.QPushButton(self.tab_8)
        self.pushButton_14.setGeometry(QtCore.QRect(30, 700, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.tab_8)
        self.pushButton_15.setGeometry(QtCore.QRect(730, 690, 190, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_15.setIcon(icon5)
        self.pushButton_15.setIconSize(QtCore.QSize(100, 46))
        self.pushButton_15.setObjectName("pushButton_15")
        self.spinBox_35 = QtWidgets.QSpinBox(self.tab_8)
        self.spinBox_35.setGeometry(QtCore.QRect(310, 330, 130, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.spinBox_35.setFont(font)
        self.spinBox_35.setStyleSheet("\n"
"QAbstractSpinBox {\n"
"\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    border: 1px solid #3A3939;\n"
"    background-color:rgb(255, 0, 102);\n"
"    color: white;\n"
"    border-radius: 2px;\n"
"    min-width: 75px;\n"
"}\n"
"\n"
"")
        self.spinBox_35.setObjectName("spinBox_35")
        self.label_114 = QtWidgets.QLabel(self.tab_8)
        self.label_114.setGeometry(QtCore.QRect(750, 330, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_114.setFont(font)
        self.label_114.setStyleSheet("\n"
"QLabel\n"
"{\n"
"/*font: 75 16pt \"Arial Unicode MS\";*/\n"
"\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 17pt \"Hacen Maghreb Bd\";\n"
"\n"
"}")
        self.label_114.setObjectName("label_114")
        self.comboBox_24 = QtWidgets.QComboBox(self.tab_8)
        self.comboBox_24.setGeometry(QtCore.QRect(450, 330, 310, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBox_24.setFont(font)
        self.comboBox_24.setObjectName("comboBox_24")
        self.pushButton_79 = QtWidgets.QPushButton(self.tab_8)
        self.pushButton_79.setGeometry(QtCore.QRect(270, 390, 170, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_79.setFont(font)
        self.pushButton_79.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/ico/addf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_79.setIcon(icon8)
        self.pushButton_79.setIconSize(QtCore.QSize(22, 22))
        self.pushButton_79.setObjectName("pushButton_79")
        self.pushButton_80 = QtWidgets.QPushButton(self.tab_8)
        self.pushButton_80.setGeometry(QtCore.QRect(760, 180, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_80.setFont(font)
        self.pushButton_80.setIcon(icon8)
        self.pushButton_80.setIconSize(QtCore.QSize(22, 22))
        self.pushButton_80.setObjectName("pushButton_80")
        self.lineEdit_81 = QtWidgets.QLineEdit(self.tab_8)
        self.lineEdit_81.setGeometry(QtCore.QRect(270, 180, 460, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_81.setFont(font)
        self.lineEdit_81.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_81.setObjectName("lineEdit_81")
        self.pushButton_125 = QtWidgets.QPushButton(self.tab_8)
        self.pushButton_125.setGeometry(QtCore.QRect(770, 240, 130, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_125.setFont(font)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/ico/removef.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_125.setIcon(icon9)
        self.pushButton_125.setIconSize(QtCore.QSize(22, 22))
        self.pushButton_125.setObjectName("pushButton_125")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_8)
        self.tableWidget.setGeometry(QtCore.QRect(40, 180, 220, 420))
        self.tableWidget.setMinimumSize(QtCore.QSize(220, 0))
        self.tableWidget.setMaximumSize(QtCore.QSize(220, 420))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("\n"
"QMenu::indicator:exclusive:unchecked:selected\n"
"{\n"
"    border-image: url(:/light/radio_unchecked_disabled.svg);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked\n"
"{\n"
"    border-image: url(:/light/radio_checked.svg);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked:selected\n"
"{\n"
"    border-image: url(:/light/radio_checked.svg);\n"
"}\n"
"\n"
"QMenu::right-arrow\n"
"{\n"
"    margin: 0.5ex;\n"
"    border-image: url(:/light/right_arrow.svg);\n"
"    width: 0.6ex;\n"
"    height: 0.9ex;\n"
"}\n"
"\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #454545;\n"
"    background-color: #EFF0F1;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    alternate-background-color: #EFF0F1;\n"
"    color: #31363B;\n"
"    border: 0.1ex solid 3A3939;\n"
"    border-radius: 0.2ex;\n"
"}\n"
"\n"
"QWidget:focus,\n"
"QMenuBar:focus\n"
"{\n"
"    border: 0.1ex solid #33A4DF;\n"
"}\n"
"\n"
"QTabWidget:focus,\n"
"QCheckBox:focus,\n"
"QRadioButton:focus,\n"
"QSlider:focus\n"
"{\n"
"    border: none;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: #FCFCFC;\n"
"    padding: 0.5ex;\n"
"    border-style: solid;\n"
"    border: 0.1ex solid #BAB9B8;\n"
"    border-radius: 0.2ex;\n"
"    color: #31363B;\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"    border: 0.1ex solid #BAB9B8;\n"
"    border-radius: 0.2ex;\n"
"    padding-top: 1ex;\n"
"    margin-top: 1ex;\n"
"}\n"
"\n"
"QGroupBox::title\n"
"{\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding-left: 0.1ex;\n"
"    padding-right: 0.1ex;\n"
"    margin-top: -0.7ex;\n"
"}\n"
"\n"
"QAbstractScrollArea\n"
"{\n"
"    border-radius: 0.2ex;\n"
"    border: 0.1ex solid #BAB9B8;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar:horizontal\n"
"{\n"
"    height: 1.5ex;\n"
"    margin: 0.3ex 1.5ex 0.3ex 1.5ex;\n"
"    border: 0.1ex transparent #2A2929;\n"
"    border-radius: 0.4ex;\n"
"    background-color: #2A2929;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background-color: #605F5F;\n"
"    min-width: 0.5ex;\n"
"    border-radius: 0.4ex;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    margin: 0ex 0.3ex 0ex 0.3ex;\n"
"    border-image: url(:/light/right_arrow_disabled.svg);\n"
"    width: 1ex;\n"
"    height: 1ex;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    margin: 0px 0.3ex 0px 0.3ex;\n"
"    border-image: url(:/light/left_arrow_disabled.svg);\n"
"    height: 1ex;\n"
"    width: 1ex;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: #2A2929;\n"
"    width: 1.5ex;\n"
"    margin: 1.5ex 0.3ex 1.5ex 0.3ex;\n"
"    border: 0.1ex transparent #2A2929;\n"
"    border-radius: 0.4ex;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: #605F5F;\n"
"    min-height: 0.5ex;\n"
"    border-radius: 0.4ex;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    margin: 0.3ex 0ex 0.3ex 0ex;\n"
"    border-image: url(:/light/up_arrow_disabled.svg);\n"
"    height: 1ex;\n"
"    width: 1ex;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    margin: 0.3ex 0ex 0.3ex 0ex;\n"
"    border-image: url(:/light/down_arrow_disabled.svg);\n"
"    height: 1ex;\n"
"    width: 1ex;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover,\n"
"QScrollBar::sub-line:vertical:on\n"
"{\n"
"\n"
"    border-image: url(:/light/up_arrow.svg);\n"
"    height: 1ex;\n"
"    width: 1ex;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:hover,\n"
"QScrollBar::add-line:vertical:on\n"
"{\n"
"    border-image: url(:/light/down_arrow.svg);\n"
"    height: 1ex;\n"
"    width: 1ex;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical,\n"
"QScrollBar::down-arrow:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #EFF0F1;\n"
"    color: #31363B;\n"
"    border: 0.1ex solid #BAB9B8;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #EFF0F1;\n"
"    color: #31363B;\n"
"    border-radius: 0.2ex;\n"
"    border: 0.1ex solid #BAB9B8;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: #BAB9B8;\n"
"    color: #31363B;\n"
"    padding: 0.5ex;\n"
"    border: 0.1ex solid #BAB9B8;\n"
"}\n"
"\n"
"QSizeGrip\n"
"{\n"
"    border-image: url(:/light/sizegrip.svg);\n"
"    width: 1.2ex;\n"
"    height: 1.2ex;\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: #EFF0F1;\n"
"    color: white;\n"
"    padding-left: 0.4ex;\n"
"    spacing: 0.2ex;\n"
"    border: 0.1ex dashed #BAB9B8;\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: #787876;\n"
"    color: white;\n"
"    padding-left: 0.4ex;\n"
"    border: 0.1ex solid #BAB9B8;\n"
"    spacing: 0.2x;\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 0.1ex;\n"
"    background-color: #BAB9B8;\n"
"    color: white;\n"
"    padding-left: 0.4ex;\n"
"    margin-left: 1ex;\n"
"    margin-right: 0.5ex;\n"
"}\n"
"\n"
"QFrame[frameShape=\"2\"],  /* QFrame::Panel == 0x0003 */\n"
"QFrame[frameShape=\"3\"],  /* QFrame::WinPanel == 0x0003 */\n"
"QFrame[frameShape=\"4\"],  /* QFrame::HLine == 0x0004 */\n"
"QFrame[frameShape=\"5\"],  /* QFrame::VLine == 0x0005 */\n"
"QFrame[frameShape=\"6\"]  /* QFrame::StyledPanel == 0x0006 */\n"
"{\n"
"    border-width: 0.1ex;\n"
"    padding: 0.1ex;\n"
"    border-style: solid;\n"
"    border-color: #EFF0F1;\n"
"    background-color: #bcbfc2;\n"
"    border-radius: 0.5ex;\n"
"}\n"
"\n"
"QStackedWidget\n"
"{\n"
"    border: 0.1ex transparent black;\n"
"}\n"
"\n"
"QToolBar\n"
"{\n"
"    border: 0.1ex transparent #393838;\n"
"    background: 0.1ex solid #EFF0F1;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QToolBar::handle:horizontal\n"
"{\n"
"    border-image: url(:/light/hmovetoolbar.svg);\n"
"    width = 1.6ex;\n"
"    height = 6.4ex;\n"
"}\n"
"\n"
"QToolBar::handle:vertical\n"
"{\n"
"    border-image: url(:/light/vmovetoolbar.svg);\n"
"    width = 5.4ex;\n"
"    height = 1ex;\n"
"}\n"
"\n"
"QToolBar::separator:horizontal\n"
"{\n"
"    border-image: url(:/light/hsepartoolbar.svg);\n"
"    width = 0.7ex;\n"
"    height = 6.3ex;\n"
"}\n"
"\n"
"QToolBar::separator:vertical\n"
"{\n"
"    border-image: url(:/light/vsepartoolbars.svg);\n"
"    width = 6.3ex;\n"
"    height = 0.7ex;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #31363B;\n"
"    background-color: qlineargradient(x1: 0.5, y1: 0.5 x2: 0.5, y2: 1, stop: 0 #EFF0F1, stop: 0.5 #eaebec);\n"
"    border-width: 0.1ex;\n"
"    border-color: #BAB9B8;\n"
"    border-style: solid;\n"
"    padding: 0.5ex;\n"
"    border-radius: 0.2ex;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:disabled\n"
"{\n"
"    background-color: #e0e1e2;\n"
"    border-width: 0.1ex;\n"
"    border-color: #b4b4b4;\n"
"    border-style: solid;\n"
"    padding-top: 0.5ex;\n"
"    padding-bottom: 0.5ex;\n"
"    padding-left: 1ex;\n"
"    padding-right: 1ex;\n"
"    border-radius: 0.2ex;\n"
"    color: #b4b4b4;\n"
"}\n"
"\n"
"QPushButton:focus\n"
"{\n"
"    color: black;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #33A4DF;\n"
"    border-style: solid;\n"
"    border: 0.1ex solid #BAB9B8;\n"
"    border-radius: 0.2ex;\n"
"    padding: 0.5ex;\n"
"    min-width: 7.5ex;\n"
"}\n"
"\n"
"QPushButton:checked\n"
"{\n"
"    background-color: #BAB9B8;\n"
"    border-color: #6A6969;\n"
"}\n"
"\n"
"QComboBox:hover,\n"
"QAbstractSpinBox:hover,\n"
"QLineEdit:hover,\n"
"QTextEdit:hover,\n"
"QPlainTextEdit:hover,\n"
"QAbstractView:hover,\n"
"QTreeView:hover\n"
"{\n"
"    border: 0.1ex solid #33A4DF;\n"
"    color: #31363B;\n"
"}\n"
"\n"
"QComboBox:hover:pressed,\n"
"QPushButton:hover:pressed,\n"
"QAbstractSpinBox:hover:pressed,\n"
"QLineEdit:hover:pressed,\n"
"QTextEdit:hover:pressed,\n"
"QPlainTextEdit:hover:pressed,\n"
"QAbstractView:hover:pressed,\n"
"QTreeView:hover:pressed\n"
"{\n"
"    background-color: #EFF0F1;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 0.3ex;\n"
"    padding-left: 0.4ex;\n"
"    selection-background-color: #4a4a4a;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: #FCFCFC;\n"
"    border-radius: 0.2ex;\n"
"    border: 0.1ex solid #BAB9B8;\n"
"    selection-background-color: #33A4DF;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 1.5ex;\n"
"\n"
"    border-left-width: 0ex;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 0.3ex;\n"
"    border-bottom-right-radius: 0.3ex;\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"    border-image: url(:/light/down_arrow_disabled.svg);\n"
"    width: 0.9ex;\n"
"    height: 0.6ex;\n"
"}\n"
"\n"
"QComboBox::down-arrow:on,\n"
"QComboBox::down-arrow:hover,\n"
"QComboBox::down-arrow:focus\n"
"{\n"
"    border-image: url(:/light/down_arrow.svg);\n"
"    width: 0.9ex;\n"
"    height: 0.6ex;\n"
"}\n"
"\n"
"QAbstractSpinBox\n"
"{\n"
"    padding: 0.5ex;\n"
"    border: 0.1ex solid #BAB9B8;\n"
"    background-color: #D9D8D7;\n"
"    color: #31363B;\n"
"    border-radius: 0.2ex;\n"
"    min-width: 7.5ex;\n"
"}\n"
"\n"
"QAbstractSpinBox:up-button\n"
"{\n"
"    background-color: transparent;\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: center right;\n"
"}\n"
"\n"
"QAbstractSpinBox:down-button\n"
"{\n"
"    background-color: transparent;\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: center left;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow,\n"
"QAbstractSpinBox::up-arrow:disabled,\n"
"QAbstractSpinBox::up-arrow:off\n"
"{\n"
"    border-image: url(:/light/up_arrow_disabled.svg);\n"
"    width: 0.9ex;\n"
"    height: 0.6ex;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow:hover\n"
"{\n"
"    border-image: url(:/light/up_arrow.svg);\n"
"    width: 0.9ex;\n"
"    height: 0.6ex;\n"
"}\n"
"\n"
"QAbstractSpinBox::down-arrow,\n"
"QAbstractSpinBox::down-arrow:disabled,\n"
"QAbstractSpinBox::down-arrow:off\n"
"{\n"
"    border-image: url(:/light/down_arrow_disabled.svg);\n"
"    width: 0.9ex;\n"
"    height: 0.6ex;\n"
"}\n"
"\n"
"QAbstractSpinBox::down-arrow:hover\n"
"{\n"
"    border-image: url(:/light/down_arrow.svg);\n"
"    width: 0.9ex;\n"
"    height: 0.6ex;\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"    border: 0ex solid black;\n"
"}\n"
"\n"
"QTabWidget{\n"
"    border: 0.1ex solid #BAB9B8;\n"
"}\n"
"\n"
"/* BORDERS */\n"
"QTabWidget::pane\n"
"{\n"
"    padding: 0.5ex;\n"
"    margin: 0.1ex;\n"
"}\n"
"\n"
"QTabWidget::pane:top\n"
"{\n"
"    border: 0.1ex solid #BAB9B8;\n"
"    top: -0.1ex;\n"
"}\n"
"\n"
"QTabWidget::pane:bottom\n"
"{\n"
"    border: 0.1ex solid #BAB9B8;\n"
"    bottom: -0.1ex;\n"
"}\n"
"\n"
"QTabWidget::pane:left\n"
"{\n"
"    border: 0.1ex solid #BAB9B8;\n"
"    right: -0.1ex;\n"
"}\n"
"\n"
"QTabWidget::pane:right\n"
"{\n"
"    border: 0.1ex solid #BAB9B8;\n"
"    left: -0.1ex;\n"
"}\n"
"\n"
"QTabBar\n"
"{\n"
"    qproperty-drawBase: 0;\n"
"    left: 0.5ex; /* move to the right by 0.5ex */\n"
"    border-radius: 0.3ex;\n"
"}\n"
"\n"
"QTabBar:focus\n"
"{\n"
"    border: 0ex transparent black;\n"
"}\n"
"\n"
"QTabBar::close-button\n"
"{\n"
"    border-image: url(:/light/close.svg);\n"
"    width: 1.2ex;\n"
"    height: 1.2ex;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTabBar::close-button:hover\n"
"{\n"
"    border-image: url(:/light/close-hover.svg);\n"
"    width: 1.2ex;\n"
"    height: 1.2ex;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTabBar::close-button:pressed\n"
"{\n"
"    border-image: url(:/light/close-pressed.svg);\n"
"    width: 1.2ex;\n"
"    height: 1.2ex;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* TOP TABS */\n"
"QTabBar::tab:top\n"
"{\n"
"    color: #31363B;\n"
"    border: 0.1ex transparent black;\n"
"    border-left: 0.1ex solid #BAB9B8;\n"
"    border-top: 0.1ex solid #BAB9B8;\n"
"    background-color: #EFF0F1;\n"
"    padding: 0.5ex;\n"
"    min-width: 5ex;\n"
"    border-top-left-radius: 0.2ex;\n"
"    border-top-right-radius: 0.2ex;\n"
"}\n"
"\n"
"QTabBar::tab:top:last,\n"
"QTabBar::tab:top:only-one\n"
"{\n"
"    color: #31363B;\n"
"    border: 0.1ex transparent black;\n"
"    border-left: 0.1ex solid #BAB9B8;\n"
"    border-right: 0.1ex solid #BAB9B8;\n"
"    border-top: 0.1ex solid #BAB9B8;\n"
"    background-color: #EFF0F1;\n"
"    padding: 0.5ex;\n"
"    min-width: 5ex;\n"
"    border-top-left-radius: 0.2ex;\n"
"    border-top-right-radius: 0.2ex;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected\n"
"{\n"
"    color: #31363B;\n"
"    background-color: #D9D8D7;\n"
"    border: 0.1ex transparent black;\n"
"    border-left: 0.1ex solid #BAB9B8;\n"
"    border-top-left-radius: 0.2ex;\n"
"    border-top-right-radius: 0.2ex;\n"
"}\n"
"\n"
"QTabBar::tab:top:first:!selected\n"
"{\n"
"    color: #31363B;\n"
"    background-color: #D9D8D7;\n"
"    border: 0.1ex transparent black;\n"
"    border-top-left-radius: 0.2ex;\n"
"    border-top-right-radius: 0.2ex;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected:hover\n"
"{\n"
"    background-color: rgba(61, 173, 232, 0.1);\n"
"    border: 0.1ex rgba(61, 173, 232, 0.1);\n"
"    border-left: 0.1ex solid #BAB9B8;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected:first:hover\n"
"{\n"
"    background-color: rgba(61, 173, 232, 0.1);\n"
"    border: 0.1ex rgba(61, 173, 232, 0.1);\n"
"}\n"
"\n"
"/* BOTTOM TABS */\n"
"QTabBar::tab:bottom\n"
"{\n"
"    color: #31363B;\n"
"    border: 0.1ex transparent black;\n"
"    border-left: 0.1ex solid #BAB9B8;\n"
"    border-bottom: 0.1ex solid #BAB9B8;\n"
"    background-color: #EFF0F1;\n"
"    padding: 0.5ex;\n"
"    border-bottom-left-radius: 0.2ex;\n"
"    border-bottom-right-radius: 0.2ex;\n"
"    min-width: 5ex;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:last,\n"
"QTabBar::tab:bottom:only-one\n"
"{\n"
"    color: #31363B;\n"
"    border: 0.1ex transparent black;\n"
"    border-left: 0.1ex solid #BAB9B8;\n"
"    border-right: 0.1ex solid #BAB9B8;\n"
"    border-bottom: 0.1ex solid #BAB9B8;\n"
"    background-color: #EFF0F1;\n"
"    padding: 0.5ex;\n"
"    border-bottom-left-radius: 0.2ex;\n"
"    border-bottom-right-radius: 0.2ex;\n"
"    min-width: 5ex;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected\n"
"{\n"
"    color: #31363B;\n"
"    background-color: #D9D8D7;\n"
"    border: 0.1ex transparent black;\n"
"    border-left: 0.1ex solid #BAB9B8;\n"
"    border-bottom-left-radius: 0.2ex;\n"
"    border-bottom-right-radius: 0.2ex;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:first:!selected\n"
"{\n"
"    color: #31363B;\n"
"    background-color: #D9D8D7;\n"
"    border: 0.1ex transparent black;\n"
"    border-bottom-left-radius: 0.2ex;\n"
"    border-bottom-right-radius: 0.2ex;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected:hover\n"
"{\n"
"    background-color: rgba(61, 173, 232, 0.1);\n"
"    border: 0.1ex rgba(61, 173, 232, 0.1);\n"
"    border-left: 0.1ex solid #BAB9B8;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected:first:hover\n"
"{\n"
"    background-color: rgba(61, 173, 232, 0.1);\n"
"    border: 0.1ex rgba(61, 173, 232, 0.1);\n"
"}\n"
"\n"
"/* LEFT TABS */\n"
"QTabBar::tab:left\n"
"{\n"
"    color: #31363B;\n"
"    border: 0.1ex transparent black;\n"
"    border-top: 0.1ex solid #BAB9B8;\n"
"    border-right: 0.1ex solid #BAB9B8;\n"
"    background-color: #EFF0F1;\n"
"    padding: 0.5ex;\n"
"    border-top-right-radius: 0.2ex;\n"
"    border-bottom-right-radius: 0.2ex;\n"
"    min-height: 5ex;\n"
"}\n"
"\n"
"QTabBar::tab:left:last,\n"
"QTabBar::tab:left:only-one\n"
"{\n"
"    color: #31363B;\n"
"    border: 0.1ex transparent black;\n"
"    border-top: 0.1ex solid #BAB9B8;\n"
"    border-bottom: 0.1ex solid #BAB9B8;\n"
"    border-right: 0.1ex solid #BAB9B8;\n"
"    background-color: #EFF0F1;\n"
"    padding: 0.5ex;\n"
"    border-top-right-radius: 0.2ex;\n"
"    border-bottom-right-radius: 0.2ex;\n"
"    min-height: 5ex;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected\n"
"{\n"
"    color: #31363B;\n"
"    background-color: #D9D8D7;\n"
"    border: 0.1ex transparent black;\n"
"    border-top: 0.1ex solid #BAB9B8;\n"
"    border-top-right-radius: 0.2ex;\n"
"    border-bottom-right-radius: 0.2ex;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected:hover\n"
"{\n"
"    background-color: rgba(61, 173, 232, 0.1);\n"
"    border: 0.1ex rgba(61, 173, 232, 0.1);\n"
"    border-top: 0.1ex solid #BAB9B8;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected:first:hover\n"
"{\n"
"    background-color: rgba(61, 173, 232, 0.1);\n"
"    border: 0.1ex rgba(61, 173, 232, 0.1);\n"
"}\n"
"\n"
"/* RIGHT TABS */\n"
"QTabBar::tab:right\n"
"{\n"
"    color: #31363B;\n"
"    border: 0.1ex transparent black;\n"
"    border-top: 0.1ex solid #BAB9B8;\n"
"    border-left: 0.1ex solid #BAB9B8;\n"
"    background-color: #D9D8D7;\n"
"    padding: 0.5ex;\n"
"    border-top-left-radius: 0.2ex;\n"
"    border-bottom-left-radius: 0.2ex;\n"
"    min-height: 5ex;\n"
"}\n"
"\n"
"QTabBar::tab:right:last,\n"
"QTabBar::tab:right:only-one\n"
"{\n"
"    color: #31363B;\n"
"    border: 0.1ex transparent black;\n"
"    border-top: 0.1ex solid #BAB9B8;\n"
"    border-bottom: 0.1ex solid #BAB9B8;\n"
"    border-left: 0.1ex solid #BAB9B8;\n"
"    background-color: #D9D8D7;\n"
"    padding: 0.5ex;\n"
"    border-top-left-radius: 0.2ex;\n"
"    border-bottom-left-radius: 0.2ex;\n"
"    min-height: 5ex;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected\n"
"{\n"
"    color: #31363B;\n"
"    background-color: #54575B;\n"
"    border: 0.1ex transparent black;\n"
"    border-top: 0.1ex solid #BAB9B8;\n"
"    border-top-left-radius: 0.2ex;\n"
"    border-bottom-left-radius: 0.2ex;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected:hover\n"
"{\n"
"    background-color: rgba(61, 173, 232, 0.1);\n"
"    border: 0.1ex rgba(61, 173, 232, 0.1);\n"
"    border-top: 0.1ex solid #BAB9B8;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected:first:hover\n"
"{\n"
"    background-color: rgba(61, 173, 232, 0.1);\n"
"    border: 0.1ex rgba(61, 173, 232, 0.1);\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:enabled\n"
"{\n"
"    border-image: url(:/light/right_arrow.svg);\n"
"}\n"
"\n"
"QTabBar QToolButton::left-arrow:enabled\n"
"{\n"
"    border-image: url(:/light/left_arrow.svg);\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:disabled\n"
"{\n"
"    border-image: url(:/light/right_arrow_disabled.svg);\n"
"}\n"
"\n"
"QTabBar QToolButton::left-arrow:disabled\n"
"{\n"
"    border-image: url(:/light/left_arrow_disabled.svg);\n"
"}\n"
"\n"
"QDockWidget\n"
"{\n"
"    background: #EFF0F1;\n"
"    border: 0.1ex solid #403F3F;\n"
"    titlebar-close-icon: url(:/light/transparent.svg);\n"
"    titlebar-normal-icon: url(:/light/transparent.svg);\n"
"}\n"
"\n"
"QDockWidget::close-button,\n"
"QDockWidget::float-button\n"
"{\n"
"    border: 0.1ex solid transparent;\n"
"    border-radius: 0.2ex;\n"
"    background: transparent;\n"
"}\n"
"\n"
"\n"
"QDockWidget::float-button\n"
"{\n"
"    border-image: url(:/dark/undock.svg);\n"
"}\n"
"\n"
"QDockWidget::float-button:hover\n"
"{\n"
"    border-image: url(:/dark/undock-hover.svg) ;\n"
"}\n"
"\n"
"QDockWidget::close-button\n"
"{\n"
"    border-image: url(:/dark/close.svg) ;\n"
"}\n"
"\n"
"QDockWidget::close-button:hover\n"
"{\n"
"    border-image: url(:/dark/close-hover.svg) ;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed\n"
"{\n"
"    border-image: url(:/dark/close-pressed.svg) ;\n"
"}\n"
"\n"
"QTreeView,\n"
"QListView\n"
"{\n"
"    border: 0.1ex solid #BAB9B8;\n"
"    background-color: #FCFCFC;\n"
"}\n"
"\n"
"\n"
"QTreeView::branch:has-siblings:!adjoins-item\n"
"{\n"
"    border-image: url(:/light/stylesheet-vline.svg) 0;\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:adjoins-item\n"
"{\n"
"    border-image: url(:/light/stylesheet-branch-more.svg) 0;\n"
"}\n"
"\n"
"QTreeView::branch:!has-children:!has-siblings:adjoins-item\n"
"{\n"
"    border-image: url(:/light/stylesheet-branch-end.svg) 0;\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings\n"
"{\n"
"    border-image: url(:/light/stylesheet-branch-end-closed.svg) 0;\n"
"    image: url(:/light/branch_closed.svg);\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings\n"
"{\n"
"    border-image: url(:/light/stylesheet-branch-end-open.svg) 0;\n"
"    image: url(:/light/branch_open.svg);\n"
"}\n"
"\n"
"QTableView::item,\n"
"QListView::item,\n"
"QTreeView::item\n"
"{\n"
"    padding: 0.3ex;\n"
"}\n"
"\n"
"QTableView::item:!selected:hover,\n"
"QListView::item:!selected:hover,\n"
"QTreeView::item:!selected:hover\n"
"{\n"
"    background-color: rgba(61, 173, 232, 0.1);\n"
"    outline: 0;\n"
"    color: #31363B;\n"
"    padding: 0.3ex;\n"
"}\n"
"\n"
"QSlider::groove:horizontal\n"
"{\n"
"    border: 0.1ex solid #EFF0F1;\n"
"    height: 0.4ex;\n"
"    background: #9CA0A4;\n"
"    margin: 0px;\n"
"    border-radius: 0.2ex;\n"
"}\n"
"\n"
"QSlider::handle:horizontal\n"
"{\n"
"    background: #D9D8D7;\n"
"    border: 0.1ex solid #BABEC2;\n"
"    width: 1.6ex;\n"
"    height: 1.6ex;\n"
"    margin: -0.8ex 0;\n"
"    border-radius: 0.9ex;\n"
"}\n"
"\n"
"QSlider::groove:vertical\n"
"{\n"
"    border: 0.1ex solid #EFF0F1;\n"
"    width: 0.4ex;\n"
"    background: #9CA0A4;\n"
"    margin: 0ex;\n"
"    border-radius: 0.3ex;\n"
"}\n"
"\n"
"QSlider::handle:vertical\n"
"{\n"
"    background: #D9D8D7;\n"
"    border: 0.1ex solid #BABEC2;\n"
"    width: 1.6ex;\n"
"    height: 1.6ex;\n"
"    margin: 0 -0.8ex;\n"
"    border-radius: 0.9ex;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:focus,\n"
"QSlider::handle:vertical:focus\n"
"{\n"
"    border: 0.1ex solid #33A4DF;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover,\n"
"QSlider::handle:vertical:hover\n"
"{\n"
"    border: 0.1ex solid #51c2fc;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal,\n"
"QSlider::add-page:vertical\n"
"{\n"
"    background: #33A4DF;\n"
"    border-radius: 0.3ex;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal,\n"
"QSlider::sub-page:vertical\n"
"{\n"
"    background: #BABEC2;\n"
"    border-radius: 0.3ex;\n"
"}\n"
"\n"
"QToolButton\n"
"{\n"
"    background-color: transparent;\n"
"    border: 0.1ex solid #BAB9B8;\n"
"    border-radius: 0.2ex;\n"
"    margin: 0.3ex;\n"
"    padding: 0.5ex;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"] /* only for MenuButtonPopup */\n"
"{\n"
"    padding-right: 2ex; /* make way for the popup button */\n"
"}\n"
"\n"
"QToolButton[popupMode=\"2\"] /* only for InstantPopup */\n"
"{\n"
"    padding-right: 1ex; /* make way for the popup button */\n"
"}\n"
"\n"
"QToolButton::menu-indicator\n"
"{\n"
"    border-image: url(:/light/down_arrow.svg);\n"
"    top: -0.7ex; left: -0.2ex; /* shift it a bit */\n"
"    width = 0.9ex;\n"
"    height = 0.6ex;\n"
"}\n"
"\n"
"QToolButton::menu-arrow\n"
"{\n"
"    border-image: url(:/light/down_arrow.svg);\n"
"    width = 0.9ex;\n"
"    height = 0.6ex;\n"
"}\n"
"\n"
"QToolButton:hover,\n"
"QToolButton::menu-button:hover\n"
"{\n"
"    background-color: transparent;\n"
"    border: 0.1ex solid #33A4DF;\n"
"}\n"
"\n"
"QToolButton:checked,\n"
"QToolButton:pressed,\n"
"QToolButton::menu-button:pressed\n"
"{\n"
"    background-color: #47b8fc;\n"
"    border: 0.1ex solid #47b8fc;\n"
"    padding: 0.5ex;\n"
"}\n"
"\n"
"QToolButton::menu-button\n"
"{\n"
"    border: 0.1ex solid #BAB9B8;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"    /* 1ex width + 0.4ex for border + no text = 2ex allocated above */\n"
"    width: 1ex;\n"
"    padding: 0.5ex;\n"
"    outline: none;\n"
"}\n"
"\n"
"QToolButton::menu-arrow:open\n"
"{\n"
"    border: 0.1ex solid #BAB9B8;\n"
"}\n"
"\n"
"QPushButton::menu-indicator\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: bottom right;\n"
"    left: 0.8ex;\n"
"}\n"
"\n"
"QTableView\n"
"{\n"
"    border: 0.1ex solid #BAB9B8;\n"
"    gridline-color: #BAB9B8;\n"
"    background-color: #FCFCFC;\n"
"}\n"
"\n"
"\n"
"QTableView,\n"
"QHeaderView\n"
"{\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QTableView::item:pressed\n"
"{\n"
"    background: #33A4DF;\n"
"    color: #31363B;\n"
"}\n"
"\n"
"QTableView::item:selected:active\n"
"{\n"
"    background: #33A4DF;\n"
"    color: #31363B;\n"
"}\n"
"\n"
"QTableView::item:selected:hover\n"
"{\n"
"    background-color: #47b8f3;\n"
"    color: #31363B;\n"
"}\n"
"\n"
"QListView::item:pressed,\n"
"QTreeView::item:pressed\n"
"{\n"
"    background: #3daee9;\n"
"    color: #31363B;\n"
"}\n"
"\n"
"QTreeView::item:selected:active,\n"
"QListView::item:selected:active\n"
"{\n"
"    background: #3daee9;\n"
"    color: #31363B;\n"
"}\n"
"\n"
"QListView::item:selected:hover,\n"
"QTreeView::item:selected:hover\n"
"{\n"
"    background-color: #51c2fc;\n"
"    color: #31363B;\n"
"}\n"
"\n"
"\n"
"QHeaderView\n"
"{\n"
"    background-color: #EFF0F1;\n"
"    border: 0.1ex transparent;\n"
"    border-radius: 0px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: #EFF0F1;\n"
"    color: #31363B;\n"
"    padding: 0.5ex;\n"
"    border: 0.1ex solid #BAB9B8;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QHeaderView::section::vertical::first,\n"
"QHeaderView::section::vertical::only-one\n"
"{\n"
"    border-top: 0.1ex solid #BAB9B8;\n"
"}\n"
"\n"
"QHeaderView::section::vertical\n"
"{\n"
"    border-top: transparent;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal::first, QHeaderView::section::horizontal::only-one\n"
"{\n"
"    border-left: 0.1ex solid #BAB9B8;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal\n"
"{\n"
"    border-left: transparent;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked\n"
"\n"
" {\n"
"    color: black;\n"
"    background-color: #b9dae7;\n"
" }\n"
"\n"
" /* style the sort indicator */\n"
"QHeaderView::down-arrow\n"
"{\n"
"    image: url(:/light/down_arrow.svg);\n"
"}\n"
"\n"
"QHeaderView::up-arrow\n"
"{\n"
"    image: url(:/light/up_arrow.svg);\n"
"}\n"
"\n"
"QTableCornerButton::section\n"
"{\n"
"    background-color: #EFF0F1;\n"
"    border: 0.1ex transparent #BAB9B8;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QToolBox\n"
"{\n"
"    padding: 0.5ex;\n"
"    border: 0.1ex transparent black;\n"
"}\n"
"\n"
"QToolBox:selected\n"
"{\n"
"    background-color: #EFF0F1;\n"
"    border-color: #33A4DF;\n"
"}\n"
"\n"
"QToolBox:hover\n"
"{\n"
"    border-color: #33A4DF;\n"
"}\n"
"\n"
"QStatusBar::item\n"
"{\n"
"    border: 0px transparent dark;\n"
"}\n"
"\n"
"QSplitter::handle\n"
"{\n"
"    border: 0.1ex dashed #BAB9B8;\n"
"}\n"
"\n"
"QSplitter::handle:hover\n"
"{\n"
"    background-color: #787876;\n"
"    border: 0.1ex solid #BAB9B8;\n"
"}\n"
"\n"
"QSplitter::handle:horizontal\n"
"{\n"
"    width: 0.1ex;\n"
"}\n"
"\n"
"QSplitter::handle:vertical\n"
"{\n"
"    height: 0.1ex;\n"
"}\n"
"\n"
"QProgressBar:horizontal\n"
"{\n"
"    background-color: #BABEC2;\n"
"    border: 0.1ex solid #EFF0F1;\n"
"    border-radius: 0.3ex;\n"
"    height: 0.5ex;\n"
"    text-align: right;\n"
"    margin-top: 0.5ex;\n"
"    margin-bottom: 0.5ex;\n"
"    margin-right: 5ex;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QProgressBar::chunk:horizontal\n"
"{\n"
"    background-color: #33A4DF;\n"
"    border: 0.1ex transparent;\n"
"    border-radius: 0.3ex;\n"
"}\n"
"\n"
"QAbstractSpinBox\n"
"{\n"
"    background-color: #EFF0F1;\n"
"}\n"
"\n"
"QSpinBox,\n"
"QDoubleSpinBox\n"
"{\n"
"    padding-right: 1.5ex;\n"
"}\n"
"\n"
"QSpinBox::up-button,\n"
"QDoubleSpinBox::up-button\n"
"{\n"
"    subcontrol-origin: content;\n"
"    subcontrol-position: right top;\n"
"\n"
"    width: 1.6ex;\n"
"    border-width: 0.1ex;\n"
"}\n"
"\n"
"QSpinBox::up-arrow,\n"
"QDoubleSpinBox::up-arrow\n"
"{\n"
"    border-image: url(:/light/up_arrow.svg);\n"
"    width: 0.9ex;\n"
"    height: 0.6ex;\n"
"}\n"
"\n"
"QSpinBox::up-arrow:hover,\n"
"QSpinBox::up-arrow:pressed,\n"
"QDoubleSpinBox::up-arrow:hover,\n"
"QDoubleSpinBox::up-arrow:pressed\n"
"{\n"
"    border-image: url(:/light/up_arrow-hover.svg);\n"
"    width: 0.9ex;\n"
"    height: 0.6ex;\n"
"}\n"
"\n"
"QSpinBox::up-arrow:disabled,\n"
"QSpinBox::up-arrow:off,\n"
"QDoubleSpinBox::up-arrow:disabled,\n"
"QDoubleSpinBox::up-arrow:off\n"
"{\n"
"   border-image: url(:/light/up_arrow_disabled.svg);\n"
"}\n"
"\n"
"QSpinBox::down-button,\n"
"QDoubleSpinBox::down-button\n"
"{\n"
"    subcontrol-origin: content;\n"
"    subcontrol-position: right bottom;\n"
"\n"
"    width: 1.6ex;\n"
"    border-width: 0.1ex;\n"
"}\n"
"\n"
"QSpinBox::down-arrow,\n"
"QDoubleSpinBox::down-arrow\n"
"{\n"
"    border-image: url(:/light/down_arrow.svg);\n"
"    width: 0.9ex;\n"
"    height: 0.6ex;\n"
"}\n"
"\n"
"QSpinBox::down-arrow:hover,\n"
"QSpinBox::down-arrow:pressed,\n"
"QDoubleSpinBox::down-arrow:hover,\n"
"QDoubleSpinBox::down-arrow:pressed\n"
"{\n"
"    border-image: url(:/light/down_arrow-hover.svg);\n"
"    width: 0.9ex;\n"
"    height: 0.6ex;\n"
"}\n"
"\n"
"QSpinBox::down-arrow:disabled,\n"
"QSpinBox::down-arrow:off,\n"
"QDoubleSpinBox::down-arrow:disabled,\n"
"QDoubleSpinBox::down-arrow:off\n"
"{\n"
"   border-image: url(:/light/down_arrow_disabled.svg);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    border: 0.1ex solid #3daef3;\n"
"    color: #31363B;\n"
"}\n"
"\n"
"QPushButton:focus\n"
"{\n"
"    background-color: qlineargradient(x1: 0.5, y1: 0.5 x2: 0.5, y2: 1, stop: 0 #4cbdff, stop: 0.5 #33a4e8);\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:focus:hover\n"
"{\n"
"    background-color: qlineargradient(x1: 0.5, y1: 0.5 x2: 0.5, y2: 1, stop: 0 #bedfec, stop: 0.5 #b9dae7);\n"
"    color: #31363B;\n"
"}\n"
"\n"
"QPushButton:focus:pressed,\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: qlineargradient(x1: 0.5, y1: 0.5 x2: 0.5, y2: 1, stop: 0 #bedfec, stop: 0.5 #b9dae7);\n"
"    color: #31363B;\n"
"}\n"
"\n"
"")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.pushButton_85 = QtWidgets.QPushButton(self.tab_8)
        self.pushButton_85.setGeometry(QtCore.QRect(270, 560, 170, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_85.setFont(font)
        self.pushButton_85.setIcon(icon9)
        self.pushButton_85.setIconSize(QtCore.QSize(22, 22))
        self.pushButton_85.setObjectName("pushButton_85")
        self.tabWidget_4.addTab(self.tab_8, "")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_11)
        self.textEdit_2.setGeometry(QtCore.QRect(100, 150, 700, 120))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_44 = QtWidgets.QLabel(self.tab_11)
        self.label_44.setGeometry(QtCore.QRect(670, 110, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_44.setFont(font)
        self.label_44.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(self.tab_11)
        self.label_45.setGeometry(QtCore.QRect(670, 290, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_45.setFont(font)
        self.label_45.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_45.setObjectName("label_45")
        self.textEdit_3 = QtWidgets.QTextEdit(self.tab_11)
        self.textEdit_3.setGeometry(QtCore.QRect(100, 330, 700, 120))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_46 = QtWidgets.QLabel(self.tab_11)
        self.label_46.setGeometry(QtCore.QRect(670, 470, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_46.setFont(font)
        self.label_46.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_46.setObjectName("label_46")
        self.textEdit_4 = QtWidgets.QTextEdit(self.tab_11)
        self.textEdit_4.setGeometry(QtCore.QRect(100, 510, 700, 120))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textEdit_4.setFont(font)
        self.textEdit_4.setObjectName("textEdit_4")
        self.pushButton_17 = QtWidgets.QPushButton(self.tab_11)
        self.pushButton_17.setGeometry(QtCore.QRect(730, 690, 190, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setAccessibleDescription("")
        self.pushButton_17.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_17.setIcon(icon5)
        self.pushButton_17.setIconSize(QtCore.QSize(100, 46))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_16 = QtWidgets.QPushButton(self.tab_11)
        self.pushButton_16.setGeometry(QtCore.QRect(30, 700, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setObjectName("pushButton_16")
        self.label_32 = QtWidgets.QLabel(self.tab_11)
        self.label_32.setGeometry(QtCore.QRect(250, 70, 330, 60))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("\n"
"QLabel\n"
"{\n"
"/*font: 75 16pt \"Arial Unicode MS\";*/\n"
"\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 17pt \"Hacen Maghreb Bd\";\n"
"\n"
"}")
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.tabWidget_4.addTab(self.tab_11, "")
        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.label_47 = QtWidgets.QLabel(self.tab_12)
        self.label_47.setGeometry(QtCore.QRect(320, 40, 320, 50))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_47.setFont(font)
        self.label_47.setStyleSheet("\n"
"QLabel\n"
"{\n"
"/*font: 75 16pt \"Arial Unicode MS\";*/\n"
"\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 17pt \"Hacen Maghreb Bd\";\n"
"\n"
"}")
        self.label_47.setAlignment(QtCore.Qt.AlignCenter)
        self.label_47.setObjectName("label_47")
        self.label_48 = QtWidgets.QLabel(self.tab_12)
        self.label_48.setGeometry(QtCore.QRect(660, 118, 140, 30))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_48.setFont(font)
        self.label_48.setStyleSheet("\n"
"QLabel\n"
"{\n"
"/*font: 75 16pt \"Arial Unicode MS\";*/\n"
"\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 17pt \"Hacen Maghreb Bd\";\n"
"\n"
"}")
        self.label_48.setObjectName("label_48")
        self.comboBox_6 = QtWidgets.QComboBox(self.tab_12)
        self.comboBox_6.setGeometry(QtCore.QRect(460, 118, 210, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_6.setFont(font)
        self.comboBox_6.setObjectName("comboBox_6")
        self.lineEdit_36 = QtWidgets.QLineEdit(self.tab_12)
        self.lineEdit_36.setGeometry(QtCore.QRect(200, 118, 240, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_36.setFont(font)
        self.lineEdit_36.setObjectName("lineEdit_36")
        self.label_49 = QtWidgets.QLabel(self.tab_12)
        self.label_49.setGeometry(QtCore.QRect(660, 198, 140, 40))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_49.setFont(font)
        self.label_49.setStyleSheet("\n"
"QLabel\n"
"{\n"
"/*font: 75 16pt \"Arial Unicode MS\";*/\n"
"\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 17pt \"Hacen Maghreb Bd\";\n"
"\n"
"}")
        self.label_49.setObjectName("label_49")
        self.lineEdit_37 = QtWidgets.QLineEdit(self.tab_12)
        self.lineEdit_37.setGeometry(QtCore.QRect(450, 198, 220, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_37.setFont(font)
        self.lineEdit_37.setPlaceholderText("")
        self.lineEdit_37.setObjectName("lineEdit_37")
        self.label_50 = QtWidgets.QLabel(self.tab_12)
        self.label_50.setGeometry(QtCore.QRect(310, 268, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_50.setFont(font)
        self.label_50.setStyleSheet("\n"
"QLabel\n"
"{\n"
"/*font: 75 16pt \"Arial Unicode MS\";*/\n"
"\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 17pt \"Hacen Maghreb Bd\";\n"
"\n"
"}")
        self.label_50.setAlignment(QtCore.Qt.AlignCenter)
        self.label_50.setObjectName("label_50")
        self.checkBox_3 = QtWidgets.QCheckBox(self.tab_12)
        self.checkBox_3.setGeometry(QtCore.QRect(650, 340, 170, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setStyleSheet("font: 75 13pt \"Arial Unicode MS\";")
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.tab_12)
        self.checkBox_4.setGeometry(QtCore.QRect(310, 340, 170, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setStyleSheet("font: 75 13pt \"Arial Unicode MS\";")
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.tab_12)
        self.checkBox_5.setGeometry(QtCore.QRect(480, 340, 170, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setStyleSheet("font: 75 13pt \"Arial Unicode MS\";")
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.tab_12)
        self.checkBox_6.setGeometry(QtCore.QRect(140, 340, 170, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setStyleSheet("font: 75 13pt \"Arial Unicode MS\";")
        self.checkBox_6.setObjectName("checkBox_6")
        self.label_51 = QtWidgets.QLabel(self.tab_12)
        self.label_51.setGeometry(QtCore.QRect(700, 430, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_51.setFont(font)
        self.label_51.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_51.setObjectName("label_51")
        self.textEdit_5 = QtWidgets.QTextEdit(self.tab_12)
        self.textEdit_5.setGeometry(QtCore.QRect(140, 470, 660, 100))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textEdit_5.setFont(font)
        self.textEdit_5.setObjectName("textEdit_5")
        self.pushButton_18 = QtWidgets.QPushButton(self.tab_12)
        self.pushButton_18.setGeometry(QtCore.QRect(32, 692, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_69 = QtWidgets.QPushButton(self.tab_12)
        self.pushButton_69.setGeometry(QtCore.QRect(205, 146, 91, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_69.setFont(font)
        self.pushButton_69.setStyleSheet("image: url(:/ico/removef.png);")
        self.pushButton_69.setText("")
        self.pushButton_69.setObjectName("pushButton_69")
        self.pushButton_70 = QtWidgets.QPushButton(self.tab_12)
        self.pushButton_70.setGeometry(QtCore.QRect(345, 146, 91, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_70.setFont(font)
        self.pushButton_70.setStyleSheet("image: url(:/ico/addf.png);")
        self.pushButton_70.setText("")
        self.pushButton_70.setObjectName("pushButton_70")
        self.pushButton_25 = QtWidgets.QPushButton(self.tab_12)
        self.pushButton_25.setGeometry(QtCore.QRect(732, 682, 190, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_25.setFont(font)
        self.pushButton_25.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_25.setIcon(icon5)
        self.pushButton_25.setIconSize(QtCore.QSize(62, 46))
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_70.raise_()
        self.pushButton_69.raise_()
        self.label_47.raise_()
        self.label_48.raise_()
        self.comboBox_6.raise_()
        self.lineEdit_36.raise_()
        self.label_49.raise_()
        self.lineEdit_37.raise_()
        self.label_50.raise_()
        self.checkBox_3.raise_()
        self.checkBox_4.raise_()
        self.checkBox_5.raise_()
        self.checkBox_6.raise_()
        self.label_51.raise_()
        self.textEdit_5.raise_()
        self.pushButton_18.raise_()
        self.pushButton_25.raise_()
        self.tabWidget_2.addTab(self.tab_12, "")
        self.tab_25 = QtWidgets.QWidget()
        self.tab_25.setObjectName("tab_25")
        self.label_116 = QtWidgets.QLabel(self.tab_25)
        self.label_116.setGeometry(QtCore.QRect(210, 190, 260, 30))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_116.setFont(font)
        self.label_116.setStyleSheet("\n"
"QLabel\n"
"{\n"
"/*font: 75 16pt \"Arial Unicode MS\";*/\n"
"\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 14pt \"Hacen Maghreb Bd\";\n"
"\n"
"}")
        self.label_116.setObjectName("label_116")
        self.label_117 = QtWidgets.QLabel(self.tab_25)
        self.label_117.setGeometry(QtCore.QRect(220, 270, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_117.setFont(font)
        self.label_117.setStyleSheet("\n"
"QLabel\n"
"{\n"
"/*font: 75 16pt \"Arial Unicode MS\";*/\n"
"\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 17pt \"Hacen Maghreb Bd\";\n"
"\n"
"}")
        self.label_117.setObjectName("label_117")
        self.label_118 = QtWidgets.QLabel(self.tab_25)
        self.label_118.setGeometry(QtCore.QRect(220, 350, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_118.setFont(font)
        self.label_118.setStyleSheet("\n"
"QLabel\n"
"{\n"
"/*font: 75 16pt \"Arial Unicode MS\";*/\n"
"\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 14pt \"Hacen Maghreb Bd\";\n"
"\n"
"}")
        self.label_118.setObjectName("label_118")
        self.label_119 = QtWidgets.QLabel(self.tab_25)
        self.label_119.setGeometry(QtCore.QRect(220, 430, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_119.setFont(font)
        self.label_119.setStyleSheet("\n"
"QLabel\n"
"{\n"
"/*font: 75 16pt \"Arial Unicode MS\";*/\n"
"\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 14pt \"Hacen Maghreb Bd\";\n"
"\n"
"}")
        self.label_119.setObjectName("label_119")
        self.label_120 = QtWidgets.QLabel(self.tab_25)
        self.label_120.setGeometry(QtCore.QRect(720, 190, 270, 30))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_120.setFont(font)
        self.label_120.setStyleSheet("\n"
"QLabel\n"
"{\n"
"/*font: 75 16pt \"Arial Unicode MS\";*/\n"
"\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 14pt \"Hacen Maghreb Bd\";\n"
"\n"
"}")
        self.label_120.setObjectName("label_120")
        self.label_121 = QtWidgets.QLabel(self.tab_25)
        self.label_121.setGeometry(QtCore.QRect(730, 270, 260, 30))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_121.setFont(font)
        self.label_121.setStyleSheet("\n"
"QLabel\n"
"{\n"
"/*font: 75 16pt \"Arial Unicode MS\";*/\n"
"\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 14pt \"Hacen Maghreb Bd\";\n"
"\n"
"}")
        self.label_121.setObjectName("label_121")
        self.label_122 = QtWidgets.QLabel(self.tab_25)
        self.label_122.setGeometry(QtCore.QRect(700, 430, 290, 30))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_122.setFont(font)
        self.label_122.setStyleSheet("\n"
"QLabel\n"
"{\n"
"/*font: 75 16pt \"Arial Unicode MS\";*/\n"
"\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 14pt \"Hacen Maghreb Bd\";\n"
"\n"
"}")
        self.label_122.setObjectName("label_122")
        self.label_123 = QtWidgets.QLabel(self.tab_25)
        self.label_123.setGeometry(QtCore.QRect(730, 350, 260, 30))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_123.setFont(font)
        self.label_123.setStyleSheet("\n"
"QLabel\n"
"{\n"
"/*font: 75 16pt \"Arial Unicode MS\";*/\n"
"\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 14pt \"Hacen Maghreb Bd\";\n"
"\n"
"}")
        self.label_123.setObjectName("label_123")
        self.lineEdit_58 = QtWidgets.QLineEdit(self.tab_25)
        self.lineEdit_58.setGeometry(QtCore.QRect(520, 190, 230, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_58.setFont(font)
        self.lineEdit_58.setObjectName("lineEdit_58")
        self.lineEdit_59 = QtWidgets.QLineEdit(self.tab_25)
        self.lineEdit_59.setGeometry(QtCore.QRect(520, 270, 230, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_59.setFont(font)
        self.lineEdit_59.setObjectName("lineEdit_59")
        self.lineEdit_60 = QtWidgets.QLineEdit(self.tab_25)
        self.lineEdit_60.setGeometry(QtCore.QRect(520, 350, 230, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_60.setFont(font)
        self.lineEdit_60.setObjectName("lineEdit_60")
        self.lineEdit_61 = QtWidgets.QLineEdit(self.tab_25)
        self.lineEdit_61.setGeometry(QtCore.QRect(520, 430, 230, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_61.setFont(font)
        self.lineEdit_61.setObjectName("lineEdit_61")
        self.lineEdit_62 = QtWidgets.QLineEdit(self.tab_25)
        self.lineEdit_62.setGeometry(QtCore.QRect(70, 190, 230, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_62.setFont(font)
        self.lineEdit_62.setObjectName("lineEdit_62")
        self.lineEdit_63 = QtWidgets.QLineEdit(self.tab_25)
        self.lineEdit_63.setGeometry(QtCore.QRect(70, 270, 230, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_63.setFont(font)
        self.lineEdit_63.setObjectName("lineEdit_63")
        self.lineEdit_64 = QtWidgets.QLineEdit(self.tab_25)
        self.lineEdit_64.setGeometry(QtCore.QRect(70, 350, 230, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_64.setFont(font)
        self.lineEdit_64.setObjectName("lineEdit_64")
        self.lineEdit_65 = QtWidgets.QLineEdit(self.tab_25)
        self.lineEdit_65.setGeometry(QtCore.QRect(70, 430, 230, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_65.setFont(font)
        self.lineEdit_65.setObjectName("lineEdit_65")
        self.label_124 = QtWidgets.QLabel(self.tab_25)
        self.label_124.setGeometry(QtCore.QRect(700, 510, 290, 30))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_124.setFont(font)
        self.label_124.setStyleSheet("\n"
"QLabel\n"
"{\n"
"/*font: 75 16pt \"Arial Unicode MS\";*/\n"
"\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 14pt \"Hacen Maghreb Bd\";\n"
"\n"
"}")
        self.label_124.setObjectName("label_124")
        self.lineEdit_83 = QtWidgets.QLineEdit(self.tab_25)
        self.lineEdit_83.setGeometry(QtCore.QRect(520, 510, 230, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_83.setFont(font)
        self.lineEdit_83.setObjectName("lineEdit_83")
        self.label_125 = QtWidgets.QLabel(self.tab_25)
        self.label_125.setGeometry(QtCore.QRect(180, 510, 290, 30))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_125.setFont(font)
        self.label_125.setStyleSheet("\n"
"QLabel\n"
"{\n"
"/*font: 75 16pt \"Arial Unicode MS\";*/\n"
"\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 14pt \"Hacen Maghreb Bd\";\n"
"\n"
"}")
        self.label_125.setObjectName("label_125")
        self.lineEdit_84 = QtWidgets.QLineEdit(self.tab_25)
        self.lineEdit_84.setGeometry(QtCore.QRect(70, 510, 230, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_84.setFont(font)
        self.lineEdit_84.setObjectName("lineEdit_84")
        self.label_74 = QtWidgets.QLabel(self.tab_25)
        self.label_74.setGeometry(QtCore.QRect(350, 60, 320, 50))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_74.setFont(font)
        self.label_74.setStyleSheet("\n"
"QLabel\n"
"{\n"
"/*font: 75 16pt \"Arial Unicode MS\";*/\n"
"\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 17pt \"Hacen Maghreb Bd\";\n"
"\n"
"}")
        self.label_74.setAlignment(QtCore.Qt.AlignCenter)
        self.label_74.setObjectName("label_74")
        self.pushButton_54 = QtWidgets.QPushButton(self.tab_25)
        self.pushButton_54.setGeometry(QtCore.QRect(32, 692, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_54.setFont(font)
        self.pushButton_54.setObjectName("pushButton_54")
        self.pushButton_77 = QtWidgets.QPushButton(self.tab_25)
        self.pushButton_77.setGeometry(QtCore.QRect(360, 630, 300, 70))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_77.setFont(font)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/ico/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_77.setIcon(icon10)
        self.pushButton_77.setIconSize(QtCore.QSize(45, 45))
        self.pushButton_77.setObjectName("pushButton_77")
        self.tabWidget_2.addTab(self.tab_25, "")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_15 = QtWidgets.QWidget()
        self.tab_15.setObjectName("tab_15")
        self.tabWidget_5 = QtWidgets.QTabWidget(self.tab_15)
        self.tabWidget_5.setGeometry(QtCore.QRect(0, -10, 1020, 1020))
        self.tabWidget_5.setStyleSheet("QPushButton\n"
"{\n"
"    color: #fff;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 40px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: rgb(139, 139, 139)\n"
"}\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    border: 1px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #00aaff, stop: 1 #00aaff);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QLineEdit {\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"\n"
"}\n"
"QLineEdit::hover\n"
"{\n"
"    border: 1px solid rgb(0, 170, 255);\n"
"    border-radius: 2px;\n"
"    color: rgb(0, 115, 255);\n"
"    border-radius: 6;\n"
"\n"
"\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: rgb(85, 190, 255);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"\n"
"")
        self.tabWidget_5.setObjectName("tabWidget_5")
        self.tab_16 = QtWidgets.QWidget()
        self.tab_16.setObjectName("tab_16")
        self.label_60 = QtWidgets.QLabel(self.tab_16)
        self.label_60.setGeometry(QtCore.QRect(530, 170, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_60.setFont(font)
        self.label_60.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_60.setAlignment(QtCore.Qt.AlignCenter)
        self.label_60.setObjectName("label_60")
        self.lineEdit_42 = QtWidgets.QLineEdit(self.tab_16)
        self.lineEdit_42.setGeometry(QtCore.QRect(530, 340, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_42.setFont(font)
        self.lineEdit_42.setObjectName("lineEdit_42")
        self.lineEdit_43 = QtWidgets.QLineEdit(self.tab_16)
        self.lineEdit_43.setGeometry(QtCore.QRect(130, 460, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_43.setFont(font)
        self.lineEdit_43.setText("")
        self.lineEdit_43.setObjectName("lineEdit_43")
        self.lineEdit_44 = QtWidgets.QLineEdit(self.tab_16)
        self.lineEdit_44.setGeometry(QtCore.QRect(130, 340, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_44.setFont(font)
        self.lineEdit_44.setText("")
        self.lineEdit_44.setObjectName("lineEdit_44")
        self.lineEdit_46 = QtWidgets.QLineEdit(self.tab_16)
        self.lineEdit_46.setGeometry(QtCore.QRect(530, 520, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_46.setFont(font)
        self.lineEdit_46.setObjectName("lineEdit_46")
        self.lineEdit_47 = QtWidgets.QLineEdit(self.tab_16)
        self.lineEdit_47.setGeometry(QtCore.QRect(130, 400, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_47.setFont(font)
        self.lineEdit_47.setText("")
        self.lineEdit_47.setObjectName("lineEdit_47")
        self.lineEdit_48 = QtWidgets.QLineEdit(self.tab_16)
        self.lineEdit_48.setGeometry(QtCore.QRect(130, 280, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_48.setFont(font)
        self.lineEdit_48.setText("")
        self.lineEdit_48.setObjectName("lineEdit_48")
        self.lineEdit_49 = QtWidgets.QLineEdit(self.tab_16)
        self.lineEdit_49.setGeometry(QtCore.QRect(530, 220, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_49.setFont(font)
        self.lineEdit_49.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_49.setObjectName("lineEdit_49")
        self.lineEdit_50 = QtWidgets.QLineEdit(self.tab_16)
        self.lineEdit_50.setGeometry(QtCore.QRect(530, 280, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_50.setFont(font)
        self.lineEdit_50.setObjectName("lineEdit_50")
        self.label_61 = QtWidgets.QLabel(self.tab_16)
        self.label_61.setGeometry(QtCore.QRect(130, 170, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_61.setFont(font)
        self.label_61.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_61.setAlignment(QtCore.Qt.AlignCenter)
        self.label_61.setObjectName("label_61")
        self.lineEdit_51 = QtWidgets.QLineEdit(self.tab_16)
        self.lineEdit_51.setGeometry(QtCore.QRect(130, 220, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_51.setFont(font)
        self.lineEdit_51.setText("")
        self.lineEdit_51.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_51.setObjectName("lineEdit_51")
        self.lineEdit_53 = QtWidgets.QLineEdit(self.tab_16)
        self.lineEdit_53.setGeometry(QtCore.QRect(530, 400, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_53.setFont(font)
        self.lineEdit_53.setObjectName("lineEdit_53")
        self.lineEdit_54 = QtWidgets.QLineEdit(self.tab_16)
        self.lineEdit_54.setGeometry(QtCore.QRect(530, 460, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_54.setFont(font)
        self.lineEdit_54.setObjectName("lineEdit_54")
        self.lineEdit_56 = QtWidgets.QLineEdit(self.tab_16)
        self.lineEdit_56.setGeometry(QtCore.QRect(130, 520, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_56.setFont(font)
        self.lineEdit_56.setText("")
        self.lineEdit_56.setObjectName("lineEdit_56")
        self.pushButton_27 = QtWidgets.QPushButton(self.tab_16)
        self.pushButton_27.setGeometry(QtCore.QRect(732, 682, 190, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_27.setFont(font)
        self.pushButton_27.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_27.setIcon(icon5)
        self.pushButton_27.setIconSize(QtCore.QSize(100, 46))
        self.pushButton_27.setObjectName("pushButton_27")
        self.lineEdit_57 = QtWidgets.QLineEdit(self.tab_16)
        self.lineEdit_57.setGeometry(QtCore.QRect(210, 110, 230, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_57.setFont(font)
        self.lineEdit_57.setObjectName("lineEdit_57")
        self.pushButton_52 = QtWidgets.QPushButton(self.tab_16)
        self.pushButton_52.setGeometry(QtCore.QRect(630, 110, 80, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_52.setFont(font)
        self.pushButton_52.setObjectName("pushButton_52")
        self.comboBox_13 = QtWidgets.QComboBox(self.tab_16)
        self.comboBox_13.setGeometry(QtCore.QRect(450, 110, 170, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_13.setFont(font)
        self.comboBox_13.setObjectName("comboBox_13")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.lineEdit_79 = QtWidgets.QLineEdit(self.tab_16)
        self.lineEdit_79.setGeometry(QtCore.QRect(390, 580, 130, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_79.setFont(font)
        self.lineEdit_79.setText("")
        self.lineEdit_79.setObjectName("lineEdit_79")
        self.pushButton_63 = QtWidgets.QPushButton(self.tab_16)
        self.pushButton_63.setGeometry(QtCore.QRect(457, 616, 60, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_63.setFont(font)
        self.pushButton_63.setStyleSheet("image: url(:/ico/addf.png);")
        self.pushButton_63.setText("")
        self.pushButton_63.setObjectName("pushButton_63")
        self.comboBox_17 = QtWidgets.QComboBox(self.tab_16)
        self.comboBox_17.setGeometry(QtCore.QRect(530, 580, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_17.setFont(font)
        self.comboBox_17.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_17.setObjectName("comboBox_17")
        self.pushButton_64 = QtWidgets.QPushButton(self.tab_16)
        self.pushButton_64.setGeometry(QtCore.QRect(393, 616, 60, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_64.setFont(font)
        self.pushButton_64.setStyleSheet("image: url(:/ico/removef.png);")
        self.pushButton_64.setText("")
        self.pushButton_64.setObjectName("pushButton_64")
        self.label_108 = QtWidgets.QLabel(self.tab_16)
        self.label_108.setGeometry(QtCore.QRect(790, 580, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_108.setFont(font)
        self.label_108.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_108.setObjectName("label_108")
        self.comboBox_18 = QtWidgets.QComboBox(self.tab_16)
        self.comboBox_18.setGeometry(QtCore.QRect(130, 580, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_18.setFont(font)
        self.comboBox_18.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_18.setObjectName("comboBox_18")
        self.pushButton_84 = QtWidgets.QPushButton(self.tab_16)
        self.pushButton_84.setGeometry(QtCore.QRect(362, 682, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_84.setFont(font)
        self.pushButton_84.setIcon(icon10)
        self.pushButton_84.setIconSize(QtCore.QSize(31, 31))
        self.pushButton_84.setObjectName("pushButton_84")
        self.pushButton_130 = QtWidgets.QPushButton(self.tab_16)
        self.pushButton_130.setGeometry(QtCore.QRect(830, 50, 160, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_130.setFont(font)
        self.pushButton_130.setObjectName("pushButton_130")
        self.progressBar = QtWidgets.QProgressBar(self.tab_16)
        self.progressBar.setGeometry(QtCore.QRect(840, 90, 140, 20))
        self.progressBar.setStyleSheet("QProgressBar {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  color: #F0F0F0;\n"
"  border-radius: 4px;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QProgressBar:disabled {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  color: #787878;\n"
"  border-radius: 4px;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"  background-color:  rgb(236, 185, 0);\n"
"  color: #19232D;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QProgressBar::chunk:disabled {\n"
"  background-color: rgb(87, 177, 255);\n"
"  color: #787878;\n"
"  border-radius: 4px;\n"
"}\n"
"")
        self.progressBar.setProperty("value", 100)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")
        self.pushButton_63.raise_()
        self.pushButton_64.raise_()
        self.label_60.raise_()
        self.lineEdit_42.raise_()
        self.lineEdit_43.raise_()
        self.lineEdit_44.raise_()
        self.lineEdit_46.raise_()
        self.lineEdit_47.raise_()
        self.lineEdit_48.raise_()
        self.lineEdit_49.raise_()
        self.lineEdit_50.raise_()
        self.label_61.raise_()
        self.lineEdit_51.raise_()
        self.lineEdit_53.raise_()
        self.lineEdit_54.raise_()
        self.lineEdit_56.raise_()
        self.pushButton_27.raise_()
        self.lineEdit_57.raise_()
        self.pushButton_52.raise_()
        self.comboBox_13.raise_()
        self.lineEdit_79.raise_()
        self.comboBox_17.raise_()
        self.label_108.raise_()
        self.comboBox_18.raise_()
        self.pushButton_84.raise_()
        self.progressBar.raise_()
        self.pushButton_130.raise_()
        self.tabWidget_5.addTab(self.tab_16, "")
        self.tab_17 = QtWidgets.QWidget()
        self.tab_17.setObjectName("tab_17")
        self.pushButton_28 = QtWidgets.QPushButton(self.tab_17)
        self.pushButton_28.setGeometry(QtCore.QRect(32, 692, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_28.setFont(font)
        self.pushButton_28.setObjectName("pushButton_28")
        self.pushButton_29 = QtWidgets.QPushButton(self.tab_17)
        self.pushButton_29.setGeometry(QtCore.QRect(732, 682, 190, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_29.setFont(font)
        self.pushButton_29.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_29.setIcon(icon5)
        self.pushButton_29.setIconSize(QtCore.QSize(100, 46))
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_117 = QtWidgets.QPushButton(self.tab_17)
        self.pushButton_117.setGeometry(QtCore.QRect(140, 580, 52, 30))
        self.pushButton_117.setStyleSheet("image: url(:/ico/removef.png);")
        self.pushButton_117.setText("")
        self.pushButton_117.setObjectName("pushButton_117")
        self.comboBox_7 = QtWidgets.QComboBox(self.tab_17)
        self.comboBox_7.setGeometry(QtCore.QRect(550, 580, 220, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBox_7.setFont(font)
        self.comboBox_7.setObjectName("comboBox_7")
        self.lineEdit_106 = QtWidgets.QLineEdit(self.tab_17)
        self.lineEdit_106.setGeometry(QtCore.QRect(530, 260, 240, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_106.setFont(font)
        self.lineEdit_106.setObjectName("lineEdit_106")
        self.textEdit_6 = QtWidgets.QTextEdit(self.tab_17)
        self.textEdit_6.setGeometry(QtCore.QRect(140, 60, 630, 80))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textEdit_6.setFont(font)
        self.textEdit_6.setObjectName("textEdit_6")
        self.comboBox_9 = QtWidgets.QComboBox(self.tab_17)
        self.comboBox_9.setGeometry(QtCore.QRect(530, 160, 240, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBox_9.setFont(font)
        self.comboBox_9.setObjectName("comboBox_9")
        self.lineEdit_105 = QtWidgets.QLineEdit(self.tab_17)
        self.lineEdit_105.setGeometry(QtCore.QRect(550, 630, 220, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_105.setFont(font)
        self.lineEdit_105.setPlaceholderText("")
        self.lineEdit_105.setObjectName("lineEdit_105")
        self.pushButton_113 = QtWidgets.QPushButton(self.tab_17)
        self.pushButton_113.setGeometry(QtCore.QRect(130, 160, 75, 30))
        self.pushButton_113.setStyleSheet("image: url(:/ico/addf.png);")
        self.pushButton_113.setText("")
        self.pushButton_113.setObjectName("pushButton_113")
        self.pushButton_33 = QtWidgets.QPushButton(self.tab_17)
        self.pushButton_33.setGeometry(QtCore.QRect(70, 210, 52, 30))
        self.pushButton_33.setStyleSheet("image: url(:/ico/removef.png);")
        self.pushButton_33.setText("")
        self.pushButton_33.setObjectName("pushButton_33")
        self.label_42 = QtWidgets.QLabel(self.tab_17)
        self.label_42.setGeometry(QtCore.QRect(780, 630, 170, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_42.setFont(font)
        self.label_42.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_42.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_42.setObjectName("label_42")
        self.label_39 = QtWidgets.QLabel(self.tab_17)
        self.label_39.setGeometry(QtCore.QRect(790, 210, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_39.setFont(font)
        self.label_39.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_39.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_39.setObjectName("label_39")
        self.lineEdit_107 = QtWidgets.QLineEdit(self.tab_17)
        self.lineEdit_107.setGeometry(QtCore.QRect(220, 210, 290, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_107.setFont(font)
        self.lineEdit_107.setObjectName("lineEdit_107")
        self.label_38 = QtWidgets.QLabel(self.tab_17)
        self.label_38.setGeometry(QtCore.QRect(780, 160, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_38.setFont(font)
        self.label_38.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_38.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_38.setObjectName("label_38")
        self.label_36 = QtWidgets.QLabel(self.tab_17)
        self.label_36.setGeometry(QtCore.QRect(780, 370, 160, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_36.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_36.setObjectName("label_36")
        self.pushButton_114 = QtWidgets.QPushButton(self.tab_17)
        self.pushButton_114.setGeometry(QtCore.QRect(200, 580, 75, 30))
        self.pushButton_114.setStyleSheet("image: url(:/ico/addf.png);")
        self.pushButton_114.setText("")
        self.pushButton_114.setObjectName("pushButton_114")
        self.lineEdit_102 = QtWidgets.QLineEdit(self.tab_17)
        self.lineEdit_102.setGeometry(QtCore.QRect(200, 630, 220, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_102.setFont(font)
        self.lineEdit_102.setPlaceholderText("")
        self.lineEdit_102.setObjectName("lineEdit_102")
        self.lineEdit_104 = QtWidgets.QLineEdit(self.tab_17)
        self.lineEdit_104.setGeometry(QtCore.QRect(220, 160, 290, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_104.setFont(font)
        self.lineEdit_104.setObjectName("lineEdit_104")
        self.label_35 = QtWidgets.QLabel(self.tab_17)
        self.label_35.setGeometry(QtCore.QRect(790, 450, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_35.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_35.setObjectName("label_35")
        self.lineEdit_108 = QtWidgets.QLineEdit(self.tab_17)
        self.lineEdit_108.setGeometry(QtCore.QRect(290, 580, 240, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_108.setFont(font)
        self.lineEdit_108.setObjectName("lineEdit_108")
        self.lineEdit_103 = QtWidgets.QLineEdit(self.tab_17)
        self.lineEdit_103.setGeometry(QtCore.QRect(530, 310, 240, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_103.setFont(font)
        self.lineEdit_103.setObjectName("lineEdit_103")
        self.label_34 = QtWidgets.QLabel(self.tab_17)
        self.label_34.setGeometry(QtCore.QRect(430, 630, 60, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_34.setObjectName("label_34")
        self.label_33 = QtWidgets.QLabel(self.tab_17)
        self.label_33.setGeometry(QtCore.QRect(780, 260, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_33.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_33.setObjectName("label_33")
        self.pushButton_115 = QtWidgets.QPushButton(self.tab_17)
        self.pushButton_115.setGeometry(QtCore.QRect(130, 210, 75, 30))
        self.pushButton_115.setStyleSheet("image: url(:/ico/addf.png);")
        self.pushButton_115.setText("")
        self.pushButton_115.setObjectName("pushButton_115")
        self.comboBox_8 = QtWidgets.QComboBox(self.tab_17)
        self.comboBox_8.setGeometry(QtCore.QRect(530, 210, 240, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBox_8.setFont(font)
        self.comboBox_8.setObjectName("comboBox_8")
        self.label_37 = QtWidgets.QLabel(self.tab_17)
        self.label_37.setGeometry(QtCore.QRect(790, 580, 170, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_37.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_37.setObjectName("label_37")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_17)
        self.groupBox_2.setGeometry(QtCore.QRect(330, 370, 440, 50))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton_17 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_17.setGeometry(QtCore.QRect(250, 10, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.radioButton_17.setFont(font)
        self.radioButton_17.setObjectName("radioButton_17")
        self.radioButton_18 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_18.setGeometry(QtCore.QRect(360, 10, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.radioButton_18.setFont(font)
        self.radioButton_18.setObjectName("radioButton_18")
        self.radioButton_19 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_19.setGeometry(QtCore.QRect(140, 10, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.radioButton_19.setFont(font)
        self.radioButton_19.setObjectName("radioButton_19")
        self.radioButton_20 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_20.setGeometry(QtCore.QRect(30, 10, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.radioButton_20.setFont(font)
        self.radioButton_20.setObjectName("radioButton_20")
        self.label_41 = QtWidgets.QLabel(self.tab_17)
        self.label_41.setGeometry(QtCore.QRect(780, 310, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_41.setFont(font)
        self.label_41.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_41.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_41.setObjectName("label_41")
        self.label_40 = QtWidgets.QLabel(self.tab_17)
        self.label_40.setGeometry(QtCore.QRect(780, 60, 160, 80))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_40.setFont(font)
        self.label_40.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_40.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_40.setObjectName("label_40")
        self.pushButton_116 = QtWidgets.QPushButton(self.tab_17)
        self.pushButton_116.setGeometry(QtCore.QRect(70, 160, 52, 30))
        self.pushButton_116.setStyleSheet("image: url(:/ico/removef.png);")
        self.pushButton_116.setText("")
        self.pushButton_116.setObjectName("pushButton_116")
        self.pushButton_118 = QtWidgets.QPushButton(self.tab_17)
        self.pushButton_118.setGeometry(QtCore.QRect(362, 682, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_118.setFont(font)
        self.pushButton_118.setIcon(icon10)
        self.pushButton_118.setIconSize(QtCore.QSize(31, 31))
        self.pushButton_118.setObjectName("pushButton_118")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_17)
        self.groupBox_4.setGeometry(QtCore.QRect(290, 440, 480, 120))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.lineEdit_101 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_101.setEnabled(False)
        self.lineEdit_101.setGeometry(QtCore.QRect(40, 60, 430, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_101.setFont(font)
        self.lineEdit_101.setObjectName("lineEdit_101")
        self.radioButton_7 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_7.setGeometry(QtCore.QRect(20, 10, 450, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.radioButton_7.setFont(font)
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_8 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_8.setGeometry(QtCore.QRect(20, 60, 400, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_8.setFont(font)
        self.radioButton_8.setText("")
        self.radioButton_8.setObjectName("radioButton_8")
        self.radioButton_8.raise_()
        self.lineEdit_101.raise_()
        self.radioButton_7.raise_()
        self.tabWidget_5.addTab(self.tab_17, "")
        self.tab_18 = QtWidgets.QWidget()
        self.tab_18.setObjectName("tab_18")
        self.tabWidget_6 = QtWidgets.QTabWidget(self.tab_18)
        self.tabWidget_6.setGeometry(QtCore.QRect(0, -10, 1250, 960))
        self.tabWidget_6.setStyleSheet("\n"
"QLabel\n"
"{\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 14pt \"Hacen Maghreb Bd\";\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #fff;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 40px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: rgb(139, 139, 139)\n"
"}\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    border: 1px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #00aaff, stop: 1 #00aaff);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QLineEdit {\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"\n"
"}\n"
"QLineEdit::hover\n"
"{\n"
"    border: 1px solid rgb(0, 170, 255);\n"
"    border-radius: 2px;\n"
"    color: rgb(0, 115, 255);\n"
"    border-radius: 6;\n"
"\n"
"\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: rgb(85, 190, 255);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"\n"
"")
        self.tabWidget_6.setObjectName("tabWidget_6")
        self.tab_19 = QtWidgets.QWidget()
        self.tab_19.setObjectName("tab_19")
        self.lineEdit_66 = QtWidgets.QLineEdit(self.tab_19)
        self.lineEdit_66.setGeometry(QtCore.QRect(280, 420, 330, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_66.setFont(font)
        self.lineEdit_66.setText("")
        self.lineEdit_66.setObjectName("lineEdit_66")
        self.lineEdit_67 = QtWidgets.QLineEdit(self.tab_19)
        self.lineEdit_67.setGeometry(QtCore.QRect(280, 480, 330, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_67.setFont(font)
        self.lineEdit_67.setText("")
        self.lineEdit_67.setObjectName("lineEdit_67")
        self.lineEdit_68 = QtWidgets.QLineEdit(self.tab_19)
        self.lineEdit_68.setGeometry(QtCore.QRect(280, 250, 330, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_68.setFont(font)
        self.lineEdit_68.setText("")
        self.lineEdit_68.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_68.setObjectName("lineEdit_68")
        self.checkBox_7 = QtWidgets.QCheckBox(self.tab_19)
        self.checkBox_7.setGeometry(QtCore.QRect(310, 710, 290, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.checkBox_7.setFont(font)
        self.checkBox_7.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.checkBox_7.setIcon(icon6)
        self.checkBox_7.setIconSize(QtCore.QSize(12, 171))
        self.checkBox_7.setObjectName("checkBox_7")
        self.comboBox_10 = QtWidgets.QComboBox(self.tab_19)
        self.comboBox_10.setGeometry(QtCore.QRect(280, 370, 170, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_10.setFont(font)
        self.comboBox_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_10.setObjectName("comboBox_10")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.label_73 = QtWidgets.QLabel(self.tab_19)
        self.label_73.setGeometry(QtCore.QRect(440, 370, 170, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_73.setFont(font)
        self.label_73.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_73.setObjectName("label_73")
        self.lineEdit_70 = QtWidgets.QLineEdit(self.tab_19)
        self.lineEdit_70.setGeometry(QtCore.QRect(280, 310, 330, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_70.setFont(font)
        self.lineEdit_70.setText("")
        self.lineEdit_70.setObjectName("lineEdit_70")
        self.pushButton_34 = QtWidgets.QPushButton(self.tab_19)
        self.pushButton_34.setGeometry(QtCore.QRect(360, 670, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_34.setFont(font)
        self.pushButton_34.setIcon(icon10)
        self.pushButton_34.setIconSize(QtCore.QSize(31, 31))
        self.pushButton_34.setObjectName("pushButton_34")
        self.pushButton_35 = QtWidgets.QPushButton(self.tab_19)
        self.pushButton_35.setGeometry(QtCore.QRect(30, 700, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_35.setFont(font)
        self.pushButton_35.setObjectName("pushButton_35")
        self.pushButton_36 = QtWidgets.QPushButton(self.tab_19)
        self.pushButton_36.setGeometry(QtCore.QRect(730, 690, 190, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_36.setFont(font)
        self.pushButton_36.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_36.setIcon(icon5)
        self.pushButton_36.setIconSize(QtCore.QSize(100, 46))
        self.pushButton_36.setObjectName("pushButton_36")
        self.pushButton_56 = QtWidgets.QPushButton(self.tab_19)
        self.pushButton_56.setGeometry(QtCore.QRect(350, 170, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_56.setFont(font)
        self.pushButton_56.setObjectName("pushButton_56")
        self.pushButton_57 = QtWidgets.QPushButton(self.tab_19)
        self.pushButton_57.setGeometry(QtCore.QRect(20, 90, 110, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_57.setFont(font)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/ico/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_57.setIcon(icon11)
        self.pushButton_57.setIconSize(QtCore.QSize(26, 30))
        self.pushButton_57.setObjectName("pushButton_57")
        self.label_107 = QtWidgets.QLabel(self.tab_19)
        self.label_107.setGeometry(QtCore.QRect(490, 540, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_107.setFont(font)
        self.label_107.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_107.setObjectName("label_107")
        self.lineEdit_69 = QtWidgets.QLineEdit(self.tab_19)
        self.lineEdit_69.setGeometry(QtCore.QRect(65, 540, 180, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_69.setFont(font)
        self.lineEdit_69.setText("")
        self.lineEdit_69.setObjectName("lineEdit_69")
        self.pushButton_62 = QtWidgets.QPushButton(self.tab_19)
        self.pushButton_62.setGeometry(QtCore.QRect(160, 577, 80, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_62.setFont(font)
        self.pushButton_62.setStyleSheet("image: url(:/ico/addf.png);")
        self.pushButton_62.setText("")
        self.pushButton_62.setObjectName("pushButton_62")
        self.comboBox_16 = QtWidgets.QComboBox(self.tab_19)
        self.comboBox_16.setGeometry(QtCore.QRect(280, 540, 220, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_16.setFont(font)
        self.comboBox_16.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_16.setObjectName("comboBox_16")
        self.pushButton_61 = QtWidgets.QPushButton(self.tab_19)
        self.pushButton_61.setGeometry(QtCore.QRect(70, 577, 80, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_61.setFont(font)
        self.pushButton_61.setStyleSheet("image: url(:/ico/removef.png);")
        self.pushButton_61.setText("")
        self.pushButton_61.setObjectName("pushButton_61")
        self.lineEdit_109 = QtWidgets.QLineEdit(self.tab_19)
        self.lineEdit_109.setGeometry(QtCore.QRect(280, 120, 330, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_109.setFont(font)
        self.lineEdit_109.setText("")
        self.lineEdit_109.setObjectName("lineEdit_109")
        self.label_43 = QtWidgets.QLabel(self.tab_19)
        self.label_43.setGeometry(QtCore.QRect(280, 70, 330, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_43.setFont(font)
        self.label_43.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_43.setAlignment(QtCore.Qt.AlignCenter)
        self.label_43.setObjectName("label_43")
        self.lcdNumber_5 = QtWidgets.QLCDNumber(self.tab_19)
        self.lcdNumber_5.setGeometry(QtCore.QRect(730, 640, 60, 35))
        self.lcdNumber_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 14pt \"Hacen Maghreb Bd\";\n"
"\n"
"    border-radius: 6;\n"
"")
        self.lcdNumber_5.setDigitCount(2)
        self.lcdNumber_5.setObjectName("lcdNumber_5")
        self.label_25 = QtWidgets.QLabel(self.tab_19)
        self.label_25.setGeometry(QtCore.QRect(780, 640, 140, 35))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 14pt \"Hacen Maghreb Bd\";\n"
"\n"
"    border-radius: 6;\n"
"")
        self.label_25.setObjectName("label_25")
        self.pushButton_62.raise_()
        self.pushButton_61.raise_()
        self.lineEdit_66.raise_()
        self.lineEdit_67.raise_()
        self.lineEdit_68.raise_()
        self.checkBox_7.raise_()
        self.label_73.raise_()
        self.lineEdit_70.raise_()
        self.pushButton_34.raise_()
        self.pushButton_35.raise_()
        self.pushButton_36.raise_()
        self.pushButton_56.raise_()
        self.pushButton_57.raise_()
        self.label_107.raise_()
        self.lineEdit_69.raise_()
        self.comboBox_16.raise_()
        self.lineEdit_109.raise_()
        self.label_43.raise_()
        self.comboBox_10.raise_()
        self.label_25.raise_()
        self.lcdNumber_5.raise_()
        self.tabWidget_6.addTab(self.tab_19, "")
        self.tab_20 = QtWidgets.QWidget()
        self.tab_20.setObjectName("tab_20")
        self.pushButton_37 = QtWidgets.QPushButton(self.tab_20)
        self.pushButton_37.setGeometry(QtCore.QRect(360, 670, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_37.setFont(font)
        self.pushButton_37.setIcon(icon10)
        self.pushButton_37.setIconSize(QtCore.QSize(31, 31))
        self.pushButton_37.setObjectName("pushButton_37")
        self.label_77 = QtWidgets.QLabel(self.tab_20)
        self.label_77.setGeometry(QtCore.QRect(440, 410, 170, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_77.setFont(font)
        self.label_77.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_77.setObjectName("label_77")
        self.lineEdit_72 = QtWidgets.QLineEdit(self.tab_20)
        self.lineEdit_72.setGeometry(QtCore.QRect(280, 290, 330, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_72.setFont(font)
        self.lineEdit_72.setText("")
        self.lineEdit_72.setObjectName("lineEdit_72")
        self.comboBox_11 = QtWidgets.QComboBox(self.tab_20)
        self.comboBox_11.setGeometry(QtCore.QRect(280, 410, 170, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_11.setFont(font)
        self.comboBox_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_11.setObjectName("comboBox_11")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.lineEdit_73 = QtWidgets.QLineEdit(self.tab_20)
        self.lineEdit_73.setGeometry(QtCore.QRect(280, 230, 330, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_73.setFont(font)
        self.lineEdit_73.setText("")
        self.lineEdit_73.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_73.setObjectName("lineEdit_73")
        self.lineEdit_74 = QtWidgets.QLineEdit(self.tab_20)
        self.lineEdit_74.setGeometry(QtCore.QRect(280, 520, 330, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_74.setFont(font)
        self.lineEdit_74.setText("")
        self.lineEdit_74.setObjectName("lineEdit_74")
        self.lineEdit_75 = QtWidgets.QLineEdit(self.tab_20)
        self.lineEdit_75.setGeometry(QtCore.QRect(280, 460, 330, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_75.setFont(font)
        self.lineEdit_75.setText("")
        self.lineEdit_75.setObjectName("lineEdit_75")
        self.lineEdit_76 = QtWidgets.QLineEdit(self.tab_20)
        self.lineEdit_76.setGeometry(QtCore.QRect(280, 350, 330, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_76.setFont(font)
        self.lineEdit_76.setText("")
        self.lineEdit_76.setObjectName("lineEdit_76")
        self.pushButton_38 = QtWidgets.QPushButton(self.tab_20)
        self.pushButton_38.setGeometry(QtCore.QRect(730, 690, 190, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_38.setFont(font)
        self.pushButton_38.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_38.setIcon(icon5)
        self.pushButton_38.setIconSize(QtCore.QSize(100, 46))
        self.pushButton_38.setObjectName("pushButton_38")
        self.pushButton_39 = QtWidgets.QPushButton(self.tab_20)
        self.pushButton_39.setGeometry(QtCore.QRect(30, 700, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_39.setFont(font)
        self.pushButton_39.setObjectName("pushButton_39")
        self.pushButton_58 = QtWidgets.QPushButton(self.tab_20)
        self.pushButton_58.setGeometry(QtCore.QRect(20, 90, 110, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_58.setFont(font)
        self.pushButton_58.setIcon(icon11)
        self.pushButton_58.setIconSize(QtCore.QSize(26, 30))
        self.pushButton_58.setObjectName("pushButton_58")
        self.lineEdit_71 = QtWidgets.QLineEdit(self.tab_20)
        self.lineEdit_71.setGeometry(QtCore.QRect(65, 580, 180, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_71.setFont(font)
        self.lineEdit_71.setText("")
        self.lineEdit_71.setObjectName("lineEdit_71")
        self.pushButton_73 = QtWidgets.QPushButton(self.tab_20)
        self.pushButton_73.setGeometry(QtCore.QRect(160, 617, 80, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_73.setFont(font)
        self.pushButton_73.setStyleSheet("image: url(:/ico/addf.png);")
        self.pushButton_73.setText("")
        self.pushButton_73.setObjectName("pushButton_73")
        self.comboBox_23 = QtWidgets.QComboBox(self.tab_20)
        self.comboBox_23.setGeometry(QtCore.QRect(280, 580, 220, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_23.setFont(font)
        self.comboBox_23.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_23.setObjectName("comboBox_23")
        self.pushButton_74 = QtWidgets.QPushButton(self.tab_20)
        self.pushButton_74.setGeometry(QtCore.QRect(70, 617, 80, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_74.setFont(font)
        self.pushButton_74.setStyleSheet("image: url(:/ico/removef.png);")
        self.pushButton_74.setText("")
        self.pushButton_74.setObjectName("pushButton_74")
        self.label_113 = QtWidgets.QLabel(self.tab_20)
        self.label_113.setGeometry(QtCore.QRect(490, 580, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_113.setFont(font)
        self.label_113.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_113.setObjectName("label_113")
        self.pushButton_119 = QtWidgets.QPushButton(self.tab_20)
        self.pushButton_119.setGeometry(QtCore.QRect(350, 170, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_119.setFont(font)
        self.pushButton_119.setObjectName("pushButton_119")
        self.lineEdit_110 = QtWidgets.QLineEdit(self.tab_20)
        self.lineEdit_110.setGeometry(QtCore.QRect(280, 120, 330, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_110.setFont(font)
        self.lineEdit_110.setText("")
        self.lineEdit_110.setObjectName("lineEdit_110")
        self.label_68 = QtWidgets.QLabel(self.tab_20)
        self.label_68.setGeometry(QtCore.QRect(280, 70, 330, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_68.setFont(font)
        self.label_68.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_68.setAlignment(QtCore.Qt.AlignCenter)
        self.label_68.setObjectName("label_68")
        self.label_64 = QtWidgets.QLabel(self.tab_20)
        self.label_64.setGeometry(QtCore.QRect(780, 640, 140, 35))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_64.setFont(font)
        self.label_64.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 14pt \"Hacen Maghreb Bd\";\n"
"\n"
"    border-radius: 6;\n"
"")
        self.label_64.setObjectName("label_64")
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.tab_20)
        self.lcdNumber_4.setGeometry(QtCore.QRect(730, 640, 60, 35))
        self.lcdNumber_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 14pt \"Hacen Maghreb Bd\";\n"
"\n"
"    border-radius: 6;\n"
"")
        self.lcdNumber_4.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdNumber_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lcdNumber_4.setLineWidth(1)
        self.lcdNumber_4.setMidLineWidth(0)
        self.lcdNumber_4.setDigitCount(2)
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.pushButton_74.raise_()
        self.pushButton_73.raise_()
        self.pushButton_37.raise_()
        self.label_77.raise_()
        self.lineEdit_72.raise_()
        self.comboBox_11.raise_()
        self.lineEdit_73.raise_()
        self.lineEdit_74.raise_()
        self.lineEdit_75.raise_()
        self.lineEdit_76.raise_()
        self.pushButton_38.raise_()
        self.pushButton_39.raise_()
        self.pushButton_58.raise_()
        self.lineEdit_71.raise_()
        self.label_113.raise_()
        self.pushButton_119.raise_()
        self.lineEdit_110.raise_()
        self.label_68.raise_()
        self.comboBox_23.raise_()
        self.label_64.raise_()
        self.lcdNumber_4.raise_()
        self.tabWidget_6.addTab(self.tab_20, "")
        self.tabWidget_5.addTab(self.tab_18, "")
        self.tab_21 = QtWidgets.QWidget()
        self.tab_21.setObjectName("tab_21")
        self.tabWidget_7 = QtWidgets.QTabWidget(self.tab_21)
        self.tabWidget_7.setGeometry(QtCore.QRect(0, -10, 1410, 1060))
        self.tabWidget_7.setStyleSheet("QTextEdit {\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"\n"
"}\n"
"QTextEdit::hover\n"
"{\n"
"    border: 1px solid rgb(0, 170, 255);\n"
"    border-radius: 2px;\n"
"    color: rgb(0, 115, 255);\n"
"    border-radius: 6;\n"
"\n"
"\n"
"}\n"
"")
        self.tabWidget_7.setObjectName("tabWidget_7")
        self.tab_22 = QtWidgets.QWidget()
        self.tab_22.setObjectName("tab_22")
        self.checkBox_8 = QtWidgets.QCheckBox(self.tab_22)
        self.checkBox_8.setGeometry(QtCore.QRect(310, 710, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.checkBox_8.setFont(font)
        self.checkBox_8.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.checkBox_8.setIcon(icon6)
        self.checkBox_8.setIconSize(QtCore.QSize(12, 171))
        self.checkBox_8.setObjectName("checkBox_8")
        self.pushButton_40 = QtWidgets.QPushButton(self.tab_22)
        self.pushButton_40.setGeometry(QtCore.QRect(30, 700, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_40.setFont(font)
        self.pushButton_40.setObjectName("pushButton_40")
        self.pushButton_41 = QtWidgets.QPushButton(self.tab_22)
        self.pushButton_41.setGeometry(QtCore.QRect(730, 690, 190, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_41.setFont(font)
        self.pushButton_41.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_41.setIcon(icon5)
        self.pushButton_41.setIconSize(QtCore.QSize(100, 46))
        self.pushButton_41.setObjectName("pushButton_41")
        self.lineEdit_82 = QtWidgets.QLineEdit(self.tab_22)
        self.lineEdit_82.setGeometry(QtCore.QRect(270, 180, 460, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_82.setFont(font)
        self.lineEdit_82.setObjectName("lineEdit_82")
        self.pushButton_82 = QtWidgets.QPushButton(self.tab_22)
        self.pushButton_82.setGeometry(QtCore.QRect(760, 180, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_82.setFont(font)
        self.pushButton_82.setIcon(icon8)
        self.pushButton_82.setIconSize(QtCore.QSize(22, 22))
        self.pushButton_82.setObjectName("pushButton_82")
        self.spinBox_36 = QtWidgets.QSpinBox(self.tab_22)
        self.spinBox_36.setGeometry(QtCore.QRect(310, 330, 130, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.spinBox_36.setFont(font)
        self.spinBox_36.setStyleSheet("\n"
"QAbstractSpinBox {\n"
"\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    border: 1px solid #3A3939;\n"
"    background-color:rgb(255, 0, 102);\n"
"    color: white;\n"
"    border-radius: 2px;\n"
"    min-width: 75px;\n"
"}\n"
"\n"
"")
        self.spinBox_36.setObjectName("spinBox_36")
        self.comboBox_25 = QtWidgets.QComboBox(self.tab_22)
        self.comboBox_25.setGeometry(QtCore.QRect(450, 330, 310, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_25.setFont(font)
        self.comboBox_25.setObjectName("comboBox_25")
        self.label_115 = QtWidgets.QLabel(self.tab_22)
        self.label_115.setGeometry(QtCore.QRect(750, 330, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_115.setFont(font)
        self.label_115.setStyleSheet("\n"
"QLabel\n"
"{\n"
"/*font: 75 16pt \"Arial Unicode MS\";*/\n"
"\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 17pt \"Hacen Maghreb Bd\";\n"
"\n"
"}")
        self.label_115.setObjectName("label_115")
        self.pushButton_81 = QtWidgets.QPushButton(self.tab_22)
        self.pushButton_81.setGeometry(QtCore.QRect(270, 390, 170, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_81.setFont(font)
        self.pushButton_81.setIcon(icon8)
        self.pushButton_81.setIconSize(QtCore.QSize(22, 22))
        self.pushButton_81.setObjectName("pushButton_81")
        self.pushButton_126 = QtWidgets.QPushButton(self.tab_22)
        self.pushButton_126.setGeometry(QtCore.QRect(770, 240, 130, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_126.setFont(font)
        self.pushButton_126.setIcon(icon9)
        self.pushButton_126.setIconSize(QtCore.QSize(22, 22))
        self.pushButton_126.setObjectName("pushButton_126")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_22)
        self.tableWidget_2.setGeometry(QtCore.QRect(40, 180, 220, 420))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setStyleSheet("\n"
"QMenu::indicator:exclusive:unchecked:selected\n"
"{\n"
"    border-image: url(:/light/radio_unchecked_disabled.svg);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked\n"
"{\n"
"    border-image: url(:/light/radio_checked.svg);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked:selected\n"
"{\n"
"    border-image: url(:/light/radio_checked.svg);\n"
"}\n"
"\n"
"QMenu::right-arrow\n"
"{\n"
"    margin: 0.5ex;\n"
"    border-image: url(:/light/right_arrow.svg);\n"
"    width: 0.6ex;\n"
"    height: 0.9ex;\n"
"}\n"
"\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #454545;\n"
"    background-color: #EFF0F1;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    alternate-background-color: #EFF0F1;\n"
"    color: #31363B;\n"
"    border: 0.1ex solid 3A3939;\n"
"    border-radius: 0.2ex;\n"
"}\n"
"\n"
"QWidget:focus,\n"
"QMenuBar:focus\n"
"{\n"
"    border: 0.1ex solid #33A4DF;\n"
"}\n"
"\n"
"QTabWidget:focus,\n"
"QCheckBox:focus,\n"
"QRadioButton:focus,\n"
"QSlider:focus\n"
"{\n"
"    border: none;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: #FCFCFC;\n"
"    padding: 0.5ex;\n"
"    border-style: solid;\n"
"    border: 0.1ex solid #BAB9B8;\n"
"    border-radius: 0.2ex;\n"
"    color: #31363B;\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"    border: 0.1ex solid #BAB9B8;\n"
"    border-radius: 0.2ex;\n"
"    padding-top: 1ex;\n"
"    margin-top: 1ex;\n"
"}\n"
"\n"
"QGroupBox::title\n"
"{\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding-left: 0.1ex;\n"
"    padding-right: 0.1ex;\n"
"    margin-top: -0.7ex;\n"
"}\n"
"\n"
"QAbstractScrollArea\n"
"{\n"
"    border-radius: 0.2ex;\n"
"    border: 0.1ex solid #BAB9B8;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar:horizontal\n"
"{\n"
"    height: 1.5ex;\n"
"    margin: 0.3ex 1.5ex 0.3ex 1.5ex;\n"
"    border: 0.1ex transparent #2A2929;\n"
"    border-radius: 0.4ex;\n"
"    background-color: #2A2929;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background-color: #605F5F;\n"
"    min-width: 0.5ex;\n"
"    border-radius: 0.4ex;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    margin: 0ex 0.3ex 0ex 0.3ex;\n"
"    border-image: url(:/light/right_arrow_disabled.svg);\n"
"    width: 1ex;\n"
"    height: 1ex;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    margin: 0px 0.3ex 0px 0.3ex;\n"
"    border-image: url(:/light/left_arrow_disabled.svg);\n"
"    height: 1ex;\n"
"    width: 1ex;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: #2A2929;\n"
"    width: 1.5ex;\n"
"    margin: 1.5ex 0.3ex 1.5ex 0.3ex;\n"
"    border: 0.1ex transparent #2A2929;\n"
"    border-radius: 0.4ex;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: #605F5F;\n"
"    min-height: 0.5ex;\n"
"    border-radius: 0.4ex;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    margin: 0.3ex 0ex 0.3ex 0ex;\n"
"    border-image: url(:/light/up_arrow_disabled.svg);\n"
"    height: 1ex;\n"
"    width: 1ex;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    margin: 0.3ex 0ex 0.3ex 0ex;\n"
"    border-image: url(:/light/down_arrow_disabled.svg);\n"
"    height: 1ex;\n"
"    width: 1ex;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover,\n"
"QScrollBar::sub-line:vertical:on\n"
"{\n"
"\n"
"    border-image: url(:/light/up_arrow.svg);\n"
"    height: 1ex;\n"
"    width: 1ex;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:hover,\n"
"QScrollBar::add-line:vertical:on\n"
"{\n"
"    border-image: url(:/light/down_arrow.svg);\n"
"    height: 1ex;\n"
"    width: 1ex;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical,\n"
"QScrollBar::down-arrow:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #EFF0F1;\n"
"    color: #31363B;\n"
"    border: 0.1ex solid #BAB9B8;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #EFF0F1;\n"
"    color: #31363B;\n"
"    border-radius: 0.2ex;\n"
"    border: 0.1ex solid #BAB9B8;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: #BAB9B8;\n"
"    color: #31363B;\n"
"    padding: 0.5ex;\n"
"    border: 0.1ex solid #BAB9B8;\n"
"}\n"
"\n"
"QSizeGrip\n"
"{\n"
"    border-image: url(:/light/sizegrip.svg);\n"
"    width: 1.2ex;\n"
"    height: 1.2ex;\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: #EFF0F1;\n"
"    color: white;\n"
"    padding-left: 0.4ex;\n"
"    spacing: 0.2ex;\n"
"    border: 0.1ex dashed #BAB9B8;\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: #787876;\n"
"    color: white;\n"
"    padding-left: 0.4ex;\n"
"    border: 0.1ex solid #BAB9B8;\n"
"    spacing: 0.2x;\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 0.1ex;\n"
"    background-color: #BAB9B8;\n"
"    color: white;\n"
"    padding-left: 0.4ex;\n"
"    margin-left: 1ex;\n"
"    margin-right: 0.5ex;\n"
"}\n"
"\n"
"QFrame[frameShape=\"2\"],  /* QFrame::Panel == 0x0003 */\n"
"QFrame[frameShape=\"3\"],  /* QFrame::WinPanel == 0x0003 */\n"
"QFrame[frameShape=\"4\"],  /* QFrame::HLine == 0x0004 */\n"
"QFrame[frameShape=\"5\"],  /* QFrame::VLine == 0x0005 */\n"
"QFrame[frameShape=\"6\"]  /* QFrame::StyledPanel == 0x0006 */\n"
"{\n"
"    border-width: 0.1ex;\n"
"    padding: 0.1ex;\n"
"    border-style: solid;\n"
"    border-color: #EFF0F1;\n"
"    background-color: #bcbfc2;\n"
"    border-radius: 0.5ex;\n"
"}\n"
"\n"
"QStackedWidget\n"
"{\n"
"    border: 0.1ex transparent black;\n"
"}\n"
"\n"
"QToolBar\n"
"{\n"
"    border: 0.1ex transparent #393838;\n"
"    background: 0.1ex solid #EFF0F1;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QToolBar::handle:horizontal\n"
"{\n"
"    border-image: url(:/light/hmovetoolbar.svg);\n"
"    width = 1.6ex;\n"
"    height = 6.4ex;\n"
"}\n"
"\n"
"QToolBar::handle:vertical\n"
"{\n"
"    border-image: url(:/light/vmovetoolbar.svg);\n"
"    width = 5.4ex;\n"
"    height = 1ex;\n"
"}\n"
"\n"
"QToolBar::separator:horizontal\n"
"{\n"
"    border-image: url(:/light/hsepartoolbar.svg);\n"
"    width = 0.7ex;\n"
"    height = 6.3ex;\n"
"}\n"
"\n"
"QToolBar::separator:vertical\n"
"{\n"
"    border-image: url(:/light/vsepartoolbars.svg);\n"
"    width = 6.3ex;\n"
"    height = 0.7ex;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #31363B;\n"
"    background-color: qlineargradient(x1: 0.5, y1: 0.5 x2: 0.5, y2: 1, stop: 0 #EFF0F1, stop: 0.5 #eaebec);\n"
"    border-width: 0.1ex;\n"
"    border-color: #BAB9B8;\n"
"    border-style: solid;\n"
"    padding: 0.5ex;\n"
"    border-radius: 0.2ex;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:disabled\n"
"{\n"
"    background-color: #e0e1e2;\n"
"    border-width: 0.1ex;\n"
"    border-color: #b4b4b4;\n"
"    border-style: solid;\n"
"    padding-top: 0.5ex;\n"
"    padding-bottom: 0.5ex;\n"
"    padding-left: 1ex;\n"
"    padding-right: 1ex;\n"
"    border-radius: 0.2ex;\n"
"    color: #b4b4b4;\n"
"}\n"
"\n"
"QPushButton:focus\n"
"{\n"
"    color: black;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #33A4DF;\n"
"    border-style: solid;\n"
"    border: 0.1ex solid #BAB9B8;\n"
"    border-radius: 0.2ex;\n"
"    padding: 0.5ex;\n"
"    min-width: 7.5ex;\n"
"}\n"
"\n"
"QPushButton:checked\n"
"{\n"
"    background-color: #BAB9B8;\n"
"    border-color: #6A6969;\n"
"}\n"
"\n"
"QComboBox:hover,\n"
"QAbstractSpinBox:hover,\n"
"QLineEdit:hover,\n"
"QTextEdit:hover,\n"
"QPlainTextEdit:hover,\n"
"QAbstractView:hover,\n"
"QTreeView:hover\n"
"{\n"
"    border: 0.1ex solid #33A4DF;\n"
"    color: #31363B;\n"
"}\n"
"\n"
"QComboBox:hover:pressed,\n"
"QPushButton:hover:pressed,\n"
"QAbstractSpinBox:hover:pressed,\n"
"QLineEdit:hover:pressed,\n"
"QTextEdit:hover:pressed,\n"
"QPlainTextEdit:hover:pressed,\n"
"QAbstractView:hover:pressed,\n"
"QTreeView:hover:pressed\n"
"{\n"
"    background-color: #EFF0F1;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 0.3ex;\n"
"    padding-left: 0.4ex;\n"
"    selection-background-color: #4a4a4a;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: #FCFCFC;\n"
"    border-radius: 0.2ex;\n"
"    border: 0.1ex solid #BAB9B8;\n"
"    selection-background-color: #33A4DF;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 1.5ex;\n"
"\n"
"    border-left-width: 0ex;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 0.3ex;\n"
"    border-bottom-right-radius: 0.3ex;\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"    border-image: url(:/light/down_arrow_disabled.svg);\n"
"    width: 0.9ex;\n"
"    height: 0.6ex;\n"
"}\n"
"\n"
"QComboBox::down-arrow:on,\n"
"QComboBox::down-arrow:hover,\n"
"QComboBox::down-arrow:focus\n"
"{\n"
"    border-image: url(:/light/down_arrow.svg);\n"
"    width: 0.9ex;\n"
"    height: 0.6ex;\n"
"}\n"
"\n"
"QAbstractSpinBox\n"
"{\n"
"    padding: 0.5ex;\n"
"    border: 0.1ex solid #BAB9B8;\n"
"    background-color: #D9D8D7;\n"
"    color: #31363B;\n"
"    border-radius: 0.2ex;\n"
"    min-width: 7.5ex;\n"
"}\n"
"\n"
"QAbstractSpinBox:up-button\n"
"{\n"
"    background-color: transparent;\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: center right;\n"
"}\n"
"\n"
"QAbstractSpinBox:down-button\n"
"{\n"
"    background-color: transparent;\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: center left;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow,\n"
"QAbstractSpinBox::up-arrow:disabled,\n"
"QAbstractSpinBox::up-arrow:off\n"
"{\n"
"    border-image: url(:/light/up_arrow_disabled.svg);\n"
"    width: 0.9ex;\n"
"    height: 0.6ex;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow:hover\n"
"{\n"
"    border-image: url(:/light/up_arrow.svg);\n"
"    width: 0.9ex;\n"
"    height: 0.6ex;\n"
"}\n"
"\n"
"QAbstractSpinBox::down-arrow,\n"
"QAbstractSpinBox::down-arrow:disabled,\n"
"QAbstractSpinBox::down-arrow:off\n"
"{\n"
"    border-image: url(:/light/down_arrow_disabled.svg);\n"
"    width: 0.9ex;\n"
"    height: 0.6ex;\n"
"}\n"
"\n"
"QAbstractSpinBox::down-arrow:hover\n"
"{\n"
"    border-image: url(:/light/down_arrow.svg);\n"
"    width: 0.9ex;\n"
"    height: 0.6ex;\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"    border: 0ex solid black;\n"
"}\n"
"\n"
"QTabWidget{\n"
"    border: 0.1ex solid #BAB9B8;\n"
"}\n"
"\n"
"/* BORDERS */\n"
"QTabWidget::pane\n"
"{\n"
"    padding: 0.5ex;\n"
"    margin: 0.1ex;\n"
"}\n"
"\n"
"QTabWidget::pane:top\n"
"{\n"
"    border: 0.1ex solid #BAB9B8;\n"
"    top: -0.1ex;\n"
"}\n"
"\n"
"QTabWidget::pane:bottom\n"
"{\n"
"    border: 0.1ex solid #BAB9B8;\n"
"    bottom: -0.1ex;\n"
"}\n"
"\n"
"QTabWidget::pane:left\n"
"{\n"
"    border: 0.1ex solid #BAB9B8;\n"
"    right: -0.1ex;\n"
"}\n"
"\n"
"QTabWidget::pane:right\n"
"{\n"
"    border: 0.1ex solid #BAB9B8;\n"
"    left: -0.1ex;\n"
"}\n"
"\n"
"QTabBar\n"
"{\n"
"    qproperty-drawBase: 0;\n"
"    left: 0.5ex; /* move to the right by 0.5ex */\n"
"    border-radius: 0.3ex;\n"
"}\n"
"\n"
"QTabBar:focus\n"
"{\n"
"    border: 0ex transparent black;\n"
"}\n"
"\n"
"QTabBar::close-button\n"
"{\n"
"    border-image: url(:/light/close.svg);\n"
"    width: 1.2ex;\n"
"    height: 1.2ex;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTabBar::close-button:hover\n"
"{\n"
"    border-image: url(:/light/close-hover.svg);\n"
"    width: 1.2ex;\n"
"    height: 1.2ex;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTabBar::close-button:pressed\n"
"{\n"
"    border-image: url(:/light/close-pressed.svg);\n"
"    width: 1.2ex;\n"
"    height: 1.2ex;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* TOP TABS */\n"
"QTabBar::tab:top\n"
"{\n"
"    color: #31363B;\n"
"    border: 0.1ex transparent black;\n"
"    border-left: 0.1ex solid #BAB9B8;\n"
"    border-top: 0.1ex solid #BAB9B8;\n"
"    background-color: #EFF0F1;\n"
"    padding: 0.5ex;\n"
"    min-width: 5ex;\n"
"    border-top-left-radius: 0.2ex;\n"
"    border-top-right-radius: 0.2ex;\n"
"}\n"
"\n"
"QTabBar::tab:top:last,\n"
"QTabBar::tab:top:only-one\n"
"{\n"
"    color: #31363B;\n"
"    border: 0.1ex transparent black;\n"
"    border-left: 0.1ex solid #BAB9B8;\n"
"    border-right: 0.1ex solid #BAB9B8;\n"
"    border-top: 0.1ex solid #BAB9B8;\n"
"    background-color: #EFF0F1;\n"
"    padding: 0.5ex;\n"
"    min-width: 5ex;\n"
"    border-top-left-radius: 0.2ex;\n"
"    border-top-right-radius: 0.2ex;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected\n"
"{\n"
"    color: #31363B;\n"
"    background-color: #D9D8D7;\n"
"    border: 0.1ex transparent black;\n"
"    border-left: 0.1ex solid #BAB9B8;\n"
"    border-top-left-radius: 0.2ex;\n"
"    border-top-right-radius: 0.2ex;\n"
"}\n"
"\n"
"QTabBar::tab:top:first:!selected\n"
"{\n"
"    color: #31363B;\n"
"    background-color: #D9D8D7;\n"
"    border: 0.1ex transparent black;\n"
"    border-top-left-radius: 0.2ex;\n"
"    border-top-right-radius: 0.2ex;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected:hover\n"
"{\n"
"    background-color: rgba(61, 173, 232, 0.1);\n"
"    border: 0.1ex rgba(61, 173, 232, 0.1);\n"
"    border-left: 0.1ex solid #BAB9B8;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected:first:hover\n"
"{\n"
"    background-color: rgba(61, 173, 232, 0.1);\n"
"    border: 0.1ex rgba(61, 173, 232, 0.1);\n"
"}\n"
"\n"
"/* BOTTOM TABS */\n"
"QTabBar::tab:bottom\n"
"{\n"
"    color: #31363B;\n"
"    border: 0.1ex transparent black;\n"
"    border-left: 0.1ex solid #BAB9B8;\n"
"    border-bottom: 0.1ex solid #BAB9B8;\n"
"    background-color: #EFF0F1;\n"
"    padding: 0.5ex;\n"
"    border-bottom-left-radius: 0.2ex;\n"
"    border-bottom-right-radius: 0.2ex;\n"
"    min-width: 5ex;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:last,\n"
"QTabBar::tab:bottom:only-one\n"
"{\n"
"    color: #31363B;\n"
"    border: 0.1ex transparent black;\n"
"    border-left: 0.1ex solid #BAB9B8;\n"
"    border-right: 0.1ex solid #BAB9B8;\n"
"    border-bottom: 0.1ex solid #BAB9B8;\n"
"    background-color: #EFF0F1;\n"
"    padding: 0.5ex;\n"
"    border-bottom-left-radius: 0.2ex;\n"
"    border-bottom-right-radius: 0.2ex;\n"
"    min-width: 5ex;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected\n"
"{\n"
"    color: #31363B;\n"
"    background-color: #D9D8D7;\n"
"    border: 0.1ex transparent black;\n"
"    border-left: 0.1ex solid #BAB9B8;\n"
"    border-bottom-left-radius: 0.2ex;\n"
"    border-bottom-right-radius: 0.2ex;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:first:!selected\n"
"{\n"
"    color: #31363B;\n"
"    background-color: #D9D8D7;\n"
"    border: 0.1ex transparent black;\n"
"    border-bottom-left-radius: 0.2ex;\n"
"    border-bottom-right-radius: 0.2ex;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected:hover\n"
"{\n"
"    background-color: rgba(61, 173, 232, 0.1);\n"
"    border: 0.1ex rgba(61, 173, 232, 0.1);\n"
"    border-left: 0.1ex solid #BAB9B8;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected:first:hover\n"
"{\n"
"    background-color: rgba(61, 173, 232, 0.1);\n"
"    border: 0.1ex rgba(61, 173, 232, 0.1);\n"
"}\n"
"\n"
"/* LEFT TABS */\n"
"QTabBar::tab:left\n"
"{\n"
"    color: #31363B;\n"
"    border: 0.1ex transparent black;\n"
"    border-top: 0.1ex solid #BAB9B8;\n"
"    border-right: 0.1ex solid #BAB9B8;\n"
"    background-color: #EFF0F1;\n"
"    padding: 0.5ex;\n"
"    border-top-right-radius: 0.2ex;\n"
"    border-bottom-right-radius: 0.2ex;\n"
"    min-height: 5ex;\n"
"}\n"
"\n"
"QTabBar::tab:left:last,\n"
"QTabBar::tab:left:only-one\n"
"{\n"
"    color: #31363B;\n"
"    border: 0.1ex transparent black;\n"
"    border-top: 0.1ex solid #BAB9B8;\n"
"    border-bottom: 0.1ex solid #BAB9B8;\n"
"    border-right: 0.1ex solid #BAB9B8;\n"
"    background-color: #EFF0F1;\n"
"    padding: 0.5ex;\n"
"    border-top-right-radius: 0.2ex;\n"
"    border-bottom-right-radius: 0.2ex;\n"
"    min-height: 5ex;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected\n"
"{\n"
"    color: #31363B;\n"
"    background-color: #D9D8D7;\n"
"    border: 0.1ex transparent black;\n"
"    border-top: 0.1ex solid #BAB9B8;\n"
"    border-top-right-radius: 0.2ex;\n"
"    border-bottom-right-radius: 0.2ex;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected:hover\n"
"{\n"
"    background-color: rgba(61, 173, 232, 0.1);\n"
"    border: 0.1ex rgba(61, 173, 232, 0.1);\n"
"    border-top: 0.1ex solid #BAB9B8;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected:first:hover\n"
"{\n"
"    background-color: rgba(61, 173, 232, 0.1);\n"
"    border: 0.1ex rgba(61, 173, 232, 0.1);\n"
"}\n"
"\n"
"/* RIGHT TABS */\n"
"QTabBar::tab:right\n"
"{\n"
"    color: #31363B;\n"
"    border: 0.1ex transparent black;\n"
"    border-top: 0.1ex solid #BAB9B8;\n"
"    border-left: 0.1ex solid #BAB9B8;\n"
"    background-color: #D9D8D7;\n"
"    padding: 0.5ex;\n"
"    border-top-left-radius: 0.2ex;\n"
"    border-bottom-left-radius: 0.2ex;\n"
"    min-height: 5ex;\n"
"}\n"
"\n"
"QTabBar::tab:right:last,\n"
"QTabBar::tab:right:only-one\n"
"{\n"
"    color: #31363B;\n"
"    border: 0.1ex transparent black;\n"
"    border-top: 0.1ex solid #BAB9B8;\n"
"    border-bottom: 0.1ex solid #BAB9B8;\n"
"    border-left: 0.1ex solid #BAB9B8;\n"
"    background-color: #D9D8D7;\n"
"    padding: 0.5ex;\n"
"    border-top-left-radius: 0.2ex;\n"
"    border-bottom-left-radius: 0.2ex;\n"
"    min-height: 5ex;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected\n"
"{\n"
"    color: #31363B;\n"
"    background-color: #54575B;\n"
"    border: 0.1ex transparent black;\n"
"    border-top: 0.1ex solid #BAB9B8;\n"
"    border-top-left-radius: 0.2ex;\n"
"    border-bottom-left-radius: 0.2ex;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected:hover\n"
"{\n"
"    background-color: rgba(61, 173, 232, 0.1);\n"
"    border: 0.1ex rgba(61, 173, 232, 0.1);\n"
"    border-top: 0.1ex solid #BAB9B8;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected:first:hover\n"
"{\n"
"    background-color: rgba(61, 173, 232, 0.1);\n"
"    border: 0.1ex rgba(61, 173, 232, 0.1);\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:enabled\n"
"{\n"
"    border-image: url(:/light/right_arrow.svg);\n"
"}\n"
"\n"
"QTabBar QToolButton::left-arrow:enabled\n"
"{\n"
"    border-image: url(:/light/left_arrow.svg);\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:disabled\n"
"{\n"
"    border-image: url(:/light/right_arrow_disabled.svg);\n"
"}\n"
"\n"
"QTabBar QToolButton::left-arrow:disabled\n"
"{\n"
"    border-image: url(:/light/left_arrow_disabled.svg);\n"
"}\n"
"\n"
"QDockWidget\n"
"{\n"
"    background: #EFF0F1;\n"
"    border: 0.1ex solid #403F3F;\n"
"    titlebar-close-icon: url(:/light/transparent.svg);\n"
"    titlebar-normal-icon: url(:/light/transparent.svg);\n"
"}\n"
"\n"
"QDockWidget::close-button,\n"
"QDockWidget::float-button\n"
"{\n"
"    border: 0.1ex solid transparent;\n"
"    border-radius: 0.2ex;\n"
"    background: transparent;\n"
"}\n"
"\n"
"\n"
"QDockWidget::float-button\n"
"{\n"
"    border-image: url(:/dark/undock.svg);\n"
"}\n"
"\n"
"QDockWidget::float-button:hover\n"
"{\n"
"    border-image: url(:/dark/undock-hover.svg) ;\n"
"}\n"
"\n"
"QDockWidget::close-button\n"
"{\n"
"    border-image: url(:/dark/close.svg) ;\n"
"}\n"
"\n"
"QDockWidget::close-button:hover\n"
"{\n"
"    border-image: url(:/dark/close-hover.svg) ;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed\n"
"{\n"
"    border-image: url(:/dark/close-pressed.svg) ;\n"
"}\n"
"\n"
"QTreeView,\n"
"QListView\n"
"{\n"
"    border: 0.1ex solid #BAB9B8;\n"
"    background-color: #FCFCFC;\n"
"}\n"
"\n"
"\n"
"QTreeView::branch:has-siblings:!adjoins-item\n"
"{\n"
"    border-image: url(:/light/stylesheet-vline.svg) 0;\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:adjoins-item\n"
"{\n"
"    border-image: url(:/light/stylesheet-branch-more.svg) 0;\n"
"}\n"
"\n"
"QTreeView::branch:!has-children:!has-siblings:adjoins-item\n"
"{\n"
"    border-image: url(:/light/stylesheet-branch-end.svg) 0;\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings\n"
"{\n"
"    border-image: url(:/light/stylesheet-branch-end-closed.svg) 0;\n"
"    image: url(:/light/branch_closed.svg);\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings\n"
"{\n"
"    border-image: url(:/light/stylesheet-branch-end-open.svg) 0;\n"
"    image: url(:/light/branch_open.svg);\n"
"}\n"
"\n"
"QTableView::item,\n"
"QListView::item,\n"
"QTreeView::item\n"
"{\n"
"    padding: 0.3ex;\n"
"}\n"
"\n"
"QTableView::item:!selected:hover,\n"
"QListView::item:!selected:hover,\n"
"QTreeView::item:!selected:hover\n"
"{\n"
"    background-color: rgba(61, 173, 232, 0.1);\n"
"    outline: 0;\n"
"    color: #31363B;\n"
"    padding: 0.3ex;\n"
"}\n"
"\n"
"QSlider::groove:horizontal\n"
"{\n"
"    border: 0.1ex solid #EFF0F1;\n"
"    height: 0.4ex;\n"
"    background: #9CA0A4;\n"
"    margin: 0px;\n"
"    border-radius: 0.2ex;\n"
"}\n"
"\n"
"QSlider::handle:horizontal\n"
"{\n"
"    background: #D9D8D7;\n"
"    border: 0.1ex solid #BABEC2;\n"
"    width: 1.6ex;\n"
"    height: 1.6ex;\n"
"    margin: -0.8ex 0;\n"
"    border-radius: 0.9ex;\n"
"}\n"
"\n"
"QSlider::groove:vertical\n"
"{\n"
"    border: 0.1ex solid #EFF0F1;\n"
"    width: 0.4ex;\n"
"    background: #9CA0A4;\n"
"    margin: 0ex;\n"
"    border-radius: 0.3ex;\n"
"}\n"
"\n"
"QSlider::handle:vertical\n"
"{\n"
"    background: #D9D8D7;\n"
"    border: 0.1ex solid #BABEC2;\n"
"    width: 1.6ex;\n"
"    height: 1.6ex;\n"
"    margin: 0 -0.8ex;\n"
"    border-radius: 0.9ex;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:focus,\n"
"QSlider::handle:vertical:focus\n"
"{\n"
"    border: 0.1ex solid #33A4DF;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover,\n"
"QSlider::handle:vertical:hover\n"
"{\n"
"    border: 0.1ex solid #51c2fc;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal,\n"
"QSlider::add-page:vertical\n"
"{\n"
"    background: #33A4DF;\n"
"    border-radius: 0.3ex;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal,\n"
"QSlider::sub-page:vertical\n"
"{\n"
"    background: #BABEC2;\n"
"    border-radius: 0.3ex;\n"
"}\n"
"\n"
"QToolButton\n"
"{\n"
"    background-color: transparent;\n"
"    border: 0.1ex solid #BAB9B8;\n"
"    border-radius: 0.2ex;\n"
"    margin: 0.3ex;\n"
"    padding: 0.5ex;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"] /* only for MenuButtonPopup */\n"
"{\n"
"    padding-right: 2ex; /* make way for the popup button */\n"
"}\n"
"\n"
"QToolButton[popupMode=\"2\"] /* only for InstantPopup */\n"
"{\n"
"    padding-right: 1ex; /* make way for the popup button */\n"
"}\n"
"\n"
"QToolButton::menu-indicator\n"
"{\n"
"    border-image: url(:/light/down_arrow.svg);\n"
"    top: -0.7ex; left: -0.2ex; /* shift it a bit */\n"
"    width = 0.9ex;\n"
"    height = 0.6ex;\n"
"}\n"
"\n"
"QToolButton::menu-arrow\n"
"{\n"
"    border-image: url(:/light/down_arrow.svg);\n"
"    width = 0.9ex;\n"
"    height = 0.6ex;\n"
"}\n"
"\n"
"QToolButton:hover,\n"
"QToolButton::menu-button:hover\n"
"{\n"
"    background-color: transparent;\n"
"    border: 0.1ex solid #33A4DF;\n"
"}\n"
"\n"
"QToolButton:checked,\n"
"QToolButton:pressed,\n"
"QToolButton::menu-button:pressed\n"
"{\n"
"    background-color: #47b8fc;\n"
"    border: 0.1ex solid #47b8fc;\n"
"    padding: 0.5ex;\n"
"}\n"
"\n"
"QToolButton::menu-button\n"
"{\n"
"    border: 0.1ex solid #BAB9B8;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"    /* 1ex width + 0.4ex for border + no text = 2ex allocated above */\n"
"    width: 1ex;\n"
"    padding: 0.5ex;\n"
"    outline: none;\n"
"}\n"
"\n"
"QToolButton::menu-arrow:open\n"
"{\n"
"    border: 0.1ex solid #BAB9B8;\n"
"}\n"
"\n"
"QPushButton::menu-indicator\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: bottom right;\n"
"    left: 0.8ex;\n"
"}\n"
"\n"
"QTableView\n"
"{\n"
"    border: 0.1ex solid #BAB9B8;\n"
"    gridline-color: #BAB9B8;\n"
"    background-color: #FCFCFC;\n"
"}\n"
"\n"
"\n"
"QTableView,\n"
"QHeaderView\n"
"{\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QTableView::item:pressed\n"
"{\n"
"    background: #33A4DF;\n"
"    color: #31363B;\n"
"}\n"
"\n"
"QTableView::item:selected:active\n"
"{\n"
"    background: #33A4DF;\n"
"    color: #31363B;\n"
"}\n"
"\n"
"QTableView::item:selected:hover\n"
"{\n"
"    background-color: #47b8f3;\n"
"    color: #31363B;\n"
"}\n"
"\n"
"QListView::item:pressed,\n"
"QTreeView::item:pressed\n"
"{\n"
"    background: #3daee9;\n"
"    color: #31363B;\n"
"}\n"
"\n"
"QTreeView::item:selected:active,\n"
"QListView::item:selected:active\n"
"{\n"
"    background: #3daee9;\n"
"    color: #31363B;\n"
"}\n"
"\n"
"QListView::item:selected:hover,\n"
"QTreeView::item:selected:hover\n"
"{\n"
"    background-color: #51c2fc;\n"
"    color: #31363B;\n"
"}\n"
"\n"
"\n"
"QHeaderView\n"
"{\n"
"    background-color: #EFF0F1;\n"
"    border: 0.1ex transparent;\n"
"    border-radius: 0px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: #EFF0F1;\n"
"    color: #31363B;\n"
"    padding: 0.5ex;\n"
"    border: 0.1ex solid #BAB9B8;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QHeaderView::section::vertical::first,\n"
"QHeaderView::section::vertical::only-one\n"
"{\n"
"    border-top: 0.1ex solid #BAB9B8;\n"
"}\n"
"\n"
"QHeaderView::section::vertical\n"
"{\n"
"    border-top: transparent;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal::first, QHeaderView::section::horizontal::only-one\n"
"{\n"
"    border-left: 0.1ex solid #BAB9B8;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal\n"
"{\n"
"    border-left: transparent;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked\n"
"\n"
" {\n"
"    color: black;\n"
"    background-color: #b9dae7;\n"
" }\n"
"\n"
" /* style the sort indicator */\n"
"QHeaderView::down-arrow\n"
"{\n"
"    image: url(:/light/down_arrow.svg);\n"
"}\n"
"\n"
"QHeaderView::up-arrow\n"
"{\n"
"    image: url(:/light/up_arrow.svg);\n"
"}\n"
"\n"
"QTableCornerButton::section\n"
"{\n"
"    background-color: #EFF0F1;\n"
"    border: 0.1ex transparent #BAB9B8;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QToolBox\n"
"{\n"
"    padding: 0.5ex;\n"
"    border: 0.1ex transparent black;\n"
"}\n"
"\n"
"QToolBox:selected\n"
"{\n"
"    background-color: #EFF0F1;\n"
"    border-color: #33A4DF;\n"
"}\n"
"\n"
"QToolBox:hover\n"
"{\n"
"    border-color: #33A4DF;\n"
"}\n"
"\n"
"QStatusBar::item\n"
"{\n"
"    border: 0px transparent dark;\n"
"}\n"
"\n"
"QSplitter::handle\n"
"{\n"
"    border: 0.1ex dashed #BAB9B8;\n"
"}\n"
"\n"
"QSplitter::handle:hover\n"
"{\n"
"    background-color: #787876;\n"
"    border: 0.1ex solid #BAB9B8;\n"
"}\n"
"\n"
"QSplitter::handle:horizontal\n"
"{\n"
"    width: 0.1ex;\n"
"}\n"
"\n"
"QSplitter::handle:vertical\n"
"{\n"
"    height: 0.1ex;\n"
"}\n"
"\n"
"QProgressBar:horizontal\n"
"{\n"
"    background-color: #BABEC2;\n"
"    border: 0.1ex solid #EFF0F1;\n"
"    border-radius: 0.3ex;\n"
"    height: 0.5ex;\n"
"    text-align: right;\n"
"    margin-top: 0.5ex;\n"
"    margin-bottom: 0.5ex;\n"
"    margin-right: 5ex;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QProgressBar::chunk:horizontal\n"
"{\n"
"    background-color: #33A4DF;\n"
"    border: 0.1ex transparent;\n"
"    border-radius: 0.3ex;\n"
"}\n"
"\n"
"QAbstractSpinBox\n"
"{\n"
"    background-color: #EFF0F1;\n"
"}\n"
"\n"
"QSpinBox,\n"
"QDoubleSpinBox\n"
"{\n"
"    padding-right: 1.5ex;\n"
"}\n"
"\n"
"QSpinBox::up-button,\n"
"QDoubleSpinBox::up-button\n"
"{\n"
"    subcontrol-origin: content;\n"
"    subcontrol-position: right top;\n"
"\n"
"    width: 1.6ex;\n"
"    border-width: 0.1ex;\n"
"}\n"
"\n"
"QSpinBox::up-arrow,\n"
"QDoubleSpinBox::up-arrow\n"
"{\n"
"    border-image: url(:/light/up_arrow.svg);\n"
"    width: 0.9ex;\n"
"    height: 0.6ex;\n"
"}\n"
"\n"
"QSpinBox::up-arrow:hover,\n"
"QSpinBox::up-arrow:pressed,\n"
"QDoubleSpinBox::up-arrow:hover,\n"
"QDoubleSpinBox::up-arrow:pressed\n"
"{\n"
"    border-image: url(:/light/up_arrow-hover.svg);\n"
"    width: 0.9ex;\n"
"    height: 0.6ex;\n"
"}\n"
"\n"
"QSpinBox::up-arrow:disabled,\n"
"QSpinBox::up-arrow:off,\n"
"QDoubleSpinBox::up-arrow:disabled,\n"
"QDoubleSpinBox::up-arrow:off\n"
"{\n"
"   border-image: url(:/light/up_arrow_disabled.svg);\n"
"}\n"
"\n"
"QSpinBox::down-button,\n"
"QDoubleSpinBox::down-button\n"
"{\n"
"    subcontrol-origin: content;\n"
"    subcontrol-position: right bottom;\n"
"\n"
"    width: 1.6ex;\n"
"    border-width: 0.1ex;\n"
"}\n"
"\n"
"QSpinBox::down-arrow,\n"
"QDoubleSpinBox::down-arrow\n"
"{\n"
"    border-image: url(:/light/down_arrow.svg);\n"
"    width: 0.9ex;\n"
"    height: 0.6ex;\n"
"}\n"
"\n"
"QSpinBox::down-arrow:hover,\n"
"QSpinBox::down-arrow:pressed,\n"
"QDoubleSpinBox::down-arrow:hover,\n"
"QDoubleSpinBox::down-arrow:pressed\n"
"{\n"
"    border-image: url(:/light/down_arrow-hover.svg);\n"
"    width: 0.9ex;\n"
"    height: 0.6ex;\n"
"}\n"
"\n"
"QSpinBox::down-arrow:disabled,\n"
"QSpinBox::down-arrow:off,\n"
"QDoubleSpinBox::down-arrow:disabled,\n"
"QDoubleSpinBox::down-arrow:off\n"
"{\n"
"   border-image: url(:/light/down_arrow_disabled.svg);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    border: 0.1ex solid #3daef3;\n"
"    color: #31363B;\n"
"}\n"
"\n"
"QPushButton:focus\n"
"{\n"
"    background-color: qlineargradient(x1: 0.5, y1: 0.5 x2: 0.5, y2: 1, stop: 0 #4cbdff, stop: 0.5 #33a4e8);\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:focus:hover\n"
"{\n"
"    background-color: qlineargradient(x1: 0.5, y1: 0.5 x2: 0.5, y2: 1, stop: 0 #bedfec, stop: 0.5 #b9dae7);\n"
"    color: #31363B;\n"
"}\n"
"\n"
"QPushButton:focus:pressed,\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: qlineargradient(x1: 0.5, y1: 0.5 x2: 0.5, y2: 1, stop: 0 #bedfec, stop: 0.5 #b9dae7);\n"
"    color: #31363B;\n"
"}\n"
"\n"
"")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        self.pushButton_86 = QtWidgets.QPushButton(self.tab_22)
        self.pushButton_86.setGeometry(QtCore.QRect(270, 560, 170, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_86.setFont(font)
        self.pushButton_86.setIcon(icon9)
        self.pushButton_86.setIconSize(QtCore.QSize(22, 22))
        self.pushButton_86.setObjectName("pushButton_86")
        self.checkBox_8.raise_()
        self.pushButton_40.raise_()
        self.pushButton_41.raise_()
        self.lineEdit_82.raise_()
        self.pushButton_82.raise_()
        self.spinBox_36.raise_()
        self.label_115.raise_()
        self.pushButton_81.raise_()
        self.pushButton_126.raise_()
        self.tableWidget_2.raise_()
        self.pushButton_86.raise_()
        self.comboBox_25.raise_()
        self.tabWidget_7.addTab(self.tab_22, "")
        self.tab_23 = QtWidgets.QWidget()
        self.tab_23.setObjectName("tab_23")
        self.pushButton_48 = QtWidgets.QPushButton(self.tab_23)
        self.pushButton_48.setGeometry(QtCore.QRect(730, 690, 190, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_48.setFont(font)
        self.pushButton_48.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_48.setIcon(icon5)
        self.pushButton_48.setIconSize(QtCore.QSize(100, 46))
        self.pushButton_48.setObjectName("pushButton_48")
        self.pushButton_49 = QtWidgets.QPushButton(self.tab_23)
        self.pushButton_49.setGeometry(QtCore.QRect(30, 700, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_49.setFont(font)
        self.pushButton_49.setObjectName("pushButton_49")
        self.pushButton_59 = QtWidgets.QPushButton(self.tab_23)
        self.pushButton_59.setGeometry(QtCore.QRect(360, 670, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_59.setFont(font)
        self.pushButton_59.setIcon(icon10)
        self.pushButton_59.setIconSize(QtCore.QSize(31, 31))
        self.pushButton_59.setObjectName("pushButton_59")
        self.textEdit_7 = QtWidgets.QTextEdit(self.tab_23)
        self.textEdit_7.setGeometry(QtCore.QRect(100, 150, 700, 120))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.textEdit_7.setFont(font)
        self.textEdit_7.setObjectName("textEdit_7")
        self.label_65 = QtWidgets.QLabel(self.tab_23)
        self.label_65.setGeometry(QtCore.QRect(670, 110, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_65.setFont(font)
        self.label_65.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_65.setObjectName("label_65")
        self.label_66 = QtWidgets.QLabel(self.tab_23)
        self.label_66.setGeometry(QtCore.QRect(670, 290, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_66.setFont(font)
        self.label_66.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_66.setObjectName("label_66")
        self.label_67 = QtWidgets.QLabel(self.tab_23)
        self.label_67.setGeometry(QtCore.QRect(670, 470, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_67.setFont(font)
        self.label_67.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_67.setObjectName("label_67")
        self.textEdit_8 = QtWidgets.QTextEdit(self.tab_23)
        self.textEdit_8.setGeometry(QtCore.QRect(100, 330, 700, 120))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.textEdit_8.setFont(font)
        self.textEdit_8.setObjectName("textEdit_8")
        self.textEdit_9 = QtWidgets.QTextEdit(self.tab_23)
        self.textEdit_9.setGeometry(QtCore.QRect(100, 510, 700, 120))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.textEdit_9.setFont(font)
        self.textEdit_9.setObjectName("textEdit_9")
        self.label_58 = QtWidgets.QLabel(self.tab_23)
        self.label_58.setGeometry(QtCore.QRect(250, 70, 330, 60))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_58.setFont(font)
        self.label_58.setStyleSheet("\n"
"QLabel\n"
"{\n"
"/*font: 75 16pt \"Arial Unicode MS\";*/\n"
"\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 17pt \"Hacen Maghreb Bd\";\n"
"\n"
"}")
        self.label_58.setAlignment(QtCore.Qt.AlignCenter)
        self.label_58.setObjectName("label_58")
        self.tabWidget_7.addTab(self.tab_23, "")
        self.tabWidget_5.addTab(self.tab_21, "")
        self.tab_24 = QtWidgets.QWidget()
        self.tab_24.setObjectName("tab_24")
        self.label_102 = QtWidgets.QLabel(self.tab_24)
        self.label_102.setGeometry(QtCore.QRect(320, 40, 320, 50))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_102.setFont(font)
        self.label_102.setStyleSheet("\n"
"QLabel\n"
"{\n"
"/*font: 75 16pt \"Arial Unicode MS\";*/\n"
"\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 17pt \"Hacen Maghreb Bd\";\n"
"\n"
"}")
        self.label_102.setAlignment(QtCore.Qt.AlignCenter)
        self.label_102.setObjectName("label_102")
        self.label_103 = QtWidgets.QLabel(self.tab_24)
        self.label_103.setGeometry(QtCore.QRect(660, 118, 140, 30))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_103.setFont(font)
        self.label_103.setStyleSheet("\n"
"QLabel\n"
"{\n"
"/*font: 75 16pt \"Arial Unicode MS\";*/\n"
"\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 17pt \"Hacen Maghreb Bd\";\n"
"\n"
"}")
        self.label_103.setObjectName("label_103")
        self.comboBox_12 = QtWidgets.QComboBox(self.tab_24)
        self.comboBox_12.setGeometry(QtCore.QRect(460, 118, 210, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_12.setFont(font)
        self.comboBox_12.setObjectName("comboBox_12")
        self.lineEdit_77 = QtWidgets.QLineEdit(self.tab_24)
        self.lineEdit_77.setGeometry(QtCore.QRect(200, 118, 240, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_77.setFont(font)
        self.lineEdit_77.setObjectName("lineEdit_77")
        self.label_104 = QtWidgets.QLabel(self.tab_24)
        self.label_104.setGeometry(QtCore.QRect(660, 198, 140, 40))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_104.setFont(font)
        self.label_104.setStyleSheet("\n"
"QLabel\n"
"{\n"
"/*font: 75 16pt \"Arial Unicode MS\";*/\n"
"\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 17pt \"Hacen Maghreb Bd\";\n"
"\n"
"}")
        self.label_104.setObjectName("label_104")
        self.lineEdit_78 = QtWidgets.QLineEdit(self.tab_24)
        self.lineEdit_78.setGeometry(QtCore.QRect(450, 198, 220, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_78.setFont(font)
        self.lineEdit_78.setPlaceholderText("")
        self.lineEdit_78.setObjectName("lineEdit_78")
        self.label_105 = QtWidgets.QLabel(self.tab_24)
        self.label_105.setGeometry(QtCore.QRect(310, 268, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_105.setFont(font)
        self.label_105.setStyleSheet("\n"
"QLabel\n"
"{\n"
"/*font: 75 16pt \"Arial Unicode MS\";*/\n"
"\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 17pt \"Hacen Maghreb Bd\";\n"
"\n"
"}")
        self.label_105.setAlignment(QtCore.Qt.AlignCenter)
        self.label_105.setObjectName("label_105")
        self.checkBox_9 = QtWidgets.QCheckBox(self.tab_24)
        self.checkBox_9.setGeometry(QtCore.QRect(650, 340, 170, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.checkBox_9.setFont(font)
        self.checkBox_9.setStyleSheet("font: 75 13pt \"Arial Unicode MS\";")
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QtWidgets.QCheckBox(self.tab_24)
        self.checkBox_10.setGeometry(QtCore.QRect(310, 340, 170, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.checkBox_10.setFont(font)
        self.checkBox_10.setStyleSheet("font: 75 13pt \"Arial Unicode MS\";")
        self.checkBox_10.setObjectName("checkBox_10")
        self.checkBox_11 = QtWidgets.QCheckBox(self.tab_24)
        self.checkBox_11.setGeometry(QtCore.QRect(480, 340, 170, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.checkBox_11.setFont(font)
        self.checkBox_11.setStyleSheet("font: 75 13pt \"Arial Unicode MS\";")
        self.checkBox_11.setObjectName("checkBox_11")
        self.checkBox_12 = QtWidgets.QCheckBox(self.tab_24)
        self.checkBox_12.setGeometry(QtCore.QRect(140, 340, 170, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.checkBox_12.setFont(font)
        self.checkBox_12.setStyleSheet("font: 75 13pt \"Arial Unicode MS\";")
        self.checkBox_12.setObjectName("checkBox_12")
        self.label_106 = QtWidgets.QLabel(self.tab_24)
        self.label_106.setGeometry(QtCore.QRect(670, 430, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_106.setFont(font)
        self.label_106.setStyleSheet("font: 75 16pt \"Arial Unicode MS\";")
        self.label_106.setObjectName("label_106")
        self.textEdit_10 = QtWidgets.QTextEdit(self.tab_24)
        self.textEdit_10.setGeometry(QtCore.QRect(140, 470, 660, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_10.setFont(font)
        self.textEdit_10.setObjectName("textEdit_10")
        self.pushButton_50 = QtWidgets.QPushButton(self.tab_24)
        self.pushButton_50.setGeometry(QtCore.QRect(32, 692, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_50.setFont(font)
        self.pushButton_50.setObjectName("pushButton_50")
        self.pushButton_71 = QtWidgets.QPushButton(self.tab_24)
        self.pushButton_71.setGeometry(QtCore.QRect(345, 146, 91, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_71.setFont(font)
        self.pushButton_71.setStyleSheet("image: url(:/ico/addf.png);")
        self.pushButton_71.setText("")
        self.pushButton_71.setObjectName("pushButton_71")
        self.pushButton_72 = QtWidgets.QPushButton(self.tab_24)
        self.pushButton_72.setGeometry(QtCore.QRect(205, 146, 91, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_72.setFont(font)
        self.pushButton_72.setStyleSheet("image: url(:/ico/removef.png);")
        self.pushButton_72.setText("")
        self.pushButton_72.setObjectName("pushButton_72")
        self.pushButton_131 = QtWidgets.QPushButton(self.tab_24)
        self.pushButton_131.setGeometry(QtCore.QRect(362, 682, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_131.setFont(font)
        self.pushButton_131.setIcon(icon10)
        self.pushButton_131.setIconSize(QtCore.QSize(31, 31))
        self.pushButton_131.setObjectName("pushButton_131")
        self.pushButton_53 = QtWidgets.QPushButton(self.tab_24)
        self.pushButton_53.setGeometry(QtCore.QRect(732, 682, 190, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_53.setFont(font)
        self.pushButton_53.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_53.setIcon(icon5)
        self.pushButton_53.setIconSize(QtCore.QSize(100, 46))
        self.pushButton_53.setObjectName("pushButton_53")
        self.pushButton_72.raise_()
        self.pushButton_71.raise_()
        self.label_102.raise_()
        self.label_103.raise_()
        self.comboBox_12.raise_()
        self.lineEdit_77.raise_()
        self.label_104.raise_()
        self.lineEdit_78.raise_()
        self.label_105.raise_()
        self.checkBox_9.raise_()
        self.checkBox_10.raise_()
        self.checkBox_11.raise_()
        self.checkBox_12.raise_()
        self.label_106.raise_()
        self.textEdit_10.raise_()
        self.pushButton_50.raise_()
        self.pushButton_131.raise_()
        self.pushButton_53.raise_()
        self.tabWidget_5.addTab(self.tab_24, "")
        self.tab_26 = QtWidgets.QWidget()
        self.tab_26.setObjectName("tab_26")
        self.label_126 = QtWidgets.QLabel(self.tab_26)
        self.label_126.setGeometry(QtCore.QRect(720, 190, 270, 30))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_126.setFont(font)
        self.label_126.setStyleSheet("\n"
"QLabel\n"
"{\n"
"/*font: 75 16pt \"Arial Unicode MS\";*/\n"
"\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 14pt \"Hacen Maghreb Bd\";\n"
"\n"
"}")
        self.label_126.setObjectName("label_126")
        self.lineEdit_85 = QtWidgets.QLineEdit(self.tab_26)
        self.lineEdit_85.setGeometry(QtCore.QRect(70, 270, 230, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_85.setFont(font)
        self.lineEdit_85.setObjectName("lineEdit_85")
        self.label_127 = QtWidgets.QLabel(self.tab_26)
        self.label_127.setGeometry(QtCore.QRect(220, 350, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_127.setFont(font)
        self.label_127.setStyleSheet("\n"
"QLabel\n"
"{\n"
"/*font: 75 16pt \"Arial Unicode MS\";*/\n"
"\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 14pt \"Hacen Maghreb Bd\";\n"
"\n"
"}")
        self.label_127.setObjectName("label_127")
        self.lineEdit_86 = QtWidgets.QLineEdit(self.tab_26)
        self.lineEdit_86.setGeometry(QtCore.QRect(520, 350, 230, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_86.setFont(font)
        self.lineEdit_86.setObjectName("lineEdit_86")
        self.label_128 = QtWidgets.QLabel(self.tab_26)
        self.label_128.setGeometry(QtCore.QRect(220, 270, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_128.setFont(font)
        self.label_128.setStyleSheet("\n"
"QLabel\n"
"{\n"
"/*font: 75 16pt \"Arial Unicode MS\";*/\n"
"\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 17pt \"Hacen Maghreb Bd\";\n"
"\n"
"}")
        self.label_128.setObjectName("label_128")
        self.lineEdit_87 = QtWidgets.QLineEdit(self.tab_26)
        self.lineEdit_87.setGeometry(QtCore.QRect(520, 270, 230, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_87.setFont(font)
        self.lineEdit_87.setObjectName("lineEdit_87")
        self.lineEdit_88 = QtWidgets.QLineEdit(self.tab_26)
        self.lineEdit_88.setGeometry(QtCore.QRect(520, 190, 230, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_88.setFont(font)
        self.lineEdit_88.setObjectName("lineEdit_88")
        self.label_129 = QtWidgets.QLabel(self.tab_26)
        self.label_129.setGeometry(QtCore.QRect(700, 510, 290, 30))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_129.setFont(font)
        self.label_129.setStyleSheet("\n"
"QLabel\n"
"{\n"
"/*font: 75 16pt \"Arial Unicode MS\";*/\n"
"\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 14pt \"Hacen Maghreb Bd\";\n"
"\n"
"}")
        self.label_129.setObjectName("label_129")
        self.label_130 = QtWidgets.QLabel(self.tab_26)
        self.label_130.setGeometry(QtCore.QRect(220, 430, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_130.setFont(font)
        self.label_130.setStyleSheet("\n"
"QLabel\n"
"{\n"
"/*font: 75 16pt \"Arial Unicode MS\";*/\n"
"\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 14pt \"Hacen Maghreb Bd\";\n"
"\n"
"}")
        self.label_130.setObjectName("label_130")
        self.lineEdit_89 = QtWidgets.QLineEdit(self.tab_26)
        self.lineEdit_89.setGeometry(QtCore.QRect(520, 510, 230, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_89.setFont(font)
        self.lineEdit_89.setObjectName("lineEdit_89")
        self.lineEdit_90 = QtWidgets.QLineEdit(self.tab_26)
        self.lineEdit_90.setGeometry(QtCore.QRect(70, 190, 230, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_90.setFont(font)
        self.lineEdit_90.setObjectName("lineEdit_90")
        self.label_131 = QtWidgets.QLabel(self.tab_26)
        self.label_131.setGeometry(QtCore.QRect(210, 190, 260, 30))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_131.setFont(font)
        self.label_131.setStyleSheet("\n"
"QLabel\n"
"{\n"
"/*font: 75 16pt \"Arial Unicode MS\";*/\n"
"\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 14pt \"Hacen Maghreb Bd\";\n"
"\n"
"}")
        self.label_131.setObjectName("label_131")
        self.label_75 = QtWidgets.QLabel(self.tab_26)
        self.label_75.setGeometry(QtCore.QRect(350, 60, 320, 50))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_75.setFont(font)
        self.label_75.setStyleSheet("\n"
"QLabel\n"
"{\n"
"/*font: 75 16pt \"Arial Unicode MS\";*/\n"
"\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 17pt \"Hacen Maghreb Bd\";\n"
"\n"
"}")
        self.label_75.setAlignment(QtCore.Qt.AlignCenter)
        self.label_75.setObjectName("label_75")
        self.lineEdit_91 = QtWidgets.QLineEdit(self.tab_26)
        self.lineEdit_91.setGeometry(QtCore.QRect(70, 430, 230, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_91.setFont(font)
        self.lineEdit_91.setObjectName("lineEdit_91")
        self.lineEdit_92 = QtWidgets.QLineEdit(self.tab_26)
        self.lineEdit_92.setGeometry(QtCore.QRect(70, 350, 230, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_92.setFont(font)
        self.lineEdit_92.setObjectName("lineEdit_92")
        self.label_132 = QtWidgets.QLabel(self.tab_26)
        self.label_132.setGeometry(QtCore.QRect(730, 350, 260, 30))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_132.setFont(font)
        self.label_132.setStyleSheet("\n"
"QLabel\n"
"{\n"
"/*font: 75 16pt \"Arial Unicode MS\";*/\n"
"\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 14pt \"Hacen Maghreb Bd\";\n"
"\n"
"}")
        self.label_132.setObjectName("label_132")
        self.label_133 = QtWidgets.QLabel(self.tab_26)
        self.label_133.setGeometry(QtCore.QRect(730, 270, 260, 30))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_133.setFont(font)
        self.label_133.setStyleSheet("\n"
"QLabel\n"
"{\n"
"/*font: 75 16pt \"Arial Unicode MS\";*/\n"
"\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 14pt \"Hacen Maghreb Bd\";\n"
"\n"
"}")
        self.label_133.setObjectName("label_133")
        self.label_134 = QtWidgets.QLabel(self.tab_26)
        self.label_134.setGeometry(QtCore.QRect(180, 510, 290, 30))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_134.setFont(font)
        self.label_134.setStyleSheet("\n"
"QLabel\n"
"{\n"
"/*font: 75 16pt \"Arial Unicode MS\";*/\n"
"\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 14pt \"Hacen Maghreb Bd\";\n"
"\n"
"}")
        self.label_134.setObjectName("label_134")
        self.lineEdit_93 = QtWidgets.QLineEdit(self.tab_26)
        self.lineEdit_93.setGeometry(QtCore.QRect(70, 510, 230, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_93.setFont(font)
        self.lineEdit_93.setObjectName("lineEdit_93")
        self.lineEdit_94 = QtWidgets.QLineEdit(self.tab_26)
        self.lineEdit_94.setGeometry(QtCore.QRect(520, 430, 230, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_94.setFont(font)
        self.lineEdit_94.setObjectName("lineEdit_94")
        self.label_135 = QtWidgets.QLabel(self.tab_26)
        self.label_135.setGeometry(QtCore.QRect(700, 430, 290, 30))
        font = QtGui.QFont()
        font.setFamily("Hacen Maghreb Bd")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_135.setFont(font)
        self.label_135.setStyleSheet("\n"
"QLabel\n"
"{\n"
"/*font: 75 16pt \"Arial Unicode MS\";*/\n"
"\n"
"    border: 1px solid;\n"
"    border-radius: 2px;\n"
"\n"
"    border-radius: 6;\n"
"\n"
"    border: 1px solid black;\n"
"    border-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"    font: 14pt \"Hacen Maghreb Bd\";\n"
"\n"
"}")
        self.label_135.setObjectName("label_135")
        self.pushButton_132 = QtWidgets.QPushButton(self.tab_26)
        self.pushButton_132.setGeometry(QtCore.QRect(400, 640, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_132.setFont(font)
        self.pushButton_132.setIcon(icon10)
        self.pushButton_132.setIconSize(QtCore.QSize(31, 31))
        self.pushButton_132.setObjectName("pushButton_132")
        self.pushButton_51 = QtWidgets.QPushButton(self.tab_26)
        self.pushButton_51.setGeometry(QtCore.QRect(32, 692, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_51.setFont(font)
        self.pushButton_51.setObjectName("pushButton_51")
        self.label_126.raise_()
        self.label_127.raise_()
        self.label_128.raise_()
        self.lineEdit_88.raise_()
        self.label_129.raise_()
        self.label_130.raise_()
        self.lineEdit_89.raise_()
        self.label_131.raise_()
        self.label_75.raise_()
        self.lineEdit_91.raise_()
        self.lineEdit_92.raise_()
        self.label_132.raise_()
        self.label_133.raise_()
        self.label_134.raise_()
        self.lineEdit_93.raise_()
        self.label_135.raise_()
        self.lineEdit_90.raise_()
        self.lineEdit_85.raise_()
        self.lineEdit_86.raise_()
        self.lineEdit_87.raise_()
        self.lineEdit_94.raise_()
        self.pushButton_132.raise_()
        self.pushButton_51.raise_()
        self.tabWidget_5.addTab(self.tab_26, "")
        self.tabWidget.addTab(self.tab_15, "")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(1000, -10, 220, 850))
        self.groupBox_5.setStyleSheet("background-color: rgba(233, 237, 242, 224);")
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_53 = QtWidgets.QLabel(self.groupBox_5)
        self.label_53.setGeometry(QtCore.QRect(0, 580, 220, 190))
        self.label_53.setStyleSheet("image: url(:/ico/pic.png);")
        self.label_53.setText("")
        self.label_53.setObjectName("label_53")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(940, 240, 280, 60))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_3.setStyleSheet("\n"
"\n"
"QPushButton\n"
"{\n"
"    background-color: rgb(233, 237, 242);\n"
"    color: rgb(75, 76, 78);\n"
"    border: 1px ;  \n"
"}\n"
"\n"
"QPushButton::hover\n"
"{\n"
"    background-color: rgb(247, 249, 250);\n"
"    color: rgb(75, 76, 78);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"    background-color: #fff;\n"
"    color: rgb(75, 76, 78);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.pushButton_3.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Egypt))
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/ico/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon12)
        self.pushButton_3.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(990, 420, 230, 60))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_2.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(233, 237, 242);\n"
"    color: rgb(75, 76, 78);\n"
"    border: 1px ;  \n"
"}\n"
"\n"
"QPushButton::hover\n"
"{\n"
"    background-color: rgb(247, 249, 250);\n"
"    color: rgb(75, 76, 78);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"    background-color: #fff;\n"
"    color: rgb(75, 76, 78);\n"
"}\n"
"")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/ico/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon13)
        self.pushButton_2.setIconSize(QtCore.QSize(46, 48))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(950, 330, 270, 60))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(233, 237, 242);\n"
"    color: rgb(75, 76, 78);\n"
"    border: 1px ;  \n"
"}\n"
"\n"
"QPushButton::hover\n"
"{\n"
"    background-color: rgb(247, 249, 250);\n"
"    color: rgb(75, 76, 78);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"    background-color: #fff;\n"
"    color: rgb(75, 76, 78);\n"
"}\n"
"")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/ico/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon14)
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setObjectName("pushButton")
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(1219, -10, 270, 850))
        self.groupBox_6.setStyleSheet("background-color: rgba(233, 237, 242, 224);")
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.groupBox_5.raise_()
        self.pushButton_3.raise_()
        self.pushButton_2.raise_()
        self.pushButton.raise_()
        self.tabWidget.raise_()
        self.groupBox_6.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(4)
        self.tabWidget_2.setCurrentIndex(5)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget_4.setCurrentIndex(0)
        self.tabWidget_5.setCurrentIndex(4)
        self.tabWidget_6.setCurrentIndex(1)
        self.tabWidget_7.setCurrentIndex(1)
        self.radioButton_8.toggled['bool'].connect(self.lineEdit_101.setEnabled)
        self.radioButton_8.clicked['bool'].connect(self.lineEdit_101.setEnabled)
        self.radioButton_6.toggled['bool'].connect(self.lineEdit_21.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit_58, self.lineEdit_59)
        MainWindow.setTabOrder(self.lineEdit_59, self.lineEdit_60)
        MainWindow.setTabOrder(self.lineEdit_60, self.lineEdit_61)
        MainWindow.setTabOrder(self.lineEdit_61, self.lineEdit_83)
        MainWindow.setTabOrder(self.lineEdit_83, self.lineEdit_62)
        MainWindow.setTabOrder(self.lineEdit_62, self.lineEdit_63)
        MainWindow.setTabOrder(self.lineEdit_63, self.lineEdit_64)
        MainWindow.setTabOrder(self.lineEdit_64, self.lineEdit_65)
        MainWindow.setTabOrder(self.lineEdit_65, self.lineEdit_84)
        MainWindow.setTabOrder(self.lineEdit_84, self.pushButton_77)
        MainWindow.setTabOrder(self.pushButton_77, self.pushButton_54)
        MainWindow.setTabOrder(self.pushButton_54, self.pushButton_45)
        MainWindow.setTabOrder(self.pushButton_45, self.pushButton_46)
        MainWindow.setTabOrder(self.pushButton_46, self.lineEdit_38)
        MainWindow.setTabOrder(self.lineEdit_38, self.comboBox_21)
        MainWindow.setTabOrder(self.comboBox_21, self.pushButton_26)
        MainWindow.setTabOrder(self.pushButton_26, self.pushButton_24)
        MainWindow.setTabOrder(self.pushButton_24, self.lineEdit_16)
        MainWindow.setTabOrder(self.lineEdit_16, self.lineEdit_2)
        MainWindow.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        MainWindow.setTabOrder(self.lineEdit_3, self.lineEdit_4)
        MainWindow.setTabOrder(self.lineEdit_4, self.lineEdit_5)
        MainWindow.setTabOrder(self.lineEdit_5, self.lineEdit_6)
        MainWindow.setTabOrder(self.lineEdit_6, self.lineEdit_7)
        MainWindow.setTabOrder(self.lineEdit_7, self.comboBox_20)
        MainWindow.setTabOrder(self.comboBox_20, self.lineEdit_12)
        MainWindow.setTabOrder(self.lineEdit_12, self.lineEdit_13)
        MainWindow.setTabOrder(self.lineEdit_13, self.lineEdit_9)
        MainWindow.setTabOrder(self.lineEdit_9, self.lineEdit_14)
        MainWindow.setTabOrder(self.lineEdit_14, self.lineEdit_15)
        MainWindow.setTabOrder(self.lineEdit_15, self.lineEdit_11)
        MainWindow.setTabOrder(self.lineEdit_11, self.comboBox_19)
        MainWindow.setTabOrder(self.comboBox_19, self.pushButton_5)
        MainWindow.setTabOrder(self.pushButton_5, self.lineEdit_80)
        MainWindow.setTabOrder(self.lineEdit_80, self.pushButton_66)
        MainWindow.setTabOrder(self.pushButton_66, self.pushButton_65)
        MainWindow.setTabOrder(self.pushButton_65, self.textEdit)
        MainWindow.setTabOrder(self.textEdit, self.comboBox)
        MainWindow.setTabOrder(self.comboBox, self.comboBox_2)
        MainWindow.setTabOrder(self.comboBox_2, self.lineEdit_19)
        MainWindow.setTabOrder(self.lineEdit_19, self.lineEdit_20)
        MainWindow.setTabOrder(self.lineEdit_20, self.radioButton)
        MainWindow.setTabOrder(self.radioButton, self.radioButton_2)
        MainWindow.setTabOrder(self.radioButton_2, self.radioButton_4)
        MainWindow.setTabOrder(self.radioButton_4, self.radioButton_3)
        MainWindow.setTabOrder(self.radioButton_3, self.radioButton_5)
        MainWindow.setTabOrder(self.radioButton_5, self.radioButton_6)
        MainWindow.setTabOrder(self.radioButton_6, self.lineEdit_21)
        MainWindow.setTabOrder(self.lineEdit_21, self.comboBox_3)
        MainWindow.setTabOrder(self.comboBox_3, self.lineEdit_24)
        MainWindow.setTabOrder(self.lineEdit_24, self.lineEdit_23)
        MainWindow.setTabOrder(self.lineEdit_23, self.pushButton_7)
        MainWindow.setTabOrder(self.pushButton_7, self.pushButton_6)
        MainWindow.setTabOrder(self.pushButton_6, self.lineEdit_17)
        MainWindow.setTabOrder(self.lineEdit_17, self.pushButton_20)
        MainWindow.setTabOrder(self.pushButton_20, self.pushButton_22)
        MainWindow.setTabOrder(self.pushButton_22, self.lineEdit_18)
        MainWindow.setTabOrder(self.lineEdit_18, self.pushButton_21)
        MainWindow.setTabOrder(self.pushButton_21, self.pushButton_23)
        MainWindow.setTabOrder(self.pushButton_23, self.lineEdit_22)
        MainWindow.setTabOrder(self.lineEdit_22, self.pushButton_76)
        MainWindow.setTabOrder(self.pushButton_76, self.pushButton_75)
        MainWindow.setTabOrder(self.pushButton_75, self.lineEdit_26)
        MainWindow.setTabOrder(self.lineEdit_26, self.lineEdit_25)
        MainWindow.setTabOrder(self.lineEdit_25, self.comboBox_4)
        MainWindow.setTabOrder(self.comboBox_4, self.lineEdit_29)
        MainWindow.setTabOrder(self.lineEdit_29, self.lineEdit_28)
        MainWindow.setTabOrder(self.lineEdit_28, self.comboBox_15)
        MainWindow.setTabOrder(self.comboBox_15, self.pushButton_10)
        MainWindow.setTabOrder(self.pushButton_10, self.pushButton_9)
        MainWindow.setTabOrder(self.pushButton_9, self.checkBox)
        MainWindow.setTabOrder(self.checkBox, self.pushButton_8)
        MainWindow.setTabOrder(self.pushButton_8, self.lineEdit_27)
        MainWindow.setTabOrder(self.lineEdit_27, self.pushButton_19)
        MainWindow.setTabOrder(self.pushButton_19, self.pushButton_60)
        MainWindow.setTabOrder(self.pushButton_60, self.lineEdit_32)
        MainWindow.setTabOrder(self.lineEdit_32, self.lineEdit_31)
        MainWindow.setTabOrder(self.lineEdit_31, self.lineEdit_35)
        MainWindow.setTabOrder(self.lineEdit_35, self.comboBox_5)
        MainWindow.setTabOrder(self.comboBox_5, self.lineEdit_34)
        MainWindow.setTabOrder(self.lineEdit_34, self.lineEdit_30)
        MainWindow.setTabOrder(self.lineEdit_30, self.comboBox_22)
        MainWindow.setTabOrder(self.comboBox_22, self.pushButton_11)
        MainWindow.setTabOrder(self.pushButton_11, self.pushButton_13)
        MainWindow.setTabOrder(self.pushButton_13, self.pushButton_12)
        MainWindow.setTabOrder(self.pushButton_12, self.lineEdit_33)
        MainWindow.setTabOrder(self.lineEdit_33, self.pushButton_68)
        MainWindow.setTabOrder(self.pushButton_68, self.pushButton_67)
        MainWindow.setTabOrder(self.pushButton_67, self.lineEdit_81)
        MainWindow.setTabOrder(self.lineEdit_81, self.pushButton_80)
        MainWindow.setTabOrder(self.pushButton_80, self.pushButton_125)
        MainWindow.setTabOrder(self.pushButton_125, self.comboBox_24)
        MainWindow.setTabOrder(self.comboBox_24, self.spinBox_35)
        MainWindow.setTabOrder(self.spinBox_35, self.pushButton_79)
        MainWindow.setTabOrder(self.pushButton_79, self.pushButton_85)
        MainWindow.setTabOrder(self.pushButton_85, self.pushButton_15)
        MainWindow.setTabOrder(self.pushButton_15, self.checkBox_2)
        MainWindow.setTabOrder(self.checkBox_2, self.pushButton_14)
        MainWindow.setTabOrder(self.pushButton_14, self.textEdit_2)
        MainWindow.setTabOrder(self.textEdit_2, self.textEdit_3)
        MainWindow.setTabOrder(self.textEdit_3, self.textEdit_4)
        MainWindow.setTabOrder(self.textEdit_4, self.pushButton_17)
        MainWindow.setTabOrder(self.pushButton_17, self.pushButton_16)
        MainWindow.setTabOrder(self.pushButton_16, self.comboBox_6)
        MainWindow.setTabOrder(self.comboBox_6, self.lineEdit_37)
        MainWindow.setTabOrder(self.lineEdit_37, self.checkBox_3)
        MainWindow.setTabOrder(self.checkBox_3, self.checkBox_5)
        MainWindow.setTabOrder(self.checkBox_5, self.checkBox_4)
        MainWindow.setTabOrder(self.checkBox_4, self.checkBox_6)
        MainWindow.setTabOrder(self.checkBox_6, self.textEdit_5)
        MainWindow.setTabOrder(self.textEdit_5, self.pushButton_18)
        MainWindow.setTabOrder(self.pushButton_18, self.lineEdit_36)
        MainWindow.setTabOrder(self.lineEdit_36, self.pushButton_70)
        MainWindow.setTabOrder(self.pushButton_70, self.pushButton_69)
        MainWindow.setTabOrder(self.pushButton_69, self.lineEdit_57)
        MainWindow.setTabOrder(self.lineEdit_57, self.comboBox_13)
        MainWindow.setTabOrder(self.comboBox_13, self.pushButton_52)
        MainWindow.setTabOrder(self.pushButton_52, self.lineEdit_49)
        MainWindow.setTabOrder(self.lineEdit_49, self.lineEdit_50)
        MainWindow.setTabOrder(self.lineEdit_50, self.lineEdit_42)
        MainWindow.setTabOrder(self.lineEdit_42, self.lineEdit_53)
        MainWindow.setTabOrder(self.lineEdit_53, self.lineEdit_54)
        MainWindow.setTabOrder(self.lineEdit_54, self.lineEdit_46)
        MainWindow.setTabOrder(self.lineEdit_46, self.comboBox_17)
        MainWindow.setTabOrder(self.comboBox_17, self.lineEdit_51)
        MainWindow.setTabOrder(self.lineEdit_51, self.lineEdit_48)
        MainWindow.setTabOrder(self.lineEdit_48, self.lineEdit_44)
        MainWindow.setTabOrder(self.lineEdit_44, self.lineEdit_47)
        MainWindow.setTabOrder(self.lineEdit_47, self.lineEdit_43)
        MainWindow.setTabOrder(self.lineEdit_43, self.lineEdit_56)
        MainWindow.setTabOrder(self.lineEdit_56, self.comboBox_18)
        MainWindow.setTabOrder(self.comboBox_18, self.pushButton_84)
        MainWindow.setTabOrder(self.pushButton_84, self.pushButton_27)
        MainWindow.setTabOrder(self.pushButton_27, self.lineEdit_79)
        MainWindow.setTabOrder(self.lineEdit_79, self.pushButton_63)
        MainWindow.setTabOrder(self.pushButton_63, self.pushButton_64)
        MainWindow.setTabOrder(self.pushButton_64, self.textEdit_6)
        MainWindow.setTabOrder(self.textEdit_6, self.comboBox_9)
        MainWindow.setTabOrder(self.comboBox_9, self.comboBox_8)
        MainWindow.setTabOrder(self.comboBox_8, self.lineEdit_106)
        MainWindow.setTabOrder(self.lineEdit_106, self.lineEdit_103)
        MainWindow.setTabOrder(self.lineEdit_103, self.radioButton_18)
        MainWindow.setTabOrder(self.radioButton_18, self.radioButton_17)
        MainWindow.setTabOrder(self.radioButton_17, self.radioButton_19)
        MainWindow.setTabOrder(self.radioButton_19, self.radioButton_20)
        MainWindow.setTabOrder(self.radioButton_20, self.radioButton_7)
        MainWindow.setTabOrder(self.radioButton_7, self.radioButton_8)
        MainWindow.setTabOrder(self.radioButton_8, self.lineEdit_101)
        MainWindow.setTabOrder(self.lineEdit_101, self.comboBox_7)
        MainWindow.setTabOrder(self.comboBox_7, self.lineEdit_105)
        MainWindow.setTabOrder(self.lineEdit_105, self.lineEdit_102)
        MainWindow.setTabOrder(self.lineEdit_102, self.pushButton_118)
        MainWindow.setTabOrder(self.pushButton_118, self.pushButton_29)
        MainWindow.setTabOrder(self.pushButton_29, self.pushButton_28)
        MainWindow.setTabOrder(self.pushButton_28, self.lineEdit_104)
        MainWindow.setTabOrder(self.lineEdit_104, self.pushButton_113)
        MainWindow.setTabOrder(self.pushButton_113, self.pushButton_116)
        MainWindow.setTabOrder(self.pushButton_116, self.lineEdit_107)
        MainWindow.setTabOrder(self.lineEdit_107, self.pushButton_115)
        MainWindow.setTabOrder(self.pushButton_115, self.pushButton_33)
        MainWindow.setTabOrder(self.pushButton_33, self.lineEdit_108)
        MainWindow.setTabOrder(self.lineEdit_108, self.pushButton_114)
        MainWindow.setTabOrder(self.pushButton_114, self.pushButton_117)
        MainWindow.setTabOrder(self.pushButton_117, self.lineEdit_109)
        MainWindow.setTabOrder(self.lineEdit_109, self.pushButton_56)
        MainWindow.setTabOrder(self.pushButton_56, self.lineEdit_68)
        MainWindow.setTabOrder(self.lineEdit_68, self.lineEdit_70)
        MainWindow.setTabOrder(self.lineEdit_70, self.comboBox_10)
        MainWindow.setTabOrder(self.comboBox_10, self.lineEdit_66)
        MainWindow.setTabOrder(self.lineEdit_66, self.lineEdit_67)
        MainWindow.setTabOrder(self.lineEdit_67, self.comboBox_16)
        MainWindow.setTabOrder(self.comboBox_16, self.pushButton_34)
        MainWindow.setTabOrder(self.pushButton_34, self.checkBox_7)
        MainWindow.setTabOrder(self.checkBox_7, self.pushButton_36)
        MainWindow.setTabOrder(self.pushButton_36, self.pushButton_35)
        MainWindow.setTabOrder(self.pushButton_35, self.pushButton_57)
        MainWindow.setTabOrder(self.pushButton_57, self.lineEdit_69)
        MainWindow.setTabOrder(self.lineEdit_69, self.pushButton_62)
        MainWindow.setTabOrder(self.pushButton_62, self.pushButton_61)
        MainWindow.setTabOrder(self.pushButton_61, self.lineEdit_110)
        MainWindow.setTabOrder(self.lineEdit_110, self.pushButton_119)
        MainWindow.setTabOrder(self.pushButton_119, self.lineEdit_73)
        MainWindow.setTabOrder(self.lineEdit_73, self.lineEdit_72)
        MainWindow.setTabOrder(self.lineEdit_72, self.lineEdit_76)
        MainWindow.setTabOrder(self.lineEdit_76, self.comboBox_11)
        MainWindow.setTabOrder(self.comboBox_11, self.lineEdit_75)
        MainWindow.setTabOrder(self.lineEdit_75, self.lineEdit_74)
        MainWindow.setTabOrder(self.lineEdit_74, self.comboBox_23)
        MainWindow.setTabOrder(self.comboBox_23, self.pushButton_37)
        MainWindow.setTabOrder(self.pushButton_37, self.pushButton_38)
        MainWindow.setTabOrder(self.pushButton_38, self.pushButton_39)
        MainWindow.setTabOrder(self.pushButton_39, self.pushButton_58)
        MainWindow.setTabOrder(self.pushButton_58, self.lineEdit_71)
        MainWindow.setTabOrder(self.lineEdit_71, self.pushButton_73)
        MainWindow.setTabOrder(self.pushButton_73, self.pushButton_74)
        MainWindow.setTabOrder(self.pushButton_74, self.lineEdit_82)
        MainWindow.setTabOrder(self.lineEdit_82, self.pushButton_82)
        MainWindow.setTabOrder(self.pushButton_82, self.pushButton_126)
        MainWindow.setTabOrder(self.pushButton_126, self.comboBox_25)
        MainWindow.setTabOrder(self.comboBox_25, self.spinBox_36)
        MainWindow.setTabOrder(self.spinBox_36, self.pushButton_81)
        MainWindow.setTabOrder(self.pushButton_81, self.pushButton_86)
        MainWindow.setTabOrder(self.pushButton_86, self.tableWidget_2)
        MainWindow.setTabOrder(self.tableWidget_2, self.checkBox_8)
        MainWindow.setTabOrder(self.checkBox_8, self.pushButton_41)
        MainWindow.setTabOrder(self.pushButton_41, self.pushButton_40)
        MainWindow.setTabOrder(self.pushButton_40, self.textEdit_7)
        MainWindow.setTabOrder(self.textEdit_7, self.textEdit_8)
        MainWindow.setTabOrder(self.textEdit_8, self.textEdit_9)
        MainWindow.setTabOrder(self.textEdit_9, self.pushButton_59)
        MainWindow.setTabOrder(self.pushButton_59, self.pushButton_48)
        MainWindow.setTabOrder(self.pushButton_48, self.pushButton_49)
        MainWindow.setTabOrder(self.pushButton_49, self.comboBox_12)
        MainWindow.setTabOrder(self.comboBox_12, self.lineEdit_78)
        MainWindow.setTabOrder(self.lineEdit_78, self.checkBox_9)
        MainWindow.setTabOrder(self.checkBox_9, self.checkBox_11)
        MainWindow.setTabOrder(self.checkBox_11, self.checkBox_10)
        MainWindow.setTabOrder(self.checkBox_10, self.checkBox_12)
        MainWindow.setTabOrder(self.checkBox_12, self.textEdit_10)
        MainWindow.setTabOrder(self.textEdit_10, self.pushButton_50)
        MainWindow.setTabOrder(self.pushButton_50, self.lineEdit_77)
        MainWindow.setTabOrder(self.lineEdit_77, self.pushButton_71)
        MainWindow.setTabOrder(self.pushButton_71, self.pushButton_72)
        MainWindow.setTabOrder(self.pushButton_72, self.pushButton_3)
        MainWindow.setTabOrder(self.pushButton_3, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.tabWidget_7)
        MainWindow.setTabOrder(self.tabWidget_7, self.tabWidget_4)
        MainWindow.setTabOrder(self.tabWidget_4, self.tableWidget)
        MainWindow.setTabOrder(self.tableWidget, self.tabWidget_2)
        MainWindow.setTabOrder(self.tabWidget_2, self.tabWidget_6)
        MainWindow.setTabOrder(self.tabWidget_6, self.tabWidget_5)
        MainWindow.setTabOrder(self.tabWidget_5, self.tabWidget_3)
        MainWindow.setTabOrder(self.tabWidget_3, self.tabWidget)
        MainWindow.setTabOrder(self.tabWidget, self.pushButton_130)
        MainWindow.setTabOrder(self.pushButton_130, self.pushButton_131)
        MainWindow.setTabOrder(self.pushButton_131, self.lineEdit_40)
        MainWindow.setTabOrder(self.lineEdit_40, self.lineEdit_39)
        MainWindow.setTabOrder(self.lineEdit_39, self.lineEdit_112)
        MainWindow.setTabOrder(self.lineEdit_112, self.lineEdit_41)
        MainWindow.setTabOrder(self.lineEdit_41, self.pushButton_83)
        MainWindow.setTabOrder(self.pushButton_83, self.lineEdit)
        MainWindow.setTabOrder(self.lineEdit, self.lineEdit_1)
        MainWindow.setTabOrder(self.lineEdit_1, self.pushButton_42)
        MainWindow.setTabOrder(self.pushButton_42, self.pushButton_44)
        MainWindow.setTabOrder(self.pushButton_44, self.pushButton_43)
        MainWindow.setTabOrder(self.pushButton_43, self.lineEdit_85)
        MainWindow.setTabOrder(self.lineEdit_85, self.lineEdit_86)
        MainWindow.setTabOrder(self.lineEdit_86, self.lineEdit_87)
        MainWindow.setTabOrder(self.lineEdit_87, self.lineEdit_88)
        MainWindow.setTabOrder(self.lineEdit_88, self.lineEdit_89)
        MainWindow.setTabOrder(self.lineEdit_89, self.lineEdit_90)
        MainWindow.setTabOrder(self.lineEdit_90, self.lineEdit_91)
        MainWindow.setTabOrder(self.lineEdit_91, self.lineEdit_92)
        MainWindow.setTabOrder(self.lineEdit_92, self.lineEdit_93)
        MainWindow.setTabOrder(self.lineEdit_93, self.lineEdit_94)
        MainWindow.setTabOrder(self.lineEdit_94, self.pushButton_132)
        MainWindow.setTabOrder(self.pushButton_132, self.pushButton_51)
        MainWindow.setTabOrder(self.pushButton_51, self.pushButton_53)
        MainWindow.setTabOrder(self.pushButton_53, self.pushButton_47)
        MainWindow.setTabOrder(self.pushButton_47, self.lineEdit_55)
        MainWindow.setTabOrder(self.lineEdit_55, self.pushButton_25)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit_39.setPlaceholderText(_translate("MainWindow", "Password"))
        self.pushButton_44.setText(_translate("MainWindow", " اضافة مستخدم"))
        self.lineEdit_40.setPlaceholderText(_translate("MainWindow", "User Name"))
        self.label_54.setText(_translate("MainWindow", "اسم المستخدم"))
        self.label_55.setText(_translate("MainWindow", "كلمة السر"))
        self.lineEdit_41.setPlaceholderText(_translate("MainWindow", "Ex@mail.com"))
        self.label_56.setText(_translate("MainWindow", "الايميل"))
        self.label_57.setText(_translate("MainWindow", "عدد المستخدمين"))
        self.pushButton_83.setText(_translate("MainWindow", " بدأ البرنامج"))
        self.label_29.setText(_translate("MainWindow", "           قاعدة بيانات خدمة الأنبا ابرام"))
        self.label_69.setText(_translate("MainWindow", "كلمة السر مرة اخري"))
        self.lineEdit_112.setPlaceholderText(_translate("MainWindow", "Password Again"))
        self.label_28.setText(_translate("MainWindow", "By Kamal ayman "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_14), _translate("MainWindow", "new user"))
        self.label_19.setText(_translate("MainWindow", "اسم المستخدم"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "User Name"))
        self.label_20.setText(_translate("MainWindow", "كلمة السر"))
        self.pushButton_42.setText(_translate("MainWindow", "تسجيل دخول"))
        self.lineEdit_1.setPlaceholderText(_translate("MainWindow", "Password"))
        self.pushButton_43.setText(_translate("MainWindow", "هل نسيت كلمة السر؟"))
        self.label_27.setText(_translate("MainWindow", "By Kamal ayman "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "login"))
        self.pushButton_45.setText(_translate("MainWindow", "ارسال رسالة مجددا"))
        self.pushButton_46.setText(_translate("MainWindow", "اعادة تسجيل دخول"))
        self.label_24.setText(_translate("MainWindow", "   الايميل"))
        self.pushButton_47.setText(_translate("MainWindow", "ارسل الي الجيميل"))
        self.label_31.setText(_translate("MainWindow", "           قاعدة بيانات خدمة الأنبا ابرام"))
        self.label_93.setText(_translate("MainWindow", "By Kamal ayman "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.comboBox_21.setCurrentText(_translate("MainWindow", "رقم الأسرة "))
        self.comboBox_21.setItemText(0, _translate("MainWindow", "رقم الأسرة "))
        self.comboBox_21.setItemText(1, _translate("MainWindow", "الرقم القومي"))
        self.pushButton_24.setText(_translate("MainWindow", "  فتح الملف"))
        self.pushButton_26.setText(_translate("MainWindow", " طباعة"))
        self.label_30.setText(_translate("MainWindow", "           قاعدة بيانات خدمة الأنبا ابرام"))
        self.label_94.setText(_translate("MainWindow", "By Kamal ayman "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_13), _translate("MainWindow", "show"))
        self.label_2.setText(_translate("MainWindow", "بيانات الزوج"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "       الرقم القومي 14 رقم"))
        self.lineEdit_15.setPlaceholderText(_translate("MainWindow", "                  المرتب"))
        self.lineEdit_9.setPlaceholderText(_translate("MainWindow", "       الرقم القومي 14 رقم"))
        self.lineEdit_7.setPlaceholderText(_translate("MainWindow", "               رقم الهاتف "))
        self.lineEdit_14.setPlaceholderText(_translate("MainWindow", "                  الوظيفة"))
        self.lineEdit_13.setPlaceholderText(_translate("MainWindow", "             أسم الشهرة "))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "                   الأسم "))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "             أسم الشهرة "))
        self.label_3.setText(_translate("MainWindow", "بيانات الزوجة"))
        self.lineEdit_12.setPlaceholderText(_translate("MainWindow", "                   الأسم "))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "                  الوظيفة"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "                  المرتب"))
        self.lineEdit_11.setPlaceholderText(_translate("MainWindow", "               رقم الهاتف "))
        self.pushButton_5.setText(_translate("MainWindow", "       التالي"))
        self.label_4.setText(_translate("MainWindow", "رقم الأسرة "))
        self.label_109.setText(_translate("MainWindow", "أب الأعتراف"))
        self.lineEdit_80.setPlaceholderText(_translate("MainWindow", "    اسم أب أعتراف"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "add client"))
        self.lineEdit_17.setPlaceholderText(_translate("MainWindow", "                اضافة محفظة "))
        self.lineEdit_18.setPlaceholderText(_translate("MainWindow", "                  اضافة حي "))
        self.radioButton_2.setText(_translate("MainWindow", "ايجار قديم"))
        self.radioButton.setText(_translate("MainWindow", "تمليك"))
        self.radioButton_4.setText(_translate("MainWindow", "ايجار جديد "))
        self.radioButton_3.setText(_translate("MainWindow", "مع الاسرة"))
        self.pushButton_6.setText(_translate("MainWindow", "رجوع"))
        self.pushButton_7.setText(_translate("MainWindow", "       التالي"))
        self.lineEdit_22.setPlaceholderText(_translate("MainWindow", "             اضافة عنوان "))
        self.label_13.setText(_translate("MainWindow", "تليفون "))
        self.label_70.setText(_translate("MainWindow", "الحي"))
        self.label_71.setText(_translate("MainWindow", "أسم الكنيسة :"))
        self.label_72.setText(_translate("MainWindow", "المحافظة "))
        self.label_76.setText(_translate("MainWindow", "علامة مميزة "))
        self.label_79.setText(_translate("MainWindow", "السكن "))
        self.label_89.setText(_translate("MainWindow", "العنوان بالتفصيل :"))
        self.label_90.setText(_translate("MainWindow", "العنوان"))
        self.label_91.setText(_translate("MainWindow", "موبايل "))
        self.label_92.setText(_translate("MainWindow", "المنطقة "))
        self.lineEdit_21.setText(_translate("MainWindow", "كنيسة "))
        self.radioButton_5.setText(_translate("MainWindow", "كنيسة الشهيد العظيم مارمينا والقديس البابا كيرلس السادس"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MainWindow", "next 1"))
        self.lineEdit_29.setPlaceholderText(_translate("MainWindow", "             السنة الدراسية او الوظيفة"))
        self.lineEdit_28.setPlaceholderText(_translate("MainWindow", "                    الدخل الشهري"))
        self.lineEdit_26.setPlaceholderText(_translate("MainWindow", "                          الأسم "))
        self.checkBox.setText(_translate("MainWindow", "اشخاص اخري تقيم مع الأسرة"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "اعزب"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "متزوج"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "ارملة"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "مطلق"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "اخري"))
        self.lineEdit_27.setPlaceholderText(_translate("MainWindow", "    اضافة أب أعتراف"))
        self.label_18.setText(_translate("MainWindow", "الحالة الاجتماعية"))
        self.label_15.setText(_translate("MainWindow", "عدد الابناء    ="))
        self.label_17.setText(_translate("MainWindow", "بيانات الأبن"))
        self.lineEdit_25.setPlaceholderText(_translate("MainWindow", "                الرقم القومي 14 رقم"))
        self.pushButton_10.setText(_translate("MainWindow", " اضافة"))
        self.pushButton_8.setText(_translate("MainWindow", "رجوع"))
        self.pushButton_9.setText(_translate("MainWindow", "       التالي"))
        self.label_62.setText(_translate("MainWindow", "أب الأعتراف"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_9), _translate("MainWindow", "Tab 1"))
        self.lineEdit_30.setPlaceholderText(_translate("MainWindow", "                    الدخل الشهري"))
        self.pushButton_11.setText(_translate("MainWindow", " اضافة"))
        self.label_21.setText(_translate("MainWindow", "الحالة الاجتماعية"))
        self.lineEdit_31.setPlaceholderText(_translate("MainWindow", "                الرقم القومي 14 رقم"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "اعزب"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "متزوج"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "ارملة"))
        self.comboBox_5.setItemText(3, _translate("MainWindow", "مطلق"))
        self.comboBox_5.setItemText(4, _translate("MainWindow", "اخري"))
        self.lineEdit_32.setPlaceholderText(_translate("MainWindow", "                          الأسم "))
        self.label_23.setText(_translate("MainWindow", "بيانات الشخص"))
        self.lineEdit_34.setPlaceholderText(_translate("MainWindow", "             السنة الدراسية او الوظيفة"))
        self.lineEdit_35.setPlaceholderText(_translate("MainWindow", "                       صلة القرابة"))
        self.pushButton_13.setText(_translate("MainWindow", "       التالي"))
        self.pushButton_12.setText(_translate("MainWindow", "رجوع"))
        self.label_112.setText(_translate("MainWindow", "أب الأعتراف"))
        self.lineEdit_33.setPlaceholderText(_translate("MainWindow", "   اضافة أب أعتراف"))
        self.label_63.setText(_translate("MainWindow", "عدد الأشخاص ="))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_10), _translate("MainWindow", "Tab 2"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("MainWindow", "next 2"))
        self.checkBox_2.setText(_translate("MainWindow", "ملاحظات اخري عن حالة الاسرة "))
        self.pushButton_14.setText(_translate("MainWindow", "رجوع"))
        self.pushButton_15.setText(_translate("MainWindow", "       التالي"))
        self.label_114.setText(_translate("MainWindow", "محتويات المنزل"))
        self.pushButton_79.setText(_translate("MainWindow", "اضف الي الجدول     "))
        self.pushButton_80.setText(_translate("MainWindow", "اضافة محتوي  "))
        self.pushButton_125.setText(_translate("MainWindow", "حذف المحتوي    "))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "اسم المحتوي"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "العدد"))
        self.pushButton_85.setText(_translate("MainWindow", "حذف من الجدول     "))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_8), _translate("MainWindow", "Tab 1"))
        self.label_44.setText(_translate("MainWindow", "أمراض"))
        self.label_45.setText(_translate("MainWindow", "أعاقة"))
        self.label_46.setText(_translate("MainWindow", "ظروف اخري"))
        self.pushButton_17.setText(_translate("MainWindow", "       التالي"))
        self.pushButton_16.setText(_translate("MainWindow", "رجوع"))
        self.label_32.setText(_translate("MainWindow", "ملاحظات اخري"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_11), _translate("MainWindow", "Tab 2"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), _translate("MainWindow", "next 3"))
        self.label_47.setText(_translate("MainWindow", "مصادر الدخل الأساسية "))
        self.label_48.setText(_translate("MainWindow", "المصدر"))
        self.lineEdit_36.setPlaceholderText(_translate("MainWindow", "             اضافة مصدر "))
        self.label_49.setText(_translate("MainWindow", "الدخل الشهري"))
        self.label_50.setText(_translate("MainWindow", "مساعدات وشهريات الكنائس"))
        self.checkBox_3.setText(_translate("MainWindow", "مساعدة مادية شهرية"))
        self.checkBox_4.setText(_translate("MainWindow", "بركة شهرية "))
        self.checkBox_5.setText(_translate("MainWindow", "مساعدة علاجية "))
        self.checkBox_6.setText(_translate("MainWindow", "مساعدات اخري"))
        self.label_51.setText(_translate("MainWindow", "اخري"))
        self.pushButton_18.setText(_translate("MainWindow", "رجوع"))
        self.pushButton_25.setText(_translate("MainWindow", "       التالي"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_12), _translate("MainWindow", "next 4"))
        self.label_116.setText(_translate("MainWindow", "كهرباء ومياه وغاز"))
        self.label_117.setText(_translate("MainWindow", "تليفون"))
        self.label_118.setText(_translate("MainWindow", "إيجار"))
        self.label_119.setText(_translate("MainWindow", "علاج"))
        self.label_120.setText(_translate("MainWindow", "مساعدات وشهريات الكنائس"))
        self.label_121.setText(_translate("MainWindow", "مساعدات علاجية"))
        self.label_122.setText(_translate("MainWindow", "المرتب الاساسى"))
        self.label_123.setText(_translate("MainWindow", "مساعدات خلال الدراسة"))
        self.label_124.setText(_translate("MainWindow", "المصدر الاضافى ( المشروع )"))
        self.label_125.setText(_translate("MainWindow", "دراسة"))
        self.label_74.setText(_translate("MainWindow", "مساعدات وشهريات الكنائس"))
        self.pushButton_54.setText(_translate("MainWindow", "رجوع"))
        self.pushButton_77.setText(_translate("MainWindow", "  حفظ كل البيانات"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_25), _translate("MainWindow", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "add"))
        self.label_60.setText(_translate("MainWindow", "بيانات الزوج"))
        self.lineEdit_42.setPlaceholderText(_translate("MainWindow", "       الرقم القومي 14 رقم"))
        self.lineEdit_43.setPlaceholderText(_translate("MainWindow", "                  المرتب"))
        self.lineEdit_44.setPlaceholderText(_translate("MainWindow", "       الرقم القومي 14 رقم"))
        self.lineEdit_46.setPlaceholderText(_translate("MainWindow", "               رقم الهاتف "))
        self.lineEdit_47.setPlaceholderText(_translate("MainWindow", "                  الوظيفة"))
        self.lineEdit_48.setPlaceholderText(_translate("MainWindow", "             أسم الشهرة "))
        self.lineEdit_49.setPlaceholderText(_translate("MainWindow", "                   الأسم "))
        self.lineEdit_50.setPlaceholderText(_translate("MainWindow", "             أسم الشهرة "))
        self.label_61.setText(_translate("MainWindow", "بيانات الزوجة"))
        self.lineEdit_51.setPlaceholderText(_translate("MainWindow", "                   الأسم "))
        self.lineEdit_53.setPlaceholderText(_translate("MainWindow", "                  الوظيفة"))
        self.lineEdit_54.setPlaceholderText(_translate("MainWindow", "                  المرتب"))
        self.lineEdit_56.setPlaceholderText(_translate("MainWindow", "               رقم الهاتف "))
        self.pushButton_27.setText(_translate("MainWindow", "       التالي"))
        self.pushButton_52.setText(_translate("MainWindow", "بحث"))
        self.comboBox_13.setItemText(0, _translate("MainWindow", "رقم الأسرة"))
        self.comboBox_13.setItemText(1, _translate("MainWindow", "الرقم القومي للزوج"))
        self.comboBox_13.setItemText(2, _translate("MainWindow", "الرقم القومي للزوجة"))
        self.lineEdit_79.setPlaceholderText(_translate("MainWindow", "    اسم أب أعتراف"))
        self.label_108.setText(_translate("MainWindow", "أب الأعتراف"))
        self.pushButton_84.setText(_translate("MainWindow", "  حفظ"))
        self.pushButton_130.setText(_translate("MainWindow", "حذف جميع البيانات"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_16), _translate("MainWindow", "add client"))
        self.pushButton_28.setText(_translate("MainWindow", "رجوع"))
        self.pushButton_29.setText(_translate("MainWindow", "       التالي"))
        self.label_42.setText(_translate("MainWindow", "موبايل "))
        self.label_39.setText(_translate("MainWindow", "الحي"))
        self.lineEdit_107.setPlaceholderText(_translate("MainWindow", "                  اضافة حي "))
        self.label_38.setText(_translate("MainWindow", "المحافظة "))
        self.label_36.setText(_translate("MainWindow", "السكن "))
        self.lineEdit_104.setPlaceholderText(_translate("MainWindow", "                اضافة محفظة "))
        self.label_35.setText(_translate("MainWindow", "أسم الكنيسة :"))
        self.lineEdit_108.setPlaceholderText(_translate("MainWindow", "             اضافة عنوان "))
        self.label_34.setText(_translate("MainWindow", "تليفون "))
        self.label_33.setText(_translate("MainWindow", "المنطقة "))
        self.label_37.setText(_translate("MainWindow", "العنوان"))
        self.radioButton_17.setText(_translate("MainWindow", "ايجار قديم"))
        self.radioButton_18.setText(_translate("MainWindow", "تمليك"))
        self.radioButton_19.setText(_translate("MainWindow", "ايجار جديد "))
        self.radioButton_20.setText(_translate("MainWindow", "مع الاسرة"))
        self.label_41.setText(_translate("MainWindow", "علامة مميزة "))
        self.label_40.setText(_translate("MainWindow", "العنوان بالتفصيل :"))
        self.pushButton_118.setText(_translate("MainWindow", "  حفظ"))
        self.lineEdit_101.setText(_translate("MainWindow", "كنيسة "))
        self.radioButton_7.setText(_translate("MainWindow", "كنيسة الشهيد العظيم مارمينا والقديس البابا كيرلس السادس"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_17), _translate("MainWindow", "next 1"))
        self.lineEdit_66.setPlaceholderText(_translate("MainWindow", "             السنة الدراسية او الوظيفة"))
        self.lineEdit_67.setPlaceholderText(_translate("MainWindow", "                    الدخل الشهري"))
        self.lineEdit_68.setPlaceholderText(_translate("MainWindow", "                          الأسم "))
        self.checkBox_7.setText(_translate("MainWindow", "اشخاص اخري تقيم مع الأسرة"))
        self.comboBox_10.setItemText(0, _translate("MainWindow", "اعزب"))
        self.comboBox_10.setItemText(1, _translate("MainWindow", "متزوج"))
        self.comboBox_10.setItemText(2, _translate("MainWindow", "ارملة"))
        self.comboBox_10.setItemText(3, _translate("MainWindow", "مطلق"))
        self.comboBox_10.setItemText(4, _translate("MainWindow", "اخري"))
        self.label_73.setText(_translate("MainWindow", "الحالة الاجتماعية"))
        self.lineEdit_70.setPlaceholderText(_translate("MainWindow", "                الرقم القومي 14 رقم"))
        self.pushButton_34.setText(_translate("MainWindow", "  حفظ"))
        self.pushButton_35.setText(_translate("MainWindow", "رجوع"))
        self.pushButton_36.setText(_translate("MainWindow", "       التالي"))
        self.pushButton_56.setText(_translate("MainWindow", "تحقق من الرقم القومي"))
        self.pushButton_57.setText(_translate("MainWindow", "  حذف"))
        self.label_107.setText(_translate("MainWindow", "أب الأعتراف"))
        self.lineEdit_69.setPlaceholderText(_translate("MainWindow", "    اضافة أب أعتراف"))
        self.label_43.setText(_translate("MainWindow", "بيانات الأبن"))
        self.label_25.setText(_translate("MainWindow", "عدد الابناء    ="))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_19), _translate("MainWindow", "Tab 1"))
        self.pushButton_37.setText(_translate("MainWindow", "  حفظ"))
        self.label_77.setText(_translate("MainWindow", "الحالة الاجتماعية"))
        self.lineEdit_72.setPlaceholderText(_translate("MainWindow", "                الرقم القومي 14 رقم"))
        self.comboBox_11.setItemText(0, _translate("MainWindow", "اعزب"))
        self.comboBox_11.setItemText(1, _translate("MainWindow", "متزوج"))
        self.comboBox_11.setItemText(2, _translate("MainWindow", "ارملة"))
        self.comboBox_11.setItemText(3, _translate("MainWindow", "مطلق"))
        self.comboBox_11.setItemText(4, _translate("MainWindow", "اخري"))
        self.lineEdit_73.setPlaceholderText(_translate("MainWindow", "                          الأسم "))
        self.lineEdit_74.setPlaceholderText(_translate("MainWindow", "                    الدخل الشهري"))
        self.lineEdit_75.setPlaceholderText(_translate("MainWindow", "             السنة الدراسية او الوظيفة"))
        self.lineEdit_76.setPlaceholderText(_translate("MainWindow", "                       صلة القرابة"))
        self.pushButton_38.setText(_translate("MainWindow", "       التالي"))
        self.pushButton_39.setText(_translate("MainWindow", "رجوع"))
        self.pushButton_58.setText(_translate("MainWindow", "  حذف"))
        self.lineEdit_71.setPlaceholderText(_translate("MainWindow", "    اضافة أب أعتراف"))
        self.label_113.setText(_translate("MainWindow", "أب الأعتراف"))
        self.pushButton_119.setText(_translate("MainWindow", "تحقق من الرقم القومي"))
        self.label_68.setText(_translate("MainWindow", "بيانات الشخص"))
        self.label_64.setText(_translate("MainWindow", "عدد الأشخاص ="))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_20), _translate("MainWindow", "Tab 2"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_18), _translate("MainWindow", "next 2"))
        self.checkBox_8.setText(_translate("MainWindow", "ملاحظات اخري عن حالة الاسرة "))
        self.pushButton_40.setText(_translate("MainWindow", "رجوع"))
        self.pushButton_41.setText(_translate("MainWindow", "       التالي"))
        self.pushButton_82.setText(_translate("MainWindow", "اضافة محتوي  "))
        self.label_115.setText(_translate("MainWindow", "محتويات المنزل"))
        self.pushButton_81.setText(_translate("MainWindow", "اضف الي الجدول     "))
        self.pushButton_126.setText(_translate("MainWindow", "حذف المحتوي    "))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "اسم المحتوي"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "العدد"))
        self.pushButton_86.setText(_translate("MainWindow", "حذف من الجدول     "))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_22), _translate("MainWindow", "Tab 1"))
        self.pushButton_48.setText(_translate("MainWindow", "       التالي"))
        self.pushButton_49.setText(_translate("MainWindow", "رجوع"))
        self.pushButton_59.setText(_translate("MainWindow", "  حفظ"))
        self.label_65.setText(_translate("MainWindow", "أمراض"))
        self.label_66.setText(_translate("MainWindow", "أعاقة"))
        self.label_67.setText(_translate("MainWindow", "ظروف اخري"))
        self.label_58.setText(_translate("MainWindow", "ملاحظات اخري"))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_23), _translate("MainWindow", "Tab 2"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_21), _translate("MainWindow", "next 3"))
        self.label_102.setText(_translate("MainWindow", "مصادر الدخل الأساسية "))
        self.label_103.setText(_translate("MainWindow", "المصدر"))
        self.lineEdit_77.setPlaceholderText(_translate("MainWindow", "             اضافة مصدر "))
        self.label_104.setText(_translate("MainWindow", "الدخل الشهري"))
        self.label_105.setText(_translate("MainWindow", "مساعدات وشهريات الكنائس"))
        self.checkBox_9.setText(_translate("MainWindow", "مساعدة مادية شهرية"))
        self.checkBox_10.setText(_translate("MainWindow", "بركة شهرية "))
        self.checkBox_11.setText(_translate("MainWindow", "مساعدة علاجية "))
        self.checkBox_12.setText(_translate("MainWindow", "مساعدات اخري"))
        self.label_106.setText(_translate("MainWindow", "اخري"))
        self.pushButton_50.setText(_translate("MainWindow", "رجوع"))
        self.pushButton_131.setText(_translate("MainWindow", "  حفظ"))
        self.pushButton_53.setText(_translate("MainWindow", "       التالي"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_24), _translate("MainWindow", "next 4"))
        self.label_126.setText(_translate("MainWindow", "مساعدات وشهريات الكنائس"))
        self.label_127.setText(_translate("MainWindow", "إيجار"))
        self.label_128.setText(_translate("MainWindow", "تليفون"))
        self.label_129.setText(_translate("MainWindow", "المصدر الاضافى ( المشروع )"))
        self.label_130.setText(_translate("MainWindow", "علاج"))
        self.label_131.setText(_translate("MainWindow", "كهرباء ومياه وغاز"))
        self.label_75.setText(_translate("MainWindow", "مساعدات وشهريات الكنائس"))
        self.label_132.setText(_translate("MainWindow", "مساعدات خلال الدراسة"))
        self.label_133.setText(_translate("MainWindow", "مساعدات علاجية"))
        self.label_134.setText(_translate("MainWindow", "دراسة"))
        self.label_135.setText(_translate("MainWindow", "المرتب الاساسى"))
        self.pushButton_132.setText(_translate("MainWindow", "  حفظ"))
        self.pushButton_51.setText(_translate("MainWindow", "رجوع"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_26), _translate("MainWindow", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_15), _translate("MainWindow", "edit"))
        self.pushButton_3.setText(_translate("MainWindow", "                            بحث"))
        self.pushButton_2.setText(_translate("MainWindow", "     تعديل او حذف"))
        self.pushButton.setText(_translate("MainWindow", "                        اضافة"))
        self.pushButton.setShortcut(_translate("MainWindow", "`"))

import pics_rc