# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myUiOnePage.ui',
# licensing of 'myUiOnePage.ui' applies.
#
# Created: Thu Jun 25 18:45:21 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1728, 874)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.startBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startBtn.setGeometry(QtCore.QRect(1470, 30, 111, 28))
        self.startBtn.setObjectName("startBtn")
        self.updateBtn = QtWidgets.QPushButton(self.centralwidget)
        self.updateBtn.setGeometry(QtCore.QRect(1590, 30, 111, 28))
        self.updateBtn.setObjectName("updateBtn")
        self.frameTxt = QtWidgets.QLabel(self.centralwidget)
        self.frameTxt.setGeometry(QtCore.QRect(1300, 100, 111, 16))
        self.frameTxt.setObjectName("frameTxt")
        self.targetTxt_2 = QtWidgets.QLabel(self.centralwidget)
        self.targetTxt_2.setGeometry(QtCore.QRect(720, 100, 121, 16))
        self.targetTxt_2.setObjectName("targetTxt_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(140, 20, 151, 20))
        self.label_5.setObjectName("label_5")
        self.loadBtn = QtWidgets.QPushButton(self.centralwidget)
        self.loadBtn.setGeometry(QtCore.QRect(1290, 30, 171, 28))
        self.loadBtn.setObjectName("loadBtn")
        self.textOut = QtWidgets.QLabel(self.centralwidget)
        self.textOut.setGeometry(QtCore.QRect(60, 510, 300, 300))
        self.textOut.setText("")
        self.textOut.setObjectName("textOut")
        self.graficOut = QtWidgets.QLabel(self.centralwidget)
        self.graficOut.setGeometry(QtCore.QRect(10, 70, 430, 430))
        self.graficOut.setText("")
        self.graficOut.setObjectName("graficOut")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(160, 490, 151, 20))
        self.label_8.setObjectName("label_8")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(60, 510, 300, 300))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 50, 430, 430))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(470, 160, 600, 600))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.frame = QtWidgets.QLabel(self.groupBox_3)
        self.frame.setGeometry(QtCore.QRect(0, 0, 600, 600))
        self.frame.setText("")
        self.frame.setObjectName("frame")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(1100, 160, 600, 600))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.target = QtWidgets.QLabel(self.groupBox_4)
        self.target.setGeometry(QtCore.QRect(0, 0, 600, 600))
        self.target.setText("")
        self.target.setObjectName("target")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1728, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.startBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Старт", None, -1))
        self.updateBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Обновить этап", None, -1))
        self.frameTxt.setText(QtWidgets.QApplication.translate("MainWindow", "Целевая сборка", None, -1))
        self.targetTxt_2.setText(QtWidgets.QApplication.translate("MainWindow", "Текущая сборка", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("MainWindow", "Графическая отладка", None, -1))
        self.loadBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Загрузить целевую сборку", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("MainWindow", "Текстовая отладка", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

