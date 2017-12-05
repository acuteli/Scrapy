# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
class TcsPipeline(object):
    def process_item(self, item, spider):
        return item
class MysqlPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect('127.0.0.1','root','12345qwert','jobs',charset='utf8')
        self.cursor = self.conn.cursor()
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()

class CnblogMysqlPipeline(MysqlPipeline):
    def process_item(self,item,spider):
        # sql = 'insert into p(title) ' \
        #       'VALUES(%s) on duplicate key update ' \
        #       'title=values(title) '
        sql = 'insert into job(job_url,job_comp,job_name,job_degree,job_smoney,job_emoney,job_address,job_comp_type,job_comp_snum,job_comp_enum,job_business,job_syear,job_eyear,job_date_pub,job_datetime,job_welfafe,job_people,job_desc,job_tag)' \
                'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) on duplicate key UPDATE job_url=VALUES (job_url),job_comp=VALUES (job_comp),job_name=VALUES (job_name),job_degree=VALUES (job_degree),job_smoney=VALUES (job_smoney),job_emoney=VALUES (job_emoney),'\
                'job_address = VALUES (job_address),job_comp_type=VALUES (job_comp_type),job_comp_snum=VALUES (job_comp_snum),job_comp_enum=VALUES (job_comp_enum),job_business=VALUES (job_business),job_syear=VALUES (job_syear),job_date_pub=VALUES (job_date_pub),job_datetime=VALUES (job_datetime),'\
                'job_welfafe=VALUES (job_welfafe),job_people=VALUES (job_people),job_desc=VALUES (job_desc),job_tag=VALUES (job_tag)'
        try:
            self.cursor.execute(sql, (item['job_url'], item['job_comp'], item['job_name'], item['job_degree'], item['job_smoney'], item['job_emoney'], item['job_address'],
                                      item['job_comp_type'],item['job_comp_snum'],item['job_comp_enum'],item['job_business'],item['job_syear'],item['job_eyear'],
                                      item['job_date_pub'],item['job_datetime'],item['job_welfafe'],item['job_people'],item['job_desc'],item['job_tag']))
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)
            print('执行语句失败')
            # 返回交给下一个管道文件处理
        return item