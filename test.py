#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/9 0009 10:30
# @Author  : wangkun
# @Site    : 
# @File    : test.py
# @Software: PyCharm
def case1():
    print('case1')


def case2():
    print('case2')


def case3():
    print('case3')


switch = {1: case1(), 2: case2(), 3: case3()}
switch[2]
