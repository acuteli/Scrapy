# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_aynu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrapy_aynu'

SPIDER_MODULES = ['scrapy_aynu.spiders']
NEWSPIDER_MODULE = 'scrapy_aynu.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy_aynu (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 16

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.2
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "Host": "www.liepin.com",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    "Upgrade-Insecure-Requests": "1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Referer": "https://www.liepin.com/event/landingpage/search_salary/?mscid=s_00_011&utm_source=sogou&utm_medium=cpc&utm_campaign=%E5%93%81%E4%B8%93&utm_content=%E4%B8%BB%E6%A0%87%E9%A2%98&utm_term=%E4%B8%BB%E6%A0%87%E9%A2%98",
    # "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Cookie": "__uuid=1511166063260.74; gr_user_id=4a4f11bd-f262-4645-a10d-a542c1e2410d; c_flag=6e9343dd53d2d7403ffcc3faf8618981; new_user=false; need_bind_tel=false; _uuid=E353D52CFFA8481F463B16F096D92E26; user_kind=0; is_lp_user=true; _fecdn_=1; JSESSIONID=56C71EE4A671C4B05E0D978C88A66DE5; abtest=0; gr_session_id_bf8a73282d811a1b=07a5729f-d1e4-4b04-a16a-745361e329d4; __tlog=1511769409390.64%7C00000000%7CR000000075%7C00000000%7C00000000; __session_seq=5; __uv_seq=5; Hm_lvt_a2647413544f5a04f00da7eee0d5e200=1511396718,1511396719,1511485328,1511769410; Hm_lpvt_a2647413544f5a04f00da7eee0d5e200=1511769631; verifycode=45187341b47e4ad5a456105a4b30e909",

}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'scrapy_aynu.middlewares.ScrapyAynuSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
#    'scrapy_aynu.middlewares.RandomUserAgent': 1,
# }

DOWNLOAD_TIMEOUT = 10

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'scrapy_aynu.pipelines.LiepinMysqlPipeline': 1,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# url指纹过滤器
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# 调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 设置爬虫是否可以中断
SCHEDULER_PERSIST = True

# 设置请求队列类型
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue" # 按优先级入队列
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"  # 按照队列模式
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack" # 按照栈进行请求的调度

# 配置redis管道文件，权重数字相对最大
ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline': 999,  # redis管道文件，自动把数据加载到redis
}

# redis连接配置
REDIS_HOST = '192.168.103.110'
REDIS_PORT = 6379