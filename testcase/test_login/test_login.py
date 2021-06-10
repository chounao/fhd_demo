import requests
from common.Logger import logger
import yaml
import os
import json
import pytest
import allure

from testcase.conftest import api_data

'''先获取yaml文件的内容'''
for key, vlue in api_data.items():
    if key == 'test_login':
        print(key)
        print(vlue)
        logger.info("获取的登录参数为：{}".format(vlue))
    body = vlue


@allure.step("步骤1：登录")
def step_1(body):
    logger.info("用户登录的账户密码为：{}".format(body))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("登录接口测试")
@allure.feature("登录接口")
class Test_login():
    @allure.story("用户登录")
    @allure.description("登录接口的测试用例")
    @allure.issue("http://192.168.16.201/chandao.rantron.biz")
    @allure.testcase("http://chandao.rantron.biz:8083/bug-view-3573.html")
    @allure.title("测试数据：【('userAccount','userPwd'】")
    def test_login(self):
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Referer": 'http://www.fhd001.com',
            "Cookie": "CNZZDATA1263048142=51987825-1583297402-null%7C1583313201; CNZZDATA1276886889=1211049750-1581389138-%7C1586500912; _pati=dceabddd4793a92e54b1f429d2dddc8b; fhdpdd_user_info_nick=cyccyccyc; fhdpdd_user_info_avatar=https://wx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTLRrXUnQ7n5vG2bXPMooFQYxyGw4vadia79F5plrgQdkrwBA3d2ObyDcpiaNYII98sBUIVxAqQmmKJA/132; fhd_user_info_nick=sunking; fhd_user_info_avatar=https://wx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTJiaGdSuKpkrLN4tlrze2OOHwicfS73TJKAScS9toziaicpjWUySrxgickrERnSicVbVtHJSC3Nx2EC5dyA/132; fhdcooperation_id=10086; fhdcooperation_username=%E5%AD%99%E5%BD%AA; fhdcooperation_isAdmin=false; fhdcooperation_isManage=false; fhdcooperation_departmentId=15; fhdcooperation_departmentName=%E7%A0%94%E5%8F%91%E4%B8%AD%E5%BF%83; fhdcooperation_postNo=10; fhdcooperation_postName=%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88; fhdcooperation_token=%7EAwwTIwJBeHVHXVxHclFAJicdcHQZXgJdRFZKUAdfQFMbBQNKEiEOFCNUQFsDQSBRRgB3EAwJRnQDFiQOQ3J3E3IBEyRxQQECTlVVThIhU0EhDRQNdx0mCRJyIBNfBhZzAhF0URIlDBQnU0AjD0FdJkZ9BBB3AEYJDx9XA18HAwYHAw9fG1UJAVpSVVE%3D%7E1%7E; userHeadImgUrl=http%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FQ0j4TwGTfTIdbOjlPgbBtWarETJdX2wSHQNx9icjrG2mpoTuUX6Uobk73BJq6Qh1pB84xC8DBURHfsqQeohlDVA%2F132; yunxu_username=%E5%AD%99%E5%BD%AA; yunxu_token=%7EClPWnK7QjstICAEPA1JSBwFTAE5QAQc%3D%7E1%7E; yunxu_chooseProjectCookieKey=123; JSESSIONID=538A8A21B4CBFD9CCBDF4490F852DE08.fap1-fhdcommon"  }  # 登录请求头
        # 发送请求
        s = requests.session()
        s.headers.update(header)
        r = s.post(url = 'http://www.fhd001.com/loginAccount.do',data=body,verify =False)
        data = json.loads(r.text)
        assert r.status_code == 200 and data['rcode'] == 0 and data["scode"] == 0
        logger.info("登录账号 {} 登录，返回信息 为：{} ，{}，期望结果{},{}".format(body,data['rcode'], data["scode"],0,0))
        return r


    @allure.story("存储cookies")
    @allure.description("存储测试用例")
    @allure.title("测试数据：{}".format("cookie"))
    def test_get_cookies(self):
        cookie = self.test_login().cookies
        cookie = requests.utils.dict_from_cookiejar(cookie)  # 转换cookies格式

        '''获取路径存储cookies'''
        path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        yamlpath = path + '/data/cookies.yaml'#获取路径c
        logger.info("加载存储路径:{}".format(yamlpath))

        """存储cookies"""
        cookies_value = {
            'cookies':cookie
        }
        with open (yamlpath,"w" ,encoding="utf-8")as f:
             yaml.dump(cookies_value,f,Dumper=yaml.Dumper)

        logger.info("存储cookies数据到：{}，存储内容为：{}".format(yamlpath,cookie))
        assert yamlpath != None and len(yamlpath)!= 1

# if __name__ == '__main__':
    #pytest.main(['-m', 'pytest', 'test_login.py', '--html=../HTML/login.html'])