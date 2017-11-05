# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import scrapy
import io
import sys
import os,json
from scrapy.selector import HtmlXPathSelector
from ..items import Sp2Item
from scrapy.http import Request
from scrapy.http.cookies import CookieJar

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')


class ChoutiSpider(scrapy.Spider):
    name = 'chouti'
    allowed_domains = ['chouti.com']
    cookies = None
    cookie_dict = {}

    # #start_requests 在父类里scrapy.Spider
    def start_requests(self):
        yield Request(url="http://dig.chouti.com/", callback=self.index,dont_filter=True)

    def index(self, response):
        #获取首页信息
        print('爬虫返回结果',response,response.url)