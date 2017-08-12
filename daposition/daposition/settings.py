# -*- coding: utf-8 -*-

# Scrapy settings for daposition project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'daposition'

SPIDER_MODULES = ['daposition.spiders']
NEWSPIDER_MODULE = 'daposition.spiders'

REDIRECT_ENABLED = False

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENTS = [  
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",  
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",  
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",  
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",  
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",  
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",  
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",  
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",  
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",  
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",  
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",  
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",  
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",  
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",  
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",  
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",  
] 

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True 

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Language':'gzip, deflate',
   'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
   'Connection':'keep-alive',
   'Cookie':
'user_trace_token=20170808160323-649591bf-7120-43d8-9497-490e96510b4f; _ga=GA1.2.1063853007.1502179410\
; LGUID=20170808160329-10a4b405-7c10-11e7-83d3-5254005c3644; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6\
=1502179410,1502237671; index_location_city=%E5%85%A8%E5%9B%BD; LGRID=20170810141345-10ec1a72-7d93-11e7-84a7-5254005c3644\
; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1502344851; X_MIDDLE_TOKEN=b97a6f74921df3e053c6db5201f5fc8d\
; X_HTTP_TOKEN=5802c9e63f23c986111ebc14e1878ba8; ab_test_random_num=0; _putrc=F4F5FEF2F7033DCE; login\
=true; unick=%E6%8B%89%E5%8B%BE%E7%94%A8%E6%88%B76638; JSESSIONID=ABAAABAAAFDABFGF6C1352F9F99EA008DE98807214CCD71\
; _ga=GA1.3.1063853007.1502179410; _gid=GA1.2.1626482216.1502336499; LGSID=20170810140051-43b3f093-7\
d91-11e7-84a7-5254005c3644',
   'Host':'m.lagou.com',
   'Upgrade-Insecure-Requests':'1',
   #'Cache-Control':'max-age=0',
   #'Cookie':'HMACCOUNT=93B7A56D26A3BC3B; BAIDUID=04ADA464B5A6800A1CFF63AA0F3F7AFE:FG=1; BIDUPSID=41368AE0DA37414C52506C1D040FC348; PSTM=1500517230; BDUSS=pzSjl-NFczRk8tclNaUFBxcDViS3dZWk5NYlRSYmVFUmhGZjNQRG5NdXdVcHhaSVFBQUFBJCQAAAAAAAAAAAEAAACbz6Utxr23srXEyq7O5bfW1tMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALDFdFmwxXRZVn; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; H_PS_PSSID=1446_21090; HMVT=7a3960b6f067eb0085b7f96ff5e660b0|1502266127|; PSINO=3',
   'User-Agent':"Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)"
}


# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'daposition.middlewares.DapositionSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    #'daposition.middlewares.MyCustomDownloaderMiddleware': 543,
    'daposition.middlewares.RandomUserAgent': 1,
    #'daposition.middlewares.IPPOOLS': 125,
    #'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 123
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'daposition.pipelines.DapositionPipeline': 300,
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
#HTTPCACHE_IGNORE_HTTP_CODES = [301,302]
HTTPERROR_ALLOWED_CODES = [301,302]
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
