import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
text= open('c:\\十九大报告全文.txt','r',encoding='GBK').read()
# type=chardet(text)
text1=text.decode(type['encoding'])

wordlist_after_jieba = jieba.cut(text , cut_all = True)
wl_space_split = " ".join(wordlist_after_jieba)
print ('-'*60)

my_wordcloud = WordCloud().generate(text_from_file_with_apath)   #wl_space_split)
plt.imshow(my_wordcloud)
# plt.axis("off")
plt.show()