#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/9 0009 11:21
# @Author  : wangkun
# @Site    : 
# @File    : ac.py
# @Software: PyCharm
# 统计元音字母——输入一个字符串，统计处其中元音字母的数量。更复杂点的话统计出每个元音字母的数量。
# 元音字母是a、e、i、o、u,字母‘y’在不是第一个字母的情况下,也被视作元音字母。其他字母均为辅音字母。
# version 1.0
str = 'yearly'
a = e = i = u = o = y = 0
if str[0] == 'y':
    print('y:%d' % (1))
print(str[1:])
for x in str:
    if x == 'a':
        a += 1
    if x == 'e':
        e += 1
    if x == 'i':
        i += 1
    if x == 'u':
        u += 1
    if x == 'o':
        o += 1
print('a:%d' % a)
print('e:%d' % e)
print('i:%d' % i)
print('o:%d' % o)
print('u:%d' % u)
