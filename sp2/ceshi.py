#!/usr/bin/python
#Author:xiaojie
# -*- coding:utf-8 -*-

# from scrapy.http import Request
# from scrapy.utils.request import request_fingerprint
#
# obj =Request(url='http://www.baidu.com',callback=lambda x:x)
# v = request_fingerprint(obj)
# print(v)

l = [1,2,3,4]
obj = iter(l)
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())