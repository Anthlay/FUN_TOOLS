import jieba
from nltk import *
from wordcloud import WordCloud
import matplotlib.pyplot as plt

words = []
with open('txt/骚话6.txt', 'rb') as f:
    for line in f.readlines():
        seg_list = jieba.cut(line, cut_all=False)
        for w in seg_list:
            words.append(w)
f.close()

fdist = FreqDist(words)
fd_sort = sorted(fdist.items(), key=lambda d: d[1],reverse=True)

wc1 = WordCloud(
    scale=16,
    background_color="white",
    font_path="C:\\Windows\\Fonts\\STFANGSO.ttf",#不加这一句显示口字形乱码
)
wc2 = wc1.generate(' '.join(words))

plt.imshow(wc2)
plt.axis("off")
plt.show()
