# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst,Join,Identity,MapCompose
from scrapy.loader import ItemLoader
import re
from urllib import parse

class Py03SpiderDay12Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class CnblogItemLoader(ItemLoader):
    # 设置默认输出管理器
    default_output_processor = TakeFirst()

# 处理简介的输入处理器
def process_industry(value): # ['\r\n','\r\n简介内容']
    if value[0].strip():
        return value[0].strip()
    else:
        return value[1].strip()
    # 最后返回的值就是['简介内容']
def dateprocessor(value):
    return value[1].strip().strip('发布于 ')

    # 提取数字
def getnum(value):
    num_pattern = re.compile(r'\d+')
    res = num_pattern.search(value)
    if res is not None:
        return res.group()
    else:
        return 0

def imgprocessor(value):
    if value:
        return ['https:' + value[0]]
    else:
        return []

def tarprocessor(value):
    if value:
        return ','.join(value)
    else:
        return '无'

class CnblogItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    industry = scrapy.Field(
        input_processor = process_industry
        # input_processor = lambda x : x[0].strip() if x[0].strip() else x[1].strip(),
    )
    content = scrapy.Field()
    author = scrapy.Field()
    date_pub = scrapy.Field(
        input_processor = dateprocessor
    )
    recommand_num = scrapy.Field()
    read_num = scrapy.Field(
        input_processor = MapCompose(getnum)
    )
    common_num = scrapy.Field(
        input_processor = MapCompose(getnum)
    )
    img_url = scrapy.Field(
        output_processor = imgprocessor
    ) # 图片的url地址
    img_path = scrapy.Field() # 本地图片的路径
    tag = scrapy.Field(
        input_processor = tarprocessor
    ) # 标签
    crawl_time = scrapy.Field() # 抓取时间