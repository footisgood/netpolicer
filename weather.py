import requests
import json
import pymongo
import time

def request(year,month):
    url='http://d1.weather.com.cn/calendar_new/' + year + '/101280701' + year + month + '.html?_=1495685758174'
    headers= {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) aPPLEwEBkIT/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
              'Referer':'http://www.weather.com.cn/weather40d/10128071.shtml'}
    return requests.get(url , headers=headers)

def parse(res):
    json_str=res.content.decode(encoding='utf-8')[11:]
    return json.loads(json_str)

def save(list):
    subkey={'date' : '日期',
            'hmax' : '最高温度','hmin' :'最低温度 ',
            'hgl':'降水概率' ,'fe':'节日','wk':'星期','time':'发布时间'}
    for dict in list:
        subdict={value : dict[key] for key,value in subkey.items()}
        forecast.insert_one(subdict)

if __name__=='__main__':
    year="2016"
    month=1
    client = pymongo.MongoClient('localhost' , 27017)
    test=client['test']
    forecast=test['forecast']
    for i in range(month,13):
        month=str(i) if i>9 else "0"+str(i)
        print (request(year,month))
        # save(parse(request(year,month)))
        # time.sleep(1)
