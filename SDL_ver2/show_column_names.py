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

show_col=youtube_vid.columns
Label(root, text="~ Displaying all column names ~",font=(" ",24),bg='black',fg='white').place(x=350,y=190)
Label(root, text=show_col,font=(" ",15),width=75).place(x=340,y=290)

exit = Button(root, text = ' Exit ', fg ='white',width=12,height=1, bd = '0',activeforeground='red',bg='black',command=root.destroy,font=(" ",30)).place(x=610,y=650)
root.mainloop()