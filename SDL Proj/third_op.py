from tkinter import *
import os
from PIL import ImageTk,Image

root = Tk() 
root.geometry('{0}x{1}+0+0'.format(root.winfo_screenwidth(), root.winfo_screenheight()))

canvas = Canvas(root, width = root.winfo_screenwidth(), height = root.winfo_screenheight())
canvas.pack()  
img = ImageTk.PhotoImage(Image.open("C:\\Users\\DELL\\Desktop\\a2.png"))  
canvas.create_image(0,0, anchor=NW, image=img) 


def complete_data():
  os.system('python show_complete_data.py') 

def disp_head_tail():
  os.system('python displaying_head.py') 

def sum_max_mean():
  os.system('python no_of_channels_and_max_no_of_videos.py') 

def desc_col():
  os.system('python describing_data_for_all_columns.py') 

def show_col():
  os.system('python show_column_names.py') 

def no_of_videos():
  os.system('python displaying_no_of_videos_by_channel.py') 

def duplicates():
  os.system('python checking_if_any_duplicate.py') 

def correlation():
  os.system('python correlation.py') 

def groupby():
  os.system('python showing_channel_groupby.py') 


Label(root, text=' 1) Complete data description  ->  ',font=(" ",23),bg='black',fg='white').place(x=350,y=70)
complete_data = Button(root, text = 'Click', fg ='black',width=10,height=1, bd = '5',activeforeground='red',bg='white',command=complete_data,font=(" ",15)).place(x=1000,y=70)

Label(root, text=' 2) Displaying head and tail   ->  ',font=(" ",23),bg='black',fg='white').place(x=350,y=140) 
head_tail = Button(root, text = 'Click', fg ='black',width=10,height=1, bd = '5',activeforeground='red',bg='white',command=disp_head_tail,font=(" ",15)).place(x=1000,y=140)

Label(root, text=' 3) Sum, Max and Mean operations on column ->  ',font=(" ",23),bg='black',fg='white').place(x=350,y=210) 
sum_max_mean = Button(root, text = 'Click', fg ='black',width=10,height=1, bd = '5',activeforeground='red',bg='white',command=sum_max_mean,font=(" ",15)).place(x=1000,y=210)

Label(root, text=' 4) Describing data for all column ->  ',font=(" ",23),bg='black',fg='white').place(x=350,y=280) 
desc_col = Button(root, text = 'Click', fg ='black',width=10,height=1, bd = '5',activeforeground='red',bg='white',command=desc_col,font=(" ",15)).place(x=1000,y=280)

Label(root, text=' 5) Display column names  ->  ',font=(" ",23),bg='black',fg='white').place(x=350,y=350) 
show_col = Button(root, text = 'Click', fg ='black',width=10,height=1, bd = '5',activeforeground='red',bg='white',command=show_col,font=(" ",15)).place(x=1000,y=350)

Label(root, text=' 6) Count of videos per channel  ->  ',font=(" ",23),bg='black',fg='white').place(x=350,y=420) 
no_of_videos = Button(root, text = 'Click', fg ='black',width=10,height=1, bd = '5',activeforeground='red',bg='white',command=no_of_videos,font=(" ",15)).place(x=1000,y=410)

Label(root, text=' 7) Handling duplicates  ->  ',font=(" ",23),bg='black',fg='white').place(x=350,y=490) 
duplicates = Button(root, text = 'Click', fg ='black',width=10,height=1, bd = '5',activeforeground='red',bg='white',command=duplicates,font=(" ",15)).place(x=1000,y=490)

Label(root, text=' 8) Correlation   ->  ',font=(" ",23),bg='black',fg='white').place(x=350,y=560) 
correlation = Button(root, text = 'Click', fg ='black',width=10,height=1, bd = '5',activeforeground='red',bg='white',command=correlation,font=(" ",15)).place(x=1000,y=560)

Label(root, text=' 9) Showing channel groupby   ->  ',font=(" ",23),bg='black',fg='white').place(x=350,y=630) 
groupby = Button(root, text = 'Click', fg ='black',width=10,height=1, bd = '5',activeforeground='red',bg='white',command=groupby,font=(" ",15)).place(x=1000,y=630)

exit = Button(root, text = ' Exit ', fg ='white',width=12,height=1, bd = '0',activeforeground='red',bg='black',command=root.destroy,font=(" ",30)).place(x=610,y=700)

root.mainloop() 