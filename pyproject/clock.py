from tkinter import *
import threading
import time
import datetime

def job(w):
    while True:
        x = datetime.datetime.now()
        segment(w,120,20,segnum[int(x.strftime("%H"))%10])#0~9
        segment(w, 20,20,segnum[int(x.strftime("%H"))//10])#0~5            
        segment(w,360,20,segnum[int(x.strftime("%M"))%10])#0~9
        segment(w, 260,20,segnum[int(x.strftime("%M"))//10])#0~5
        segment(w,600,20,segnum[int(x.strftime("%S"))%10])#0~9
        segment(w, 500,20,segnum[int(x.strftime("%S"))//10])#0~5
        time.sleep(1)

def segment(w,x,y,value):
    color=['white','red']
    w.create_oval(x   ,     y, x+52, y+10 , fill=color[int(value[0])]) #a
    w.create_oval(x+50,  y+ 5, x+60, y+60 , fill=color[int(value[1])]) #b
    w.create_oval(x+50, y+ 70, x+60, y+125, fill=color[int(value[2])]) #c
    w.create_oval(x   , y+120, x+52, y+130, fill=color[int(value[3])]) #d
    w.create_oval(x-10, y+ 70,   x,  y+125, fill=color[int(value[4])]) #e
    w.create_oval(x-10, y+  5,   x,  y+60 , fill=color[int(value[5])]) #f
    w.create_oval(x   , y+ 60, x+52, y+70 , fill=color[int(value[6])]) #g
        
master = Tk()
#        abcdefg
segnum=['1111110','0110000','1101101','1111001','0110011','1011011','1011111','1110000','1111111','1110011']
flag=1
w = Canvas(master, width=800, height=200,bg='white')
w.pack()
count=0
mt=Frame(master)
mt.pack()

segment(w,120,20,segnum[0])
segment(w, 20,20,segnum[0])
w.create_oval(210,50,220,60, fill='red')
w.create_oval(210,100,220,110, fill='red')
segment(w,360,20,segnum[0])
segment(w, 260,20,segnum[0])
w.create_oval(450,50,460,60, fill='red')
w.create_oval(450,100,460,110, fill='red')
segment(w,600,20,segnum[0])
segment(w, 500,20,segnum[0])

t = threading.Thread(target = job, args = (w,))
t.start()
 
mainloop()
