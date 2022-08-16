"""
第一题的计算结果
4902423
使用方式:
token 无校验 不使用token依可
将以下代码的token 换成自己抓包的token 即可使用。共有两处需要替换的token
不需要请求时间 直接用当前时间即可
"""
import time
import requests
from utils.first_app import Sign
from loguru import logger


headers = {
    'Host': 'appmatch.yuanrenxue.com',
    'accept-language': 'zh-CN,zh;q=0.8',
    'user-agent': 'Mozilla/5.0 (Linux; U; Android 11; zh-cn; M2010J19SC Build/RKQ1.201004.002) AppleWebKit/533.1 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.1',
    'cache-control': 'no-cache',
}


class FirstHandle:

    def __init__(self):
        self.sign = Sign()

    def get_page(self, page):
        ctime = int(time.time())
        headers['content-type'] = 'application/x-www-form-urlencoded'
        target_str = f"page={page}{ctime}"
        sign = self.sign.sign(target_str)
        data = {
            'page': page,
            'sign': sign,
            't': ctime,
            'token': '抓包采用自己的token'
        }
        response = requests.post('https://appmatch.yuanrenxue.com/app1', headers=headers, data=data)
        return response.json()

    def get_result(self):
        total = 0
        for i in range(1, 101):
            logger.info(f"开始处理第{i}页数据...")
            data = self.get_page(i)
            data_list = data.get("data")
            for one in data_list:
                val = one.get("value").strip()
                total += int(val)
        logger.info(f"最终结果为:{total}")


if __name__ == '__main__':
    fh = FirstHandle()
    fh.get_result()

