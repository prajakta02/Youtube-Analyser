import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from tkinter import *
import os
from PIL import ImageTk,Image
from tabulate import tabulate

root = Tk()
root.title("YOUTUBE ANALYSER") 
root.geometry('{0}x{1}+0+0'.format(root.winfo_screenwidth(), root.winfo_screenheight()))

canvas = Canvas(root, width = root.winfo_screenwidth(), height = root.winfo_screenheight())
canvas.pack()  
img = ImageTk.PhotoImage(Image.open("C:\\Users\\DELL\\Desktop\\a2.png"))  
canvas.create_image(0,0, anchor=NW, image=img) 


youtube_vid= pd.read_csv('USvideos_modified.csv')
new_table=youtube_vid[['views','likes','dislikes','trend_day_count','subscriber']]

Label(root, text="~ Correlation ~",font=(" ",24),bg='black',fg='white').place(x=350,y=130)
p=tabulate(new_table.corr(),tablefmt="simple",headers=['views','likes','dislikes','trend_day_count','subscriber'],showindex="always",numalign='center',floatfmt=".1f")
Label(root, text=p,font=(" ",15),width=70).place(x=370,y=200)

exit = Button(root, text = ' Exit ', fg ='white',width=12,height=1, bd = '0',activeforeground='red',bg='black',command=root.destroy,font=(" ",30)).place(x=610,y=650)

root.mainloop()
