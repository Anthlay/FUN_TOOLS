import requests
import time

#简单的单线程爬虫
link_list = []
with open('urlsforthread.txt','r') as file:
    file_list = file.readlines()
    for eachone in file_list:
        link = eachone.split('\t')
        #link = link.replace('\n','')
        link_list.append(link)

start = time.time()
for eachone in link_list:
    try:
        r = requests.get(eachone)
        print(r.status_code,eachone)
    except Exception as e:
        print('Error:', e)
end = time.time()
print('串行的总时间为:',end-start)
