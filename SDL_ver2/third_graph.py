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



def subsc_bar():
  os.system('python bar_graph_no_of_sbscribers.py')

def likes_dis():
  os.system('python bar_graph_likes_dislikes.py')

def pie_chart():
  os.system('python pie_chart_no_of_views.py')

def heat_map():
  os.system('python heat_map_correlation.py')

Label(root, text='  Bar Graph (Number of subscribers) ->  ',font=(" ",23),bg='black',fg='white').place(x=350,y=190)
subsc_bar = Button(root, text = 'GRAPH 1', fg ='black',width=10,height=1, bd = '5',activeforeground='red',bg='white',command=subsc_bar,font=(" ",15)).place(x=950,y=190)

Label(root, text='  Bar Graph (Likes Vs Dislikes) ->  ',font=(" ",23),bg='black',fg='white').place(x=350,y=290)
likes_dis = Button(root, text = 'GRAPH 2', fg ='black',width=10,height=1, bd = '5',activeforeground='red',bg='white',command=likes_dis,font=(" ",15)).place(x=950,y=290)

Label(root, text='  Pie Chart (Number of views) ->  ',font=(" ",23),bg='black',fg='white').place(x=350,y=390)
pie_chart = Button(root, text = 'GRAPH 3', fg ='black',width=10,height=1, bd = '5',activeforeground='red',bg='white',command=pie_chart,font=(" ",15)).place(x=950,y=390)

Label(root, text='  Heat Map (Correlation) ->  ',font=(" ",23),bg='black',fg='white').place(x=350,y=490)
heat_map = Button(root, text = 'GRAPH 4', fg ='black',width=10,height=1, bd = '5',activeforeground='red',bg='white',command=heat_map,font=(" ",15)).place(x=950,y=490)


exit = Button(root, text = ' Exit ', fg ='white',width=12,height=1, bd = '0',activeforeground='red',bg='black',command=root.destroy,font=(" ",30)).place(x=610,y=650)

 
'''def main():
    t.onclick(click)
    t.mainloop()'''

root.mainloop() 

