# -- coding: utf-8 --

import cv2 as cv
import os
import sys
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
#from tkinter import *
#import tkinter as tk
#import tkinter.ttk as ttk
from tkinter import filedialog as fd
import numpy as np
from PIL import Image, ImageTk

import proj_5
import correct

def PrintContoursRect(frame, arrRects):
    cv.drawContours(frame, arrRects, -1, (255,0,0), 2, cv.LINE_AA) # рисуем прямоугольник
            

def PrintCoordsRect(frame, arrRects):
    color = (0,0,0)
    arrLenSides = correct.CalculateLenSides(arrRects)
    lenSide = arrLenSides[0][0]
    for i in range(len(arrRects)):
        #for j in range(len(arrRects[i])):
        cv.putText(frame, str((arrRects[i][0][0], arrRects[i][0][1])) , (arrRects[i][0][0]+3,                arrRects[i][0][1]+13), cv.FONT_HERSHEY_SIMPLEX, 0.4, color, 1)
        cv.putText(frame, str((arrRects[i][1][0], arrRects[i][1][1])) , (arrRects[i][1][0]-int(lenSide/2.5), arrRects[i][1][1]+13), cv.FONT_HERSHEY_SIMPLEX, 0.4, color, 1)
        cv.putText(frame, str((arrRects[i][2][0], arrRects[i][2][1])) , (arrRects[i][2][0]-int(lenSide/2.5),   arrRects[i][2][1]-10), cv.FONT_HERSHEY_SIMPLEX, 0.4, color, 1)
        cv.putText(frame, str((arrRects[i][3][0], arrRects[i][3][1])) , (arrRects[i][3][0]+3,                arrRects[i][3][1]-10), cv.FONT_HERSHEY_SIMPLEX, 0.4, color, 1)


def PrintCountRects(frame, arrRects):
    color = (0,0,0)
    cv.putText(frame, 'Count rectangles: ' + str(len(arrRects)), (30, 30), cv.FONT_HERSHEY_SIMPLEX, 0.7, color, 1)


#def LoadFile(event): 
#    fn = fd.Open(root, filetypes = [('*.txt files', '.txt')]).show()
#    if fn == '':
#        return
#    textbox.delete('1.0', 'end') 
#    textbox.insert('1.0', open(fn, 'rt').read())

# главное окно
#root = Tk()
#root.title("Вывод")
#root.geometry("1050x650")

#notebook = ttk.Notebook(root, width=1000, height=700)
#notebook.pack(fill='both', expand='yes')

fileName = ' '
def LoadFile(event): 
    global fileName
    fileName = fd.askopenfilename()
    print(fileName)

def Load(event):
    global root
    root.quit()

def Destr(event):
    root.update()

    


#def ShowWindow(frame):
#    resizedframe = cv.resize(frame, (500, 500))
#    cv.imwrite('resizedFrame.png', resizedframe)

#    # ПЕРВАЯ ВКЛАДКА
#    # первая вкладка (вкладка "сборки")
#    f1 = Label(root)

#    # добавляем первую вкладку на главное окно
#    notebook.add(f1, text='Сборки')

#    # get resized images
#    frameImg = Image.open("resizedFrame.png")
#    renderFrame = ImageTk.PhotoImage(frameImg)

#    targImg = Image.open("resizedTarg.png")
#    renderTarg = ImageTk.PhotoImage(targImg)

#    # label img
#    labelImg1 = Label(f1, image=renderFrame)
#    labelImg1.image = renderFrame
#    labelImg1.place(relx=.0, rely=.2)

#    labelImg2 = Label(f1, image=renderTarg) 
#    labelImg2.image = renderTarg
#    labelImg2.place(relx=.5, rely=.2)

#    # label text
#    label0 = Label(f1, text="Текущая сборка", justify=LEFT)
#    label0.place(relx=.2, rely=.13)

#    label1 = Label(f1, text="Целевая сборка", justify=LEFT)
#    label1.place(relx=.70, rely=.13)


#    # ВТОРАЯ ВКЛАДКА
#    # вторая вкладка (вкладка "отладка")
#    f2 = Label(root)

#    notebook.add(f2, text='Отладка')

#    # кнопки
#    loadBtn = Button(f2, text="Загрузить целевую сборку")
#    loadBtn.bind("<Button-1>", LoadFile)
#    #print("hellllooooooo")

#    #if fileName != ' ':
#    #    print(fileName)
#    #name= fd.askopenfilename()
#    #print(name)
#    updateBtn = Button(f2, text="Обновить этап")
#    #loadBtn.place(x=10, y=30)
#    #updateBtn.place(x=180, y=30)
#    loadBtn.place(x=780, y=30)
#    updateBtn.place(x=940, y=30)
#    updateBtn.bind('<Button-1>', proj_5.Printt)
#    updateBtn.bind('<Button-2>', Load)
#    updateBtn.bind('<Button-3>', Destr)
#    root.mainloop() # цикл не выходит пока не нажмешь кнопку выхода - это раз, и два - то что Printt() не отображает 44, а Print() отображает
































    
#def ShowWindow(frame):
#    resizedframe = cv.resize(frame, (500, 500))
#    cv.imwrite('resizedFrame.png', resizedframe)

#    root = Tk()
#    root.title("Вывод")
#    root.geometry("1050x650")


    
#    notebook = ttk.Notebook(root, width=1000, height=700)
#    notebook.pack(fill='both', expand='yes')

#    f1 = Text(root)
#    f2 = Text(root)
#    f3 = Text(root)

#    notebook.add(f1, text='page1')
#    notebook.add(f2, text='page2')
#    notebook.add(f3, text='page3')


#    # btns
#    loadBtn = Button(text="Загрузить целевую сборку")
#    updateBtn = Button(text="Обновить этап")
#    #updateBtn.bind('<Button-1>', Process().!!!!!!!!1())

#    loadBtn.place(x=10, y=10)
#    updateBtn.place(x=180, y=10)

#    # get resized images
#    frameImg = Image.open("resizedFrame.png")
#    renderFrame = ImageTk.PhotoImage(frameImg)

#    targImg = Image.open("resizedTarg.png")
#    renderTarg = ImageTk.PhotoImage(targImg)

#    # label img
#    labelImg1 = Label(root, image=renderFrame)
#    labelImg1.image = renderFrame
#    labelImg1.place(relx=.0, rely=.2)

#    labelImg2 = Label(root, image=renderTarg) 
#    labelImg2.image = renderTarg
#    labelImg2.place(relx=.5, rely=.2)

#    # label text
#    label0 = Label(text="Текущая сборка", justify=LEFT)
#    label0.place(relx=.2, rely=.13)

#    label1 = Label(text="Целевая сборка", justify=LEFT)
#    label1.place(relx=.70, rely=.13)

    


#    root.mainloop()


















































    #    #cv.imshow("res", frame)


    ##root = tk()
    ##root.title("вывод")
    ###root.geometry("1024x640")
    ##root.geometry("1210x750")

    ### btns

    ##loadbtn = button(text="загрузить целевую сборку")
    ##updatebtn = button(text="обновить этап")

    ##loadbtn.place(x=10, y=10)
    ##updatebtn.place(x=180, y=10)


    ### label img

    ##img = image.open("tkimg.png")
    ##render = imagetk.photoimage(img)
    ##labelimg0 = label(root, image=render)
    ##labelimg0.image = render
    ##labelimg0.place(relx=.0, rely=.065)

    ##labelimg1 = label(root, image=render)
    ##labelimg1.image = render
    ##labelimg1.place(relx=.333, rely=.065)

    ##labelimg2 = label(root, image=render)
    ##labelimg2.image = render
    ##labelimg2.place(relx=.666, rely=.065)

        
    ### label text

    ##label0 = label(text="целевая сборка", justify=left)
    ##label0.place(relx=.130, rely=.6)

    ##label1 = label(text="текущая сборка", justify=left)
    ##label1.place(relx=.460, rely=.6)

    ##label2 = label(text="графическая отладка", justify=left)
    ##label2.place(relx=.794, rely=.6)

    ###label3 = label(text="текстовая отладка", justify=left)
    ###label3.place(relx=.2, rely=.3)


    #resizedframe = cv.resize(frame, (500, 500))
    #cv.imwrite('tkimg.png', resizedframe)

    #root = Tk()
    #root.title("Вывод")
    #root.geometry("1050x650")
    ##root.geometry("800x800")

    ## btns

    #loadBtn = Button(text="Загрузить целевую сборку")
    #updateBtn = Button(text="Обновить этап")
    #updateBtn.bind('<Button-1>', Main().Process())


    ##name= fd.askopenfilename() 
    ##print(name)


    #loadBtn.place(x=10, y=10)
    #updateBtn.place(x=180, y=10)


    ## label img

    #img = Image.open("tkimg.png")
    #render = ImageTk.PhotoImage(img)

    #targetImg = Image.open("tkimgTarget.png")
    #renderTarget = ImageTk.PhotoImage(targetImg)

    ##labelImg0 = Label(root, image=render)
    ##labelImg0.image = render
    ##labelImg0.place(relx=.0, rely=.0)

    #labelImg1 = Label(root, image=render)
    #labelImg1.image = render
    #labelImg1.place(relx=.0, rely=.2)

    #labelImg2 = Label(root, image=renderTarget) 
    #labelImg2.image = renderTarget
    #labelImg2.place(relx=.5, rely=.2)

        
    ## label text

    #label0 = Label(text="Текущая сборка", justify=LEFT)
    #label0.place(relx=.2, rely=.13)

    #label1 = Label(text="Целевая сборка", justify=LEFT)
    #label1.place(relx=.70, rely=.13)

    ##label2 = Label(text="Графическая отладка", justify=LEFT)
    ##label2.place(relx=.794, rely=.6)

    ##label3 = Label(text="Текстовая отладка", justify=LEFT)
    ##label3.place(relx=.2, rely=.3)

    ##myText = '''
    ##Не найдены элементы. Внесите элемент с кодом "1"
    ##в поле зрения веб-камеры и нажмите кнопку "Обновить этап"
    ##'''

    ##label4 = Label(text=myText, justify=LEFT)
    ##label4.place(relx=.3, rely=.3)



    ## ghttps://ru.stackoverflow.com/questions/919894/%D0%9C%D0%BE%D0%B4%D1%83%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5-%D0%BD%D0%B0%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D1%84%D0%B5%D0%B9%D1%81%D0%B0-python-tkinter


    ##root = Tk()
    ##root.title('test')

    ##notebook = ttk.Notebook(root, width=1000, height=700)
    ##notebook.pack(fill='both', expand='yes')

    ###f1 = Text(root)
    ###f2 = Text(root)
    ###f3 = Text(root)

    ###nb.add(f1, text='page1')
    ###nb.add(f2, text='page2')
    ###nb.add(f3, text='page3')

    ### a_tab
    ##a_tab = tk.Frame(notebook)

    ##img = Image.open("tkimg.png")
    ##render = ImageTk.PhotoImage(img)
    ##labelImg0 = Label(root, image=render)


    ### b_tab
    ##b_tab = tk.Frame(notebook)

    ##notebook.add(a_tab, text="Сборки")
    ##notebook.add(b_tab, text="Отладка")





    #root.mainloop()


    ## photo = ImageTk.PhotoImage(image = Image.fromarray(frame)) # преобразуем изобжаение из массива NumPy в PhotoImage
    ## label = Label(image=photo)
    ## label.image = photo # получили ссылку
    ## label.pack()



    ##!!!!! имеет место быть функции render