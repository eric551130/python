# Dummy file to make this directory a package.
import tkinter as ok
import time
import threading
def job():
    while(True):
        print("switch on sale")
        w.create_oval(x-r,y-r,x+r,y+r, fill='black')
        w.create_oval(x-r+100,y-r,x+r+100,y+r, fill='black')
        w.create_oval(x-r-100,y-r,x+r-100,y+r, fill='green')
        time.sleep(1.5)
        w.create_oval(x-r,y-r,x+r,y+r, fill='yellow')
        w.create_oval(x-r+100,y-r,x+r+100,y+r, fill='black')
        w.create_oval(x-r-100,y-r,x+r-100,y+r, fill='black')
        time.sleep(1.5)
        w.create_oval(x-r,y-r,x+r,y+r, fill='black')
        w.create_oval(x-r+100,y-r,x+r+100,y+r, fill='red')
        w.create_oval(x-r-100,y-r,x+r-100,y+r, fill='black')
        time.sleep(1.5)

        
root=ok.Tk()
w=ok.Canvas(root,width=400,height=400,bg='white')
w.pack()
x=200
y=100
r=50
w.create_oval(x-r,y-r,x+r,y+r, fill='yellow')
w.create_oval(x-r+100,y-r,x+r+100,y+r, fill='red')
w.create_oval(x-r-100,y-r,x+r-100,y+r, fill='green')
w.create_rectangle(x-160,y-60,x+160,y+60, fill='pink')
threading.Thread(target=job).start()

root.mainloop()
