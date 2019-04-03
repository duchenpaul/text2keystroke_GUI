# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'text2keystroke_framework.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_text2keystroke(object):
    def setupUi(self, text2keystroke):
        text2keystroke.setObjectName("text2keystroke")
        text2keystroke.resize(741, 465)
        text2keystroke.setMinimumSize(QtCore.QSize(741, 465))
        text2keystroke.setMaximumSize(QtCore.QSize(741, 465))
        text2keystroke.setWindowOpacity(1.0)
        text2keystroke.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(text2keystroke)
        self.centralwidget.setObjectName("centralwidget")
        self.fileModeButton = QtWidgets.QPushButton(self.centralwidget)
        self.fileModeButton.setGeometry(QtCore.QRect(610, 160, 101, 31))
        self.fileModeButton.setMinimumSize(QtCore.QSize(101, 0))
        self.fileModeButton.setMaximumSize(QtCore.QSize(101, 16777215))
        self.fileModeButton.setAcceptDrops(False)
        self.fileModeButton.setCheckable(False)
        self.fileModeButton.setObjectName("fileModeButton")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 290, 701, 151))
        self.groupBox.setObjectName("groupBox")
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        self.listWidget.setGeometry(QtCore.QRect(10, 20, 681, 121))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.clearListButton = QtWidgets.QPushButton(self.groupBox)
        self.clearListButton.setGeometry(QtCore.QRect(660, 110, 31, 31))
        self.clearListButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("src/wipe.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clearListButton.setIcon(icon)
        self.clearListButton.setObjectName("clearListButton")
        self.typeButton = QtWidgets.QPushButton(self.centralwidget)
        self.typeButton.setGeometry(QtCore.QRect(600, 220, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.typeButton.setFont(font)
        self.typeButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.typeButton.setObjectName("typeButton")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 571, 271))
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tabWidget.setObjectName("tabWidget")
        self.TextModeTab = QtWidgets.QWidget()
        self.TextModeTab.setObjectName("TextModeTab")
        self.groupBox_2 = QtWidgets.QGroupBox(self.TextModeTab)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 10, 561, 231))
        self.groupBox_2.setObjectName("groupBox_2")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 541, 201))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(520, 190, 31, 31))
        self.pushButton.setText("")
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.TextModeTab, "")
        self.ProfileModeTab = QtWidgets.QWidget()
        self.ProfileModeTab.setObjectName("ProfileModeTab")
        self.profileList = QtWidgets.QListWidget(self.ProfileModeTab)
        self.profileList.setGeometry(QtCore.QRect(10, 10, 221, 231))
        self.profileList.setObjectName("profileList")
        self.profileText = QtWidgets.QTextBrowser(self.ProfileModeTab)
        self.profileText.setEnabled(True)
        self.profileText.setGeometry(QtCore.QRect(240, 10, 311, 231))
        self.profileText.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.profileText.setObjectName("profileText")
        self.tabWidget.addTab(self.ProfileModeTab, "")
        text2keystroke.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(text2keystroke)
        self.statusBar.setObjectName("statusBar")
        text2keystroke.setStatusBar(self.statusBar)

        self.retranslateUi(text2keystroke)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(text2keystroke)

    def retranslateUi(self, text2keystroke):
        _translate = QtCore.QCoreApplication.translate
        text2keystroke.setWindowTitle(_translate("text2keystroke", "text2keystroke"))
        self.fileModeButton.setText(_translate("text2keystroke", "Open File"))
        self.groupBox.setTitle(_translate("text2keystroke", "Status"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("text2keystroke", "kkk"))
        item = self.listWidget.item(1)
        item.setText(_translate("text2keystroke", "bbb"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.typeButton.setText(_translate("text2keystroke", "Type"))
        self.groupBox_2.setTitle(_translate("text2keystroke", "Text Box"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TextModeTab), _translate("text2keystroke", "Text Mode"))
        self.profileText.setHtml(_translate("text2keystroke", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">021131</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ProfileModeTab), _translate("text2keystroke", "Profile Mode"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    text2keystroke = QtWidgets.QMainWindow()
    ui = Ui_text2keystroke()
    ui.setupUi(text2keystroke)
    text2keystroke.show()
    sys.exit(app.exec_())

