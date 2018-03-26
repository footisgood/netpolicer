import requests , bs4

url='https://fz.anjuke.com/community/jinana/o2' #晋安区房价
url='https://fz.anjuke.com/community/o2'  #福州全市房价
url='https://fz.anjuke.com/community/cangshan/o2'
#为什么会是这样呢？我打开浏览器是正常的页面，用requests访问就不能得到
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome","Accept": "text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,*/*;q=0.8"}
nno=0
f=open('c:\\1.txt','w',encoding='utf-8')
f.write(url + '\n')

def GetOnePage(url):
    global nno    #需要在一个函数内修改全局变量，就要用这个
    global f
    data = requests.get(url, headers=headers).text.encode('utf-8')
    # data=open('c:\\1.txt','r').read().encode('utf-8')
    # print (data.text)
    soup = bs4.BeautifulSoup(data, 'lxml')
    titles = soup.find_all('div', class_='li-itemmod')
    for i in titles:
        nno += 1
        house_name = i.find('h3').text.strip()
        house_price = i.find('strong').text.strip()
        print(str(nno) + '   ' +house_name + '   :   ' + house_price)
        f.write(str(nno) + '   ' +house_name + '   :   ' + house_price + '\n')
        # print (i.attrs)  #得到字典{'_soj': 'xqlb', 'class': ['li-itemmod'], 'link': 'https://fz.anjuke.com/community/view/584458'}
        # print (i['_soj'].attrs)
        # print ('-'*80)

#main pro
print('The price sorted in Fuzhou , Jinanqu')
print('No.     Name                   Price')
GetOnePage(url)
for n in range (2,10):
    url1=url+'-p'+str(n)
    GetOnePage(url1)
f.close()

'''
def get_html(url):
    proxy = {'http':'117.90.1.251:9000',
        'http':'117.90.252.173:9000'}
    heads = {}
    heads['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
    req = requests.get(url, headers=heads )     #,proxies=proxy)
    html = req.text
    return html

def get_ipport(html):
    regex = r'<td data-title="IP">(.+)</td>'
    iplist = re.findall(regex, html)
    regex2 = '<td data-title="PORT">(.+)</td>'
    portlist = re.findall(regex2, html)
    regex3 = r'<td data-title="类型">(.+)</td>'
    typelist = re.findall(regex3, html)
    sumray = []
    for i in iplist:
        for p in portlist:
            for t in typelist:
                pass
            pass
        a = t+','+i + ':' + p
        sumray.append(a)
    print('高匿代理')
    print(sumray)


if __name__ == '__main__':
    url = 'http://www.kuaidaili.com/free/'
    get_ipport(get_html(url))
'''