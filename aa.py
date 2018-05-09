#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/8 0008 22:32
# @Author  : wangkun
# @Site    : 
# @File    : aa.py.py
# @Software: PyCharm

# 逆转字符串——输入一个字符串，将其逆转并输出
# version 1.0
str = 'asdf'
ss = ''
for x in str:
    ss = x + ss
print(ss)
# version 1.1
# 切片特性，a[i:j:k],k默认为1.k>0时，i默认为0，j默认为len(a);k<0时，i默认为-1,k默认为-len(a)-1
print(str[::-1])
