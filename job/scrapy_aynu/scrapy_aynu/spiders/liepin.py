# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_aynu.items import ZhaopinItem
import datetime
from datetime import timedelta
import re
from scrapy_aynu.items import ZhaopinItem
from scrapy_redis.spiders import RedisCrawlSpider


class LiepinSpider(RedisCrawlSpider):
    name = 'liepin'
    allowed_domains = ['liepin.com']
    # start_urls = ['https://www.liepin.com/']
    redis_key = 'liepinspider:urls'

    rules = (
        # Rule(LinkExtractor(allow=r'zhaopin/.*'),  follow=True),

            # / zhaopin /?key = java & d_sfrom = search_industry

        Rule(LinkExtractor(allow=r'adremote/'), follow=True),
        Rule(LinkExtractor(allow=r'zhaopin/?industryType'), follow=True),
        Rule(LinkExtractor(allow=r'zhaopin/?d_sfrom=search_fp_nvbar&init=\d+'), follow=True),

        Rule(LinkExtractor(allow=r'www.liepin.com/[a-z]{1,}/\d+\.shtml'), callback='parse_item', follow=True),

    )
    num_pattren = re.compile(r'\d+')

    def parse_item(self, response):
        # print('-'*150)
        item = ZhaopinItem()
        job_url = response.url
        job_comp = response.xpath('//div[@class="title-info"]//a/text()').extract()
        if len(job_comp):
            job_name = response.xpath('//div[@class="title-info"]/h1/text()').extract()
            if len(job_name):
                job_comp = job_comp[0]
            else:
                job_comp = ''
            job_degree = response.xpath('//div[@class="job-qualifications"]/span[1]/text()').extract()[0]
            job_money = response.xpath('//div[@class="job-item"]//p/text()').extract()[0].split()
            job_money = job_money.pop()
            if '万' in job_money:
                job_smoney = job_money.split('-')[0]
                job_smoney = int(job_smoney) * 10
                job_emoney = job_money.replace('万','').split('-')[1]
                job_emoney = int(job_emoney) * 10
            else:
                job_smoney = 0
                job_emoney = 0
            job_address = response.xpath('//p[@class="basic-infor"]//a/text()')
            if len(job_address):
                job_address = job_address.extract()[0]
            else:
                job_address = ''
            job_comp_num = response.xpath('//ul[@class="new-compintro"]/li[2]/text()').extract()[0]
            job_comp_num = job_comp_num.replace('公司规模：','')
            if '-' in job_comp_num:
                    job_comp_snum = job_comp_num.split('-')[0]
                    job_comp_enum = job_comp_num.replace('人', '').split('-')[1]
            else:
                print(job_comp_num)
                job_comp_snum = job_comp_num.replace('人以上', '')
                job_comp_enum = job_comp_num.replace('人以上', '')

            job_business = response.xpath('//ul[@class="new-compintro"]/li/a/text()')
            if len(job_business):
                job_business = job_business.extract()[0]
            else:
                job_business = ''
            job_year = response.xpath('//div[@class="job-qualifications"]//span[2]/text()').extract()[0]
            job_syear, job_eyear = self.process_year(job_year)
            job_date_pub = response.xpath('//p[@class="basic-infor"]//time/text()').extract()[0].strip()

            job_datetime = datetime.datetime.now().strftime("%Y-%m-%d")
            job_welfafe = response.xpath('//div[@class="tag-list"]/span/text()').extract()
            job_welfafe = ','.join(job_welfafe)

            job_desc = response.xpath('//div[@class="content content-word"]/text()').extract()
            job_desc = ''.join(job_desc)

            item['job_url'] = job_url
            item['job_comp'] = job_comp
            item['job_name'] = job_name
            item['job_degree'] = job_degree
            item['job_smoney'] = job_smoney
            item['job_emoney'] = job_emoney
            item['job_address'] = job_address
            item['job_comp_snum'] = job_comp_snum
            item['job_comp_enum'] = job_comp_enum
            item['job_business'] = job_business
            item['job_syear'] = job_syear
            item['job_eyear'] = job_eyear
            item['job_date_pub'] = job_date_pub
            item['job_datetime'] = job_datetime
            item['job_welfafe'] = job_welfafe
            item['job_desc'] = job_desc
            # print(item)
            yield item


        # print(job_desc,'----------------------------',job_request)

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








