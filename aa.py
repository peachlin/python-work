#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/8 0008 22:32
# @Author  : wangkun
# @Site    : 
# @File    : aa.py.py
# @Software: PyCharm

# 逆转字符串——输入一个字符串，将其逆转并输出
str = input()
ss = ''
for x in str:
    ss = x + ss
print(ss)
