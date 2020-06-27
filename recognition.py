# -*- coding: utf-8 -*-

import cv2 as cv
import sys
import os
from PIL import Image
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, Activation, BatchNormalization, AveragePooling2D
from tensorflow.keras.optimizers import SGD, RMSprop, Adam
import tensorflow as tf
import numpy as np

import correct
from cnnNeural import cnn_digits_predict

def nothing():
    pass

def GetHsvMinMax(frame):
    cv.namedWindow( "result" ) # создаем главное окно
    cv.namedWindow( "settings" ) # создаем окно настроек

    # создаем 6 бегунков для настройки начального и конечного цвета фильтра
    cv.createTrackbar('h1', 'settings', 0, 255, nothing)
    cv.createTrackbar('s1', 'settings', 0, 255, nothing)
    cv.createTrackbar('v1', 'settings', 0, 255, nothing)
    cv.createTrackbar('h2', 'settings', 255, 255, nothing)
    cv.createTrackbar('s2', 'settings', 255, 255, nothing)
    cv.createTrackbar('v2', 'settings', 255, 255, nothing)
    cv.createTrackbar('default', 'settings', 0, 1, nothing)

    while True: 
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV )
        # считываем значения бегунков
        h1 = cv.getTrackbarPos('h1', 'settings')
        s1 = cv.getTrackbarPos('s1', 'settings')
        v1 = cv.getTrackbarPos('v1', 'settings')
        h2 = cv.getTrackbarPos('h2', 'settings')
        s2 = cv.getTrackbarPos('s2', 'settings')
        v2 = cv.getTrackbarPos('v2', 'settings')
        df = cv.getTrackbarPos('default', 'settings')
        if (df == 1):
            cv.destroyWindow("settings")
            cv.namedWindow( "settings" ) 
            cv.createTrackbar('h1', 'settings', 0, 255, nothing)
            cv.createTrackbar('s1', 'settings', 0, 255, nothing)
            cv.createTrackbar('v1', 'settings', 0, 255, nothing)
            cv.createTrackbar('h2', 'settings', 255, 255, nothing)
            cv.createTrackbar('s2', 'settings', 255, 255, nothing)
            cv.createTrackbar('v2', 'settings', 255, 255, nothing)
            cv.createTrackbar('default', 'settings', 0, 1, nothing)
        
        # формируем начальный и конечный цвет фильтра
        hsv_min = np.array((h1, s1, v1), np.uint8)
        hsv_max = np.array((h2, s2, v2), np.uint8)

        # накладываем фильтр на кадр в модели HSV
        thresh = cv.inRange(hsv, hsv_min, hsv_max)

        #показ изображения через несколько итераций, комп тупит
        #if count % 5 == 0:
        cv.imshow('result', thresh)

        # cap.release()
        print("hsv_min = np.array((",h1,", ",s1,", ",v1,"), np.uint8)")
        print("hsv_max = np.array((",h2,", ",s2,", ",v2,"), np.uint8)")
        # cv.destroyAllWindows()
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
        #return 0


def InsertColor():
    hsv_all = list()

    #зеленый вечером на белом фоне вспышка на 1 позиции
    #hsv_min = np.array(( 5 ,  59 ,  0 ), np.uint8)
    #hsv_max = np.array(( 255 ,  255 ,  255 ), np.uint8)

    # для всех цветов кубиков
    hsv_min = np.array(( 0 ,  60 ,  0 ), np.uint8)
    hsv_max = np.array(( 255 ,  255 ,  255 ), np.uint8)

    hsv_all.append(hsv_min)
    hsv_all.append(hsv_max)
        
    # hsv_min = np.array((0, 54, 5), np.uint8)
    # hsv_max = np.array((187, 255, 253), np.uint8)
    # hsv_all.append(hsv_min)
    # hsv_all.append(hsv_max)
        
    return hsv_all


def GetRectangles(frame, hsv_all):
    hsv = cv.cvtColor( frame, cv.COLOR_BGR2HSV ) # меняем цветовую модель с BGR на HSV
    #проходим по всем hsv
    i = 0
    while i < len(hsv_all):
        hsv_min = hsv_all[i]
        hsv_max = hsv_all[i+1]
        i += 2
        # применяем цветовой фильтр
        thresh = cv.inRange( hsv, hsv_min, hsv_max )
        # ищем контуры и складируем их в переменную contours
        _,contours, _  = cv.findContours( thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        # получаем вершины прямоугольников
        fullArrRects = list()
        for cnt in contours:
            rect = cv.minAreaRect(cnt) # пытаемся вписать прямоугольник
            area = int(rect[1][0]*rect[1][1]) # вычисление площади
            if area > 1500:
                arrRects = cv.boxPoints(rect) # поиск четырех вершин прямоугольника
                arrRects = np.int0(arrRects) # округление координат
                fullArrRects.append(arrRects)

    # поиск координаты левого верхнего угла кубика
    arrTopLeftAngles = correct.FindTopLeftAngle(fullArrRects)
    # массив, в котором перечисление начинается с верхней левой координаты
    sortedArrRects = correct.SortArrRects(fullArrRects, arrTopLeftAngles)

    return sortedArrRects



def GetQR(frame, arrRects):
        neuralModel = tf.keras.models.load_model('cnn_digits_28x28.h5', compile=False)

        # тут будут все qr-коды в виде номеров элементов массива (элементом массива является массив координат углов кубика)
        # например qr-код "1", значит элемент массива (координаты кубика с этим кодом) будет первым элементов данного массива
        # из этого вывод - что данный массив будет отсортирован по qr-кодам по возрастанию
        arrCodes = list()

        #for i in range(len(arrRects)):
        for i in range(10):
            arrCodes.append(0)

        for rect in range(len(arrRects)):
            firstPoint = 0
            endPoint = 2
            x = 0
            y = 1
            firstPointX = arrRects[rect][firstPoint][x]
            firstPointY = arrRects[rect][firstPoint][y]
            endPointX = arrRects[rect][endPoint][x]
            endPointY = arrRects[rect][endPoint][y]

            testFrame = frame[firstPointY:endPointY, firstPointX:endPointX]

            #перевести в hsv и регулировать уже насыщенности/яркости искать черный тупо)

            # формируем начальный и конечный цвет фильтра
            #hsv_min = np.array(( 0 ,  87 ,  66 ), np.uint8)
            #hsv_max = np.array(( 255 ,  255 ,  255 ), np.uint8)

            # фильтр для дневного освещения + вспышка + освещение настольной лампы

            hsv_min = np.array(( 0 ,  0 ,  33 ), np.uint8)
            hsv_max = np.array(( 255 ,  255 ,  255 ), np.uint8)

            # накладываем фильтр на кадр в модели HSV
            img = cv.inRange(testFrame, hsv_min, hsv_max)


            qr = 0
                
            #пока закомментил, надо этот кусов для массивА массивОВ фреймов для более точной реализации распознавания

            #buff = list()
            #count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            #max = 0
            #if cv.imwrite('cnnimg.png', img):        
            #    for i in range(20):
            #        qr = cnn_digits_predict(neuralModel)
            #        if qr == 0:
            #            i -= 1
            #            break
            #        #buff.append(qr)
            #        else:
            #            count[qr] += 1

            #    for j in range(10):
            #        if count[j] > max:
            #            max = count[j]
            #            qr = j

            #    print(qr)

            if cv.imwrite('cnnimg.png', img):        
                qr = cnn_digits_predict(neuralModel)
            if (qr != 0):
                print(qr)
                  


            #if type(qr) == int and qr < len(arrRects):
            #    arrCodes[qr] = arrRects[rect]



            # проверка на последовательность
            #flag = False
            #for i in range(len(codesDict)):
                #for j in range(len(codesDict)):
                    #if codesDict[str(i+1)] != None:
                    #    print(codesDict[str(i+1)])
                    #    flag = True
                    #    print("yes")
                #print (codesDict[str(i+1)])
                    
            #if len(arrCodes) > 0:
            #    print("CODE:   ", qr)
                #SortQr()

                #break
            #return arrCodes
            # return np.array(resized)


