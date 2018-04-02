#本程序作用是遍历所有的文件,算出其MD5
import os
import hashlib
import datetime
import pandas as pd

def GetFileMd5(filename):
    if not os.path.isfile(filename):
        return
    m = hashlib.md5()
    # 需要使用二进制格式读取文件内容
    a_file = open(filename, 'rb')
    m.update(a_file.read())
    a_file.close()
    return m.hexdigest()

if __name__=='__main__':
    n=0
    SearchLists = ['JPG' , 'PNG' , 'TXT']
    all=os.walk(r'c:\intel')
    format='%5s |  %80.60s | %40s'
    print (format%('No.','Filename','MD5'))
    allfile =[]
    allmd5 = []
    for foldername , sub , filenames in all :
        for filename in filenames:
            if filename[-3:].upper() in SearchLists :
                n +=1
                #格式化输出示例print('That is %10.2s' % (name2))  整个输出为10列，变量从开始起截取的长度为2，默认右对齐，左边用8(10-2)个空格填充。
                f='/'.join((foldername,filename))  #注意join是用在字符串序列上的
                md5=GetFileMd5(f)
                print (format%(str(n),f,md5))
                allfile.append(f)
                allmd5.append(md5)

    submission = pd.DataFrame({ '文件名': allfile , 'MD5': allmd5 })
    submission.to_csv("submission.csv", index=True , encoding="utf_8_sig")  #需要encoding=utf_8_sig解决中文乱码问题
