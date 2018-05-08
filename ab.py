#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/8 0008 22:43
# @Author  : wangkun
# @Site    : 
# @File    : ab.py
# @Software: PyCharm
# 拉丁猪文字游戏——这是一个英语语言游戏。
# 基本规则是将一个英语单词的第一个辅音音素的字母移动到词尾并且加上后缀-ay
# （譬如“banana”会变成“anana-bay”）。可以在维基百科上了解更多内容
str = 'banana'
yuanyin = list('aeiou')
y = ''
for x in str:
    if x in yuanyin:
        break
    y += x
print(str.replace(y, '', 1) + '-' + y + 'ay')
