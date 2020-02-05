# coding=utf-8
from bs4 import BeautifulSoup
from urllib.request import urlopen


def getPostsByPageUrl(listUrl):
    html = urlopen(listUrl)
    soup = BeautifulSoup(html.read(), "html.parser")

    list = soup.find(attrs={"id": "threadlist"})
    posts = list.findAll(attrs={"class": "tr3"})

    # hasPost 标记是否有过文章了，endCommPost表示是否顶部的那几篇文章被过滤掉了
    flagArr = {"hasPost": False, "endCommPost": False}

    for post in posts:
        nameObj = post.find(attrs={"class": "subject_t"})
        authAndDate = post.find(attrs={"class": "author"})

        if authAndDate:
            flagArr['hasPost'] = True

        if authAndDate == None and flagArr['hasPost'] == True:
            flagArr['endCommPost'] = True

        # 第一页有置顶文章，需要去掉
        # if flagArr['hasPost'] == True and flagArr['endCommPost'] == True and authAndDate != None:
        name = nameObj.string.replace(u'\xa0', u' ')
        auth = authAndDate.find(attrs={"class": "_cardshow"}).string
        date = authAndDate.find("p").string

        print(name)
        '''
        print(auth)
        print(date)
        '''

    # 返回下一页url，如果没有返回false
    nextUrl = soup.find(attrs={"class": "pages_next"})
    if nextUrl != None:
        return nextUrl['href']
    else:
        return False


domain = "http://bbs.xinjs.cn/"
url = domain + "thread.php?fid=45&page=2"

while url:
    tempUrl = getPostsByPageUrl(url)
    break

    if tempUrl:
        url = domain + tempUrl
    else:
        break

print('<<< succ >>')