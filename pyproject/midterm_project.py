from tkinter import *
import time
import os
from selenium import webdriver
import threading
import datetime

def weather():
    cityname=CityVar.get()
    cityname=cityname.replace('台','臺')
    web = webdriver.Chrome('chromedriver.exe')
    web.get('http://www.cwb.gov.tw/V8/C/W/OBS_Map.html')
    posts=web.find_elements_by_class_name('wrapper')
    data=posts[0].text
    data=data.split('\n')
    temperture=None
    for j in range(len(data)):
        if data[j]==cityname:
            temperture=(data[j+1])   
    web.close()      
    if temperture==None:   
        AnsArr='查無 {} 的資料'.format(cityname)
        Anslabel.configure(text=AnsArr, font=("微軟正黑體",20))    
    else:    
        AnsArr='{} 溫度為 : {} ℃'.format(cityname,temperture)
        Anslabel.configure(text=AnsArr, font=("微軟正黑體",20))         

def clear():
    Anslabel.configure(text="")
    entry1.delete(0,END)

def segment(w,x,y,value):
    color=['white','red']
    w.create_oval(x   ,     y, x+52, y+10 , fill=color[int(value[0])]) #a
    w.create_oval(x+50,  y+ 5, x+60, y+60 , fill=color[int(value[1])]) #b
    w.create_oval(x+50, y+ 70, x+60, y+125, fill=color[int(value[2])]) #c
    w.create_oval(x   , y+120, x+52, y+130, fill=color[int(value[3])]) #d
    w.create_oval(x-10, y+ 70,   x,  y+125, fill=color[int(value[4])]) #e
    w.create_oval(x-10, y+  5,   x,  y+60 , fill=color[int(value[5])]) #f
    w.create_oval(x   , y+ 60, x+52, y+70 , fill=color[int(value[6])]) #g

def job(w):
    while True:
        x = datetime.datetime.now()
        segment(w,190,20,segnum[int(x.strftime("%H"))%10])#0~9
        segment(w, 90,20,segnum[int(x.strftime("%H"))//10])#0~5            
        segment(w,430,20,segnum[int(x.strftime("%M"))%10])#0~9
        segment(w, 330,20,segnum[int(x.strftime("%M"))//10])#0~5
        segment(w,670,20,segnum[int(x.strftime("%S"))%10])#0~9
        segment(w, 570,20,segnum[int(x.strftime("%S"))//10])#0~5
        time.sleep(1)


#####主視窗
master = Tk()
master.geometry('800x500')
master.title('10703072A溫度查詢')
###########

########7段顯示器時鐘
segnum=['1111110','0110000','1101101','1111001','0110011','1011011','1011111','1110000','1111111','1110011']

timeframe=Frame(master, width=800, height=50)
timeframe.pack(side=TOP)
timelable=Label(timeframe, text='現在時間', font=("微軟正黑體",20),)
timelable.place(x=10,y=10)

w = Canvas(master, width=800, height=170)
w.pack()
segment(w,190,20,segnum[0])
segment(w, 90,20,segnum[0])
w.create_oval(280,50,290,60, fill='red')
w.create_oval(280,100,290,110, fill='red')
segment(w,430,20,segnum[0])
segment(w, 330,20,segnum[0])
w.create_oval(520,50,530,60, fill='red')
w.create_oval(520,100,530,110, fill='red')
segment(w,670,20,segnum[0])
segment(w, 570,20,segnum[0])

t = threading.Thread(target = job, args = (w,))
t.start()

#####################

######處理氣候溫度
CityVar=StringVar()
label1=Label(master, text='查詢各縣市溫度', font=("微軟正黑體",24))
label1.pack()

Aframe=Frame(master)
Aframe.pack(side=TOP)
Alabel=Label(Aframe, text='輸入縣市:', font=("微軟正黑體",20))
Alabel.pack(side=LEFT)
entry1=Entry(Aframe,textvariable=CityVar,font=(20))
entry1.pack(side=LEFT)

Anslabel=Label(master)
Anslabel.pack()

Bframe=Frame(master,width=200,height=100)
Bframe.pack(side=TOP)
searchButton=Button(Bframe,text='查詢', command=weather,font=(20))
searchButton.place(x=20,y=10)
clearBurtton=Button(Bframe,text='清除', command=clear,font=(20))
clearBurtton.place(x=120,y=10)
###################


mainloop()