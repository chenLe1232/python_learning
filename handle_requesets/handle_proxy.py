import requests

# 带着阿布云的代理模式 使用的是动态版的
proxy = {
    "http":"http://HS2WUWF8RS32S9ED:9B19029B70680277@http-dyn.abuyun.com:9020",
    "https":"http://HS2WUWF8RS32S9ED:9B19029B70680277@http-dyn.abuyun.com:9020"
}
url = 'http://httpbin.org/ip'

for i in range(5):
    response = requests.get(url=url, proxies=proxy)
    print(response.text)