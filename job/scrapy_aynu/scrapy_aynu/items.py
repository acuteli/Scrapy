# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyAynuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ZhaopinItem(scrapy.Item):
    job_url = scrapy.Field()     #职位详情连接
    job_comp = scrapy.Field()    #公司名
    job_name = scrapy.Field()    #工作名
    job_degree = scrapy.Field()  #学历
    job_smoney = scrapy.Field()  #开始薪资
    job_emoney = scrapy.Field()   #结束薪资
    job_address = scrapy.Field()  #工作地址
    job_comp_snum = scrapy.Field() #起始人数
    job_comp_enum = scrapy.Field()  #结束人数
    job_business = scrapy.Field()  #公司主营
    job_syear = scrapy.Field()   #工作经验开始年份
    job_eyear = scrapy.Field()  #工作经验结束年份
    job_date_pub = scrapy.Field()  #发布日期
    job_datetime = scrapy.Field()   #爬取日期
    job_welfafe = scrapy.Field()   #公司福利
    job_desc = scrapy.Field()   #公司简介





