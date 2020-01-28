import itchat
import time
#print('扫一下弹出来的二维码')
itchat.auto_login(hotReload=True)
names = 'short'


while(True):
    boom_remark_name = names
    message = '滚去学习！！！'
    boom_obj = itchat.search_friends(remarkName=boom_remark_name)[0]['UserName']
    itchat.send_msg(msg=message, toUserName=boom_obj)
    print(str(boom_remark_name)+'   已发送!')
    time.sleep(5)

