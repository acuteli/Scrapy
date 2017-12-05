# 项目介绍

1.运行环境:
   python3.5 + MySql + django + Scrapy + redis

2.项目文件: 
   scrapy_aynu存放猎聘网爬虫文件: .scrapy_aynu/spiders/liepin.py

   tcs存放智联的爬虫文件:  .tcs/spider/zhaopin.py

   aynu_job: 存放项目关于django的相关文件
   
   sql: 存放项目所需要的MySql数据库文件

3.功能介绍:
  > 使用Scrapy对智联招聘和猎聘网数据进行了全栈爬取,分析自己需要的字段写入数据库方便后期页面展示;
  > 使用RedisCrawlSpider分布式爬取数据,开启cookie,使用抓包工具抓取HEAERS来放入settings文件,设置DOWNLOAD_DELAY 来反反爬;

## 项目运行

1. 克隆项目:

2. 创建并配置虚拟环境:

   创建虚拟环境: 
	```
	virtualenv env
	```
   激活虚拟环境:
	```
	windows:
	env\Scripts\activate
	linux:
	source env/bin/activate
	```
3. 安装依赖环境:
	```
	pip install -r requirements.txt
	```
4. 数据库操作:
   > 导入数据表job.sql和job3.sql可以合并数据库
   > 对于django来说执行迁移数据库的操作

5. 对于配置文件
	1.\scrapy_aynu\scrapy_aynu\settings
	  42行: DEFAULT_REQUEST_HEADERS = {抓取你的headers}
	  124行: REDIS_HOST = '要连接redis的ip'
	  125行: REDIS_PORT = redis的端口号
   


效果展示:
	![](https://i.imgur.com/WvZUWgp.png)
	![](https://i.imgur.com/peKKJ6d.png)
	![](https://i.imgur.com/iNTfhP6.png)
	
  



						   
   