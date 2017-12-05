# -*- coding: utf-8 -*-
import scrapy
import random
from py_scrapy import settings
from scrapy.conf import settings

class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['https://baidu.com/']

    def parse(self, response):
        # headers = {
        #     # "User-Agent" : random.choice(settings.USER_AGENT)
        #     'User-Agent':random.choice(settings['USER_AGENT'])
        # }
        # # yield scrapy.Request('http://www.xicidaili.com',headers=headers)
        # yield scrapy.Request('http://www.xicidaili.com',headers=headers,callback=self.parsexici)

        print(response.status)

    def parsexici(self, response):
        print(response.status)
