# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
#from lagou.settings import IPPOOL
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware

class DapositionSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class RandomUserAgent(object):
    # 根据预定义的列表随机更换用户代理
    def __init__(self,agents):  
        self.agents = agents
        
    @classmethod  
    def from_crawler(cls,crawler):  
        return cls(crawler.settings.getlist('USER_AGENTS'))  
  
  
    def process_request(self,request,spider):  
        request.headers.setdefault('User-Agent',random.choice(self.agents))  


class IPPOOLS(HttpProxyMiddleware):
    # 初始化方法
    def __init__(self,ip=''):
        self.ip = ip
    # process_request()方法，主要进行请求处理
    def process_request(self, request, spider):
        # 先随机选择一个ip
        thisip = random.choice(IPPOOL)
        # 输出当前选择的IP，便于调试观察
        print('当前使用的IP是：', thisip['ipaddr'])
        # 将对应的IP实际添加为具体的代理，用该IP进行爬取
        request.meta['proxy'] = 'http://'+thisip['ipaddr']
