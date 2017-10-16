#!/usr/bin/python
#Author:xiaojie
# -*- coding:utf-8 -*-

'''
自动登入抽屉并点赞
'''
import requests
import user


r1 = requests.get('http://dig.chouti.com/help/service')
r1_cookie_dict = r1.cookies.get_dict()

r2 = requests.post('http://dig.chouti.com/login',
             data={
                'phone':user.USER, #用户名
                'password':user.PWD, #密码  配置改了 写自己的帐号密码
                'oneMonth':'1'
             },
                   cookies=r1_cookie_dict)


r3 = requests.post('http://dig.chouti.com/link/vote?linksId=14726881',
                   cookies=r1_cookie_dict)
print(r3.text)





