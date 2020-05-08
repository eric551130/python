from tkinter import *
import threading
import time

global count

def b1():
    global flag
    flag=flag*int(-1)
    
def job(w):
    global count
    while True:
        if flag==-1:
            segment(w,360,20,segnum[count%10])#0~9
            segment(w, 260,20,segnum[int(count/10)%6])#0~5
            segment(w,120,20,segnum[int(count/60)%10])#0~9
            segment(w, 20,20,segnum[int(count/600)%6])#0~5
            time.sleep(1)
            count=count+1
        
def segment(w,x,y,value):
    color=['gray','red']
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
master.geometry('800x800')
w = Canvas(master, width=800, height=200,bg='black')
w.pack()
count=0
mt=Frame(master)
mt.pack()
mb=Frame(master)
mb.pack(side="bottom")
b = Button(mt,text='顯示按鈕',activebackground='purple',command=b1, width="30")
b.pack()

segment(w,120,20,segnum[0])
segment(w, 20,20,segnum[0])
w.create_oval(210,50,220,60, fill='red')
w.create_oval(210,100,220,110, fill='red')
segment(w,360,20,segnum[0])
segment(w, 260,20,segnum[0])

t = threading.Thread(target = job, args = (w,))
t.start()
 
mainloop()
