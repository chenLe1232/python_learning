import requests
import re
import time

# 保持登入的session
index_url = 'http://account.chinaunix.net/login'
header = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "Cache-Control":"max-age=0",
    "Connection":"keep-alive",
    "Host":"account.chinaunix.net",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36 "
}

login_session = requests.session()
token_search = re.compile(r'name="_token"\svalue="(.*?)"')
index_response = login_session.get(url=index_url, headers=header)
# print(index_response.text)
token_value = re.search(token_search,index_response.text).group(1)
# print(token_value)
data = {
    "username": "carline",
    "password": "lechen9527",
    "_token":token_value,
    "_t": int(time.time())
}

login_url = 'http://account.chinaunix.net/login/login'
login_response = login_session.post(url=login_url,headers=header,data=data)
# print(login_response.text)
phone_url = 'http://account.chinaunix.net/ucenter/user/index'
phone_response = login_session.get(url=phone_url,headers=header)
print(phone_response.text)