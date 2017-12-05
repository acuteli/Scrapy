# -*- coding: utf-8 -*-
import json
import redis  # pip install redis
import pymysql

def main():
    # 指定redis数据库信息
    rediscli = redis.StrictRedis(host='127.0.0.1', port = 6379, db = 0)
    # 指定mysql数据库
    mysqlcli = pymysql.connect(host='127.0.0.1', user='root', passwd='12345qwert', db='jobs', charset='utf8',)

    # 无限循环
    while True:
        source, data = rediscli.blpop(["zhaopin:items"])  # 从redis里提取数据

        item = json.loads(data.decode('utf-8'))  # 把 json转字典

        try:
            # 使用cursor()方法获取操作游标
            cur = mysqlcli.cursor()
            # 使用execute方法执行SQL INSERT语句
            sql = 'insert into job(job_url,job_comp,job_name,job_degree,job_smoney,job_emoney,job_address,job_comp_type,job_comp_snum,job_comp_enum,job_business,job_syear,job_eyear,job_date_pub,job_datetime,job_welfafe,job_people,job_desc,job_tag)' \
                  'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) on duplicate key UPDATE job_url=VALUES (job_url),job_comp=VALUES (job_comp),job_name=VALUES (job_name),job_degree=VALUES (job_degree),job_smoney=VALUES (job_smoney),job_emoney=VALUES (job_emoney),' \
                  'job_address = VALUES (job_address),job_comp_type=VALUES (job_comp_type),job_comp_snum=VALUES (job_comp_snum),job_comp_enum=VALUES (job_comp_enum),job_business=VALUES (job_business),job_syear=VALUES (job_syear),job_date_pub=VALUES (job_date_pub),job_datetime=VALUES (job_datetime),' \
                  'job_welfafe=VALUES (job_welfafe),job_people=VALUES (job_people),job_desc=VALUES (job_desc),job_tag=VALUES (job_tag)'
            cur.execute(sql, (item['job_url'], item['job_comp'], item['job_name'], item['job_degree'], item['job_smoney'], item['job_emoney'], item['job_address'],
                                      item['job_comp_type'],item['job_comp_snum'],item['job_comp_enum'],item['job_business'],item['job_syear'],item['job_eyear'],
                                      item['job_date_pub'],item['job_datetime'],item['job_welfafe'],item['job_people'],item['job_desc'],item['job_tag']))
            # 提交sql事务
            mysqlcli.commit()
            #关闭本次操作
            cur.close()
            print("插入 %s" % item['job_name'])
        except pymysql.Error as e:
            mysqlcli.rollback()
            print("插入错误", str(e))

if __name__ == '__main__':
    main()