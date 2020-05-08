import time
import os
from selenium import webdriver

def weather(cityname):
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
            return(data[j-1])
    web.close()        
    return '沒有發現'

name='台南'
temperturn=weather(name)           

print(name,temperturn)