# Lagou_daposition

[Purpose]: fetch the recruitment info of 'data analysis' and related position from lagou.com and analysis the factors like city distribution, work year, education and salary, etc.

[data acquisition]: From: https://www.lagou.com/jobs/positionAjax.json?px=default&city={}&needAddtionalResult=false By: Scrapy Content: daposition

[data storage]: Mysql: lagou_daposition

[data analysis]: By: Jupyter notebook Content: Lagou_DA_position.ipynb

目的： 获取拉勾网 数据分析 相关岗位的招聘信息，并分析城市，工作年限，教育，薪资等数据

数据获取： scrapy抓取 拉勾 股东户数信息(https://xueqiu.com/stock/f10/shareholdernum.json?symbol=SH%s&page=%i'%(sh,shcounter) 文件名：daposition

数据存储: Mysql: lagou_daposition

数据分析：jupyter 文件名：Lagou_DA_position.ipynb