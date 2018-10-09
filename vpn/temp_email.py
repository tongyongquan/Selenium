# encoding:utf-8
import requests
import time
from lxml import etree

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
s = requests.Session()
r = s.get('http://24mail.chacuo.net/',headers=headers)
selector = etree.HTML(r.text)
email_id = selector.xpath('//*[@id="converts"]/@value')
print(email_id)
data = {
    'data': email_id,
    'type': 'refresh',
    'arg': ''
}
while(1):
    time.sleep(3)
    r = s.post('http://24mail.chacuo.net/', data=data)
    selector = etree.HTML(r.text)
    print(r.text)
    res2 = s.get('http://24mail.chacuo.net/')
    selector2 = etree.HTML(res2.text)
    email_content = selector2.xpath('//*[@id="mailview_data"]/div/text()')
    print(email_content)
