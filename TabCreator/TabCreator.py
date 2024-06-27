import pyscreenshot 
import pytesseract
import cv2
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from tkinter import messagebox 
from PIL import Image,ImageTk
import time
import os
from numba import jit

ex_dir = ''

def screenshot_base():
    path = str(dir_tf.get())
    x1 = int(scren_coords_x1_tf.get())
    y1 = int(scren_coords_y1_tf.get())
    x2 = int(scren_coords_x2_tf.get())
    y2 = int(scren_coords_y2_tf.get())

    i = pyscreenshot.grab(bbox=(x1, y1, x2, y2))
    i.save(f'{path}\\test.jpg')
    time_before = int(timer_tf.get())
    while time_before:
        time.sleep(1)
        time_before-=1
    return path

def take_screenshots():
    path = str(dir_tf.get())
    x1 = int(scren_coords_x1_tf.get())
    y1 = int(scren_coords_y1_tf.get())
    x2 = int(scren_coords_x2_tf.get())
    y2 = int(scren_coords_y2_tf.get())
    pytesseract.pytesseract.tesseract_cmd = r'D:\Teseract\tesseract.exe'
    time_before = int(timer_tf.get())
    while time_before:
        time.sleep(1)
        time_before-=1
    time_between = int(interval_tf.get())
    length = int(video_length_tf.get())+1
    index=0
    textOld=''
    textNew='1'
    window.title('Proccesing...')
    while length:
        if textOld!=textNew:
            index+=1
            i = pyscreenshot.grab(bbox=(x1, y1, x2, y2))
            i.save(f'{path}\\tab{index}.jpg')
            image = cv2.imread(f'{path}\\tab{index}.jpg')
            if time_between!=0:
                time.sleep(time_between)
            else:
                textNew = pytesseract.image_to_string(image,config='--psm 13')
            textOld=textNew
        else:
            time.sleep(0.5)
            i = pyscreenshot.grab(bbox=(x1, y1, x2, y2))
            i.save(f'{path}\\temp.jpg')
            image = cv2.imread(f'{path}\\temp.jpg')
            textNew = pytesseract.image_to_string(image,config='--psm 11')
            os.remove(f'{path}\\temp.jpg')
        print(textNew)
        length-=1
    messagebox.showinfo('showInfo','Done')
def take_dir():
    text = filedialog.askdirectory()
    dir_tf.delete(0,END)
    dir_tf.insert(0,text)
    return

def take_screenshot():
    path = screenshot_base()
    ex_image = ImageTk.PhotoImage(Image.open(f'{path}\\test.jpg').resize((250,250)))
    label_image.configure(image=ex_image)
    label_image.image = ex_image
    

window = Tk() #Создаём окно приложения.
window.geometry('800x600')
window.title("Input")
frame = Frame(
   window, 
   padx = 10, #Задаём отступ по горизонтали.
   pady = 10 #Задаём отступ по вертикали.
)
frame.pack(expand=True)

scren_coords_lb = Label(
   frame,
   text="Screenshot coordinates",
)
scren_coords_lb.grid(row=1, column=1)

scren_coords_x1_tf = Entry(
   frame, #Используем нашу заготовку с настроенными отступами.
   textvariable='10'
)
scren_coords_x1_tf.grid(row=2, column=1)
scren_coords_x1_tf.insert(0,'x1')

scren_coords_y1_tf = Entry(
   frame, #Используем нашу заготовку с настроенными отступами.
)
scren_coords_y1_tf.grid(row=3, column=1)
scren_coords_y1_tf.insert(0,'y1')

scren_coords_x2_tf = Entry(
   frame, #Используем нашу заготовку с настроенными отступами.
)
scren_coords_x2_tf.grid(row=2, column=2)
scren_coords_x2_tf.insert(0,'x2')

scren_coords_y2_tf = Entry(
   frame, #Используем нашу заготовку с настроенными отступами.
)
scren_coords_y2_tf.grid(row=3, column=2)
scren_coords_y2_tf.insert(0,'y2')

dir_lb = Label(
   frame,
   text="Screenshots directory",
)
dir_lb.grid(row=4, column=1)

dir_btn = Button(
   frame, #Заготовка с настроенными отступами.
   text='Choose', #Надпись на кнопке.
   command=take_dir
)
dir_btn.grid(row=4, column=3)

interval_lb = Label(
   frame,
   text="Interval between screnshots"
)
interval_lb.grid(row=5, column=1)

timer_lb = Label(
   frame,
   text="Timer before start",
)
timer_lb.grid(row=6, column=1)

dir_tf = Entry(
   frame,
)
dir_tf.grid(row=4, column=2, pady=5)

interval_tf = Entry(
   frame, #Используем нашу заготовку с настроенными отступами.
)
interval_tf.grid(row=5, column=2, padx=5)
interval_tf.insert(0,'0')

video_length_lb = Label(
   frame, #Используем нашу заготовку с настроенными отступами.
   text = 'Video length'
)
video_length_lb.grid(row=7, column=1)

video_length_tf = Entry(
   frame, #Используем нашу заготовку с настроенными отступами.
)
video_length_tf.grid(row=7, column=2)
video_length_tf.insert(0,'60')
timer_tf = Entry(
   frame, #Используем нашу заготовку с настроенными отступами.
)
timer_tf.grid(row=6, column=2)
timer_tf.insert(0,'0')

start_btn = Button(
   frame, #Заготовка с настроенными отступами.
   text='Start', #Надпись на кнопке.
   command=take_screenshots
)
start_btn.grid(row=10, column=2)
take_one_btn = Button(
   frame, #Заготовка с настроенными отступами.
   text='Take one', #Надпись на кнопке.
   command=take_screenshot
)
take_one_btn.grid(row=10, column=1)



label_image = Label(frame)

label_image.grid(row = 12, column=1)

window.mainloop()

