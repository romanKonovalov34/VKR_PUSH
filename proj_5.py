
import cv2 as cv
import os
import sys
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog as fd
import numpy as np
from PIL import Image, ImageTk
import tensorflow as tf
from tensorflow import keras
import re

from PySide2 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QThread

from myUiOnePage import Ui_MainWindow
import recognition
import correct
import window

targFn = ' '
previousFileName = ' '
fileName = ' '
warning = ' фыва'

class MyFile(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, uiTarget):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.uiTarget = uiTarget

    def browse(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', '.')
        fileName = re.findall(r'\w+[.]png|jpg|\w+",', str(fileName))
        #global fileName
        #fileName = filename[0]
        #return filename[0]
        global targFn
        targFn = fileName[0]
        pixmapTarget = QtGui.QPixmap(targFn)
        self.uiTarget.setPixmap(pixmapTarget)

def RotateImg(img, angle):
    img_center = tuple(np.array(img.shape[1::-1]) / 2)
    rot_mat = cv.getRotationMatrix2D(img_center, angle, 1.0)
    result = cv.warpAffine(img, rot_mat, img.shape[1::-1], flags=cv.INTER_LINEAR)
    return result

class MyThread(QThread):
    def __init__(self, hsv_all, uiFrame, uiTarget, uiUpdateBtn, uiTextOut, uiGraficOut):
        QThread.__init__(self)
        self.hsv_all = hsv_all
        self.uiFrame = uiFrame
        self.uiTarget = uiTarget
        self.uiUpdateBtn = uiUpdateBtn
        self.uiTextOut = uiTextOut
        self.uiGraficOut = uiGraficOut

    def __del__(self):
        self.wait()

    def updateTarg(self):
        global targFn
        img = cv.imread(targFn)
        img = cv.resize(img, (600, 600))
        arrRects = recognition.GetRectangles(img, self.hsv_all)
        if len(arrRects) > 0:
            recognition.GetQR(img, arrRects)
            window.PrintContoursRect(img, arrRects)
            window.PrintCoordsRect(img, arrRects)
            window.PrintCountRects(img, arrRects)
            cv.imwrite('resizedTarg.png', img)
            pixmapTarget = QtGui.QPixmap('resizedTarg.png')
            self.uiTarget.setPixmap(pixmapTarget)

        else:
            global warning
            warning = 'Rectangles not found'


    def updateFrame(self):
        global warning
        if warning != ' ':
            #self.uiTextOut.setText(" Загружена неверная целевая сборка.\n На изображении не найдены кубики.")
            #self.uiTextOut.setText(" Ошибок на данном этапе нет.")
            #self.uiTextOut.setText(" Необходимо внести элемент с кодом «1»\n в поле зрения веб-камеры и нажать кнопку\n «Обновить этап».")
            self.uiTextOut.setText(" Ошибок нет.\n Изделие собрано правильно.")

            #return 0
        while True:
            img = cv.imread('imgForUpdate.png')
            if img is not None:
                break
        #1920x1080
        img = cv.resize(img, (640, 360))
        #1200x1080
        #img = cv.resize(img, (600, 540))
        img = RotateImg(img, 180)
        arrRects = recognition.GetRectangles(img, self.hsv_all)
        if len(arrRects) > 0:
            window.PrintContoursRect(img, arrRects)
            window.PrintCoordsRect(img, arrRects)
            window.PrintCountRects(img, arrRects)
            cv.imwrite('resizedImgForUpdate.png', img)
            pixmapFrame = QtGui.QPixmap('resizedImgForUpdate.png')
            self.uiFrame.setPixmap(pixmapFrame)

        
    def run(self):
        cap = cv.VideoCapture('test0.MOV')
        while cap:
            ret, img = cap.read()
            cv.imwrite('imgForUpdate.png', img)


def main():

    # создание приложения
    app = QtWidgets.QApplication(sys.argv)
    
    # создание формы и инициализация UI
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    # логика программы
    #hsv_all = recognition.InsertColor()
    #myFile = MyFile()
    #global fileName
    #global previousFileName
    #myFile.browse()
    #targFn = ' '
    #if fileName != previousFileName:
    #    targFn = fileName

    #    #targFnArr = myFile.browse()
    #    #targFn = targFnArr[0]
    #    targ = cv.imread(targFn)
    #    procTarg, arrRectsTarg = OnlyProc(targ, hsv_all)
    #    cv.imwrite('procTarg.png', procTarg)
    #    pixmapTarg = QtGui.QPixmap('procTarg.png')
    #    ui.target.setPixmap(pixmapTarg)
    #    #previousFileName = fileName


    # логика программы
    hsv_all = recognition.InsertColor()
    myFile = MyFile(ui.target)
    #global targFn
    #if targFn != ' ':
    #    print('aueeeeeeeeeeeeeeeeeeeee')
    #    targ = cv.imread(targFn)
    #    procTarg, arrRectsTarg = OnlyProc(targ, hsv_all)
    #    cv.imwrite('procTarg.png', procTarg)
    #    pixmapTarg = QtGui.QPixmap('procTarg.png')
    #    ui.target.setPixmap(pixmapTarg)

    hsv_all = recognition.InsertColor()

    myThread = MyThread(hsv_all, ui.frame, ui.target, ui.updateBtn, ui.textOut, ui.graficOut)
    #ui.loadBtn.clicked.connect(myThread.load(myFile))
    #ui.loadBtn.clicked.connect(myFile.browse)
    ui.loadBtn.clicked.connect(myFile.browse)
    ui.startBtn.clicked.connect(myThread.start)
    ui.updateBtn.clicked.connect(myThread.updateTarg)
    ui.updateBtn.clicked.connect(myThread.updateFrame)


    # запуск главного цикла
    sys.exit(app.exec_())

    #hsv_all = recognition.InsertColor()

    #targ = cv.imread('gry.png')
    #arrRectsTarg = OnlyProc(targ, hsv_all)

    #cap = cv.VideoCapture('test1.MOV')
    #EveryProc(cap, hsv_all)
    

if __name__ == '__main__':
    main()
