# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'text2keystroke_framework.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import text2keystroke
import time

import config

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_text2keystroke(object):
    def setupUi(self, text2keystroke_gui):
        text2keystroke_gui.setObjectName("text2keystroke")
        text2keystroke_gui.resize(741, 465)
        text2keystroke_gui.setMinimumSize(QtCore.QSize(741, 465))
        text2keystroke_gui.setMaximumSize(QtCore.QSize(741, 465))
        text2keystroke_gui.setWindowOpacity(1.0)
        text2keystroke_gui.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(text2keystroke_gui)
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
        self.wipeButton = QtWidgets.QPushButton(self.groupBox_2)
        self.wipeButton.setGeometry(QtCore.QRect(520, 190, 31, 31))
        self.wipeButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("src/wipe.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.wipeButton.setIcon(icon)
        self.wipeButton.setObjectName("wipeButton")
        self.tabWidget.addTab(self.TextModeTab, "")
        self.ProfileModeTab = QtWidgets.QWidget()
        self.ProfileModeTab.setObjectName("ProfileModeTab")
        self.tabWidget.addTab(self.ProfileModeTab, "")
        text2keystroke_gui.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(text2keystroke_gui)
        self.statusBar.setObjectName("statusBar")
        text2keystroke_gui.setStatusBar(self.statusBar)
        self.retranslateUi(text2keystroke_gui)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(text2keystroke_gui)

    def retranslateUi(self, text2keystroke_gui):
        _translate = QtCore.QCoreApplication.translate
        text2keystroke_gui.setWindowTitle(_translate("text2keystroke", "text2keystroke"))
        self.fileModeButton.setText(_translate("text2keystroke", "Open File"))
        self.groupBox.setTitle(_translate("text2keystroke", "History"))
        self.typeButton.setText(_translate("text2keystroke", "Type"))
        self.groupBox_2.setTitle(_translate("text2keystroke", "Text Box"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TextModeTab), _translate("text2keystroke", "Text Mode"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ProfileModeTab), _translate("text2keystroke", "Profile Mode"))
        self.statusBar.showMessage('Standby.')
        # self.typeButton.setToolTip('This is an example self.typeButton')
        self.typeButton.clicked.connect(self.type)
        self.wipeButton.clicked.connect(self.textEdit.clear)
        self.listWidget.itemDoubleClicked.connect(self.item_click)

    def append_history(self, text):
        '''Append item to history'''
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.addItem(text)
        self.listWidget.setSortingEnabled(__sortingEnabled)

    def type(self):
        text = self.textEdit.toPlainText()
        print(text)
        if not text:
            return
        self.textEdit.setEnabled(False)
        self.typeButton.setEnabled(False)
        self.statusBar.showMessage('Sleeping for {}s...'.format(config.sleepTime))
        # time.sleep(config.sleepTime)
        self.statusBar.showMessage('Typing... ' + text)
        # text2keystroke.type_multilines(text)

        self.statusBar.showMessage('Done!')
        self.textEdit.setEnabled(True)
        self.typeButton.setEnabled(True)
        self.append_history(text)

    def item_click(self, item):
        self.statusBar.showMessage(item.text())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    text2keystroke_gui = QtWidgets.QMainWindow()
    ui = Ui_text2keystroke()
    ui.setupUi(text2keystroke_gui)
    text2keystroke_gui.show()
    sys.exit(app.exec_())
