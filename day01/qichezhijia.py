#!/usr/bin/python
#Author:xiaojie
# -*- coding:utf-8 -*-
'''
爬取汽车之家 新闻里面的图片
'''
import requests
from bs4 import BeautifulSoup

# http方式
response = requests.get('http://www.autohome.com.cn/news/')
response.encoding='gbk'


# 文件方式
# with open('autohome_new_txt','r',encoding='utf-8') as f:
#     data = f.read()

root = BeautifulSoup(response.text,'html.parser')
outer_div_obj = root.find(name='div',attrs={'id':'auto-channel-lazyload-article'})

li_obj_list = outer_div_obj.find_all('li') # [标签对象,标签对象]
for li_obj in li_obj_list:
    h3 = li_obj.find(name='h3')
    if not h3:
        continue
    title_obj = li_obj.find('h3')
    summary_obj = li_obj.find('p')
    img_obj = li_obj.find('img')
    src = img_obj.attrs.get('src') #图片url没有http
    # print(src)
    # print(h3.text,li.find(name='a').get('href'))
    # print(title_obj.text,summary_obj.text)

    img_url = 'http:'+src #图片url
    # print(img_url)

    img_file_name = img_url.rsplit('/', maxsplit=1)[1]
    # print(img_file_name) #图片名字

    img_res = requests.get(img_url)
    with open(img_file_name,'wb') as f:
        f.write(img_res.content)
