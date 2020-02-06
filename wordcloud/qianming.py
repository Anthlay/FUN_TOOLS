import jieba
from nltk import *
from wordcloud import WordCloud
import matplotlib.pyplot as plt

words = []
bg_image_path = "pic/loc.jpg"
with open('txt/suki.txt', 'rb') as f:
    for line in f.readlines():
        seg_list = jieba.cut(line, cut_all=False)
        for w in seg_list:
            words.append(w)
f.close()

fdist = FreqDist(words)
fd_sort = sorted(fdist.items(), key=lambda d: d[1],reverse=True)
back_coloring = plt.imread(bg_image_path)  # 设置背景图片
wc1 = WordCloud(
    scale=16,
    background_color="black",
    mask = back_coloring,
    font_path="C:\\Windows\\Fonts\\STFANGSO.ttf",#不加这一句显示口字形乱码
)
wc2 = wc1.generate(' '.join(words))

plt.imshow(wc2)
plt.axis("off")
plt.show()
wc1.to_file("pic/wordcloud.jpg")
