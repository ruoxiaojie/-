#!/usr/bin/python
#Author:xiaojie
# -*- coding:utf-8 -*-
'''
自动登入github
'''

import requests
from bs4 import BeautifulSoup


# 1. 获取token和cookie
r1 = requests.get(url='https://github.com/login')
b1 = BeautifulSoup(r1.text, 'html.parser')
authenticity_token = b1.find(attrs={'name': 'authenticity_token'}).get('value')

# cookie返回给你
r1_cookie_dict = r1.cookies.get_dict()
# print(authenticity_token)
print(r1_cookie_dict)

'''
utf8:✓
authenticity_token:PN1EDb+bEouYtY4a7dGGgOoXjESIkeBIFgeUHoSxChpHCEprpnDeRE26Ba6SjR2hkExHiTH6HWKeUGMAUonEIQ==
login:edwd
password:qwdqw
commit:Sign in
'''


# 2. 发送用户认证
r2 = requests.post(
    url='https://github.com/session',
    data={
        'commit': 'Sign in',
        'utf8': '✓',
        'authenticity_token': authenticity_token,
        'login': '475030894@qq.com',
        'password': 'liujiehahha',

    },
    cookies=r1_cookie_dict
)
r2_cookie_dict = r2.cookies.get_dict()  # {}


all_cookie_dict = {}
all_cookie_dict.update(r2_cookie_dict)
all_cookie_dict.update(r1_cookie_dict)


## 登录成功之后，可以查看的页面

r3 = requests.get(
    url='https://github.com/settings/emails',
    cookies=all_cookie_dict
)

print(r3.text)
print(r3.content)


















