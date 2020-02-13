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
first_five=youtube_vid.head()

channel_len=len(youtube_vid['channel_title'].value_counts(ascending=True))
Label(root, text='~ No of channels in data base ~',font=(" ",20),bg='black',fg='white').place(x=350,y=70)
Label(root, text=channel_len,font=(" ",15),width=50).place(x=350,y=110)



max_no_of_videos = max(youtube_vid['channel_title'].value_counts(ascending=True))
Label(root, text='~ Max no of videos by a single channel ~',font=(" ",20),bg='black',fg='white').place(x=350,y=270)
Label(root, text=max_no_of_videos,font=(" ",15),width=50).place(x=350,y=320)


Label(root, text="~ Mean of comments ~",font=(" ",20),bg='black',fg='white').place(x=350,y=500)
Label(root, text=youtube_vid['comment_count'].mean,font=(" ",15),width=50).place(x=350,y=550)

exit = Button(root, text = ' Exit ', fg ='white',width=12,height=1, bd = '0',activeforeground='red',bg='black',command=root.destroy,font=(" ",30)).place(x=610,y=650)
root.mainloop()