from selenium import webdriver

def weather(city,temper):
    cityname='基隆'
    cityname=cityname.replace('台','臺')

    web = webdriver.Chrome('chromedriver.exe')
    web.get('http://www.cwb.gov.tw/V8/C/W/OBS_Map.html')
    posts=web.find_elements_by_class_name('wrapper')
    data=posts[0].text
    data=data.split('\n')
    i=0
    web.close()
    for y in range(42,79,2):
        city.append(data[y])
    for x in range(43,80,2):
        temper.append(data[x])

from random import randint
TRAIN_SET_tem = 40
TRAIN_SET_COUNT = 5000

TRAIN_INPUT = list()
TRAIN_OUTPUT = list()
for i in range(TRAIN_SET_COUNT):
    a = randint(TRAIN_SET_tem*-1,TRAIN_SET_tem)
    if a>=25:
        op=1
    else:
        op=-1
    TRAIN_INPUT.append([a])
    TRAIN_OUTPUT.append(op)

from sklearn.linear_model import LinearRegression

predictor = LinearRegression(n_jobs=-1)
predictor.fit(X=TRAIN_INPUT, y=TRAIN_OUTPUT)

print('+---------------------+---------------+')
print('| Outside Temperature | Wear a Jacket |')
print('+---------------------+---------------+')
temper=[]
city=[]
weather(city,temper)

for i in range(len(temper)):    
    X_TEST = [[int(float(temper[i]))]]
    outcome = predictor.predict(X=X_TEST)
    coefficients = predictor.coef_
    #print('Outcome : {}\nCoefficients : {}'.format(outcome, coefficients))
    if(outcome<0):
        ans='yes'
    else:
        ans='no'
    print('| {}:{}°C   | {}            |'.format(city[i],X_TEST, ans))


print('+---------------------+---------------+')

