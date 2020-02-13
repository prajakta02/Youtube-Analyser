import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from tkinter import *
import os
from PIL import ImageTk,Image
from tabulate import tabulate

root = Tk() 
root.geometry('{0}x{1}+0+0'.format(root.winfo_screenwidth(), root.winfo_screenheight()))

canvas = Canvas(root, width = root.winfo_screenwidth(), height = root.winfo_screenheight())
canvas.pack()  
img = ImageTk.PhotoImage(Image.open("C:\\Users\\DELL\\Desktop\\a2.png"))  
canvas.create_image(0,0, anchor=NW, image=img) 


youtube_vid= pd.read_csv('USvideos_modified.csv')
new_table=youtube_vid[['channel_title','video_id','likes','dislikes']]
#head=new_table.head
group=new_table.groupby(['channel_title','video_id'])
Label(root, text="~ Showing channels groupby ~ ",font=(" ",20),bg='black',fg='white').place(x=350,y=70)

g=tabulate(group.first(),tablefmt="simple",showindex="always",numalign='center',floatfmt=".1f")
Label(root, text=g,font=(" ",15),width=70,height=50).place(x=370,y=130)
#print(g)
exit = Button(root, text = ' Exit ', fg ='white',width=12,height=1, bd = '0',activeforeground='red',bg='black',command=root.destroy,font=(" ",30)).place(x=900,y=50)

root.mainloop()
#print(group.first())