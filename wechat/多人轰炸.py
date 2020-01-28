import itchat
import time
#print('扫一下弹出来的二维码')
itchat.auto_login(hotReload=True)
names = ['chengli','fang','genggeng','hanling','juan','ll','short','md','miao','qiaohong','shuai',
         'sunhao','wangdan','whp','xiangxiang','xinxin']
name = ['short','short']
for i in range(16):
    boom_remark_name = names[i]
    #boom_remark_name = '亚述'
    #message = input('输入你要轰炸的内容：')
    message = '支付宝五福了解一下'
    boom_obj = itchat.search_friends(remarkName=boom_remark_name)[0]['UserName']
    itchat.send_msg(msg=message, toUserName=boom_obj)
    #print(str(boom_remark_name)+'   已发送!')
