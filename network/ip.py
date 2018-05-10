#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/9 0009 18:28
# @Author  : wangkun
# @Site    : 
# @File    : ip.py
# @Software: PyCharm
# IP注册地查询——输入ip地址，查询该ip是在哪注册的。
# version 1.0
import ssl
import urllib.request
import json

host = 'https://dm-81.data.aliyun.com'
path = '/rest/160601/ip/getIpInfo.json'
appcode = 'd5145a0874d1420291248fe48d90c87e'
querys = 'ip=15.1.23.4'
url = host + path + '?' + querys
req = urllib.request.Request(url, None, {'Authorization': 'APPCODE ' + appcode}, None, None, 'GET')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
resp = urllib.request.urlopen(req, context=ctx)
content = resp.read()
if (content):
    print(json.loads(content.decode('utf-8'))['data']['country'])
