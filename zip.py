import requests
import bs4
import json

def get_from_web():
#这部分代码截取了花瓣上面的代码,再提取出JSON部分
    url='http://huaban.com/boards/42191079/'
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome","Accept": "text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,*/*;q=0.8"}
    t=requests.get(url,headers=headers).text
    a1='app.page["board"] = '
    t1=t[t.find(a1)+len(a1):]  #截去头
    a2='app._csr'
    t2=t1[:t1.find(a2)-2]  #-2才能去掉"tags":[]}]};最后的 ， 此时t2就是中间的数据串json部分了
    json_t=json.loads(t2)
    print(json_t['pins'])
    # f=open(r'c:\o2.txt','w',encoding='utf-8')
    # f.write(t2)
    # f.close()
    n=0
    for x in json_t['pins']:
        a=str(x['orig_source'])
        if a != 'None' :
            n +=1
            fn='c:\\ooo\\' + str(n) + r'.jpg'
            print ('Now downloading %d picture ---%s----%s'%(n,fn,a))
            with open(fn,'wb') as f:
                f.write(requests.get(a).content)


def get_from_file():
#现在已经把JSON保存在文件里面了，来分析
    f=open(r'c:\o2.txt' , 'r' , encoding='utf-8')
    s_text=f.read()
    f.close()
    json_t=json.loads(s_text)
    for x in json_t['pins']:
        print(str(x['orig_source']))


if __name__ == '__main__':
    doit=get_from_web()


# print(t)
# soup=bs4.BeautifulSoup(t,'lxml')
# f=open(r'c:\jsonhtml.txt' , 'w' ,encoding='utf-8')
# f.write(soup.prettify())
# f.close()


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