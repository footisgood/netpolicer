import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os

s_file=r'c:\十九大报告全文.txt'
(path,name)=os.path.split(s_file)
name=name[:-4]
# os._exit(0)

text=open(s_file, 'r' , encoding='gbk').read()

print(text)
# the font from github: https://github.com/adobe-fonts
font = r'C:\Windows\Fonts\simhei.ttf'
wc = WordCloud(collocations=False, font_path=font, width=1400, height=1400, margin=2).generate(text.lower())
plt.imshow(wc)
plt.axis('off')
plt.show()
wc.to_file(name+'.png') # 把词云保存下来