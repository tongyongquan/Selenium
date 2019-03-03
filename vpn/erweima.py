# -*- coding:UTF-8 -*-

import qrcode

img = qrcode.make('ssr://MTc4LjE3MC41NC43OTo1NzU5MjphdXRoX2FlczEyOF9tZDU6Y2hhY2hhMjA6dGxzMS4yX3RpY2tldF9hdXRoOlVqRnBRa053Lz9vYmZzcGFyYW09JnByb3RvcGFyYW09JnJlbWFya3M9Y0c5eWJ5NW1kVzdsaFkzb3RMbm5pWWptcktmbXRMTG51cl9vdDY4Jmdyb3VwPVVHOXliLVdGamVpMHVlZUppQQ')
img.save('test.png')
