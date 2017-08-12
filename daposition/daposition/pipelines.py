# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymysql

def dbHandle():
    conn = pymysql.connect(
        host='localhost',
        db = 'lagou',
        user='root',
        passwd='111111',
        charset='utf8',
        use_unicode=True
    )
    return conn


class DapositionPipeline(object):
    def process_item(self, item, spider):
        dbObject = dbHandle()
        cursor = dbObject.cursor()
        
        sql = 'insert into lagou.daposition(\
        	companyId,\
        	positionName,\
			workYear,\
			education,\
			jobNature,\
			positionId,\
			createTime,\
			city,\
			industryField,\
			positionAdvantage,\
			salary,\
			companySize,\
			approve,\
			companyShortName,\
			positionLables,\
			industryLables,\
			companyLabelList,\
			financeStage,\
			district,\
			firstType,\
			secondType,\
			isSchoolJob,\
			companyFullName)\
        	 values(%s,%s,%s,%s,%s,%s,\
        	 		%s,%s,%s,%s,%s,%s,\
        	 		%s,%s,%s,%s,%s,%s,\
        	 		%s,%s,%s,%s,%s\
        	 )'
        
        lis =(item['companyId']
			,item['positionName']
			,item['workYear']
			,item['education']
			,item['jobNature']
			,item['positionId']
			,item['createTime']
			,item['city']
			,item['industryField']
			,item['positionAdvantage']
			,item['salary']
			,item['companySize']
			,item['approve']
			,item['companyShortName']                  
			,str(item['positionLables'])
			,str(item['industryLables'])
			,str(item['companyLabelList'])
			,item['financeStage']
			,item['district']
			,item['firstType']
			,item['secondType']
			,item['isSchoolJob']
			,item['companyFullName']
			)
        try:
            cursor.execute(sql,lis)
            dbObject.commit()
            print(item['positionName'],'writen sucessed')
        
        except Exception as e:
            print('DB writer failllllll',e)
            dbObject.rollback()
        else:
            #print('DB writer success')
            dbObject.close()
        return item