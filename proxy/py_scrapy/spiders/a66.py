# -*- coding: utf-8 -*-
import scrapy
from py_scrapy.items import ProxyItem


class A66Spider(scrapy.Spider):
    name = '66'
    allowed_domains = ['www.66ip.cn']
    start_urls = ['http://www.66ip.cn/index.html']

    def parse(self, response):
        proxy_list = response.xpath('//div[@align="center"]//tr')[1:]
        # print(proxy_list)
        for proxy in proxy_list:
            item = ProxyItem()
            host = proxy.xpath('./td[1]/text()').extract()
            port = proxy.xpath('./td[2]/text()').extract()
            # print(host,port)

            item['host'] = host
            item['port'] = port

            yield item
        # next_url = response.xpath('//a[13]/@href').extract()
        # print(next_url)
        # yield scrapy.Request('http://www.66ip.cn'+ next_url[0],callback=self.parse)

        for page in range(1,1066):
            next_url = 'http://www.66ip.cn/%d.html' % page

            yield scrapy.Request(next_url,callback=self.parse)


