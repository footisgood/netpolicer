#{"id":12937098,"play_path_64":"http://audio.xmcdn.com/group15/M08/18/8D/wKgDaFbeR_yAvuCQAAw0b5YRfnM585.m4a","play_path_32":"http://audio.xmcdn.com/group15/M04/18/62/wKgDZVbeSAbAu648AASrDDaPrkI164.m4a","play_path":"http://audio.xmcdn.com/group15/M08/18/8D/wKgDaFbeR_yAvuCQAAw0b5YRfnM585.m4a","duration":98,"title":"U16-1 Listening and Understanding","nickname":"YoYo老师","uid":35880913,"waveform":"group15/M04/18/62/wKgDZVbeR__A0IedAAAJHGA-Dms6183.js","upload_id":"u_11774406","cover_url":"http://fdfs.xmcdn.com/group8/M01/19/96/wKgDYFbeSDvhxqJuAAEGnY-g8f4453.jpg","cover_url_142":"http://fdfs.xmcdn.com/group8/M01/19/96/wKgDYFbeSDvhxqJuAAEGnY-g8f4453_web_large.jpg","formatted_created_at":"3月8日 11:34","is_favorited":False,"play_count":35997,"comments_count":60,"shares_count":0,"favorites_count":84,"album_id":3827795,"album_title":"青少版新概念1B配套MP3","intro":None,"have_more_intro":False,"time_until_now":"2年前","category_name":"train","category_title":"外语","played_secs":None,"is_paid":False,"is_free":None,"price":None,"discounted_price":None}
#本程序的目的，是从列表目录中找到每一个课文的网页
#然后从课文网页中提取出音频文件的实际地址，经过测试，音频文件的实际地址并未在网页源代码中，而是通过点击按钮之后，调入了JSON，在里面有播放的地址
#网页地址和实际JSON文件的地址之间的关系：https://m.ximalaya.com/35880913/sound/12937354  --->>>  http://m.ximalaya.com/tracks/12937098.json
#新概念1B的所有课文列表：http://m.ximalaya.com/35880913/album/3827795
#总结一下，这里其实包含3步：一是总列表http://m.ximalaya.com/35880913/album/3827795，找每篇文章https://m.ximalaya.com/35880913/sound/12937354
#第二，从每篇文章中，找到文章标题，并找到JSON。http://m.ximalaya.com/tracks/12937098.json，实际音频地址在里面的play_path项中，可通过data.get('play_path','')得到
#第三，找到最终的http://audio.xmcdn.com/group15/M08/18/8D/wKgDaFbeR_yAvuCQAAw0b5YRfnM585.m4a这样的地址后，

import requests , json , bs4

# a={"id":12937098,"play_path_64":"http://audio.xmcdn.com/group15/M08/18/8D/wKgDaFbeR_yAvuCQAAw0b5YRfnM585.m4a","play_path_32":"http://audio.xmcdn.com/group15/M04/18/62/wKgDZVbeSAbAu648AASrDDaPrkI164.m4a","play_path":"http://audio.xmcdn.com/group15/M08/18/8D/wKgDaFbeR_yAvuCQAAw0b5YRfnM585.m4a","duration":98,"title":"U16-1 Listening and Understanding","nickname":"YoYo老师","uid":35880913,"waveform":"group15/M04/18/62/wKgDZVbeR__A0IedAAAJHGA-Dms6183.js","upload_id":"u_11774406","cover_url":"http://fdfs.xmcdn.com/group8/M01/19/96/wKgDYFbeSDvhxqJuAAEGnY-g8f4453.jpg","cover_url_142":"http://fdfs.xmcdn.com/group8/M01/19/96/wKgDYFbeSDvhxqJuAAEGnY-g8f4453_web_large.jpg","formatted_created_at":"3月8日 11:34","is_favorited":False,"play_count":35997,"comments_count":60,"shares_count":0,"favorites_count":84,"album_id":3827795,"album_title":"青少版新概念1B配套MP3","intro":None,"have_more_intro":False,"time_until_now":"2年前","category_name":"train","category_title":"外语","played_secs":None,"is_paid":False,"is_free":None,"price":None,"discounted_price":None}
# print (a.keys())
# for i in a.items():
#     print (i[0])

def getjson(url1): #从一个页面得到JSON
    #url1='https://m.ximalaya.com/35880913/sound/12937354'
    n=len(url1)-1
    while url1[n] != '/':
        n -=1
    url2='http://m.ximalaya.com/tracks/' + url1[n+1:] + '.json'
    s_data=requests.get(url2)    #访问网站得到所有JSON数据，注意是TEXT
    data=json.loads(s_data.text) #转化为JSON格式一个是json.loads(str)  一个是json.dumps(jsondata)
    return(data.get('play_path',''))

#main
#TODO:从一个单元的播放页面得到实际音频下载地址
s_url='https://m.ximalaya.com/35880913/sound/12937354'
#print (getjson(s_url))
# s_url='http://audio.xmcdn.com/group11/M03/0B/FB/wKgDa1beSXHwHn6oAAP1mnfXDhU396.m4a'
# exit()


#TODO:从一个列表页面取得所有地址
s_all='http://m.ximalaya.com/35880913/album/3827795'  #这个是新概念1B的地址
# s_all='http://m.ximalaya.com/35880913/album/3827799'  #这里是青少版新概念2A配套MP3
s=requests.get(s_all).text
ss1=bs4.BeautifulSoup(s,'lxml')
k=ss1.find_all('a','col info')
for i in range(len(k)):

    href=k[i]['href'].strip()
    title=k[i].text.strip()
    #终于实验出来了！！！这个是网址！['href']
    # #k[i]的类型是bs4.element.tag，如果要得到文本，需要用k[i].text

    print ('No. %d \'s title is :%s and the URL is %s'%(i,title,href))
    s_downloadhref=getjson(href)
    filename='c:\\cql\\' + title + '.m4a'
    r = requests.get(s_downloadhref)
    with open(filename, "wb") as code:
        code.write(r.content)

print ('I total DOWNLOAD : %d M4A FILENAMES!!!'%(len(k)))
