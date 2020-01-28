import itchat
import requests
import time
def get_response(_info):
    print(_info)
    api_url = 'http://www.tuling123.com/openapi/api'
    data = {
        'key' : '21890c71313d49d389f595c5bf134e09',
        'info' : _info,
        'userid':'微信自动回复机器人'
    }
    r = requests.post(api_url,data=data).json()
    print(r.get('text'))
    return r

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    time.sleep(1)
    return ">> " + get_response(msg["Text"])["text"]

if __name__ =='__main__':
    #itchat.auto_login(hotReload=True)
    itchat.auto_login()
    itchat.run()