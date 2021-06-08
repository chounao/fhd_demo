import os
import codecs
import configparser
from common.Logger import logger

def get_config():
    proDir = os.path.split(os.path.realpath(__file__))[0]
    configPath = os.path.join(proDir, "config.ini")

    cf = configparser.ConfigParser()
    cf.read(configPath)
    login_url = cf['HTTP']['login_url']
    work_url = cf['HTTP']['work_url']
    saas_url = cf['HTTP']['saas_url']
    logger.info("获取登录链接：{}，操作链接：{}，SaaS链接：{}".format(login_url,work_url,saas_url))
    return login_url,work_url,saas_url


if __name__ == '__main__':
    get_config()
