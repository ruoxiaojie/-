# -*- coding: utf-8 -*-
import scrapy


class DigchoutiSpider(scrapy.Spider):
    name = 'digchouti'
    allowed_domains = ['chouti.com']
    start_urls = ['http://chouti.com/']

    def parse(self, response):
        pass
