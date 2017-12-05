# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
class MysqlPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect('127.0.0.1','root','123456','temp',charset='utf8')
        self.cursor = self.conn.cursor()
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()


class CnblogMysqlPipeline(MysqlPipeline):
    def process_item(self,item,spider):
        sql = 'insert into cnblog(url,) ' \
              'VALUES(%s,%s,%s,%s,%s,%s,%s,%s) on duplicate key update pname=values(pname),pnumber=VALUES(pnumber)'
        try:
            self.cursor.execute(sql, (
            item['url'], item['pname'], item['pnumber'], item['ptype'], item['location'], item['duty'],
            item['requirement'], item['date_time']))
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)
            print('执行语句失败')
            # 返回交给下一个管道文件处理
        return item