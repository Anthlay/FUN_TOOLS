import random

if __name__ == "__main__":
    xx = input("请输入文章主题:")
    for x in xx:
        tmp = str()
        while ( len(tmp) < 6000 ) :
            分支 = random.randint(0,100)
            if 分支 < 5:
                tmp += 另起一段()
            elif 分支 < 20 :
                tmp += 来点名人名言()
            else:
                tmp += next(下一句废话)
        tmp = tmp.replace("x",xx)
        print(tmp)
