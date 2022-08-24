import requests

headers = {
    'Host': 'appmatch.yuanrenxue.com',
    'accept-language': 'zh-CN,zh;q=0.8',
    'user-agent': 'Mozilla/5.0 (Linux; U; Android 11; zh-cn; M2010J19SC Build/RKQ1.201004.002) AppleWebKit/533.1 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.1',
    'content-type': 'application/x-www-form-urlencoded',
    'cache-control': 'no-cache',
}

data = 'm=5b4ff9b2779cc38e486682f22c42c20b6d11c21a47abacb93032fdbf2f18b08f&page=18&token=BWGxW5KMGHzb9jv9zqRyoXzXiiQuZifLNrsDRbi6tT0b8KLMyusq3Lm5%20UAU6AG1'

response = requests.post('https://appmatch.yuanrenxue.com/app3', headers=headers, data=data)
print(response.json())