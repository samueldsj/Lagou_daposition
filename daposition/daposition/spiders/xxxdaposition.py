# -*- coding: utf-8 -*-

import scrapy
import json
from daposition.items import DapositionItem
#import re

class DapositionSpider(scrapy.Spider):
    name = 'xxxdaposition'
    allowed_domains = ['m.lagou.com']
    #start_urls = ['http://www.lagou.com/zhaopin/shujuyunying']


    custom_settings = {
    'DEFAULT_REQUEST_HEADERS': {
        'Host': 'www.lagou.com',
        'Origin': 'http://m.lagou.com',
        'Referer': 'http://m.lagou.com/jobs/list_java?px=default&city=%E5%85%A8%E5%9B%BD',
        'X-Requested-With': 'XMLHttpRequest',
        }
    }

    #INDEX_URL_TEMPLATE = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city={}&needAddtionalResult=false'
    COOKIES_ORIGINAL = 'user_trace_token=20170113145256-ea1ee772-d95c-11e6-a5f1-525400f775ce; LGUID=20170113145256-ea1eeb7a-d95c-11e6-a5f1-525400f775ce; PRE_UTM=m_cf_cpt_baidu_pc; PRE_HOST=bzclk.baidu.com; PRE_SITE=http%3A%2F%2Fbzclk.baidu.com%2Fadrc.php%3Ft%3D06KL00c00f77lk60UqFg0FNkUs0B84dm00000PMAMj300000XdPY7C.THL0oUhY1x60UWdBmy-bIy9EUyNxTAT0T1d9mHu9nyFWm10snA7Wnvwb0ZRqrDNaf1RLnHPAf1bkn19an1cYPH6YPW0sPjTzPW-7nj60mHdL5iuVmv-b5Hc3rHmsPHb3n1mhTZFEuA-b5HDv0ARqpZwYTjCEQLILIz4_myIEIi4WUvYE5LNYUNq1ULNzmvRqUNqWu-qWTZwxmh7GuZNxTAn0mLFW5HcsnWnk%26tpl%3Dtpl_10085_14394_1%26l%3D1050461913%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E6%25258B%252589%2525E5%25258B%2525BE%2525E7%2525BD%252591%2525E5%2525AE%252598%2525E7%2525BD%252591-%2525E4%2525B8%252593%2525E4%2525B8%25259A%2525E7%25259A%252584%2525E4%2525BA%252592%2525E8%252581%252594%2525E7%2525BD%252591%2525E6%25258B%25259B%2525E8%252581%252598%2525E5%2525B9%2525B3%2525E5%25258F%2525B0%25252C%2526xp%253Did%28%252522m4c6eceef%252522%29%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D230%26wd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26issp%3D1%26f%3D3%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3Dbaiduhome_pg%26oq%3Ddata%2525E5%2525A4%25258D%2525E6%252595%2525B0%26inputT%3D2899%26prefixsug%3Dlagou%26rsp%3D0; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F%3Futm_source%3Dm_cf_cpt_baidu_pc; _gat=1; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=53; index_location_city=%E6%B7%B1%E5%9C%B3; login=false; unick=""; _putrc=""; JSESSIONID=71FF46159FDD2BBB7BC033C34D4FC590; TG-TRACK-CODE=index_search; SEARCH_ID=78d24ca82c0a4cf7bffdc456c7b2082f; _ga=GA1.2.317118795.1484290377; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1484290377,1484290895,1486095035,1486732078; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1486733367; LGSID=20170210210757-f143586d-ef91-11e6-8f66-5254005c3644; LGRID=20170210212927-f1db18c6-ef94-11e6-a159-525400f775ce'
    

    # 获取 岗位："数据分析”、"爬虫" 的页面序列，传递给parse()
    def start_requests(self):
        reqs = []
        start_requests_item = {'positionName':''}
    
        #for i in range(155): # 数据分析 职位总共155页
        for i in range(1):
            da_url = 'http://m.lagou.com/search.json?city=全国&positionName=数据分析&pageNo=%s'%i
            start_requests_item['positionName'] = '数据分析'
            self.log('da_url ==== 数据分析 第%s页'%i)
            self.log(da_url)
            yield scrapy.Request(url=da_url, meta=start_requests_item)
        
        #for i in range(28): # 爬虫 职位总共27页
        for n in range(1):
            scrapy_url = 'http://m.lagou.com/search.json?city=全国&positionName=爬虫&pageNo=%s'%n
            start_requests_item['positionName'] = '爬虫'
            self.log('scrapy_url ==== 爬虫 第%s页'%n)
            yield scrapy.Request(url=scrapy_url, meta=start_requests_item)
        self.log(' ~~~~~~~~ finish start_requests ~~~~~~~~ ')



    #解析response中的 positionId 字段，使用回调函数 parse_position()获取详细岗位id信息，传入parse_jobpage抓取详细岗位信息
    def parse(self,response):
        parse_item = {'positionName':'',
                      'positionId':''}


        '''headers = {
        "Accept":"*/*",
        "Accept-Encoding":"gzip, deflate, sdch",
        "Accept-Language":"zh-CN,zh;q=0.8",
        "Cache-Control":"max-age=0",
        "Connection":"keep-alive",
        "Host": "www.lagou.com",
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
    }

        #cookie = 'user_trace_token=20170808160323-649591bf-7120-43d8-9497-490e96510b4f; _ga=GA1.2.1063853007.1502179410; LGUID=20170808160329-10a4b405-7c10-11e7-83d3-5254005c3644; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1502179410,1502237671; index_location_city=%\E5%\85%\A8%\E5%\9B%\BD; LGRID=20170810141345-10ec1a72-7d93-11e7-84a7-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1502344851; X_MIDDLE_TOKEN=b97a6f74921df3e053c6db5201f5fc8d; X_HTTP_TOKEN=5802c9e63f23c986111ebc14e1878ba8; ab_test_random_num=0; _putrc=F4F5FEF2F7033DCE; login=true; unick=%\E6%\8B%\89%\E5%\8B%\BE%\E7%\94%\A8%\E6%\88%\B76638; JSESSIONID=ABAAABAAAFDABFGF6C1352F9F99EA008DE98807214CCD71; _ga=GA1.3.1063853007.1502179410; _gid=GA1.2.1626482216.1502336499; LGSID=20170810140051-43b3f093-7d91-11e7-84a7-5254005c3644'
        cookies = {
        'user_trace_token':'20170808160323-649591bf-7120-43d8-9497-490e96510b4f',
        '_ga':'GA1.2.1063853007.1502179410',
        'LGUID':'20170808160329-10a4b405-7c10-11e7-83d3-5254005c3644',
        'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6':'1502179410,1502237671',
        'index_location_city':'%\E5%\85%\A8%\E5%\9B%\BD',
        'LGRID':'20170810151214-3c8df040-7d9b-11e7-84a8-5254005c3644',
        'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6':'1502349127',
        'X_MIDDLE_TOKEN':'b97a6f74921df3e053c6db5201f5fc8d',
        'X_HTTP_TOKEN':'5802c9e63f23c986111ebc14e1878ba8',
        'ab_test_random_num':'0',
        '_putrc':'F4F5FEF2F7033DCE',
        #'login':'true',
        'login':'false',
        'unick':'%\E6%\8B%\89%\E5%\8B%\BE%\E7%\94%\A8%\E6%\88%\B76638',
        'JSESSIONID':'ABAAABAAAFDABFGF6C1352F9F99EA008DE98807214CCD71',
        '_ga':'GA1.3.1063853007.1502179410',
        '_gid':'GA1.2.1626482216.1502336499',
        'LGSID':'20170810140051-43b3f093-7d91-11e7-84a7-5254005c3644',
    }'''


        cookies = [dict(name=v.split('=')[0], value=v.split('=')[1]) for v in self.COOKIES_ORIGINAL.split(';')]
        #self.log('cookies =====111111=====%s'%cookies)

        parsepage_content = json.loads(response.body)
        self.log('da_page========== %s'%page_content)

        parse_item['positionName'] = response.meta['positionName']
        #print('111111',page_content.get('content')['data']['page'])
        #print('222222',page_content.get('content')['data']['page']['result'][0]["positionId"])
        parse_item['positionId'] = parsepage_content.get('content')['data']['page']['result'][0]["positionId"]
        self.log('parse_item  %s'%parse_item)

        parse_url = 'http://m.lagou.com/jobs/%s.html'%parse_item['positionId']
        self.log('parse_url  [%s]'%parse_url)
        meta = {
        'dont_redirect': True,  # 禁止网页重定向
        'handle_httpstatus_list': [301, 302],  # 对哪些异常返回进行处理
        'positionName': parse_item['positionName'],
        'positionId': parse_item['positionId']
        }
        yield scrapy.Request(url=parse_url, meta=meta, cookies=cookies, callback=self.parse_jobpage)
        self.log(' ~~~~~~~~ finish parse ~~~~~~~~ ')



    # 抓取详细岗位信息，存进最终的 jobpage_item 中，再通过pipelien存入mysql
    def parse_jobpage(self,response):
        print('\n9999999',response.status)
        jobpage_item = DapositionItem()
        jobpage_item['positionName'] = response.meta['positionName']
        jobpage_item['positionId'] = response.meta['positionId']
        #jobpage_item['postitle'] = response.xpath('//div[@title]')
        #/html/body/div[1]/div[1]/h2
        print('0000000',response.body)
        #print('1111111',response.xpath("//div[@class='postitle']"))

        #self.log('jobpage_item  %s'%jobpage_item)
        pass

