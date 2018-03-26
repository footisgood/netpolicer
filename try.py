lyric= ''
f=open('c:\\福州市房价.txt','r',encoding='utf-8')
lyric=f.read()
# print(lyric)
# print (lyric)
import wordcloud
# w=wordcloud.WordCloud.generate_from_text('adsfadsfdsa')
# print(wordcloud)


import jieba.analyse
result=jieba.analyse.textrank(lyric,topK=50,withWeight=True)
print (result)
keywords=dict()
for i in result :
    keywords[i[0]]=i[1]
print (keywords)

# form pillow import Image,ImageSequence
#
# import numpy as np
# import matplotlib.pyplot as plt
# from wordcloud import WordCloud,ImageColorGenerator
# image=Image.open('c:\\cloud.jpg')
# graph=np.array(image)
# wc=WordCloud(font_path='./fonts/simhet.ttf',background_color='White',max_word=50,mask=graph)
# wc.generate_from_frequencies(keywords)
# image_color=ImageColorGenerator(graph)
# plt.imshow(wc)
# plt.imshow(wc.recolor(color_func=image_color))
# plt.axis('off')
# plt.show()
