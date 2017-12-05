from scrapy import cmdline
import os

os.chdir('scrapy_aynu/spiders')
cmdline.execute('scrapy runspider liepin.py'.split())



