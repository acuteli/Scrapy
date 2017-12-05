# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TcsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ZhilianItem(scrapy.Item):
    job_url = scrapy.Field() #链接地址
    job_comp = scrapy.Field() #公司名字
    job_name = scrapy.Field() #职业岗位
    job_degree = scrapy.Field() #学历
    job_smoney = scrapy.Field() #薪资
    job_emoney = scrapy.Field() #薪资
    job_address = scrapy.Field() #公司地址
    job_comp_type = scrapy.Field() #公司类型(民营,国营)
    job_comp_snum = scrapy.Field() #公司规模
    job_comp_enum = scrapy.Field() #公司规模
    job_business = scrapy.Field() #公司主营job_business
    job_syear = scrapy.Field()  #工作经验
    job_eyear = scrapy.Field()  #工作经验
    job_date_pub = scrapy.Field() #发布日期
    job_datetime = scrapy.Field() #爬取日志
    job_welfafe = scrapy.Field() #福利
    job_people = scrapy.Field() #招的人数
    job_desc = scrapy.Field() #岗位职责
    job_tag = scrapy.Field() #职业标签
