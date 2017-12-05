# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class PyScrapyPipeline(object):
    def process_item(self, item, spider):
        return item


class MysqlPipline(object):
    def __init__(self):
        self.conn = pymysql.connect('127.0.0.1', 'root', '12345qwert', 'aynu', charset='utf8')
        self.cursor = self.conn.cursor()

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

class ProxyMysqlPipeline(MysqlPipline):
    def process_item(self, item, spider):

        if spider.name == '66':
            sql = 'insert into proxy66(host,port) ' \
                  'VALUES(%s,%s) on duplicate key update port=values(port)'
            try:
                self.cursor.execute(sql, (item['host'], item['port']))
                self.conn.commit()
            except Exception as e:
                self.conn.rollback()
                print(e)
                print('执行语句失败')
                # 返回交给下一个管道文件处理
        return item


