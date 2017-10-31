# -*- coding: utf-8 -*-
import scrapy
import io
import sys
import os
from scrapy.selector import HtmlXPathSelector
from ..items import Sp1Item

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')


class ChoutiSpider(scrapy.Spider):
    name = 'chouti'
    allowed_domains = ['chouti.com']
    start_urls = ['http://dig.chouti.com/']

    def parse(self, response):
        # print(response.text)
        hxs = HtmlXPathSelector(response)
        # reslt = hxs.select('//div[@id="yellow-msg-box-intohot"]') #[<HtmlXPathSelector xpath='//div[@id="yellow-msg-box-intohot"]' data='<div class="yellow-comment-msg-box" id="'>]
        item_list = hxs.select(
            '//div[@id="content-list"]/div[@class="item"]')  # [<HtmlXPathSelector xpath='//div[@id="yellow-msg-box-intohot"]' data='<div class="yellow-comment-msg-box" id="'>]
        for item in item_list:
            title = item.select('./div[@class="news-content"]/div[@class="part2"]/@share-title').extract_first()
            url = item.select('./div[@class="news-content"]/div[@class="part2"]/@share-pic').extract_first()
            # print(v)
            obj = Sp1Item(title=title, url=url)
            yield obj

