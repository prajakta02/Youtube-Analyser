from tkinter import *
import os                                                       #for connectivity
from PIL import ImageTk,Image                                   #for img display

root = Tk() 
#root.geometry('640x640+0+0')
root.geometry('{0}x{1}+0+0'.format(root.winfo_screenwidth(), root.winfo_screenheight()))

canvas = Canvas(root, width = root.winfo_screenwidth(), height = root.winfo_screenheight())
#canvas = Canvas(root, width = '{0}x{1}+0+0', height ='{0}x{1}+0+0' )  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open("C:\\Users\\DELL\\Desktop\\a.png"))  
canvas.create_image(0,0, anchor=NW, image=img) 


def call_sec_pg():
	os.system('python sec_pg.py')

Label(root, text='                                         ~~ YOUTUBE ANALYSIS  ~~                                                     ',bg="black", fg ='white',font=("arial ",35)).place(x=0,y=70)

start = Button(root, text = '  Start ', fg ='white',width=12,height=1, bd = '0',activeforeground='red',bg='black',command=call_sec_pg,font=(" ",30)).place(x=470,y=620)

exit = Button(root, text = ' Exit ', fg ='white',width=12,height=1, bd = '0',activeforeground='red',bg='black',command=root.destroy,font=(" ",30)).place(x=970,y=620)

root.mainloop() 
