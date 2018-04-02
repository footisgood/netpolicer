import requests
import bs4
import json

url='http://huaban.com/boards/42191079/'
t=requests.get(url).text
# print(t)
# soup=bs4.BeautifulSoup(t,'lxml')
# f=open(r'c:\jsonhtml.txt' , 'w' ,encoding='utf-8')
# f.write(soup.prettify())
# f.close()

a1='app.page["board"] = '
t1=t[t.find(a1)+len(a1):]  #截去头
a2='app._csr'
t2=t1[:t1.find(a2)-2]  #-2才能去掉"tags":[]}]};最后的;
#此时t2就是中间的数据串json部分了
json_t=json.loads(t2)
print(json_t)


# import os
# fo='d:\\'
# all=os.walk(fo)
# n=0
# for foldername , sub , filenames in all :
#     for filename in filenames :
#         if filename[-3:].upper() == 'JPG':
#             print (filename)
#             n +=1
#
# print ('found total %d files.'%n)
#
# os.get