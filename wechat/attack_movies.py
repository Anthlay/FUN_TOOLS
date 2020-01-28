encoding: 'UTF-8'
import csv
import time
import sys
import requests
import os
import re
import itchat
import time
itchat.auto_login()#自动登录
boom_remark_name = 'short'       #接收消息用户的备注

#请求头部分

link_6v = r"http://www.6vhao.tv"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.108 Safari/537.36 2345Explorer/8.8.3.16721'}
r = requests.get(link_6v, headers=headers)

r.encoding = 'gb2312'
html = r.text

# 正则表达式部分

list_HTTP = re.findall("https://.*?com", html)
list_nname1 = re.findall('target="_blank">.*?(.*?)</a></li>', html)
list_nname2 = re.findall('target=_blank>.*?(.*?)</a>&nbsp;', html)  # 括号里的重复部分表示只选择缺失部分
list_nname3 = re.findall('title=".*?(.*?)"/><span></span></a><p><a href', html)
list_nname4 = re.findall('target="_blank"><img src=".*?(.*?)" title="', html)  # 海报图片的网址
list_nname = list_nname1 + list_nname2 + list_nname3

boom_obj = itchat.search_friends(remarkName=boom_remark_name)[0]['UserName']
while True:
    message = '首页电影： '
    for i in range(10):
             #发送的消息为某电影网站主页上新上的前十个电影
        message += list_nname[i]
        message += ' '
    print('已发送。。。'+str(message))
    itchat.send_msg(msg=message, toUserName=boom_obj)

    time.sleep(1800)        #每隔半小时发送一次