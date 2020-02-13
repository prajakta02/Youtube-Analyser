import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from tkinter import *
import os
from PIL import ImageTk,Image

root = Tk()
root.title("YOUTUBE ANALYSER") 
root.geometry('{0}x{1}+0+0'.format(root.winfo_screenwidth(), root.winfo_screenheight()))

canvas = Canvas(root, width = root.winfo_screenwidth(), height = root.winfo_screenheight())
canvas.pack()  
img = ImageTk.PhotoImage(Image.open("C:\\Users\\DELL\\Desktop\\a2.png"))  
canvas.create_image(0,0, anchor=NW, image=img) 

youtube_vid= pd.read_csv('USvideos_modified.csv')

duplicate=youtube_vid['channel_title'].duplicated()

Label(root, text="~ Display duplicate data and its length ~",font=(" ",20),bg='black',fg='white').place(x=350,y=30)
Label(root, text=duplicate,font=(" ",15),width=70).place(x=350,y=80)
Label(root, text=len(duplicate),font=(" ",15),width=70).place(x=350,y=375)

drop= youtube_vid['channel_title'].drop_duplicates()
Label(root, text="~ After dropping duplicate data ~",font=(" ",20),bg='black',fg='white').place(x=350,y=410)
Label(root, text=drop,font=(" ",15),width=70).place(x=350,y=470)

exit = Button(root, text = ' Exit ', fg ='white',width=12,height=1, bd = '0',activeforeground='red',bg='black',command=root.destroy,font=(" ",25)).place(x=1200,y=5)
root.mainloop()


