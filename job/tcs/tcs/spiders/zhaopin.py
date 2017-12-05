# -*- coding: utf-8 -*-
import scrapy
from scrapy.spider import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import datetime
from datetime import timedelta
from tcs.items import ZhilianItem
import re
from scrapy_redis.spiders import RedisCrawlSpider


class ZhaopinSpider(RedisCrawlSpider):
    name = 'zhaopin'
    allowed_domains = ['jobs.zhaopin.com']
    # start_urls = ['http://jobs.zhaopin.com/']
    redis_key = 'zhaopinspider:urls'

    rules = (
        # / bj20700001 /

        # Rule(LinkExtractor(allow=r'bj\d+/?'), follow=True),
        # Rule(LinkExtractor(allow=r'jobs.zhaopin.com/bj\d+/$'), follow=True),
        Rule(LinkExtractor(allow=r'jobs.zhaopin.com/bj[0-9]+/$'), follow=True),
        Rule(LinkExtractor(allow=r'/in[0-9]+/$'), follow=True),
        Rule(LinkExtractor(allow=r'[0-9].htm'), callback='parse_item', follow=True),

    )

    num_pattren = re.compile(r'\d+')
    def parse_item(self, response):
        # print(response.url)
        item = ZhilianItem()
        #链接地址
        job_url = response.url
        #公司名字
        job_comp = response.css('.top-fixed-box h2 a::text').extract()
        if len(job_comp):
            job_comp = job_comp[0]
        else:
            job_comp = ''
        #职业岗位
        job_name = response.css('.top-fixed-box h1::text').extract()
        if len(job_name):
            job_name = job_name[0]
        else:
            job_name = ''
        #学历
        job_degree = response.xpath('//ul[@class="terminal-ul clearfix"]/li[6]/strong/text()').extract()
        if len(job_degree):
            job_degree = job_degree[0]
        else:
            job_degree = '0'
        #薪资job_smoney job_emoney
        job_money = response.xpath('//ul[@class="terminal-ul clearfix"]/li[1]/strong/text()').extract()
        if len(job_money):
            job_money = job_money[0]
            if '/' in job_money:
                job_smoney = job_money.split('-')[0]
                job_smoney = round(int(job_smoney)/1000)
                job_emoney = job_money.replace('元/月', '').split('-')[1]
                job_emoney = round(int(job_emoney)/1000)
            else:
                job_smoney = 0
                job_emoney = 0
        #公司地址job_address
        job_address = response.xpath('//ul[@class="terminal-ul clearfix"]/li[2]/strong/a/text()').extract()
        if len(job_address):
            job_address = job_address[0]
        else:
            job_address = '无'
        #公司类型(民营,国营)job_comp_type
        job_comp_type = response.xpath('//ul[@class="terminal-ul clearfix terminal-company mt20"]/li[2]/strong/text()').extract()[0]
        #公司规模job_comp_snum job_comp_enum
        job_comp_num = response.xpath('//ul[@class="terminal-ul clearfix terminal-company mt20"]/li[1]/strong/text()').extract()
        if len(job_comp_num):
            job_comp_num = job_comp_num.pop()
            if '-' in job_comp_num:
                job_comp_snum = job_comp_num.split('-')[0]
                job_comp_enum = job_comp_num.replace('人', '').split('-')[1]
            else:
                print(job_comp_num)
                job_comp_snum = job_comp_num.replace('人以上','')
                job_comp_enum = job_comp_num.replace('人以上','')

        #公司主营job_business
        job_business = response.xpath('//ul[@class="terminal-ul clearfix terminal-company mt20"]/li/strong/a/text()').extract()[0]
        #工作经验job_syear job_eyear
        job_year = response.xpath('//ul[@class="terminal-ul clearfix"]/li[5]//strong/text()').extract()[0]
        job_syear, job_eyear = self.process_year(job_year)
        #发布日期job_date_pub
        job_date_pub = response.xpath('//ul[@class="terminal-ul clearfix"]//strong/span/text()').extract()[0]
        #爬取日志job_datetime
        # job_datetime = datetime.datetime.now().strftime('%Y-%m-%d')
        job_datetime = datetime.datetime.now().strftime("%Y-%m-%d")
        #福利job_welfafe
        job_welfaf = response.css('.welfare-tab-box span::text').extract()
        job_welfafe = ','.join(job_welfaf)
        #招的人数job_people
        job_peopl = response.xpath('//ul[@class="terminal-ul clearfix"]//strong/text()').extract()[-1]
        job_people = job_peopl.split('人')[0]
        #岗位职责job_desc
        job_desc = response.xpath('//div[@class="tab-inner-cont"]/p/text()').extract()
        job_desc = ''.join(job_desc).strip()

        #岗位要求job_request
        #职业标签job_ta
        job_tag = response.xpath('//ul[@class="terminal-ul clearfix"]//strong/a/text()').extract()[-1]
        # print(job_url,job_smoney,job_emoney)


        item['job_url'] = job_url
        item['job_comp'] = job_comp
        item['job_name'] = job_name
        item['job_degree'] = job_degree
        item['job_smoney'] = job_smoney
        item['job_emoney'] = job_emoney
        item['job_address'] = job_address
        item['job_comp_type'] = job_comp_type
        item['job_comp_snum'] = job_comp_snum
        item['job_comp_enum'] = job_comp_enum
        item['job_business'] = job_business
        item['job_syear'] = job_syear
        item['job_eyear'] = job_eyear
        item['job_date_pub'] = job_date_pub
        item['job_datetime'] = job_datetime
        item['job_welfafe'] = job_welfafe
        item['job_people'] = job_people
        item['job_desc'] = job_desc
        item['job_tag'] = job_tag

        yield item


    def process_year(self,year):
        if '-' in year:
            res = self.num_pattren.findall(year)
            syear = res[0]
            eyear = res[1]
        elif '以上' in year:
            res = self.num_pattren.search(year)
            syear = res.group()
            eyear = res.group()
        else:
            syear = 0
            eyear = 0
        return syear,eyear
