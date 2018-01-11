#!/usr/bin/python3.5
# Author: xiaojie

import requests
import time
from bs4 import BeautifulSoup


##糗事百科

url = 'https://www.qiushibaike.com/text/page/'
num = 1
for i in range(1,14):
	url = 'https://www.qiushibaike.com/text/page/'
	url = url + str(i)
	time.sleep(0.5) #慢点爬
	print('get ===> ' + url)
	response = requests.get(url)
	res = BeautifulSoup(response.text,'html.parser')
	res_obj_list = res.find_all(name='a',attrs={'class':'contentHerf'})

	# res_obj = res.find(name='div',attrs={'id':'content'})
	# print(res_obj)
	# res_obj_list = res_obj.find_all(name='a',attrs={'class':'contentHerf'})
	# print(res_obj_list)
	# print(res_obj_list.find('span'))

	file = r"C:\Users\Administrator\Desktop\python3\python3\duanzi.txt"
	for res_obj in res_obj_list:
		a = res_obj.find(name='span')
		b = a.text.strip()
		# print(b)
		with open(file,mode='a+',encoding='utf-8') as f:
			f.write(str(num) + ': ' + b + '\n')
			num += 1





