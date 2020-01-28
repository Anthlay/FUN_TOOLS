encoding: 'UTF-8'
#正则表达式真他妈没意思^_^……
#全部内容已可保存到txt
import csv
import time
import sys
import requests
import os
import re

from bs4 import BeautifulSoup
path_txt  =  "E:/pyprject/gets_today.txt"
path_csv = "E:/pyprject/gets_td.xlsx"
#写入TXT
def save(output):
#output = '\t'.join(list_nname)将列表转化为字符串的操作

        try:
                with open(path_txt,"a+") as f:
                        f.write(output)
        
        except  UnicodeEncodeError:
                        print("解码异常")
        else:
                #print("写入文件成功")
                f.close()

#按顺序输出并存储列表元素为TXT格式
def txt_opt(list_nname):
        i=1
        for x in list_nname:
                #序号+名称
                print("%d: "%(i)+x,end=' ')
                output2 = ": " + x +"\n"
                save("%d"%i+output2)
                print("写入文件成功")
                print()
                i=i+1
        save("输出时间："+time.ctime())
        print("输出时间："+time.ctime())
#存储列表元素为csv格式
def csv_opt(list_nname):
        with open('gets_td.csv','a+',encoding='UTF-8',newline='')as csvfile:#如果不指定newline='',则一行只有一个元素
                w = csv.writer(csvfile)
                w.writerows(list_nname)
                w.writerow(time.ctime())
#链接网址
link_baidu = r"http://www.baidu.com"
link_qidian = r"http://www.qidian.com"
link_qidian_paihang = r"https://www.qidian.com/rank?chn=21"
link_blog = r"http://www.santostang.com"
link_db250 = r"http://movie.douban.com/top250"
link_6v = r"http://www.6vhao.tv"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.108 Safari/537.36 2345Explorer/8.8.3.16721'}
r = requests.get(link_6v,headers = headers)
#防止乱码
print(r.encoding)
r.encoding = 'gb2312'
html = r.text
#正则表达式部分

list_HTTP = re.findall("https://.*?com",html)
list_nname1 = re.findall('target="_blank">.*?(.*?)</a></li>',html)
list_nname2 = re.findall('target=_blank>.*?(.*?)</a>&nbsp;',html)#括号里的重复部分表示只选择缺失部分
list_nname3 = re.findall('title=".*?(.*?)"/><span></span></a><p><a href',html)
list_nname4 = re.findall('target="_blank"><img src=".*?(.*?)" title="',html)#海报图片的网址
list_nname = list_nname1 + list_nname2 + list_nname3 

#list_nname.sort()  #重新排序@_@，排序之前在列表最前方能看到最近更新电影

'''
#BeautifSoup部分
soup = BeautifulSoup(html,"html.parser")
soup.prettify()

list_nname = soup.find_all("p",class_="keywords")

for i in range(len(list_nname)):
        name = list_nname[i].a.text.strip()
        print("%d: "%i+name)
        save("%d: "%i+name+"\n")
        print("写入文件成功-_-"+'\n')
        
print(time.ctime())
save(time.ctime())
'''
#输出列表元素数量，即电影数量，这种情况下中间不能有逗号@_@
print("共获取%s个电影名称："% len(list_nname))
txt_opt(list_nname)  #输出并保存为TXT文件
csv_opt(list_nname)  #输出并保存为csv文件

'''
#下载图片
j = 1
k="dd"
for x in list_nname4:
        k = x
        r_img = requests.get(k,headers = headers)
        with open(j+'/'+j+'.jpg','wb')as f:
                f.write(r_img.content)
        j=j+1
f.close()
'''
