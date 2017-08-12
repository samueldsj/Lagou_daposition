# -*- coding: utf-8 -*-

import scrapy
import json
from daposition.items import DapositionItem
#import re

class DapositionSpider(scrapy.Spider):
    name = 'xxdaposition'
    allowed_domains = ['m.lagou.com']
    #start_urls = ['http://www.lagou.com/zhaopin/shujuyunying']

    # 获取 岗位："数据分析”、"爬虫" 的页面序列，传递给parse()
    def start_requests(self):
        reqs = []
        start_requests_item = {'positionName':''}
    

        #for i in range(155): # 数据分析 职位总共155页
        for i in range(1):
            da_url = 'http://m.lagou.com/search.json?city=全国&positionName=数据分析&pageNo=%s'%i
            start_requests_item['positionName'] = '数据分析'
            self.log('数据分析 第%s页'%i)
            #self.log('da_url ==== %s'%da_url)
            yield scrapy.Request(url=da_url, meta=start_requests_item)
        
        #for i in range(28): # 爬虫 职位总共27页
        for n in range(1):
            scrapy_url = 'http://m.lagou.com/search.json?city=全国&positionName=爬虫&pageNo=%s'%n
            #scrapy_url = 'http://m.lagou.com/search.json?city=全国&positionName=爬虫&pageNo=30'
            start_requests_item['positionName'] = '爬虫'
            self.log('爬虫 第%s页'%n)
            self.log('scrapy_url ==== %s'%scrapy_url)
            yield scrapy.Request(url=scrapy_url, meta=start_requests_item)
        self.log(' ~~~~~~~~ finish start_requests ~~~~~~~~ ')

    #解析response中的 positionId 字段，使用回调函数 parse_position()获取详细岗位id信息，传入parse_jobpage抓取详细岗位信息
    def parse(self,response):
        parse_item = {'positionName':'',
                      'positionId':''}


        parsepage_content = json.loads(response.body)
        #self.log('da_page========== %s'%parsepage_content)
        parse_item['positionName'] = response.meta['positionName']

        counter = 0
        result = parsepage_content.get('content')['data']['page']['result']
        self.log('len  ======= [%s]'%len(result))

        if len(result)>0: # 防止没有内容
            for id in result:
                parse_item['positionId'] = result[counter]["positionId"]
                headers  = {
                    'Cookie':'user_trace_token=20170603115043-d0c257a054ee44f99177a3540d44dda1; LGUID=20170603115044-d1e2b4d1-480f-11e7-96cf-525400f775ce; JSESSIONID=ABAAABAAAGHAABHAA8050BE2E1D33E6C2A80E370FE9167B; _gat=1; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; index_location_city=%E5%85%A8%E5%9B%BD; login=false; unick=""; _putrc=""; _ga=GA1.2.922290439.1496461627; X_HTTP_TOKEN=3876430f68ebc0ae0b8fac6c9f163d45; _ga=GA1.3.922290439.1496461627; LGSID=20170720174323-df1d6e50-6d2f-11e7-ac93-5254005c3644; LGRID=20170720174450-12fc5214-6d30-11e7-b32f-525400f775ce; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1500541369; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1500543655',
                    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
                    'referer':'http://m.lagou.com/jobs/%s.html'%parse_item['positionId']}
                

                self.log('parse_item[positionId]  ======= [%s]'%parse_item['positionId'])
                self.log('parse_item[positionId]  ======= [%s]'%headers)

                parse_url = 'http://m.lagou.com/jobs/%s.html'%parse_item['positionId']
                #self.log('parse_url  ======= [%s]'%parse_url)
                meta = {
                    #'dont_redirect': True,  # 禁止网页重定向
                    #'handle_httpstatus_list': [301, 302],  # 对哪些异常返回进行处理
                    'positionName': parse_item['positionName'],
                    'positionId': parse_item['positionId']}
                counter += 1
                yield scrapy.Request(url=parse_url, meta=meta, headers=headers, callback=self.parse_jobpage)
        self.log(' ~~~~~~~~ finish parse ~~~~~~~~ ')


    # 抓取详细岗位信息，存进最终的 jobpage_item 中，再通过pipelien存入mysql
    def parse_jobpage(self,response):
        #self.log('response.body ~~~~~~~~~~ [%s]'%response.body)
        #self.log('response.code ~~~~~~~~~~ [%s]'%response.code)
        jobpage_item = DapositionItem()

        jobpage_item['positionName'] = response.meta['positionName']
        jobpage_item['positionId'] = response.meta['positionId']

        jobpage_item['postitle'] = response.xpath("//div[@class='postitle']/h2[@class='title']/text()").extract()[0].strip()
        jobpage_item['salary'] = response.xpath("//span[@class='item salary']/span[@class='text']/text()").extract()[0].strip()
        jobpage_item['workaddress'] = response.xpath("//span[@class='item workaddress']/span[@class='text']/text()").extract()[0].strip()
        jobpage_item['jobnature'] = response.xpath("//span[@class='item jobnature']/span[@class='text']/text()").extract()[0].strip()
        jobpage_item['workyear'] = response.xpath("//span[@class='item workyear']/span[@class='text']/text()").extract()[0].strip()
        jobpage_item['education'] = response.xpath("//span[@class='item education']/span[@class='text']/text()").extract()[0].strip()
        jobpage_item['temptation'] = response.xpath("//div[@class='temptation']/text()").extract()[0].strip()
        
        jobpage_item['company_title'] = response.xpath("//div[@class='dleft']/h2[@class='title']/text()").extract()[0].strip()
        jobpage_item['company_info'] = response.xpath("//div[@class='dleft']/p[@class='info']/text()").extract()[0].strip()
        
        jobpage_item['positiondesc0'] = response.xpath("//div[@class='positiondesc']/div[@class='content']/p[1]/text()").extract()[0].strip()
        jobpage_item['positiondesc1'] = response.xpath("//div[@class='positiondesc']/div[@class='content']/p[2]/text()").extract()[0].strip()
        jobpage_item['positiondesc2'] = response.xpath("//div[@class='positiondesc']/div[@class='content']/p[3]/text()").extract()[0].strip()
        jobpage_item['positiondesc3'] = response.xpath("//div[@class='positiondesc']/div[@class='content']/p[4]/text()").extract()[0].strip()
        jobpage_item['positiondesc4'] = response.xpath("//div[@class='positiondesc']/div[@class='content']/p[5]/text()").extract()[0].strip()
        jobpage_item['positiondesc5'] = response.xpath("//div[@class='positiondesc']/div[@class='content']/p[6]/text()").extract()[0].strip()
        jobpage_item['positiondesc6'] = response.xpath("//div[@class='positiondesc']/div[@class='content']/p[7]/text()").extract()[0].strip()
        jobpage_item['positiondesc7'] = response.xpath("//div[@class='positiondesc']/div[@class='content']/p[8]/text()").extract()[0].strip()
        jobpage_item['positiondesc8'] = response.xpath("//div[@class='positiondesc']/div[@class='content']/p[9]/text()").extract()[0].strip()
        jobpage_item['positiondesc9'] = response.xpath("//div[@class='positiondesc']/div[@class='content']/p[10]/text()").extract()[0].strip()
        #jobpage_item['positiondesc10'] = response.xpath("//div[@class='positiondesc']/div[@class='content']/p[11]/text()").extract()[0].strip()
        #jobpage_item['positiondesc11'] = response.xpath("//div[@class='positiondesc']/div[@class='content']/p[12]/text()").extract()[0].strip()

        #jobpage_item['positioneval'] = response.xpath("//li[@class='list-item-empty list-item']/text()").extract()[0].strip()
        self.log('jobpage_item  %s'%jobpage_item)
        
        yield jobpage_item

