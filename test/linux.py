#!/usr/bin/python3.5
# Author: xiaojie
import pdfkit
import requests,os
from bs4 import BeautifulSoup
if not os.path.exists("pdf"):
    os.mkdir("pdf")
os.chdir("pdf")
url = 'http://www.apelearn.com/study_v2/'
response = requests.get(url=url)
response.encoding='utf-8'
res = BeautifulSoup(response.text,'html.parser')
div_obj = res.find(name='div',attrs={'class':'sidebar'})
li_obj = div_obj.find_all('li')
for i in li_obj:
    a = i.find('a')
    url = 'http://www.apelearn.com/study_v2/'
    html = a.attrs.get('href')
    url = url + html
    print(url)
    pdfFileName = html.replace("html", "pdf")
    config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
    try:
        pdfkit.from_url(url, pdfFileName,configuration=config)
    except:
        pass
