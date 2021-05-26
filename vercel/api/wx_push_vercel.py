import os
import json
import requests
from flask import Flask, Response, redirect,url_for,request,abort

def get_tocken(corp_id,agent_secret):
    url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={agent_secret}'
    resp = requests.get(url)
    return resp.json()['access_token']

def push_msg(agent_id,access_token,msg_content):
    url = f'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}'
    headers = {'Content-Type': 'application/json'}
    data = {
               "touser" : "@all",
               "toparty" : "",
               "totag" : "",
               "msgtype" : "text",
               "agentid" : agent_id,
               "text" : {
                   "content" : msg_content
               },
               "safe":0,
               "enable_id_trans": 0,
               "enable_duplicate_check": 0,
               "duplicate_check_interval": 1800
            }
    resp = requests.post(url, headers=headers, data=json.dumps(data))
    return resp.json()


app = Flask(__name__)
@app.route('/<push_sckey_user>.send', methods=['GET', 'POST'])
def pusher(push_sckey_user):
    corp_id      = os.getenv('CORP_ID')       # 企业ID
    agent_id     = int(os.getenv('AGENT_ID')) # 应用ID(int型)
    agent_secret = os.getenv('AGENT_SECRET')  # 应用的Secrst
    push_sckey   = os.getenv('PUSH_SCKEY')   # 推送程序的的SCKEY

    if push_sckey_user == push_sckey :
        if request.method == 'GET':
            msg_content = request.args.get('text')
        elif request.method == 'POST':
            msg_content = request.form['text']
        else:
            return Response('method not right!', mimetype="text/html")


        try:
            access_token = get_tocken(corp_id,agent_secret)
        except Exception as e:
            return Response('access_token error!', mimetype="text/html")
        try:
            resp         = push_msg(agent_id,access_token,msg_content)
        except Exception as e:
            return Response('push_msg!', mimetype="text/html")
        
        if resp['errmsg'] == 'ok':
            return Response('push msg succeed!', mimetype="text/html")
        else:
            return Response('push msg failed!', mimetype="text/html")
    else:
        return Response('sckey not right!', mimetype="text/html")

# if __name__ == '__main__':
#     app.run(debug=True,host="0.0.0.0")