# -*- coding:UTF-8 -*-

import qrcode

img = qrcode.make('ssr://MTc4LjE3MC41NC43OTo1NzU5MjphdXRoX2FlczEyOF9tZDU6Y2hhY2hhMjA6dGxzMS4yX3RpY2tldF9hdXRoOlVqRnBRa053Lz9vYmZzcGFyYW09JnByb3RvcGFyYW09JnJlbWFya3M9NW9pUjU1cUVjM055UHo4Jmdyb3VwPTVvaVI1NXFFYzNOeVB6OA')
img.save('test.png')
