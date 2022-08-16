"""
第二题 rpc 调用
4934024
token 未校验
"""
import time
import frida
import requests
from loguru import logger


def my_message_handler(message, payload):
    logger.info(f"message=>{message}")
    logger.info(f"payloa=>{payload}")


# 通过usb连接
device = frida.get_usb_device(10)
logger.info(f'设备=>{device}')

session = device.attach("猿人学2022")
logger.info(f'session=>{session}')

# # load script
with open("../js/second_rpc.js", encoding="utf-8") as f:
    script = session.create_script(f.read())
script.on("message", my_message_handler)
script.load()

# 测试用例
# res = script.exports.invokesign("6:1645678987")
# print(res)


def get_url():
    headers = {
        'Host': 'appmatch.yuanrenxue.com',
        'accept-language': 'zh-CN,zh;q=0.8',
        'user-agent': 'Mozilla/5.0 (Linux; U; Android 11; zh-cn; M2010J19SC Build/RKQ1.201004.002) AppleWebKit/533.1 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.1',
        'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
        'cache-control': 'no-cache',
    }
    params = {
        'token': ''
    }
    total = 0
    for page in range(1, 101):
        ctime = int(time.time())
        cstr = f"{page}:{ctime}"
        sign = script.exports.invokesign(cstr)
        data = {
            'page': page,
            'ts': ctime,
            'sign': sign
        }
        response = requests.post('https://appmatch.yuanrenxue.com/app2', headers=headers, params=params, data=data)
        data_list = response.json().get("data")
        for one in data_list:
            val = one.get("value").strip()
            total += int(val)
    logger.info(f"total:{total}")


if __name__ == '__main__':
    get_url()





