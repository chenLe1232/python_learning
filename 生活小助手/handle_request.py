# import requests
#   在发送请求的时候必须导入requests 这个包
# 通过get这个方法来请求数据 request.get
# url

# response = requests.get(url="http://www.qq.com")
# 查看返回 text
# print(response.text)

import requests

# 自定义一个请求头
header = {
    'user-agent': 'imooc/v1'
}
# data = {"key1": "value1", "key2": "value2"}
# response = requests.post("http://httpbin.org/get", params = data)
# data = {"name":"imooc"}
# response = requests.post('http://httpbin.org/post', data=data)
# print(response.text)

# 发送自动的请求头
# response = requests.get("http://httpbin.org/ip", headers = header)
# print(response.status_code)
# print(response.headers, '返回头')
# print(response.request.headers, '请求头')

# response = requests.get('http://www.github.com', timeout= 2)
# print(response.status_code)

# url = 'https://www.baidu.com'
# header = {
#     'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36'
# }
# response = requests.get(url=url, headers=header)
# print(response.headers)
# # 返回的是一个cookie对象，行为和字典类似，拿取到对象自己想要的值
# print(response.cookies)
# print(response.cookies['BAIDUID'])

# 定制一个cookie

url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='hello imooc')
response = requests.get(url=url,cookies=cookies)
print(response.json())
