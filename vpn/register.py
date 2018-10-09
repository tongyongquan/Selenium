# encoding:utf-8

import requests

headers = {
    'Pragma': 'no-cache',
    'Origin': 'http://poro.ws',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Cache-Control': 'no-cache',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Referer': 'http://poro.ws/auth/register',
}

data = {
  'email': '',
  'passwd': '',
  'repasswd': '',
  'verifycode': '',
  'code': '',
  'agree': 'on'
}

response = requests.post('http://poro.ws/auth/register', headers=headers, data=data)
# 解码content比特流
print(response.content.decode('unicode_escape'))
