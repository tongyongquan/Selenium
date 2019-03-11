# -*- coding: UTF-8 -*-
#
import qrcode
import requests
import re

cookies = {
    'uid': '355543',
    'email': '11070969926^%^40qq.com',
    'key': 'c2b3761f082606e6f12d099f5b0f18d3d1264000eb777',
}

headers = {
    'Pragma': 'no-cache',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Accept': 'text/html, */*; q=0.01',
    'Cache-Control': 'no-cache',
    'X-Requested-With': 'XMLHttpRequest',
    'Proxy-Connection': 'keep-alive',
    'Referer': 'http://poro.fun/user/node',
}

response = requests.get('http://poro.fun/user/node/45', headers=headers, cookies=cookies)
res=re.findall('ssr:(.*?)"',response.text)
print(res)
t=0
for result in res:
    my_ssr='ssr:'+result.split('JnJlbWFya')[0]+'JnJlbWFya3M9NW9pUjU1cUVjM055UHo4Jmdyb3VwPTVvaVI1NXFFYzNOeVB6OA'
    img = qrcode.make(my_ssr)
    t+=1
    img.save('test%d.png'%t)
