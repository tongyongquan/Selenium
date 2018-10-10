# encoding:utf-8
import requests
import time
from lxml import etree
import json

headers = {
    'Pragma': 'no-cache',
    'Origin': 'http://24mail.chacuo.net',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': '*/*',
    'Cache-Control': 'no-cache',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Referer': 'http://24mail.chacuo.net/',
}

# 使用会话先获取邮箱id
s = requests.Session()
r = s.get('http://24mail.chacuo.net/',headers=headers)
selector = etree.HTML(r.text)
email_id = selector.xpath('//*[@id="converts"]/@value')
print(email_id)

# 发送刷新检查是否有邮件并得到邮件id
data = {
    'data': email_id,
    'type': 'refresh',
    'arg': ''
}
while(1):
    time.sleep(3)
    r = s.post('http://24mail.chacuo.net/', data=data)
    r_json = json.loads(r.text)
    mid = r_json['data'][0]['list'][0]['MID']
    if mid:
        break

# 获取邮件内容
data2 = {
    'data': email_id,
    'type': 'mailinfo',
    'arg': 'f='+str(mid)
}
r2 = s.post('http://24mail.chacuo.net/', data=data2)
r2_json = json.loads(r.text)
r2_json['data'][0][1][0]['DATA']