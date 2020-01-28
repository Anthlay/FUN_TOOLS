import io
import re

import itchat
import jieba


def parse_signature():
    itchat.login()
    siglist = []
    friends = itchat.get_friends(update=True)[1:]
    for i in  friends:
        signature = i["Signature"].strip().replace("span","").replace("class","").replace("emoji","")
        rep = re.compile("lf\d+\w|[<>/=]")
        signature = rep.sub("",signature)
        siglist.append(signature)
    text = "".join(siglist)
    with io.open('qianming.txt', 'a', encoding='utf-8') as f:
        wordlist = jieba.cut(text, cut_all=True)
        word_space_split = " ".join(wordlist)
        f.write(word_space_split)
        f.close()
if __name__ =='__main__':
    parse_signature()