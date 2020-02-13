from tkinter import *
import os
from PIL import ImageTk,Image

root = Tk() 
root.geometry('{0}x{1}+0+0'.format(root.winfo_screenwidth(), root.winfo_screenheight()))

canvas = Canvas(root, width = root.winfo_screenwidth(), height = root.winfo_screenheight())
canvas.pack()  
img = ImageTk.PhotoImage(Image.open("C:\\Users\\DELL\\Desktop\\a2.png"))  
canvas.create_image(0,0, anchor=NW, image=img) 


def call_op():
	os.system('python third_op.py')

def call_graph():
	os.system('python third_graph.py')

Label(root, text='    ~~ Choose from below options ~~      ',font=(" ",30),bg='black',fg='white').place(x=450,y=120)

op1 = Button(root, text = ' Operation ', fg ='black',width=10,height=1, bd = '10',activeforeground='red',bg='white',command=call_op,font=(" ",25)).place(x=640,y=300)
graph = Button(root, text = ' Graph ', fg ='black',width=10,height=1, bd = '10',activeforeground='red',bg='white',command=call_graph,font=(" ",25)).place(x=640,y=500)

exit = Button(root, text = ' Exit ', fg ='white',width=12,height=1, bd = '0',activeforeground='red',bg='black',command=root.destroy,font=(" ",30)).place(x=610,y=650)

root.mainloop() 
