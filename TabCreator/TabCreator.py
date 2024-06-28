import pytesseract
import cv2
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox 
from PIL import Image,ImageTk, ImageGrab
import time
import os

ex_dir = ''
x1=0
x2=0
y1=0
y2 = 0
path=''

def screenshot_base():
    global x1,x2,y1,y2,path
    path = str(dir_tf.get())
    x1 = int(screen_coords_x1_tf.get())
    y1 = int(screen_coords_y1_tf.get())
    x2 = int(screen_coords_x2_tf.get())
    y2 = int(screen_coords_y2_tf.get())

def take_screenshots():
    screenshot_base()
    pytesseract.pytesseract.tesseract_cmd = dir_pytesseract_tf.get()
    print(path)
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
        if time_between==0:
            if textOld!=textNew:
                  index+=1
                  i = ImageGrab.grab(bbox=(x1, y1, x2, y2))
                  i.save(f'{path}\\tab{index}.jpg')
                  image = cv2.imread(f'{path}\\tab{index}.jpg')
                  print('readed')
                  if time_between!=0:
                     time.sleep(time_between)
                  else:
                     textNew = pytesseract.image_to_string(image,config='--psm 13')
                  textOld=textNew
            else:
                  time.sleep(0.5)
                  i = ImageGrab.grab(bbox=(x1, y1, x2, y2))
                  i.save(f'{path}\\temp.jpg')
                  image = cv2.imread(f'{path}\\temp.jpg')
                  textNew = pytesseract.image_to_string(image,config='--psm 11')
                  os.remove(f'{path}\\temp.jpg')
        else:
            index+=1
            i = ImageGrab.grab(bbox=(x1, y1, x2, y2))
            i.save(f'{path}\\tab{index}.jpg')
            image = cv2.imread(f'{path}\\tab{index}.jpg')
            time.sleep(time_between)   
        print(textNew)
        length-=1
    messagebox.showinfo('showInfo','Done')
    window.title('Done')
def take_dir():
    text = filedialog.askdirectory()
    dir_tf.delete(0,END)
    dir_tf.insert(0,text)
    return

def take_file():
    file = filedialog.askopenfile(mode='r',filetypes=[('exe file', '*.exe')])
    path = os.path.abspath(file.name)
    dir_pytesseract_tf.delete(0,END)
    dir_pytesseract_tf.insert(0,path)
    return

def take_screenshot():
    screenshot_base()
    i = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    i.save(f'{path}\\test.jpg')
    time_before = int(timer_tf.get())
    while time_before:
        time.sleep(1)
        time_before-=1
    ex_image = ImageTk.PhotoImage(Image.open(f'{path}\\test.jpg').resize((250,250)))
    label_image.configure(image=ex_image)
    label_image.image = ex_image
    

window = Tk()
window.geometry('800x600')
window.title("Input")
frame = Frame(
   window, 
   padx = 10, 
   pady = 10 
)
frame.pack(expand=True)

screen_coords_lb = Label(
   frame,
   text="Screenshot coordinates",
)
screen_coords_lb.grid(row=1, column=1)

screen_coords_x1_tf = Entry(
   frame, #Используем нашу заготовку с настроенными отступами.
   textvariable='10'
)
screen_coords_x1_tf.grid(row=2, column=1)
screen_coords_x1_tf.insert(0,'x1')

screen_coords_y1_tf = Entry(
   frame, #Используем нашу заготовку с настроенными отступами.
)
screen_coords_y1_tf.grid(row=3, column=1)
screen_coords_y1_tf.insert(0,'y1')

screen_coords_x2_tf = Entry(
   frame, #Используем нашу заготовку с настроенными отступами.
)
screen_coords_x2_tf.grid(row=2, column=2)
screen_coords_x2_tf.insert(0,'x2')

screen_coords_y2_tf = Entry(
   frame, #Используем нашу заготовку с настроенными отступами.
)
screen_coords_y2_tf.grid(row=3, column=2)
screen_coords_y2_tf.insert(0,'y2')

dir_lb = Label(
   frame,
   text="Screenshots directory",
)
dir_lb.grid(row=4, column=1)

dir_pytesseract_lb = Label(
   frame,
   text="tesseract.exe directory",
)
dir_pytesseract_lb.grid(row=5, column=1)

dir_pytesseract_btn = Button(
   frame, #Заготовка с настроенными отступами.
   text='Choose', #Надпись на кнопке.
   command=take_file
)
dir_pytesseract_btn.grid(row=5, column=3)

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
interval_lb.grid(row=6, column=1)

timer_lb = Label(
   frame,
   text="Timer before start",
)
timer_lb.grid(row=7, column=1)

dir_tf = Entry(
   frame,
)
dir_tf.grid(row=4, column=2)

dir_pytesseract_tf = Entry(
   frame,
)
dir_pytesseract_tf.grid(row=5, column=2)


interval_tf = Entry(
   frame, #Используем нашу заготовку с настроенными отступами.
)
interval_tf.grid(row=6, column=2)
interval_tf.insert(0,'0')

video_length_lb = Label(
   frame, #Используем нашу заготовку с настроенными отступами.
   text = 'Video length'
)
video_length_lb.grid(row=8, column=1)

video_length_tf = Entry(
   frame, #Используем нашу заготовку с настроенными отступами.
)
video_length_tf.grid(row=8, column=2)
video_length_tf.insert(0,'60')

timer_tf = Entry(
   frame, #Используем нашу заготовку с настроенными отступами.
)
timer_tf.grid(row=7, column=2)
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