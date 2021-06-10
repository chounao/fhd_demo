import requests
import json
import time
import hmac
import hashlib
import base64
import urllib.parse
import os


from urllib3 import encode_multipart_formdata

class DingDingWebHook():
    def __init__(self):
        self.url = 'https://oapi.dingtalk.com/robot/send?access_token=4ab68ffa05ae3f34189d8dd9cefdcac463e2851e166e0cf2e3aa506c966e1ceb'
        #self.data = recycle.cancelWaybillCode()
        self.access_token = '4ab68ffa05ae3f34189d8dd9cefdcac463e2851e166e0cf2e3aa506c966e1ceb'
        self.secret = 'SEC01cb9ebe4f3e2d45648e275fad4bc3ed35528d474a3f9fafb309a786f4455521'
    # def get_url(self):
    #     timestamp = str(round(time.time() * 1000))
    #     secret = self.secret
    #     secret_enc = secret.encode('utf-8')
    #     string_to_sign = '{}\n{}'.format(timestamp, secret)
    #     string_to_sign_enc = string_to_sign.encode('utf-8')
    #     hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    #     sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    #     # print(timestamp)
    #     # print(sign)
    #     url = self.url+'&timestamp='+timestamp+'&sign='+sign
    #     # print(url)
    #     return url

    # def get_token(self):
    #     params = {
    #         # "appkey": self.appkey,
    #         "appsecret": self.secret
    #     }
    #     try:
    #         res = requests.get("https://oapi.dingtalk.com/gettoken", params=params)
    #         access_token = res.json().get("access_token")
    #         print(access_token)
    #         return access_token
    #     except Exception as e:
    #         print(e)
    # def get_media_id(self):
    #     '''上传文件并且返回对应的media_id'''
    #     url_post = "https://oapi.dingtalk.com/media/upload?access_token="+self.get_token()+'&type=file'
    #     headers = {}
    #     data = {'access_token': self.access_token,'type': 'file'}
    #     #获取路径
    #     path = os. path.dirname(os.path.dirname(__file__))+ '/data/cookies.yaml'
    #     # files = {'media':open(path,'rb')}
    #     file_name = 'cookies.yaml'
    #     data['media'] = (file_name, open(path, 'rb').read())  # 说明：file_name,不支持中文，必须为应为字符
    #     print(data['media'])
    #     encode_data = encode_multipart_formdata(data)
    #     data = encode_data[0]
    #     headers['Content-Type'] = encode_data[1]
    #     r = requests.post(url_post,headers=headers, data=data)
    #     print(r.text,r.status_code)
    #     media_id = json.loads(r.text)["media_id"]
    #     print(media_id)
    #     return media_id
    def dingTalk(self):

        headers={
            "Content-Type": "application/json",
            "Charset": "UTF-8"
                }
        send_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        # down_load_url = "https://oapi.dingtalk.com/media/downloadFile?access_token=%s&media_id=%s" % (
        # self.access_token, self.get_media_id)
        data = {
            "actionCard": {
                "title": "测试",
                "text":"%s \n\n更新时间：%s \n\n报告地址 %s" % ('测试报告', send_time,"http://localhost:63342/ding_Talk.py/HTML/login.html?_ijt=kg69h5sirqnvvrtp358vdd5i09"),
                "hideAvatar": "0",
                "btnOrientation": "0",
                # "btns": [
                #     {
                #         "title": "点击下载数据",
                #         "actionURL": down_load_url
                #     },
                #
                # ]

            },
            "msgtype": "actionCard"
        }
        r = requests.post(self.ur, data=json.dumps(data), headers=headers)
        print(r.text)
        return json.loads(r.text)




    # def get_urltext(self):
    #     path = os.path.dirname(os.path.dirname(__file__))
    #     yamlpath = path + 'HTML/login.html'
    #
    #     option = webdriver.ChromeOptions()
    #     option.add_argument('--headless')
    #     driver = webdriver.Chrome(chrome_options=option)

if __name__ == '__main__':
    a =DingDingWebHook()
    a.dingTalk()

