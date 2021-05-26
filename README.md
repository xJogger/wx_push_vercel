# wx_push_vercel

基于Vercel和企业微信实现微信消息推送。

效果类似于以下项目：

[Server酱](https://sct.ftqq.com/)

[基于腾讯云Serverless实现的企业微信应用消息推送服务](https://github.com/zyh94946/wx-msg-push-tencent)

需要：github账户、企业微信

第一步，建立企业微信，并获取企业ID（CORP_ID），应用ID（AGENT_ID）和应用secret（AGENT_SECRET）。

教程可参考 [这里](https://github.com/zyh94946/wx-msg-push-tencent#%E5%88%9B%E5%BB%BA%E5%BA%94%E7%94%A8) ，但是不需要获取media_id，本应用只支持文本的推送。

第二步，fork本仓库。

第三步，用Github账号登录Vercel，点击创建项目，导入fork的本仓库，如图。

<img src="https://raw.githubusercontent.com/xJogger/wx_push_vercel/main/img/1.jpg" />

第四步，设置参数。

<img src="https://raw.githubusercontent.com/xJogger/wx_push_vercel/main/img/2.jpg" />

如图，首先设置你的项目名，也是之后的域名前缀。之后设置程序根目录为vercel（中间那个红框），最后将之前获取的企业ID（CORP_ID），应用ID（AGENT_ID）和应用secret（AGENT_SECRET）分别设置为环境变量。同时，设置一个复杂的PUSH_SCKEY，防止别人盗用你的接口。

最后，点击Deply部署即可。

如何使用：

假设最后部署成功的url为https://wx.vercel.app/ ，你设置的PUSH_SCKEY为11223344，那么如下get请求就可以发送消息了：

```
https://wx.vercel.app/11223344.send?text=你的服务器挂了
```

或者这样发送post请求也可以：

```python
import requests
url = f'https://wx.vercel.app/11223344.send'
data = {
           "text" : "你好\n你的服务器挂了",
        }
resp = requests.post(url, data=data)
print(resp.text)
```

