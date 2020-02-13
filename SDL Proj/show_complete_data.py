import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


from tkinter import *
import os
from PIL import ImageTk,Image

root = Tk() 
root.geometry('{0}x{1}+0+0'.format(root.winfo_screenwidth(), root.winfo_screenheight()))

canvas = Canvas(root, width = root.winfo_screenwidth(), height = root.winfo_screenheight())
canvas.pack()  
img = ImageTk.PhotoImage(Image.open("C:\\Users\\DELL\\Desktop\\a2.png"))  
canvas.create_image(0,0, anchor=NW, image=img) 
youtube_vid= pd.read_csv('USvideos_modified.csv')

Label(root, text=' ~ Complete data description ~   ',font=(" ",23),bg='black',fg='white').place(x=350,y=150)
Label(root, text=youtube_vid,font=(" ",15),width=75,bg='white',fg='black').place(x=350,y=250)

exit = Button(root, text = ' Exit ', fg ='white',width=12,height=1, bd = '0',activeforeground='red',bg='black',command=root.destroy,font=(" ",30)).place(x=610,y=650)

root.mainloop() 
