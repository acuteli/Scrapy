from scrapy import cmdline
import os

os.chdir('tcs/spiders')
cmdline.execute('scrapy runspider zhaopin.py'.split())



