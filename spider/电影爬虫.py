encoding: 'UTF-8'
# 正则表达式真他妈没意思^_^……
# 全部内容已可保存到txt
import csv
import time
import sys
import requests
import os
import re




link_6v = r"http://www.6vhao.tv"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.108 Safari/537.36 2345Explorer/8.8.3.16721'}
r = requests.get(link_6v, headers=headers)
# 防止乱码
print(r.encoding)
r.encoding = 'gb2312'
html = r.text
# 正则表达式部分

list_HTTP = re.findall("https://.*?com", html)
list_nname1 = re.findall('target="_blank">.*?(.*?)</a></li>', html)
list_nname2 = re.findall('target=_blank>.*?(.*?)</a>&nbsp;', html)  # 括号里的重复部分表示只选择缺失部分
list_nname3 = re.findall('title=".*?(.*?)"/><span></span></a><p><a href', html)
list_nname4 = re.findall('target="_blank"><img src=".*?(.*?)" title="', html)  # 海报图片的网址
list_nname = list_nname1 + list_nname2 + list_nname3

# list_nname.sort()  #重新排序@_@，排序之前在列表最前方能看到最近更新电影

# 输出列表元素数量，即电影数量，这种情况下中间不能有逗号@_@
#print("共获取%s个电影名称：" % len(list_nname))

for i in range(10):
    print(list_nname1[i])

for i in range(10):
    print(list_nname2[i])
#for i in range(10):
    #print(list_nname3[i])
