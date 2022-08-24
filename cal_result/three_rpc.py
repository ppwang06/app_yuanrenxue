"""
猿人学app 第三题
此函数传入的的值为: 0141661318660000 1661318659000
函数执行返回结果为 6f62132a5db2b97f1209cc3d5b638a837253c7bd706313e424cd07692f7073d2

5127426
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
with open("../js/three_rpc.js", encoding="utf-8") as f:
    script = session.create_script(f.read())
script.on("message", my_message_handler)
script.load()

# 第三题测试用例
# res = script.exports.invoke_sign_three("0141661318660000", 1661318659000)
# print(res)


def get_url():
    headers = {
        'Host': 'appmatch.yuanrenxue.com',
        'accept-language': 'zh-CN,zh;q=0.8',
        'user-agent': 'Mozilla/5.0 (Linux; U; Android 11; zh-cn; M2010J19SC Build/RKQ1.201004.002) AppleWebKit/533.1 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.1',
        'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
        'cache-control': 'no-cache',
    }
    total = 0
    for page in range(1, 101):
        logger.info(f"开始请求第:{page}页")
        ctime = int(time.time() * 1000)
        cstr = f"{page}{ctime}".zfill(16)
        sign = script.exports.invoke_sign_three(cstr, ctime)
        data = {
            'page': page,
            'm': sign
        }
        response = requests.post('https://appmatch.yuanrenxue.com/app3', headers=headers, data=data)
        data_list = response.json().get("data")
        for one in data_list:
            val = one.get("value").strip()
            total += int(val)
    logger.info(f"total:{total}")


if __name__ == '__main__':
    get_url()