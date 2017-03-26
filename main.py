import itchat
import datetime
import requests

KEY = '6e760a6039a64d46ba6f174f7d74b278'
API_URL = 'http://www.tuling123.com/openapi/api'


def get_tuling_response(msg,id):
    apiUrl = API_URL
    data = {
        'key':KEY,
        'info':msg,
        'userid': id
    }
    try:
        r= requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        print("Tuling connection failed")
        return



@itchat.msg_register([itchat.content.TEXT,itchat.content.VOICE],isFriendChat=True)
def get_friend_msg(msg):
    print("{}: {}".format(msg['FromUserName'],msg['Text']))
    print(msg)
    tuling_msg = get_tuling_response(msg['Text'],msg['FromUserName'])
    itchat.send_msg(u'{} -auto reply {}:{}'.format(tuling_msg,datetime.datetime.now().hour,
                                                    datetime.datetime.now().minute),msg['FromUserName'])

@itchat.msg_register([itchat.content.TEXT,itchat.content.VOICE],isGroupChat=True)
def get_group_msg(msg):
    print("{}: {}".format(msg['FromUserName'],msg['Text']))
    print(msg)
    return

itchat.auto_login(hotReload=True,enableCmdQR=True)
itchat.run()