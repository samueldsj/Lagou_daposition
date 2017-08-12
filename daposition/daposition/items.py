# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DapositionItem(scrapy.Item):
    # define the fields for your item here like:
    #https://www.lagou.com/jobs/2458328.html
    '''positionName = scrapy.Field()
    positionId = scrapy.Field()
    postitle = scrapy.Field()
    salary = scrapy.Field()
    workaddress = scrapy.Field()
    jobnature = scrapy.Field()
    workyear = scrapy.Field()
    education = scrapy.Field()
    temptation = scrapy.Field()
    company_title = scrapy.Field()
    company_info = scrapy.Field()
    positiondesc0 = scrapy.Field()
    positiondesc1 = scrapy.Field()
    positiondesc2 = scrapy.Field()
    positiondesc3 = scrapy.Field()
    positiondesc4 = scrapy.Field()
    positiondesc5 = scrapy.Field()
    positiondesc6 = scrapy.Field()
    positiondesc7 = scrapy.Field()
    positiondesc8 = scrapy.Field()
    positiondesc9 = scrapy.Field()
    #positiondesc10 = scrapy.Field()
    #positiondesc11 = scrapy.Field()
    #positioneval = scrapy.Field()'''
    
    #formatCreateTime
    companyId = scrapy.Field()
    positionId = scrapy.Field()
    positionName = scrapy.Field()
    createTime = scrapy.Field()
    positionAdvantage = scrapy.Field()
    salary = scrapy.Field()
    workYear = scrapy.Field()
    education = scrapy.Field()
    city = scrapy.Field()
    jobNature = scrapy.Field()
    approve = scrapy.Field()
    industryField = scrapy.Field()
    companyShortName = scrapy.Field()
    financeStage = scrapy.Field()
    positionLables = scrapy.Field()
    industryLables = scrapy.Field()
    companySize = scrapy.Field()
    district = scrapy.Field()
    companyLabelList = scrapy.Field()
    companyFullName = scrapy.Field()
    firstType = scrapy.Field()
    secondType = scrapy.Field()
    isSchoolJob = scrapy.Field()
    '''url = scrapy.Field()
    companySize = scrapy.Field()
    firstType = scrapy.Field()
    workYear = scrapy.Field()
    education = scrapy.Field()
    financeStage = scrapy.Field()
    city = scrapy.Field()
    district = scrapy.Field()
    industryField = scrapy.Field()
    createTime = scrapy.Field()
    positionLables = scrapy.Field()
    salary = scrapy.Field()
    positionName = scrapy.Field()
    jobNature = scrapy.Field()
    companyFullName = scrapy.Field()
    companyLabelList = scrapy.Field()
    descript = scrapy.Field()'''
    pass


class BookDataItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    book_name = scrapy.Field()
    descript = scrapy.Field()
    auth = scrapy.Field()
    price = scrapy.Field()
    pass
