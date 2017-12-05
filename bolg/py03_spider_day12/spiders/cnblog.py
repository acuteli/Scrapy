# -*- coding: utf-8 -*-
import scrapy
import re
from urllib import parse
from py03_spider_day12.items import CnblogItem
import datetime

class CnblogSpider(scrapy.Spider):
    name = 'cnblog'
    allowed_domains = ['cnblogs.com']
    start_urls = ['https://www.cnblogs.com/cate/python/1']

    # 解析列表页
    def parse(self, response):
        article_list = response.xpath('//div[@class="post_item"]')
        for article in article_list:
            cnitem = CnblogItem()
            # 文章链接
            url = article.xpath('.//h3/a/@href').extract()[0]
            # 文章标题
            title = article.xpath('.//h3/a/text()').extract()[0]
            # 获取文章简介
            industry = article.xpath('.//p[@class="post_item_summary"]/text()').extract()
            if industry[0].strip():
                industry = industry[0]
            else:
                industry = industry[1].strip()
            # 作者
            author = article.xpath('.//a[@class="lightblue"]/text()').extract()[0]
            # 获取文章发布日期
            date_pub = article.xpath('.//div[@class="post_item_foot"]/text()').extract()[1].strip().strip('发布于 ')
            # 推荐数
            recommand_num = article.xpath('.//span[@class="diggnum"]/text()').extract()[0]
            # 阅读数
            read_num = article.xpath('.//span[@class="article_view"]/a/text()').extract()[0]
            read_num = self.getnum(read_num)
            # 评论数
            common_num = article.xpath('.//span[@class="article_comment"]/a/text()').extract()[0]
            common_num = self.getnum(common_num)
            # 头像img_url
            img_url = article.xpath('.//img[@class="pfs"]/@src').extract()
            if img_url:
                img_url = parse.urljoin(response.url,img_url[0])
            else:
                img_url = []
            # print(author,recommand_num,read_num,common_num)
            # print(img_url)
            cnitem['url'] = url
            cnitem['title'] = title
            cnitem['industry'] = industry
            cnitem['author'] = author
            cnitem['date_pub'] = date_pub
            cnitem['recommand_num'] = recommand_num
            cnitem['read_num'] = read_num
            cnitem['common_num'] = common_num
            cnitem['img_url'] = [img_url] if img_url else []

            # 详情页请求加入队列
            yield scrapy.Request(url,callback=self.parse_detail,meta={'data' : cnitem})


        # 获取下一页链接
        next_url = response.xpath('//div[@class="pager"]/a/@href').extract()[-1]
        next_url = parse.urljoin(response.url,next_url)

        # 加入请求队列
        yield scrapy.Request(next_url,callback=self.parse)

    def parse_detail(self,response):
        cnitem = response.meta['data']

        #获取文章内容
        content = response.xpath('//div[@class="post"]').extract()[0]
        cnitem['content'] = content

        # 获取文章标签
        tag = response.xpath('//div[@id="EntryTag"]/a/text()').extract()
        if tag:
            tag = ','.join(tag)
        else:
            tag = ''

        cnitem['tag'] = tag

        # 加入爬取时间
        crawl_time = datetime.datetime.now().strftime('%Y-%m-%d')
        cnitem['crawl_time'] = crawl_time

        # 管道文件
        yield cnitem

    # 提取数字
    def getnum(self,value):
        num_pattern = re.compile(r'\d+')
        res = num_pattern.search(value)
        if res is not None:
            return res.group()
        else:
            return 0
