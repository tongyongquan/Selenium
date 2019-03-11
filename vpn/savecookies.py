# -*- coding:UTF-8 -*-

import requests

headers = {
    'Origin': 'http://poro.fun',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Referer': 'http://poro.fun/auth/login',
    'X-Requested-With': 'XMLHttpRequest',
    'Proxy-Connection': 'keep-alive',
}

data = {
  'email': '1070969926@qq.com',
  'passwd': 'tong5228648',
  'remember_me': 'week'
}

response = requests.post('http://poro.fun/auth/login', headers=headers, data=data)
print(response)
print(response.content.decode('unicode_escape'))
print(requests.utils.dict_from_cookiejar(response.cookies))
