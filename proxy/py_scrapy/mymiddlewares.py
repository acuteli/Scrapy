from fake_useragent import UserAgent
from py_scrapy import settings
import random
import base64

class RandomUserAgent(object):
    #处理请求函数
    def __init__(self,crawler):  #爬虫对象
        # crawler.settings.get('')
        #获取配置文件中的配置信息
        self.ua_type = crawler.setting.get('RANDOM_UA_TYPE','random')
        self.ua = UserAgent()


    @classmethod
    def from_crawler(cls,crawler):
        return cls(crawler)

    def process_request(self,request,spider):
        request.headers.setdefault('User-Agent', getattr(self.ua, self.ua_type))

class FreeRandomProxy(object):
    def process_request(self,request,spider):
        proxy = random.choice(settings.FREE_PROXIES)
        # proxy = get_proxy.getproxy()
        request.meta['proxy'] = '%s://%s:%s' % (proxy[2], proxy[0], proxy[1])

class AuthRandomProxy(object):
    def process_request(self,request,spider):
        proxy = random.choice(settings.AUTH_PROXIES)
        # 设置代理的认证信息
        auth = base64.b64encode(bytes(proxy['auth'], 'utf-8'))
        request.headers['Proxy-Authorization'] = b'Basic ' + auth
        # 设置代理ip
        request.meta['proxy'] = 'http://' + proxy['host']