from tkinter import *
import time
import os
from selenium import webdriver

def weather():
    cityname=Avar.get()
    cityname=cityname.replace('台','臺')
#    print(cityname)
    web = webdriver.Chrome('chromedriver.exe')
    web.get('http://www.cwb.gov.tw/V8/C/W/OBS_Map.html')
    posts=web.find_elements_by_class_name('wrapper')
    data=posts[0].text
#    print(data)
    data=data.split('\n')
    for j in range(len(data)):
        if data[j]==cityname:
            Ans=(data[j+1])
    web.close()        
    AnsArr='{} 溫度為 : {} 度'.format(cityname,Ans)
    label2.configure(text=AnsArr)    

root = Tk()
root.geometry('400x400')

Avar=StringVar()
label1=Label(root, text='查詢各縣市溫度')
label1.pack()


Alabel=Label(root, text='輸入縣市:')
Alabel.pack()
entry1=Entry(root,textvariable=Avar)
entry1.pack()

label2=Label(root)
label2.pack()
Button1=Button(root,text='查詢', command=weather)
Button1.pack()

root.mainloop()
