#!/usr/bin/python
#Author:xiaojie
# -*- coding:utf-8 -*-


from requests.auth import HTTPBasicAuth,HTTPDigestAuth
import requests
ret = requests.get('192.168.1.1/login',auth=HTTPBasicAuth('admin','admin'))
print(ret.text)