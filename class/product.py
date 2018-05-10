#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/9 0009 17:43
# @Author  : wangkun
# @Site    : 
# @File    : product.py
# @Software: PyCharm
# 产品库存管理——创建一个管理产品库存的应用。
# 建立一个产品类，包含价格、id、库存数量。然后建立一个库存类，记录各种产品并能计算库存的总价值。
# version 1.0
class Product(object):
    def __init__(self, id, price, num):
        self.id = id
        self.price = price
        self.num = num

    def print(self):
        print('id:%s,price:%s,num:%s' % (self.id, self.price, self.num))


class Store(object):
    def __init__(self, products):
        self.products = products

    def getValue(self):
        i = 0
        for x in self.products:
            i += x.price * x.num
        return i


p_a = Product('1', 12, 2)
p_b = Product('2', 23, 5)
p_c = Product('3', 24, 6)

s_1 = Store([p_a, p_b, p_c])
print('value is %d' % s_1.getValue())
