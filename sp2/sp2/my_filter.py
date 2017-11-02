#!/usr/bin/python
# Author:xiaojie
# -*- coding:utf-8 -*-
from scrapy.utils.request import request_fingerprint
from scrapy.http import Request

class MyDupeFilter(object):
    def __init__(self):
        self.visited_url = set()

    @classmethod
    def from_settings(cls, settings):

        return cls()

    def request_seen(self, request):
        # print(request.url,request.callback)
        # return True
        fp = request_fingerprint(request)
        if fp in self.visited_url:
            return True
        self.visited_url.add(fp)
        return False

    def open(self):
        pass
        print('open replication')

    def close(self, reason):
        pass
        print('close replication')

    def log(self, request, spider):
        pass
        print('repeat', request.url)